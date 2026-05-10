# Object classes from AP that represent different types of options that you can create
from Options import Option, FreeText, NumericOption, Toggle, DefaultOnToggle, Choice, TextChoice, Range, NamedRange, OptionGroup, PerGameCommonOptions, Visibility
# These helper methods allow you to determine if an option has been set, or what its value is, for any player in the multiworld
from ..Helpers import is_option_enabled, get_option_value
from typing import Type, Any


####################################################################
# NOTE: At the time that options are created, Manual has no concept of the multiworld or its own world.
#       Options are defined before the world is even created.
#
# Example of creating your own option:
#
#   class MakeThePlayerOP(Toggle):
#       """Should the player be overpowered? Probably not, but you can choose for this to do... something!"""
#       display_name = "Make me OP"
#
#   options["make_op"] = MakeThePlayerOP
#
#
# Then, to see if the option is set, you can call is_option_enabled or get_option_value.
#####################################################################


# To add an option, use the before_options_defined hook below and something like this:
#   options["total_characters_to_win_with"] = TotalCharactersToWinWith
#
class Playground(Toggle):
    """This removes Challenges #1, #2, and #13 Locations."""
    display_name = "Exclude Tutorial Challenges?"

class BattleArenas(Toggle):
    """This adds Arena related items/locations"""
    display_name = "Include Arena Locations?"

class TimeTrials(Toggle):
    """This adds the Time Trial Checks for each Track"""
    display_name = "Include Time Trial Locations?"

class Elimination(Toggle):
    """This adds the Elimination Checks for each Track/Cup"""
    display_name = "Include Elimination Locations?"

class ArenaChallenges(Toggle):
    """This adds the Arena challenges found in Challenges"""
    display_name = "Include Arena Battles in Challenges?"

class TimeTrialChallenges(Toggle):
    """This adds the Time Trial challenges found in Challenges"""
    display_name = "Include Time Trials in Challenges?"

class EliminationChallenges(Toggle):
    """This adds the Elimination Race challenges found in Challenges"""
    display_name = "Include Elimination Races in Challenges?"

class CTR99(Toggle):
    """This adds all CTR related items/locations to the pool. (Affected by Time Trial/Elimination Options)"""
    display_name = "Include Crash Team Racing Tracks?"

class CTTR(Toggle):
    """This adds all CTTR related items/locations to the pool. (Affected by Time Trial/Elimination Options)"""
    display_name = "Include Crash Tag Team Racing Tracks?"

class CTRNF(Toggle):
    """This adds all CTR:NF related items/locations to the pool. (Affected by Time Trial/Elimination Options)"""
    display_name = "Include Crash Team Racing: Nitro-Fueled Tracks?"

class MKDD(Toggle):
    """This adds all MKDD related items/locations to the pool. (Affected by Time Trial/Elimination Options)"""
    display_name = "Include Mario Kart: Double Dash!! Tracks?"

class MKDS(Toggle):
    """This adds all MKDS related items/locations to the pool. (Affected by Time Trial/Elimination Options)"""
    display_name = "Include Mario Kart DS Tracks?"

class SR(Toggle):
    """This adds all Sonic Riders related items/locations to the pool. (Affected by Time Trial/Elimination Options)"""
    display_name = "Include Sonic Riders Tracks?"

class LR(Toggle):
    """This adds all LEGO Racers related items/locations to the pool. (Affected by Time Trial/Elimination Options)"""
    display_name = "Include LEGO Racers Tracks?"

class OriginalTracks(Toggle):
    """This adds all the Cups related to Original Tracks from the Steam Workshop. (Currently: Seren/KVBA)"""
    display_name = "Include Original Tracks?"

class Goal1(DefaultOnToggle):
    """Goal debug setting that disabled locations if goal1 is enabled"""

class Goal2(DefaultOnToggle):
    """Goal debug setting that disabled locations if goal2 is enabled"""

class Goal3(DefaultOnToggle):
    """Goal debug setting that disabled locations if goal3 is enabled"""

class Goal4(DefaultOnToggle):
    """Goal debug setting that disabled locations if goal4 is enabled"""

# This is called before any manual options are defined, in case you want to define your own with a clean slate or let Manual define over them
def before_options_defined(options: dict[str, Type[Option[Any]]]) -> dict[str, Type[Option[Any]]]:
    options["include_playground_challenges"] = Playground
    options["include_arenas"] = BattleArenas
    options["include_time_trials"] = TimeTrials
    options["include_elimination"] = Elimination
    options["include_arena_challenges"] = ArenaChallenges
    options["include_time_trial_challenges"] = TimeTrialChallenges
    options["include_elimination_challenges"] = EliminationChallenges
    options["include_ctr99"] = CTR99
    options["include_cttr"] = CTTR
    options["include_ctrnf"] = CTRNF
    options["include_mkdd"] = MKDD
    options["include_mkds"] = MKDS
    options["include_sr"] = SR
    options["include_lr"] = LR
    options["include_og"] = OriginalTracks
    options["goal1"] = Goal1
    options["goal2"] = Goal2
    options["goal3"] = Goal3
    options["goal4"] = Goal4
    return options

# This is called after any manual options are defined, in case you want to see what options are defined or want to modify the defined options
def after_options_defined(options: Type[PerGameCommonOptions]):
    # To access a modifiable version of options check the dict in options.type_hints
    # For example if you want to change DLC_enabled's display name you would do:
    # options.type_hints["DLC_enabled"].display_name = "New Display Name"

    #  Here's an example on how to add your aliases to the generated goal
    # options.type_hints['goal'].aliases.update({"example": 0, "second_alias": 1})
    # options.type_hints['goal'].options.update({"example": 0, "second_alias": 1})  #for an alias to be valid it must also be in options
    options.type_hints["goal1"].visibility = Visibility.none
    options.type_hints["goal2"].visibility = Visibility.none
    options.type_hints["goal3"].visibility = Visibility.none
    options.type_hints["goal4"].visibility = Visibility.none
    pass

# Use this Hook if you want to add your Option to an Option group (existing or not)
def before_option_groups_created(groups: dict[str, list[Type[Option[Any]]]]) -> dict[str, list[Type[Option[Any]]]]:
    # Uses the format groups['GroupName'] = [TotalCharactersToWinWith]
    return groups

def after_option_groups_created(groups: list[OptionGroup]) -> list[OptionGroup]:
    return groups
