from __future__ import annotations
from typing import TYPE_CHECKING
from BaseClasses import Item, ItemClassification
from .names import ItemNames, level_names
if TYPE_CHECKING:
    from .world import VividlopeWorld
import math

# There's so few items in this game I just decided to give them all IDs by hand
ITEM_NAME_TO_ID = {
    "Level 1 Unlock": 1,
    "Level 2 Unlock": 2,
    "Level 3 Unlock": 3,
    "Level 4 Unlock": 4,
    "Level 5 Unlock": 5,
    "Level 6 Unlock": 6,
    "Level 7 Unlock": 7,
    "Level 8 Unlock": 8,
    "Level 9 Unlock": 9,
    "Finale Unlock": 10,
    "Level X Unlock": 11,

    ItemNames.impact_unlock.value:     20,
    ItemNames.dash_unlock.value:       21,
    ItemNames.stamp_unlock.value:      22,
    ItemNames.wrap_unlock.value:       23,
    ItemNames.balloon_unlock.value:    24,
    ItemNames.burst_unlock.value:      25,
    ItemNames.bomb_unlock.value:       26,
    ItemNames.insta_unlock.value:      27,
    ItemNames.superjump_unlock.value:  28,
    ItemNames.max_power_unlock.value:  29,
    ItemNames.good_shoes_unlock.value: 30,
    ItemNames.shield_unlock.value:     31,

    ItemNames.shop_upgrade.value: 40,

    ItemNames.impact_filler.value:     50,
    ItemNames.dash_filler.value:       51,
    ItemNames.stamp_filler.value:      52,
    ItemNames.wrap_filler.value:       53,
    ItemNames.balloon_filler.value:    54,
    ItemNames.burst_filler.value:      55,
    ItemNames.bomb_filler.value:       56,
    ItemNames.max_power_filler.value:  57,
    ItemNames.good_shoes_filler.value: 58,
    ItemNames.extra_life_filler.value: 59,

    ItemNames.attire_1.value:         70,
    ItemNames.attire_2.value:         71,
    ItemNames.attire_3.value:         72,
    ItemNames.attire_4.value:         73,
    ItemNames.attire_5.value:         74,
    ItemNames.attire_6.value:         75,
    ItemNames.attire_7.value:         76,
    ItemNames.attire_8.value:         77,
    ItemNames.attire_9.value:         78,
    ItemNames.attire_10.value:        79,
    ItemNames.attire_11.value:        80,
    ItemNames.attire_12.value:        81,
    ItemNames.attire_13.value:        82,
    ItemNames.attire_14.value:        83,
    ItemNames.attire_15.value:        84,
    ItemNames.attire_16.value:        85,
    ItemNames.attire_17.value:        86,
    ItemNames.attire_18.value:        87,
    ItemNames.attire_19.value:        88,
    ItemNames.attire_20.value:        89,
    ItemNames.attire_21.value:        90,
    ItemNames.attire_22.value:        91,
    ItemNames.attire_23.value:        92,
    ItemNames.attire_24.value:        93,
    ItemNames.attire_25.value:        94,

    ItemNames.flowers.value:       100,
    ItemNames.paint_rollers.value: 101,
    ItemNames.paint_buckets.value: 102,
    ItemNames.bubbles.value:       103,
    ItemNames.snowmen.value:       104,

    ItemNames.enemy_trap_1.value:  110,
    ItemNames.enemy_trap_2.value:  111,
    ItemNames.enemy_trap_3.value:  112,
    ItemNames.enemy_trap_4.value:  113,
    ItemNames.enemy_trap_5.value:  114,
    ItemNames.enemy_trap_6.value:  115,
    ItemNames.enemy_trap_7.value:  116,
    ItemNames.enemy_trap_8.value:  117,
    ItemNames.enemy_trap_9.value:  118,
    ItemNames.enemy_trap_10.value: 119,
}

DEFAULT_ITEM_CLASSIFICATIONS = {
    "Level 1 Unlock": ItemClassification.progression,
    "Level 2 Unlock": ItemClassification.progression,
    "Level 3 Unlock": ItemClassification.progression,
    "Level 4 Unlock": ItemClassification.progression,
    "Level 5 Unlock": ItemClassification.progression,
    "Level 6 Unlock": ItemClassification.progression,
    "Level 7 Unlock": ItemClassification.progression,
    "Level 8 Unlock": ItemClassification.progression,
    "Level 9 Unlock": ItemClassification.progression,
    "Level X Unlock": ItemClassification.progression,
    "Finale Unlock": ItemClassification.progression,

    ItemNames.impact_unlock:     ItemClassification.progression,
    ItemNames.dash_unlock:       ItemClassification.progression,
    ItemNames.stamp_unlock:      ItemClassification.progression,
    ItemNames.wrap_unlock:       ItemClassification.progression,
    ItemNames.balloon_unlock:    ItemClassification.progression,
    ItemNames.burst_unlock:      ItemClassification.useful,
    ItemNames.bomb_unlock:       ItemClassification.useful,
    ItemNames.insta_unlock:      ItemClassification.useful,
    ItemNames.superjump_unlock:  ItemClassification.progression,
    ItemNames.max_power_unlock:  ItemClassification.useful,
    ItemNames.good_shoes_unlock: ItemClassification.useful,
    ItemNames.shield_unlock:     ItemClassification.useful,

    ItemNames.shop_upgrade: ItemClassification.progression,

    ItemNames.impact_filler:     ItemClassification.filler,
    ItemNames.dash_filler:       ItemClassification.filler,
    ItemNames.stamp_filler:      ItemClassification.filler,
    ItemNames.wrap_filler:       ItemClassification.filler,
    ItemNames.balloon_filler:    ItemClassification.filler,
    ItemNames.burst_filler:      ItemClassification.filler,
    ItemNames.bomb_filler:       ItemClassification.filler,
    ItemNames.max_power_filler:  ItemClassification.filler,
    ItemNames.good_shoes_filler: ItemClassification.filler,
    ItemNames.extra_life_filler: ItemClassification.useful,

    ItemNames.attire_1:          ItemClassification.filler,
    ItemNames.attire_2:          ItemClassification.filler,
    ItemNames.attire_3:          ItemClassification.filler,
    ItemNames.attire_4:          ItemClassification.filler,
    ItemNames.attire_5:          ItemClassification.filler,
    ItemNames.attire_6:          ItemClassification.filler,
    ItemNames.attire_7:          ItemClassification.filler,
    ItemNames.attire_8:          ItemClassification.filler,
    ItemNames.attire_9:          ItemClassification.filler,
    ItemNames.attire_10:         ItemClassification.filler,
    ItemNames.attire_11:         ItemClassification.filler,
    ItemNames.attire_12:         ItemClassification.filler,
    ItemNames.attire_13:         ItemClassification.filler,
    ItemNames.attire_14:         ItemClassification.filler,
    ItemNames.attire_15:         ItemClassification.filler,
    ItemNames.attire_16:         ItemClassification.filler,
    ItemNames.attire_17:         ItemClassification.filler,
    ItemNames.attire_18:         ItemClassification.filler,
    ItemNames.attire_19:         ItemClassification.filler,
    ItemNames.attire_20:         ItemClassification.filler,
    ItemNames.attire_21:         ItemClassification.filler,
    ItemNames.attire_22:         ItemClassification.filler,
    ItemNames.attire_23:         ItemClassification.filler,
    ItemNames.attire_24:         ItemClassification.filler,
    ItemNames.attire_25:         ItemClassification.filler,

    ItemNames.flowers:       ItemClassification.useful,
    ItemNames.paint_rollers: ItemClassification.useful,
    ItemNames.paint_buckets: ItemClassification.useful,
    ItemNames.bubbles:       ItemClassification.useful,
    ItemNames.snowmen:       ItemClassification.useful,

    ItemNames.enemy_trap_1:  ItemClassification.trap,
    ItemNames.enemy_trap_2:  ItemClassification.trap,
    ItemNames.enemy_trap_3:  ItemClassification.trap,
    ItemNames.enemy_trap_4:  ItemClassification.trap,
    ItemNames.enemy_trap_5:  ItemClassification.trap,
    ItemNames.enemy_trap_6:  ItemClassification.trap,
    ItemNames.enemy_trap_7:  ItemClassification.trap,
    ItemNames.enemy_trap_8:  ItemClassification.trap,
    ItemNames.enemy_trap_9:  ItemClassification.trap,
    ItemNames.enemy_trap_10: ItemClassification.trap,
}

class VividlopeItem(Item):
    game = "VIVIDLOPE"

def get_random_filler_item_name(world: VividlopeWorld) -> str:
    random = world.random.randint(0, 9)
    filler = [
        ItemNames.impact_filler,
        ItemNames.dash_filler,
        ItemNames.stamp_filler,
        ItemNames.wrap_filler,
        ItemNames.balloon_filler,
        ItemNames.burst_filler,
        ItemNames.bomb_filler,
        ItemNames.max_power_filler,
        ItemNames.good_shoes_filler,
        ItemNames.extra_life_filler, # Might be too common?
    ]
    return filler[random]

def create_item_with_correct_classification(world: VividlopeWorld, name: str) -> VividlopeItem:
    classification = DEFAULT_ITEM_CLASSIFICATIONS[name]
    return VividlopeItem(name, classification, ITEM_NAME_TO_ID[name], world.player)

def create_all_items(world: VividlopeWorld) -> None:
    itempool: list[Item] = [
        world.create_item(ItemNames.impact_unlock),
        world.create_item(ItemNames.dash_unlock),
        world.create_item(ItemNames.stamp_unlock),
        world.create_item(ItemNames.wrap_unlock),
        world.create_item(ItemNames.balloon_unlock),
        world.create_item(ItemNames.burst_unlock),
        world.create_item(ItemNames.bomb_unlock),
        world.create_item(ItemNames.insta_unlock),
        world.create_item(ItemNames.superjump_unlock),
        world.create_item(ItemNames.max_power_unlock),
        world.create_item(ItemNames.good_shoes_unlock),

        world.create_item(ItemNames.shop_upgrade),
        world.create_item(ItemNames.shop_upgrade),
        world.create_item(ItemNames.shop_upgrade),
        world.create_item(ItemNames.shop_upgrade),
        world.create_item(ItemNames.shop_upgrade),

        world.create_item(ItemNames.attire_1.value),
        world.create_item(ItemNames.attire_2.value),
        world.create_item(ItemNames.attire_3.value),
        world.create_item(ItemNames.attire_4.value),
        world.create_item(ItemNames.attire_5.value),
        world.create_item(ItemNames.attire_6.value),
        world.create_item(ItemNames.attire_7.value),
        world.create_item(ItemNames.attire_8.value),
        world.create_item(ItemNames.attire_9.value),
        world.create_item(ItemNames.attire_10.value),
        world.create_item(ItemNames.attire_11.value),
        world.create_item(ItemNames.attire_12.value),
        world.create_item(ItemNames.attire_13.value),
        world.create_item(ItemNames.attire_14.value),
        world.create_item(ItemNames.attire_15.value),
        world.create_item(ItemNames.attire_16.value),
        world.create_item(ItemNames.attire_17.value),
        world.create_item(ItemNames.attire_18.value),
        world.create_item(ItemNames.attire_19.value),
        world.create_item(ItemNames.attire_20.value),
        world.create_item(ItemNames.attire_21.value),
        world.create_item(ItemNames.attire_22.value),
        world.create_item(ItemNames.attire_23.value),
        world.create_item(ItemNames.attire_24.value),
        world.create_item(ItemNames.attire_25.value),

        world.create_item(ItemNames.flowers.value),
        world.create_item(ItemNames.paint_rollers.value),
        world.create_item(ItemNames.paint_buckets.value),
        world.create_item(ItemNames.bubbles.value),
        world.create_item(ItemNames.snowmen.value),
    ]

    # Create shield unlock; possibly add it to your starting inventory
    shield_item = world.create_item(ItemNames.shield_unlock)
    if world.options.start_with_shield:
        world.push_precollected(shield_item)
    else:
        itempool.append(shield_item)

    # Handle the Early Offensive Item option
    if world.options.early_offense != 0:
        offensive_items = [
            ItemNames.impact_unlock,
            ItemNames.dash_unlock,
            ItemNames.wrap_unlock,
            ItemNames.balloon_unlock,
            ItemNames.stamp_unlock,
        ]
        # Don't include Stamp Hammer if Noir option is set
        if world.options.early_offense == 2:
            offensive_items.pop()

        # Give one offensive item at random
        world.multiworld.early_items[world.player][world.random.choice(offensive_items)] = 1

    # Give the player a random level to start so they don't have 0 checks at the start of their game
    # We can only pick Level X as the starting level if Finale is our goal and it isn't excluded (Finale can never be the starting level)
    if (world.options.goal_condition == 1 or world.options.exclude_level_x):
        random_starting_level = world.random.randint(0, 8)
    else:
        random_starting_level = world.random.randint(0, 9)

    for i in range(0, 11):
        # Skip creating the unlock for the goal world since we wont need it
        if (i == 10 and world.options.goal_condition == 0) or (  # Finale
            i == 9 and world.options.goal_condition == 1):  # Level X
            continue

        # Skip creating unlock for excluded levels
        if (i == 10 and world.options.exclude_finale) or (  # Finale
            i == 9 and world.options.exclude_level_x):  # Level X
            continue

        unlock_item = world.create_item(f"{level_names[i]} Unlock")
        if i == random_starting_level:
            world.push_precollected(unlock_item)
        else:
            itempool.append(unlock_item)

    number_of_items = len(itempool)
    number_of_unfilled_locations = len(world.multiworld.get_unfilled_locations(world.player))
    needed_number_of_filler_items = number_of_unfilled_locations - number_of_items

    # Replace percentage of filler with traps
    if (world.options.trap_fill_percentage != 0):
        trap_weights = []
        trap_weights += ([ItemNames.enemy_trap_1] * world.options.blib_enemy_trap_weight.value)
        trap_weights += ([ItemNames.enemy_trap_2] * world.options.draco_enemy_trap_weight.value)
        trap_weights += ([ItemNames.enemy_trap_3] * world.options.fuse_enemy_trap_weight.value)
        trap_weights += ([ItemNames.enemy_trap_4] * world.options.gero_enemy_trap_weight.value)
        trap_weights += ([ItemNames.enemy_trap_5] * world.options.green_goo_enemy_trap_weight.value)
        trap_weights += ([ItemNames.enemy_trap_6] * world.options.parrot_enemy_trap_weight.value)
        trap_weights += ([ItemNames.enemy_trap_7] * world.options.prodigy_enemy_trap_weight.value)
        trap_weights += ([ItemNames.enemy_trap_8] * world.options.remover_enemy_trap_weight.value)
        trap_weights += ([ItemNames.enemy_trap_9] * world.options.ufo_enemy_trap_weight.value)
        trap_weights += ([ItemNames.enemy_trap_10] * world.options.vlad_enemy_trap_weight.value)
        trap_count = 0 if (len(trap_weights) == 0) else math.ceil(needed_number_of_filler_items * (world.options.trap_fill_percentage.value / 100.0))
        needed_number_of_filler_items -= trap_count
        trap_pool = []
        for i in range(trap_count):
            trap_item = world.random.choice(trap_weights)
            trap_pool.append(world.create_item(trap_item))
        itempool += trap_pool

    itempool += [world.create_filler() for _ in range(needed_number_of_filler_items)]

    world.multiworld.itempool += itempool