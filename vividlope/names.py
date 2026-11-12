from enum import StrEnum

level_names: dict[int, str] = {
    0: "Level 1",
    1: "Level 2",
    2: "Level 3",
    3: "Level 4",
    4: "Level 5",
    5: "Level 6",
    6: "Level 7",
    7: "Level 8",
    8: "Level 9",
    9: "Level X",
    10: "Finale",
}
stage_prefixes: dict[int, str] = {
    0: "1-",
    1: "2-",
    2: "3-",
    3: "4-",
    4: "5-",
    5: "6-",
    6: "7-",
    7: "8-",
    8: "9-",
    9: "X-",
    10: "Finale Part ",
}

class LocationSuffix(StrEnum):
    level_clear = "Clear"

    stage_clear =   "Completion"
    stage_d =       "D Rank"
    stage_dp =      "D+ Rank"
    stage_c =       "C Rank"
    stage_cp =      "C+ Rank"
    stage_b =       "B Rank"
    stage_bp =      "B+ Rank"
    stage_a =       "A Rank"
    stage_ap =      "A+ Rank"
    stage_s =       "S Rank"
    stage_sp =      "S+ Rank"
    stage_v =       "V Rank"

    # Event items
    stage_clear_event = "Stage Clear Event"
    level_clear_event = "Level Clear Event"

class ItemNames(StrEnum):
    # Powerup Unlocks
    impact_unlock = "Impact Unlock"
    dash_unlock = "Dash Unlock"
    stamp_unlock = "Stamp Unlock"
    wrap_unlock = "Wrap Paper Unlock"
    balloon_unlock = "Paint Balloon Unlock"
    burst_unlock = "Paint Burst Unlock" # Shop exclusive
    bomb_unlock = "Bomb Unlock"
    insta_unlock = "Instabomb Unlock" # Level exclusive
    superjump_unlock = "Superjump Unlock" # Level exclusive
    max_power_unlock = "Max Power Unlock" # Shop exclusive
    good_shoes_unlock = "Good Shoes Unlock" # Shop exclusive
    shield_unlock = "Shield Unlock"

    # Filler unlocks
    impact_filler     = "[Filler]: Impact"
    dash_filler       = "[Filler]: Dash"
    stamp_filler      = "[Filler]: Stamp"
    wrap_filler       = "[Filler]: Wrap Paper"
    balloon_filler    = "[Filler]: Paint Balloon"
    burst_filler      = "[Filler]: Paint Burst"
    bomb_filler       = "[Filler]: Bomb"
    max_power_filler  = "[Filler]: Max Power"
    good_shoes_filler = "[Filler]: Good Shoes"
    extra_life_filler = "1UP"

    # Shop upgrades
    shop_upgrade = "Progressive Shop Upgrade"

    # Attires
    attire_1 =  "Attire 1 (Blue/White/Azure)"
    attire_2 =  "Attire 2 (Green/Red/Spearmint)"
    attire_3 =  "Attire 3 (Pink/Green/Lavender)"
    attire_4 =  "Attire 4 (Orange/Yellow/Chocolate)"
    attire_5 =  "Attire 5 (Purple/Blue/Amber)"
    attire_6 =  "Attire 6 (Beige/Gift Wrap/Silk)"
    attire_7 =  "Attire 7 (Denim)"
    attire_8 =  "Attire 8 (Tracksuit/Amaranth)"
    attire_9 =  "Attire 9 (Wooden/Mahogany)"
    attire_10 = "Attire 10 (Zig-Zag)"
    attire_11 = "Attire 11 (Buoy/Wet/Salmon)"
    attire_12 = "Attire 12 (Contrast/Camo)"
    attire_13 = "Attire 13 (Sunshine/Charcoal/Fiery)"
    attire_14 = "Attire 14 (Snowflake/Ice/Aurora)"
    attire_15 = "Attire 15 (Flannel/Polka Dot)"
    attire_16 = "Attire 16 (Elegant/Tin Foil/Slate)"
    attire_17 = "Attire 17 (Arcade/Moonlight)"
    attire_18 = "Attire 18 (Lollipop/Twist/Crimson)"
    attire_19 = "Attire 19 (Pastel/Chicken/Pop)"
    attire_20 = "Attire 20 (Angelic)"
    attire_21 = "Attire 21 (Hat/Banana/Cursed)"
    attire_22 = "Attire 22 (Noise)"
    attire_23 = "Attire 23 (Fuzzy/Gaudy)"
    attire_24 = "Attire 24 (Recycle/Vintage/Time)"
    attire_25 = "Attire 25 (Black/Golden/Red)"

    # Level element unlocks
    flowers = "Flowers"
    paint_rollers = "Paint Rollers"
    paint_buckets = "Paint Buckets"
    bubbles = "Bubbles"
    snowmen = "Snowmen"

    # Enemy traps
    enemy_trap_1 = "Blib Enemy Trap"
    enemy_trap_2 = "Draco Enemy Trap"
    enemy_trap_3 = "Fuse Enemy Trap"
    enemy_trap_4 = "Gero Enemy Trap"
    enemy_trap_5 = "Green Goo Enemy Trap"
    enemy_trap_6 = "Parrot Enemy Trap"
    enemy_trap_7 = "Prodigy Enemy Trap"
    enemy_trap_8 = "Remover Enemy Trap"
    enemy_trap_9 = "UFO Enemy Trap"
    enemy_trap_10 = "Vlad Enemy Trap"

    # Events
    level_clear_event = "Level Clear Event Item"