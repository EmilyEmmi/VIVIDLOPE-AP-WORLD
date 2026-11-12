from .names import ItemNames
from rule_builder.rules import Has, HasAll, Rule, HasAny

class Stage:
    level: int
    stage: int
    req_items: Rule|None
    req_items_rank: Rule|None

    def __init__(self, level: int, stage: int, req_items: Rule|None = None, req_items_rank: Rule|None = None):
        self.level = level
        self.stage = stage
        self.req_items = req_items
        self.req_items_rank = req_items_rank

    def location_id(self) -> int:
        return self.level * 100 + (self.stage - 1)

stage_data: list[Stage] = [
    Stage(1, 1),
    Stage(1, 2),
    Stage(1, 3),
    Stage(1, 4),
    Stage(1, 5),
    Stage(1, 6),
    Stage(1, 7),
    Stage(1, 8),
    Stage(1, 9),
    Stage(1, 10),
    Stage(1, 11),
    Stage(1, 12),
    Stage(1, 13),
    Stage(1, 14),
    Stage(1, 15),
    Stage(2, 1),
    Stage(2, 2),
    Stage(2, 3),
    Stage(2, 4),
    Stage(2, 5),
    Stage(2, 6),
    Stage(2, 7),
    Stage(2, 8),
    Stage(2, 9),
    Stage(2, 10),
    Stage(2, 11),
    Stage(2, 12),
    Stage(2, 13),
    Stage(2, 14),
    Stage(2, 15),
    Stage(3, 1),
    Stage(3, 2),
    Stage(3, 3),
    Stage(3, 4),
    Stage(3, 5),
    Stage(3, 6),
    Stage(3, 7),
    Stage(3, 8),
    Stage(3, 9),
    Stage(3, 10),
    Stage(3, 11),
    Stage(3, 12),
    Stage(3, 13),
    Stage(3, 14),
    Stage(3, 15),
    Stage(4, 1),
    Stage(4, 2),
    Stage(4, 3),
    Stage(4, 4),
    Stage(4, 5, HasAny(ItemNames.wrap_unlock.value, ItemNames.stamp_unlock.value)), # spikes
    Stage(4, 6, HasAny(ItemNames.wrap_unlock.value, ItemNames.stamp_unlock.value)), # spikes
    Stage(4, 7),
    Stage(4, 8),
    Stage(4, 9, Has(ItemNames.wrap_unlock.value)), # spikes
    Stage(4, 10),
    Stage(4, 11),
    Stage(4, 12),
    Stage(4, 13, None, Has(ItemNames.stamp_unlock.value)), # spikes
    Stage(4, 14, None, Has(ItemNames.wrap_unlock.value)), # spikes
    Stage(4, 15),
    Stage(5, 1),
    Stage(5, 2),
    Stage(5, 3),
    Stage(5, 4),
    Stage(5, 5),
    Stage(5, 6),
    Stage(5, 7),
    Stage(5, 8),
    Stage(5, 9),
    Stage(5, 10),
    Stage(5, 11),
    Stage(5, 12),
    Stage(5, 13),
    Stage(5, 14),
    Stage(5, 15, None, HasAny(ItemNames.wrap_unlock.value, ItemNames.stamp_unlock.value)), # spikes
    Stage(6, 1),
    Stage(6, 2),
    Stage(6, 3),
    Stage(6, 4),
    Stage(6, 5, Has(ItemNames.superjump_unlock.value)),
    Stage(6, 6),
    Stage(6, 7),
    Stage(6, 8),
    Stage(6, 9),
    Stage(6, 10),
    Stage(6, 11),
    Stage(6, 12),
    Stage(6, 13),
    Stage(6, 14),
    Stage(6, 15),
    Stage(7, 1),
    Stage(7, 2),
    Stage(7, 3, Has(ItemNames.superjump_unlock.value)),
    Stage(7, 4),
    Stage(7, 5),
    Stage(7, 6, Has(ItemNames.stamp_unlock.value)), # spikes
    Stage(7, 7, None, Has(ItemNames.impact_unlock.value)),
    Stage(7, 8),
    Stage(7, 9),
    Stage(7, 10),
    Stage(7, 11),
    Stage(7, 12),
    Stage(7, 13),
    Stage(7, 14),
    Stage(7, 15),
    Stage(8, 1),
    Stage(8, 2),
    Stage(8, 3),
    Stage(8, 4),
    Stage(8, 5),
    Stage(8, 6),
    Stage(8, 7),
    Stage(8, 8),
    Stage(8, 9, None, HasAny(ItemNames.wrap_unlock.value, ItemNames.balloon_unlock.value)), # landmines
    Stage(8, 10),
    Stage(8, 11),
    Stage(8, 12),
    Stage(8, 13, None, HasAny(ItemNames.wrap_unlock.value, ItemNames.stamp_unlock.value)), # landmines
    Stage(8, 14, None, Has(ItemNames.stamp_unlock.value)), # landmines
    Stage(8, 15, Has(ItemNames.superjump_unlock.value)),
    Stage(9, 1),
    Stage(9, 2),
    Stage(9, 3),
    Stage(9, 4),
    Stage(9, 5, None, Has(ItemNames.wrap_unlock.value)), # landmines
    Stage(9, 6),
    Stage(9, 7),
    Stage(9, 8),
    Stage(9, 9),
    Stage(9, 10),
    Stage(9, 11),
    Stage(9, 12),
    Stage(9, 13),
    Stage(9, 14),
    Stage(9, 15),
    Stage(10, 1, HasAny(ItemNames.wrap_unlock.value, ItemNames.balloon_unlock.value, ItemNames.dash_unlock.value)), # spikes
    Stage(10, 2),
    Stage(10, 3),
    Stage(10, 4),
    Stage(10, 5),
    Stage(10, 6),
    Stage(10, 7, Has(ItemNames.superjump_unlock.value)),
    Stage(10, 8),
    Stage(10, 9, Has(ItemNames.impact_unlock.value)), # spikes
    Stage(10, 10),
    Stage(10, 11),
    Stage(10, 12, None, Has(ItemNames.stamp_unlock.value)), # spikes AND landmines
    Stage(10, 13, Has(ItemNames.superjump_unlock.value)),
    Stage(10, 14, None, Has(ItemNames.stamp_unlock.value)), # landmines
    Stage(10, 15),
    Stage(11, 1),
    Stage(11, 2),
    Stage(11, 3),
    Stage(11, 4),
    Stage(11, 5),
    Stage(11, 6),
    Stage(11, 7),
]

level_clear_count = [8, 10, 9, 8, 8, 9, 8, 10, 8, 15, 7]