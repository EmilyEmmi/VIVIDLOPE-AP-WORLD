from dataclasses import dataclass

from Options import Choice, OptionGroup, PerGameCommonOptions, Range, Toggle, DefaultOnToggle

class DeathLink(Toggle):
    """
    When you get KOed, all other players with Deathlink enabled receive a death, and vice versa.
    """
    display_name = "DeathLink"

class DeathLinkAmnesty(Range):
    """
    You won't send a DeathLink until you are KOed this many times.
    Since it is very easy to get KOed in this game, playing with this set to 1 is not recommended.
    """
    display_name = "DeathLink Amnesty"
    range_start = 1
    range_end = 50
    default = 5

class GoalCondition(Choice):
    """
    The win/victory condition for this world.
    finale: Goal when the Finale is cleared.
    level_x: Goal when Level X is fully cleared.
    """
    display_name = "Goal Condition"
    option_finale = 0
    option_level_x = 1
    default = 0

class GoalUnlock(Range):
    """
    The number of levels you need to clear to automatically unlock your goal.
    If your goal condition is Level X, Finale counts as clearing a level.
    """
    display_name = "Clears Until Unlock"

    range_start = 1
    range_end = 10
    default = 6

class StageShuffle(Toggle):
    """
    Whether stages are shuffled to be in a random order.
    """
    display_name = "Shuffle Stages"


class ExcludeFinale(Toggle):
    """
    Excludes Finale from stage shuffle.
    If your goal is Level X, it is also excluded from the multiworld.
    """
    display_name = "Exclude Finale"


class ExcludeLevelX(DefaultOnToggle):
    """
    Excludes Level X from stage shuffle.
    If your goal is Finale, it is also excluded from the multiworld.
    """
    display_name = "Exclude Level X"


class RankChecks(Choice):
    """
    Splits Stage Completion checks into multiple checks depending on rank.
    You earn them by completing a level and reaching that rank or above.
    none: No rank checks, only one check for clearing the stage.
    partial: One check for clearing the stage, one check for reaching the max rank (defined by max_rank_check below).
    full: One check for each rank, starting from D rank up to the max rank, excluding include plus ranks with the exception of S+.
    NOTICE: Using full will SIGNIFICANTLY increase the number of locations (up to 11 times compared to none), so use with caution!
    """
    display_name = "Rank Checks"
    option_none = 0
    option_partial = 1
    option_full = 2
    default = 0

class MaxRankCheck(Choice):
    """
    The max rank expected for rank checks, from D-V. Earning a V rank requires playing in Hard.
    Plus ranks are written as (letter)p (Ex: S+ -> sp).
    """
    display_name = "Max Rank Check"
    option_d = 0
    option_dp = 1
    option_c = 2
    option_cp = 3
    option_b = 4
    option_bp = 5
    option_a = 6
    option_ap = 7
    option_s = 8
    option_sp = 9
    option_v = 10
    default = 8

class StartWithShield(DefaultOnToggle):
    """
    Start with the Shield power-up unlocked.
    """
    display_name = "Start With Shield"


class NerfedFinale(DefaultOnToggle):
    """
    Stages in Finale will have their usual percentage required in Stage Shuffle.
    When disabled, all tiles have to be flipped, which can be very tedious in some stages.
    """
    display_name = "Easier Finale in Stage Shuffle"


class ForcedCharacter(Choice):
    """
    Forces you to play as one of the three playable characters.
    off - You can choose anyone at the start.
    cerise - Play as Cerise.
    ecru - Play as Ecru.
    msnoir - Play as Ms. Noir.
    Note that Ms. Noir's 4 attacks are locked behind the powerups they are based on (Paint Balloon, Wrap Paper, Impact, and Dash), regardless of this option.
    """
    display_name = "Forced Character"
    option_off = 0
    option_cerise = 1
    option_ecru = 2
    option_msnoir = 3
    default = 0


class EarlyOffense(Choice):
    """
    Places a random offensive item in Sphere 1.
    off - Place all offensive items normally.
    on - Places Stamp Hammer, Impact, Dash, Wrap Paper, or Paint Balloon in Sphere 1.
    noir - Places one of the above, excluding Stamp Hammer (meaning you're guaranteed at least one of Ms Noir's attacks).
    """
    display_name = "Early Offensive Item"
    option_off = 0
    option_on = 1
    option_noir = 2
    default = 0


class TrapFillPercentage(Range):
    """
    Replace a percentage of filler items in the item pool with random traps.
    """
    display_name = "Trap Fill Percentage"
    range_start = 0
    range_end = 100
    default = 0


class BaseTrapWeight(Choice):
    """
    Base Class for Trap Weights
    """
    option_none = 0
    option_low = 1
    option_medium = 2
    option_high = 4
    default = 2


class BlibEnemyTrapWeight(BaseTrapWeight):
    """
    Likelihood of a receiving a trap which spawns a Blib.
    This is a fast ball-shaped enemy.
    """
    display_name = "Blib Enemy Trap Weight"


class DracoEnemyWeight(BaseTrapWeight):
    """
    Likelihood of a receiving a trap which spawns a Draco.
    This is a flying dragon-like enemy.
    """
    display_name = "Draco Enemy Trap Weight"


class FuseEnemyTrapWeight(BaseTrapWeight):
    """
    Likelihood of a receiving a trap which spawns a Fuse.
    This is a bomb-shaped enemy that chases the player and explodes.
    """
    display_name = "Fuse Enemy Trap Weight"


class GeroEnemyTrapWeight(BaseTrapWeight):
    """
    Likelihood of a receiving a trap which spawns a Gero.
    This is a fast frog-like enemy that chases the player.
    """
    display_name = "Gero Enemy Trap Weight"


class GreenGooEnemyTrapWeight(BaseTrapWeight):
    """
    Likelihood of a receiving a trap which spawns Green Goo.
    This is a green humanoid enemy that clones itself and drains power when touched.
    """
    display_name = "Green Goo Enemy Trap Weight"


class ParrotEnemyTrapWeight(BaseTrapWeight):
    """
    Likelihood of a receiving a trap which spawns a Parrot.
    This is a humanoid enemy that messes with the player's visuals.
    """
    display_name = "Parrot Enemy Trap Weight"


class ProdigyEnemyTrapWeight(BaseTrapWeight):
    """
    Likelihood of a receiving a trap which spawns a Prodigy.
    This is a fast, small heart-shaped enemy.
    """
    display_name = "Vlad Enemy Trap Weight"


class RemoverEnemyTrapWeight(BaseTrapWeight):
    """
    Likelihood of a receiving a trap which spawns a Remover.
    This is a blue X enemy that reverts tiles back to their original color.
    """
    display_name = "Remover Enemy Trap Weight"


class UFOEnemyTrapWeight(BaseTrapWeight):
    """
    Likelihood of a receiving a trap which spawns a UFO.
    This is a flying UFO-like enemy that spawns shockwaves.
    """
    display_name = "UFO Enemy Trap Weight"


class VladEnemyTrapWeight(BaseTrapWeight):
    """
    Likelihood of a receiving a trap which spawns a Vlad.
    This is a creepy-looking enemy that chases the player and spawns shockwaves.
    """
    display_name = "Vlad Enemy Trap Weight"


@dataclass
class VividlopeOptions(PerGameCommonOptions):
    deathlink: DeathLink
    deathlink_amnesty: DeathLinkAmnesty
    goal_condition: GoalCondition
    goal_unlock: GoalUnlock
    stage_shuffle: StageShuffle
    rank_checks: RankChecks
    max_rank_check: MaxRankCheck
    start_with_shield: StartWithShield
    nerfed_finale: NerfedFinale
    exclude_finale: ExcludeFinale
    exclude_level_x: ExcludeLevelX
    forced_character: ForcedCharacter
    early_offense: EarlyOffense
    trap_fill_percentage: TrapFillPercentage
    blib_enemy_trap_weight: BlibEnemyTrapWeight
    draco_enemy_trap_weight: DracoEnemyWeight
    fuse_enemy_trap_weight: FuseEnemyTrapWeight
    gero_enemy_trap_weight: GeroEnemyTrapWeight
    green_goo_enemy_trap_weight: GreenGooEnemyTrapWeight
    parrot_enemy_trap_weight: ParrotEnemyTrapWeight
    prodigy_enemy_trap_weight: ProdigyEnemyTrapWeight
    remover_enemy_trap_weight: RemoverEnemyTrapWeight
    ufo_enemy_trap_weight: UFOEnemyTrapWeight
    vlad_enemy_trap_weight: VladEnemyTrapWeight