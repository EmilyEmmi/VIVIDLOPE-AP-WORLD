from collections.abc import Mapping
from typing import Any

# Imports of base Archipelago modules must be absolute.
from worlds.AutoWorld import World

# Imports of your world's files must be relative.
from . import locations, items
from . import options as vividlope_options  # rename due to a name conflict with World.options
from .names import stage_prefixes, level_names, LocationSuffix
from .data import stage_data

# Logging
import logging
logger = logging.getLogger("VIVIDLOPE")

UT_SLOT_DATA_OPTION_NAMES = (
    "deathlink",
    "deathlink_amnesty",
    "goal_condition",
    "goal_unlock",
    "stage_shuffle",
    "exclude_finale",
    "exclude_level_x",
    "rank_checks",
    "max_rank_check",
    "nerfed_finale",
    "forced_character",
)

class VividlopeWorld(World):
    """
    description
    """

    game = "VIVIDLOPE"

    options_dataclass = vividlope_options.VividlopeOptions
    options: vividlope_options.VividlopeOptions

    location_name_to_id = locations.generate_location_table()
    item_name_to_id = items.ITEM_NAME_TO_ID

    origin_region_name = "Overworld"

    # Mapping for stage shuffle
    stage_shuffle_order: list

    ut_can_gen_without_yaml = True
    
    def pre_fill(self):
        return items.create_all_items

    def create_regions(self) -> None:
        locations.create_map_regions(self)
        locations.attach_shuffled_levels(self)

    """def set_rules(self) -> None:
        rules.set_all_rules(self)"""

    def create_items(self) -> None:
        items.create_all_items(self)

    def create_item(self, name: str) -> items.VividlopeItem:
        return items.create_item_with_correct_classification(self, name)

    def get_filler_item_name(self) -> str:
        return items.get_random_filler_item_name(self)

    def fill_slot_data(self) -> Mapping[str, Any]:
        slot_data = {
            "options": self.options.as_dict(*UT_SLOT_DATA_OPTION_NAMES),
        }
        # Add stage shuffle order to slot data
        if (self.options.stage_shuffle):
            slot_data["stage_shuffle_order"] = self.stage_shuffle_order
        return slot_data

    # Display actual stage location in hints
    def extend_hint_information(self, hint_data: dict[int, dict[int, str]]) -> None:
        if not self.options.stage_shuffle:
            return
        
        stage_hint_data = {}
        stage_index = 0
        for orig_stage in stage_data:
            stage_id = self.stage_shuffle_order[stage_index]
            placed_level = stage_id // 100
            placed_stage = stage_id % 100 + 1

            # Display level name only unless we're in Finale
            if orig_stage.level == 11:
                orig_name = f"{stage_prefixes[orig_stage.level-1]}{orig_stage.stage}"
            else:
                orig_name = f"{level_names[orig_stage.level-1]}"

            # Don't run for excluded levels
            if (orig_stage.level == 11 and self.options.exclude_finale and self.options.goal_condition != 0):
                stage_index += 1
                continue
            if (orig_stage.level == 10 and self.options.exclude_level_x and self.options.goal_condition != 1):
                stage_index += 1
                continue

            location_names = []
            if self.options.rank_checks != 2 or orig_stage.level == 11:
                location_names.append(f"{stage_prefixes[placed_level-1]}{placed_stage} {LocationSuffix.stage_clear}")
            if self.options.rank_checks != 0 and orig_stage.level != 11:
                all_location_names = [
                    f"{stage_prefixes[placed_level-1]}{placed_stage} {LocationSuffix.stage_d}",
                    f"{stage_prefixes[placed_level-1]}{placed_stage} {LocationSuffix.stage_dp}",
                    f"{stage_prefixes[placed_level-1]}{placed_stage} {LocationSuffix.stage_c}",
                    f"{stage_prefixes[placed_level-1]}{placed_stage} {LocationSuffix.stage_cp}",
                    f"{stage_prefixes[placed_level-1]}{placed_stage} {LocationSuffix.stage_b}",
                    f"{stage_prefixes[placed_level-1]}{placed_stage} {LocationSuffix.stage_bp}",
                    f"{stage_prefixes[placed_level-1]}{placed_stage} {LocationSuffix.stage_a}",
                    f"{stage_prefixes[placed_level-1]}{placed_stage} {LocationSuffix.stage_ap}",
                    f"{stage_prefixes[placed_level-1]}{placed_stage} {LocationSuffix.stage_s}",
                    f"{stage_prefixes[placed_level-1]}{placed_stage} {LocationSuffix.stage_sp}",
                    f"{stage_prefixes[placed_level-1]}{placed_stage} {LocationSuffix.stage_v}",
                ]
                if self.options.rank_checks == 1:
                    location_name = all_location_names[self.options.max_rank_check]
                    location_names.append(location_name)
                else:
                    for n in range(0, self.options.max_rank_check+1):
                        location_name = all_location_names[n]
                        location_names.append(location_name)

            for locationName in location_names:
                location = self.multiworld.get_location(locationName, self.player)
                stage_hint_data[location.address] = orig_name

            stage_index += 1
        hint_data[self.player] = stage_hint_data

    # All stuff for UT
    @staticmethod
    def interpret_slot_data(slot_data: dict[str, Any]) -> dict[str, Any]:
        return slot_data

    def _get_ut_slot_data(self) -> dict[str, Any] | None:
        re_gen_passthrough = getattr(self.multiworld, "re_gen_passthrough", {})
        if re_gen_passthrough and self.game in re_gen_passthrough:
            slot_data: dict[str, Any] = re_gen_passthrough[self.game]
            if isinstance(slot_data, dict):
                return slot_data
        return None

    def _restore_ut_slot_data(self, slot_data: dict[str, Any]) -> None:
        if slot_data.get("options") == None:
            return
        for option_name in UT_SLOT_DATA_OPTION_NAMES:
            if option_name not in slot_data["options"]:
                continue
            option = getattr(self.options, option_name, None)
            if option is not None:
                setattr(self.options, option_name, option.from_any(slot_data["options"][option_name]))

        stage_shuffle_order = slot_data.get("stage_shuffle_order")
        if isinstance(stage_shuffle_order, list):
            self.stage_shuffle_order = stage_shuffle_order
        elif self.options.stage_shuffle:
            logger.warning(
                "VIVIDLOPE (%s): UT slot data is missing stage_shuffle_order while stage shuffle is enabled. "
                "Tracker logic may be inaccurate.",
                self.player_name,
            )
    
    def generate_early(self) -> None:
        # Prevent generation failure if we exclude too many levels
        if self.options.goal_unlock >= 10 and ((self.options.exclude_finale and self.options.goal_condition != 0) or (self.options.exclude_level_x and self.options.goal_condition != 1)):
            logger.warning(f"VIVIDLOPE ({self.player_name}): Reduced goal unlock to 9 since too many levels are excluded")
            self.options.goal_unlock.value = 9
                    
        self.stage_shuffle_order = []

        slot_data = self._get_ut_slot_data()
        if slot_data:
            self._restore_ut_slot_data(slot_data)