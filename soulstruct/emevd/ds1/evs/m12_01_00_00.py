"""
linked:


strings:

"""
from soulstruct.emevd.ds1 import *


@NeverRestart
def Constructor():
    """ 0: Event 0 """
    RunEvent(11210700)
    SkipLinesIfClient(10)
    DisableObject(1211988)
    DeleteFX(1211989, erase_root_only=False)
    DisableObject(1211994)
    DeleteFX(1211995, erase_root_only=False)
    DisableObject(1211996)
    DeleteFX(1211997, erase_root_only=False)
    DisableObject(1211998)
    DeleteFX(1211999, erase_root_only=False)
    DisableObject(1211986)
    DeleteFX(1211987, erase_root_only=False)
    DisableHitbox(1213061)
    SkipLinesIfFlagOff(2, 11210539)
    EnableHitbox(1213061)
    DisableHitbox(1213060)
    RunEvent(11215090)
    RunEvent(11215091)
    RunEvent(11215092)
    DisableMapSound(1213800)
    SkipLinesIfFlagOff(6, 11210000)
    RunEvent(11210000)
    DisableObject(1211790)
    DeleteFX(1211791, erase_root_only=False)
    DisableObject(1211792)
    DeleteFX(1211793, erase_root_only=False)
    SkipLines(8)
    RunEvent(11215000)
    RunEvent(11215001)
    RunEvent(11215002)
    RunEvent(11215003)
    RunEvent(11215004)
    RunEvent(11215005)
    RunEvent(11210000)
    RunEvent(11215006, slot=0, args=(1210810, 1210800, 34720000))
    RunEvent(11215006, slot=1, args=(1210811, 1210801, 34720010))
    RunEvent(11215006, slot=2, args=(1210812, 1210802, 34720020))
    RunEvent(11215007)
    RunEvent(11215008)
    RunEvent(11215009)
    DisableMapSound(1213801)
    SkipLinesIfFlagOff(7, 11210001)
    RunEvent(11210001)
    DisableObject(1211890)
    DeleteFX(1211891, erase_root_only=False)
    DisableObject(1211892)
    DeleteFX(1211893, erase_root_only=False)
    DisableHitbox(1213001)
    SkipLines(7)
    RunEvent(11215010)
    RunEvent(11215011)
    RunEvent(11215012)
    RunEvent(11215013)
    RunEvent(11215014)
    RunEvent(11215015)
    RunEvent(11210001)
    DisableMapSound(1213802)
    SkipLinesIfFlagOff(4, 11210002)
    RunEvent(11210002)
    DisableObject(1211990)
    DeleteFX(1211991, erase_root_only=False)
    SkipLines(8)
    RunEvent(11215020)
    RunEvent(11215021)
    RunEvent(11215022)
    RunEvent(11215027)
    RunEvent(11215023)
    RunEvent(11215024)
    RunEvent(11215025)
    RunEvent(11210002)
    RunEvent(11215026)
    DisableMapSound(1213803)
    IfFlagOn(1, 11210592)
    IfFlagOff(1, 11210004)
    SkipLinesIfConditionTrue(3, 1)
    DisableObject(1211690)
    DeleteFX(1211691, erase_root_only=False)
    DisableHitbox(1213001)
    SkipLinesIfFlagOn(8, 11210004)
    RunEvent(11215060)
    RunEvent(11215061)
    RunEvent(11215062)
    RunEvent(11215063)
    RunEvent(11215064)
    RunEvent(11215066)
    RunEvent(11215065)
    RunEvent(11210005)
    SkipLinesIfFlagOff(1, 11210002)
    RegisterBonfire(11210992, obj=1211950, reaction_distance=2.0, reaction_angle=180.0, initial_kindle_level=0)
    RegisterBonfire(11210984, obj=1211963, reaction_distance=2.0, reaction_angle=180.0, initial_kindle_level=0)
    RegisterBonfire(11210976, obj=1211961, reaction_distance=2.0, reaction_angle=180.0, initial_kindle_level=0)
    RegisterBonfire(11210968, obj=1211962, reaction_distance=2.0, reaction_angle=180.0, initial_kindle_level=0)
    RegisterBonfire(11210960, obj=1211964, reaction_distance=2.0, reaction_angle=180.0, initial_kindle_level=0)
    RegisterLadder(start_climbing_flag=11210210, stop_climbing_flag=11210211, obj=1211110)
    RegisterLadder(start_climbing_flag=11210212, stop_climbing_flag=11210213, obj=1211111)
    RegisterLadder(start_climbing_flag=11210214, stop_climbing_flag=11210215, obj=1211112)
    RunEvent(11215100)
    RunEvent(11215110, slot=0, args=(1210101, 1212502, 0.0, 1212502), arg_types='iifi')
    RunEvent(11215110, slot=1, args=(1210102, 1212502, 0.0, 1212502), arg_types='iifi')
    RunEvent(11215110, slot=2, args=(1210103, 1212502, 10.0, 1212506), arg_types='iifi')
    RunEvent(11215110, slot=3, args=(1210104, 1212502, 10.0, 1212506), arg_types='iifi')
    RunEvent(11215115, slot=0, args=(1210101, 1212502, 1212501))
    RunEvent(11215115, slot=1, args=(1210102, 1212502, 1212501))
    RunEvent(11215120, slot=0, args=(1210105, 1210106, 1210107, 51210030))
    RunEvent(11215140, slot=0, args=(1210150, 1212503, 1212504, 1212505, 11215151, 11215152, 11215153))
    RunEvent(11215140, slot=1, args=(1210151, 1212523, 1212524, 1212525, 11215154, 11215155, 11215156))
    RunEvent(11210050)
    RunEvent(11210051)
    RunEvent(11210052)
    RunEvent(11210053)
    RunEvent(11210054)
    RunEvent(11210055)
    RunEvent(11210056)
    RunEvent(11210057)
    RunEvent(11210040)
    RunEvent(11210041)
    RunEvent(11210042)
    RunEvent(11210043)
    RunEvent(11210004)
    RunEvent(11215050)
    RunEvent(11215051)
    RunEvent(11215052)
    RunEvent(11210025)
    RunEvent(11210021)
    RunEvent(11215040)
    RunEvent(11215041)
    RunEvent(11210020)
    RunEvent(11215043)
    RunEvent(11215044)
    RunEvent(11210330, slot=0, args=(11210310, 11210315, 11210330))
    RunEvent(11210310, slot=0, args=(1210300, 11210310))
    RunEvent(11210310, slot=1, args=(1210301, 11210311))
    RunEvent(11210310, slot=2, args=(1210302, 11210312))
    RunEvent(11210310, slot=3, args=(1210303, 11210313))
    RunEvent(11210310, slot=4, args=(1210304, 11210314))
    RunEvent(11210310, slot=5, args=(1210305, 11210315))
    RunEvent(11210600, slot=0, args=(1211600, 11210600))
    RunEvent(11210600, slot=1, args=(1211601, 11210601))
    RunEvent(11210600, slot=2, args=(1211602, 11210602))
    RunEvent(11210600, slot=4, args=(1211604, 11210604))
    RunEvent(11210600, slot=5, args=(1211605, 11210605))
    RunEvent(11210230, slot=0, args=(1211210, 1211650, 125, 126))
    RunEvent(11210350, slot=0, args=(1210200, 33007200))
    RunEvent(11210350, slot=1, args=(1210201, 33007000))
    RunEvent(11210350, slot=2, args=(1210202, 33007100))
    RunEvent(11210350, slot=3, args=(1210203, 33007300))
    RunEvent(11210350, slot=4, args=(1210204, 33007100))
    RunEvent(11210350, slot=5, args=(1210260, 41601000))
    RunEvent(11210100)
    RunEvent(11210103)
    RunEvent(11210110)
    RunEvent(11210120)
    RunEvent(11210123)
    RunEvent(11210130)
    RunEvent(11210133)
    RunEvent(11210140)
    RunEvent(11210150)
    RunEvent(11210170, slot=0, args=(11215220, 1213050, 1212105))
    RunEvent(11210170, slot=1, args=(11215221, 1213051, 1212115))
    RunEvent(11210170, slot=2, args=(11215222, 1213052, 1212125))
    RunEvent(11210170, slot=3, args=(11215223, 1213053, 1212135))
    RunEvent(11210170, slot=4, args=(11215224, 1213054, 1212145))
    DisableMapSound(1213810)
    DisableMapSound(1213811)
    RunEvent(11210200, slot=0, args=(1211200, 1212200))
    RunEvent(11210200, slot=1, args=(1211201, 1212201))
    RunEvent(11210205, slot=0, args=(1211200, 1212200, 11210200))
    RunEvent(11210205, slot=1, args=(1211201, 1212201, 11210201))
    RunEvent(11210300)
    RunEvent(11215250, slot=0, args=(1211300, 1213160))
    RunEvent(11215250, slot=1, args=(1211301, 1213161))
    RunEvent(11215250, slot=2, args=(1211302, 1213162))
    RunEvent(11215250, slot=3, args=(1211303, 1213163))
    RunEvent(11215250, slot=4, args=(1211304, 1213164))
    RunEvent(11215250, slot=5, args=(1211305, 1213165))
    RunEvent(11215250, slot=6, args=(1211306, 1213166))
    RunEvent(11215250, slot=7, args=(1211307, 1213167))
    RunEvent(11215250, slot=8, args=(1211308, 1213168))
    RunEvent(11215250, slot=9, args=(1211309, 1213169))
    RunEvent(11215250, slot=10, args=(1211310, 1213170))
    RunEvent(11215250, slot=11, args=(1211311, 1213171))
    RunEvent(11215250, slot=12, args=(1211312, 1213172))
    RunEvent(11215250, slot=13, args=(1211313, 1213173))
    RunEvent(11215250, slot=14, args=(1211314, 1213174))
    RunEvent(11215250, slot=15, args=(1211315, 1213175))
    RunEvent(11215250, slot=16, args=(1211316, 1213176))
    RunEvent(11215250, slot=17, args=(1211317, 1213177))
    RunEvent(11215250, slot=18, args=(1211318, 1213178))
    RunEvent(11215250, slot=19, args=(1211319, 1213179))
    RunEvent(11215250, slot=20, args=(1211320, 1213180))
    RunEvent(11215250, slot=21, args=(1211321, 1213181))
    RunEvent(11215250, slot=22, args=(1211322, 1213182))
    RunEvent(11215250, slot=23, args=(1211323, 1213183))
    RunEvent(11215160, slot=0, args=(1210600,))
    RunEvent(11215165, slot=0, args=(1210600,))
    RunEvent(11215170, slot=0, args=(1210600,))
    RunEvent(11215175, slot=0, args=(1210600,))
    RunEvent(11215180, slot=0, args=(1210600, 1212180))
    RunEvent(11210680, slot=0, args=(1210600,))
    RunEvent(11215185, slot=0, args=(1210600,))
    SetNetworkUpdateRate(1210601, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    RunEvent(11215160, slot=1, args=(1210601,))
    RunEvent(11215165, slot=1, args=(1210601,))
    RunEvent(11215170, slot=1, args=(1210601,))
    RunEvent(11215175, slot=1, args=(1210601,))
    RunEvent(11215180, slot=1, args=(1210601, 1212181))
    RunEvent(11210680, slot=1, args=(1210601,))
    RunEvent(11215185, slot=1, args=(1210601,))


@NeverRestart
def Preconstructor():
    """ 50: Event 50 """
    DisableCharacter(6731)
    RunEvent(11215030, slot=1, args=(6732, 11215036, 11215035, 11210901, 1212082, 1212083, 11215032, 11210900))
    RunEvent(11210900, slot=0, args=(6731,))
    RunEvent(11210900, slot=1, args=(6732,))
    RunEvent(11210905, slot=0, args=(6731, 11215035, 1212080, 1213030, 11210900, 11215032))
    RunEvent(11210905, slot=1, args=(6732, 11215036, 1212082, 1213031, 11210901, 11215033))
    RunEvent(11210510, slot=0, args=(6720, 1822))
    RunEvent(11210520, slot=0, args=(6720, 1820, 1839, 1823))
    RunEvent(11210530, slot=0, args=(6720, 1820, 1839, 1821))
    RunEvent(11210535)
    RunEvent(11210910)
    RunEvent(11210912)
    RunEvent(11210915)
    SkipLinesIfFlagOff(2, 1842)
    DisableObject(1211130)
    DeleteFX(1213150, erase_root_only=False)
    RunEvent(11210510, slot=1, args=(6730, 1841))
    RunEvent(11210520, slot=1, args=(6730, 1840, 1859, 1842))
    RunEvent(11210544)
    RunEvent(11210538)
    RunEvent(11210520, slot=2, args=(6750, 1870, 1889, 1872))
    SkipLinesIfFlagOn(1, 11210001)
    DisableObject(1211220)
    IfFlagOn(-1, 1861)
    IfFlagOn(-1, 1862)
    SkipLinesIfConditionTrue(1, -1)
    DisableCharacter(6740)
    RunEvent(11210510, slot=3, args=(6740, 1863))
    RunEvent(11210520, slot=3, args=(6740, 1860, 1869, 1864))
    RunEvent(11210531, slot=0, args=(6740, 1860, 1869, 1861))
    RunEvent(11210532, slot=0, args=(6740, 1860, 1869, 1862))
    RunEvent(11210533, slot=0, args=(6740, 1860, 1869, 1865))
    RunEvent(11210534, slot=0, args=(6740, 1860, 1869, 1865))
    RunEvent(11210543)
    DisableCharacter(6700)
    SkipLinesIfClient(3)
    RunEvent(11210540)
    RunEvent(11210541)
    RunEvent(11210542)
    SkipLinesIfFlagOn(1, 11210345)
    DisableFlagRange((11210340, 11210345))
    DisableGravity(6760)
    EnableImmortality(6760)
    DisableHealthBar(6760)
    AddSpecialEffect(6760, 5300)
    EnableObjectInvulnerability(1211250)
    RunEvent(11210340)
    RunEvent(11210341)
    RunEvent(11210345)
    RunEvent(11210346)
    RunEvent(11210347)
    EndOfAnimation(1211606, 0)
    EndOfAnimation(1211607, 0)
    RunEvent(11217000)
    RunEvent(11210015)


@NeverRestart
def Event11210090(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int, ARG_12_15: int):
    """ 11210090: Event 11210090 """
    SkipLinesIfThisEventSlotOff(3)
    DisableObject(ARG_0_3)
    DeleteFX(ARG_4_7, erase_root_only=False)
    End()
    IfDialogPromptActivated(1, prompt_text=10010403, anchor_entity=ARG_8_11, anchor_type=MapEntityType.Region, facing_angle=0.0, max_distance=0.0, model_point=0, human_or_hollow_only=True, line_intersects=ARG_0_3)
    IfDialogPromptActivated(2, prompt_text=10010407, anchor_entity=ARG_12_15, anchor_type=MapEntityType.Region, facing_angle=0.0, max_distance=0.0, model_point=0, human_or_hollow_only=True, line_intersects=ARG_0_3)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionTrue(2, 2)
    Move(PLAYER, destination=ARG_8_11, destination_type=MapEntityType.Region, model_point=-1, short_move=True)
    SkipLines(1)
    Move(PLAYER, destination=ARG_12_15, destination_type=MapEntityType.Region, model_point=-1, short_move=True)
    ForceAnimation(PLAYER, 7410)
    DisableObject(ARG_0_3)
    DeleteFX(ARG_4_7, erase_root_only=True)


@RestartOnRest
def Event11215090():
    """ 11215090: Event 11215090 """
    EndIfThisEventOn()
    DisableCharacter(1210900)
    DisableCharacter(1210901)
    DisableCharacter(1210902)
    DisableCharacter(1210903)
    DisableCharacter(1210904)
    DisableCharacter(1210905)
    DisableCharacter(1210906)
    DisableCharacter(1210907)
    DisableCharacter(1210908)
    DisableCharacter(1210909)
    DisableCharacter(1210910)
    DisableCharacter(1210911)
    DisableCharacter(1210912)
    DisableCharacter(1210913)
    DisableCharacter(1210914)
    DisableCharacter(1210915)
    DisableCharacter(1210916)
    DisableCharacter(1210917)
    DisableCharacter(1210918)
    DisableCharacter(1210919)
    DisableCharacter(1210920)
    DisableCharacter(1210921)
    DisableCharacter(1210922)
    DisableCharacter(1210923)
    DisableCharacter(1210924)
    DisableCharacter(1210925)
    IfFlagOn(0, 11210080)
    EndIfFlagOn(735)
    EnableFlag(5000)
    EnableCharacter(1210900)
    EnableCharacter(1210901)
    EnableCharacter(1210902)
    EnableCharacter(1210903)
    EnableCharacter(1210904)
    EnableCharacter(1210905)
    EnableCharacter(1210906)
    EnableCharacter(1210907)
    EnableCharacter(1210908)
    EnableCharacter(1210909)
    EnableCharacter(1210910)
    EnableCharacter(1210911)
    EnableCharacter(1210912)
    EnableCharacter(1210913)
    EnableCharacter(1210914)
    EnableCharacter(1210915)
    EnableCharacter(1210916)
    EnableCharacter(1210917)
    EnableCharacter(1210918)
    EnableCharacter(1210919)
    EnableCharacter(1210920)
    EnableCharacter(1210921)
    EnableCharacter(1210922)
    EnableCharacter(1210923)
    EnableCharacter(1210924)
    EnableCharacter(1210925)


@RestartOnRest
def Event11215091():
    """ 11215091: Event 11215091 """
    IfFlagOn(-1, 11215095)
    IfFlagOn(-1, 735)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFlagOff(1, 735)
    DisableFlag(735)
    DisableFlag(11210080)
    DisableFlag(11215095)
    EnableFlag(5001)
    Kill(1210900, award_souls=False)
    Kill(1210901, award_souls=False)
    Kill(1210902, award_souls=False)
    Kill(1210903, award_souls=False)
    Kill(1210904, award_souls=False)
    Kill(1210905, award_souls=False)
    Kill(1210906, award_souls=False)
    Kill(1210907, award_souls=False)
    Kill(1210908, award_souls=False)
    Kill(1210909, award_souls=False)
    Kill(1210910, award_souls=False)
    Kill(1210911, award_souls=False)
    Kill(1210912, award_souls=False)
    Kill(1210913, award_souls=False)
    Kill(1210914, award_souls=False)
    Kill(1210915, award_souls=False)
    Kill(1210916, award_souls=False)
    Kill(1210917, award_souls=False)
    Kill(1210918, award_souls=False)
    Kill(1210919, award_souls=False)
    Kill(1210920, award_souls=False)
    Kill(1210921, award_souls=False)
    Kill(1210922, award_souls=False)
    Kill(1210923, award_souls=False)
    Kill(1210924, award_souls=False)
    Kill(1210925, award_souls=False)


@RestartOnRest
def Event11215092():
    """ 11215092: Event 11215092 """
    EndIfClient()
    IfBlackWorldTendencyComparison(1, comparison_type=ComparisonType.GreaterThan, value=50)
    IfInsideMap(1, game_map=OOLACILE)
    IfConditionTrue(-1, input_condition=1)
    IfFlagOn(-1, 11210080)
    IfConditionTrue(0, input_condition=-1)
    WaitFrames(1)
    IfBlackWorldTendencyComparison(2, comparison_type=ComparisonType.GreaterThan, value=50)
    IfInsideMap(2, game_map=OOLACILE)
    IfConditionTrue(-2, input_condition=2)
    IfFlagOn(-2, 11210080)
    RestartIfConditionFalse(-2)
    WaitFrames(1)
    IfBlackWorldTendencyComparison(3, comparison_type=ComparisonType.GreaterThan, value=50)
    IfInsideMap(3, game_map=OOLACILE)
    IfConditionTrue(-3, input_condition=3)
    IfFlagOn(-3, 11210080)
    RestartIfConditionFalse(-3)
    WaitFrames(1)
    IfBlackWorldTendencyComparison(4, comparison_type=ComparisonType.GreaterThan, value=50)
    IfInsideMap(4, game_map=OOLACILE)
    IfConditionTrue(-4, input_condition=4)
    IfFlagOn(-4, 11210080)
    RestartIfConditionFalse(-4)
    WaitFrames(1)
    IfBlackWorldTendencyComparison(5, comparison_type=ComparisonType.GreaterThan, value=50)
    IfInsideMap(5, game_map=OOLACILE)
    IfConditionTrue(-5, input_condition=5)
    IfFlagOn(-5, 11210080)
    RestartIfConditionFalse(-5)
    WaitFrames(1)
    IfBlackWorldTendencyComparison(6, comparison_type=ComparisonType.GreaterThan, value=50)
    IfInsideMap(6, game_map=OOLACILE)
    IfConditionTrue(-6, input_condition=6)
    IfFlagOn(-6, 11210080)
    RestartIfConditionFalse(-6)
    EnableFlag(11210080)
    Wait(600.0)
    IfBlackWorldTendencyComparison(7, comparison_type=ComparisonType.LessThanOrEqual, value=50)
    IfInsideMap(7, game_map=OOLACILE)
    RestartIfConditionFalse(7)
    DisableFlag(11210080)
    EnableFlag(11215095)


@RestartOnRest
def Event11215000():
    """ 11215000: Event 11215000 """
    IfFlagOff(1, 11210000)
    IfDialogPromptActivated(1, prompt_text=10010403, anchor_entity=1212888, anchor_type=MapEntityType.Region, facing_angle=0.0, max_distance=0.0, human_or_hollow_only=True, line_intersects=1211790, boss_version=True)
    IfConditionTrue(0, input_condition=1)
    RotateToFaceEntity(PLAYER, 1212887)
    ForceAnimation(PLAYER, 7410, wait_for_completion=True)
    Restart()


@NeverRestart
def Event11215001():
    """ 11215001: Event 11215001 """
    IfFlagOff(1, 11210000)
    IfFlagOn(1, 11215003)
    IfCharacterType(1, PLAYER, CharacterType.WhitePhantom)
    IfDialogPromptActivated(1, prompt_text=10010403, anchor_entity=1212888, anchor_type=MapEntityType.Region, facing_angle=0.0, max_distance=0.0, human_or_hollow_only=False, line_intersects=1211790)
    IfConditionTrue(0, input_condition=1)
    RotateToFaceEntity(PLAYER, 1212887)
    ForceAnimation(PLAYER, 7410)
    Restart()


@NeverRestart
def Event11215002():
    """ 11215002: Event 11215002 """
    SkipLinesIfThisEventOn(3)
    IfFlagOff(1, 11210000)
    IfCharacterInsideRegion(1, PLAYER, region=1212886)
    IfConditionTrue(0, input_condition=1)
    SkipLinesIfClient(2)
    NotifyBossBattleStart()
    SetNetworkUpdateAuthority(1210800, UpdateAuthority.Forced)
    ActivateMultiplayerBuffs(1210800)


@RestartOnRest
def Event11215003():
    """ 11215003: Event 11215003 """
    SkipLinesIfThisEventOn(5)
    DisableAI(1210800)
    IfFlagOn(1, 11215002)
    IfCharacterInsideRegion(1, PLAYER, region=1212886)
    IfConditionTrue(0, input_condition=1)
    EnableAI(1210800)
    EnableBossHealthBar(1210800, name=3471, slot=0)
    ForceAnimation(1210800, 3017, wait_for_completion=True)


@NeverRestart
def Event11215004():
    """ 11215004: Event 11215004 """
    DisableNetworkSync()
    IfFlagOff(1, 11210000)
    IfFlagOn(1, 11215003)
    SkipLinesIfHost(1)
    IfFlagOn(1, 11215001)
    IfCharacterInsideRegion(1, PLAYER, region=1212886)
    IfConditionTrue(0, input_condition=1)
    EnableMapSound(1213800)


@NeverRestart
def Event11215005():
    """ 11215005: Event 11215005 """
    DisableNetworkSync()
    IfFlagOn(1, 11215004)
    IfFlagOn(1, 11210000)
    IfConditionTrue(0, input_condition=1)
    DisableMapSound(1213800)


@RestartOnRest
def Event11210000():
    """ 11210000: Event 11210000 """
    SkipLinesIfThisEventOff(5)
    DisableCharacter(1210800)
    Kill(1210800, award_souls=False)
    DisableCharacter(1210810)
    Kill(1210810, award_souls=False)
    End()
    IfHealthLessThanOrEqual(0, 1210800, 0.0)
    Wait(1.0)
    PlaySoundEffect(anchor_entity=1210800, sound_type=SoundType.s_SFX, sound_id=777777777)
    IfCharacterDead(0, 1210800)
    EnableFlag(11210000)
    KillBoss(1210800)
    DisableObject(1211790)
    DeleteFX(1211791, erase_root_only=True)
    DisableObject(1211792)
    DeleteFX(1211793, erase_root_only=True)


@RestartOnRest
def Event11215006(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int):
    """ 11215006: Event 11215006 """
    DisableCharacter(ARG_0_3)
    SkipLinesIfThisEventSlotOff(4)
    SetDisplayMask(ARG_4_7, bit_index=0, switch_type=OnOffChange.On)
    SetHitboxMask(ARG_4_7, bit_index=1, switch_type=OnOffChange.Off)
    AICommand(ARG_4_7, command_id=20, slot=0)
    End()
    SkipLinesIfFlagOn(1, 11210000)
    IfFlagOn(1, 11215002)
    IfCharacterBackreadEnabled(1, ARG_4_7)
    IfConditionTrue(0, input_condition=1)
    CreateNPCPart(ARG_4_7, npc_part_id=3471, part_index=NPCPartType.Part1, part_health=200, damage_correction=1.0, body_damage_correction=1.0, is_invincible=False, start_in_stop_state=False)
    IfCharacterPartHealthLessThanOrEqual(2, ARG_4_7, npc_part_id=3471, value=0)
    IfHealthLessThanOrEqual(3, ARG_4_7, 0.0)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(3)
    Move(ARG_0_3, destination=ARG_4_7, destination_type=MapEntityType.Character, model_point=150, copy_draw_hitbox=ARG_4_7)
    EnableCharacter(ARG_0_3)
    ResetAnimation(ARG_4_7, disable_interpolation=False)
    ForceAnimation(ARG_4_7, 8000)
    ForceAnimation(ARG_0_3, 8100)
    SetDisplayMask(ARG_4_7, bit_index=0, switch_type=OnOffChange.On)
    SetHitboxMask(ARG_4_7, bit_index=1, switch_type=OnOffChange.Off)
    AICommand(ARG_4_7, command_id=20, slot=0)
    ReplanAI(ARG_4_7)
    IfCharacterHuman(-7, PLAYER)
    IfCharacterHollow(-7, PLAYER)
    EndIfConditionFalse(-7)
    AwardItemLot(ARG_8_11, host_only=True)


@RestartOnRest
def Event11215008():
    """ 11215008: Event 11215008 """
    IfFlagOn(0, 11215007)
    IfStandingOnHitbox(-1, 1213020)
    IfStandingOnHitbox(-2, 1213021)
    IfCharacterInsideRegion(-2, PLAYER, region=1212003)
    IfConditionTrue(-3, input_condition=-1)
    IfConditionTrue(-3, input_condition=-2)
    IfConditionTrue(0, input_condition=-3)
    SkipLinesIfFinishedConditionTrue(3, -1)
    SetNest(1210801, 1212010)
    SetNest(1210802, 1212011)
    SkipLines(2)
    SetNest(1210801, 1212007)
    SetNest(1210802, 1212008)
    AICommand(1210801, command_id=10, slot=1)
    AICommand(1210802, command_id=10, slot=1)
    IfStandingOnHitbox(-2, 1213020)
    IfStandingOnHitbox(-2, 1213021)
    IfCharacterInsideRegion(-2, PLAYER, region=1212003)
    IfConditionFalse(0, input_condition=-2)
    AICommand(1210801, command_id=-1, slot=1)
    AICommand(1210802, command_id=-1, slot=1)
    Restart()


@RestartOnRest
def Event11215007():
    """ 11215007: Event 11215007 """
    IfFlagOn(0, 11210001)
    DisableAI(1210801)
    DisableAI(1210802)
    IfCharacterInsideRegion(1, PLAYER, region=1212004)
    IfCharacterOutsideRegion(1, PLAYER, region=1212001)
    IfCharacterOutsideRegion(1, PLAYER, region=1212002)
    IfConditionTrue(-1, input_condition=1)
    IfAttacked(-1, 1210801, attacking_character=10000)
    IfAttacked(-1, 1210802, attacking_character=10000)
    IfConditionTrue(0, input_condition=-1)
    EnableAI(1210801)
    ForceAnimation(1210801, 3017)
    WaitFrames(15)
    EnableAI(1210802)
    ForceAnimation(1210802, 3017)
    WaitFrames(15)
    ReplanAI(1210801)
    ReplanAI(1210802)


@RestartOnRest
def Event11215009():
    """ 11215009: Event 11215009 """
    IfFlagOn(0, 11210001)
    IfCharacterInsideRegion(0, PLAYER, region=1212006)
    Move(1210801, destination=1212007, destination_type=MapEntityType.Region, model_point=-1, copy_draw_hitbox=1210800)
    Move(1210802, destination=1212008, destination_type=MapEntityType.Region, model_point=-1, copy_draw_hitbox=1210800)
    SetNest(1210801, 1212007)
    SetNest(1210802, 1212008)
    IfCharacterInsideRegion(0, PLAYER, region=1212009)
    Move(1210801, destination=1212010, destination_type=MapEntityType.Region, model_point=-1, copy_draw_hitbox=1210800)
    Move(1210802, destination=1212011, destination_type=MapEntityType.Region, model_point=-1, copy_draw_hitbox=1210800)
    SetNest(1210801, 1212010)
    SetNest(1210802, 1212011)
    Restart()


@NeverRestart
def Event11217000():
    """ 11217000: Event 11217000 """
    IfCharacterInsideRegion(3, PLAYER, region=1212005)
    IfCharacterOutsideRegion(4, PLAYER, region=1212005)
    EndIfConditionTrue(4)
    IfCharacterDead(1, 1210801)
    IfCharacterDead(2, 1210802)
    SkipLinesIfFinishedConditionTrue(2, 1)
    Move(1210801, destination=1212007, destination_type=MapEntityType.Region, model_point=-1, copy_draw_hitbox=1210800)
    SetNest(1210801, 1212007)
    SkipLinesIfFinishedConditionTrue(2, 2)
    Move(1210802, destination=1212008, destination_type=MapEntityType.Region, model_point=-1, copy_draw_hitbox=1210800)
    SetNest(1210802, 1212008)


@RestartOnRest
def Event11215010():
    """ 11215010: Event 11215010 """
    IfFlagOff(1, 11210001)
    IfDialogPromptActivated(1, prompt_text=10010403, anchor_entity=1212898, anchor_type=MapEntityType.Region, facing_angle=0.0, max_distance=0.0, human_or_hollow_only=True, line_intersects=1211890, boss_version=True)
    IfConditionTrue(0, input_condition=1)
    RotateToFaceEntity(PLAYER, 1212897)
    ForceAnimation(PLAYER, 7410, wait_for_completion=True)
    Restart()


@NeverRestart
def Event11215011():
    """ 11215011: Event 11215011 """
    IfFlagOff(1, 11210001)
    IfFlagOn(1, 11215013)
    IfCharacterType(1, PLAYER, CharacterType.WhitePhantom)
    IfDialogPromptActivated(1, prompt_text=10010403, anchor_entity=1212898, anchor_type=MapEntityType.Region, facing_angle=0.0, max_distance=0.0, human_or_hollow_only=False, line_intersects=1211890)
    IfConditionTrue(0, input_condition=1)
    RotateToFaceEntity(PLAYER, 1212897)
    ForceAnimation(PLAYER, 7410)
    Restart()


@NeverRestart
def Event11215012():
    """ 11215012: Event 11215012 """
    SkipLinesIfThisEventOn(3)
    IfFlagOff(1, 11210001)
    IfCharacterInsideRegion(1, PLAYER, region=1212896)
    IfConditionTrue(0, input_condition=1)
    SkipLinesIfClient(2)
    NotifyBossBattleStart()
    SetNetworkUpdateAuthority(1210820, UpdateAuthority.Forced)
    ActivateMultiplayerBuffs(1210820)
    EnableFlag(11210537)


@RestartOnRest
def Event11215013():
    """ 11215013: Event 11215013 """
    SkipLinesIfFlagOff(3, 11210001)
    DisableCharacter(1210820)
    Kill(1210820, award_souls=False)
    End()
    SkipLinesIfFlagOn(3, 11210030)
    DisableCharacter(1210820)
    DisableObject(1211100)
    DisableObject(1211101)
    DisableAI(1210820)
    SkipLinesIfThisEventOn(11)
    IfFlagOn(1, 11215012)
    IfCharacterInsideRegion(1, PLAYER, region=1212896)
    IfConditionTrue(0, input_condition=1)
    SkipLinesIfFlagOn(9, 11210030)
    SkipLinesIfMultiplayer(2)
    PlayCutscene(120110, skippable=True, fade_out=False, player_id=PLAYER)
    SkipLines(1)
    PlayCutscene(120110, skippable=False, fade_out=False, player_id=PLAYER)
    WaitFrames(1)
    EnableObject(1211100)
    EnableObject(1211101)
    EnableCharacter(1210820)
    EnableFlag(11210030)
    EnableAI(1210820)
    EnableBossHealthBar(1210820, name=4100, slot=0)
    EnableHitbox(1213001)


@NeverRestart
def Event11215014():
    """ 11215014: Event 11215014 """
    DisableNetworkSync()
    IfFlagOff(1, 11210001)
    IfFlagOn(1, 11215013)
    SkipLinesIfHost(1)
    IfFlagOn(1, 11215011)
    IfCharacterInsideRegion(1, PLAYER, region=1212896)
    IfConditionTrue(0, input_condition=1)
    EnableMapSound(1213801)


@NeverRestart
def Event11215015():
    """ 11215015: Event 11215015 """
    DisableNetworkSync()
    IfFlagOn(1, 11215014)
    IfFlagOn(1, 11210001)
    IfConditionTrue(0, input_condition=1)
    DisableMapSound(1213801)


@RestartOnRest
def Event11210001():
    """ 11210001: Event 11210001 """
    SkipLinesIfThisEventOff(6)
    DisableCharacter(1210820)
    Kill(1210820, award_souls=False)
    DisableBackread(1210820)
    EnableCharacter(1210801)
    EnableCharacter(1210802)
    End()
    DisableBackread(6720)
    DisableCharacter(1210801)
    DisableCharacter(1210802)
    IfHealthLessThanOrEqual(0, 1210820, 0.0)
    Wait(1.0)
    PlaySoundEffect(anchor_entity=1210820, sound_type=SoundType.s_SFX, sound_id=777777777)
    IfCharacterDead(0, 1210820)
    EnableFlag(11210001)
    EnableFlag(121)
    KillBoss(1210820)
    DisableFlag(11217060)
    DisableFlag(11217070)
    DisableFlag(11217080)
    DisableFlag(11217090)
    DisableObject(1211890)
    DeleteFX(1211891, erase_root_only=True)
    DisableObject(1211892)
    DeleteFX(1211893, erase_root_only=True)
    DisableHitbox(1213001)
    Wait(17.0)
    DisableBackread(1210820)
    EnableBackread(6720)
    EnableCharacter(1210801)
    EnableCharacter(1210802)


@NeverRestart
def Event11210015():
    """ 11210015: Event 11210015 """
    DisableNetworkSync()
    IfFlagOn(1, 11210001)
    IfEntityBeyondDistance(1, 10000, 6720, radius=80.0)
    IfConditionTrue(0, input_condition=1)
    DisableBackread(6720)
    IfFlagOn(2, 11210001)
    IfEntityWithinDistance(2, 10000, 6720, radius=80.0)
    IfConditionTrue(0, input_condition=2)
    EnableBackread(6720)
    Restart()


@RestartOnRest
def Event11215020():
    """ 11215020: Event 11215020 """
    IfFlagOff(1, 11210002)
    IfDialogPromptActivated(1, prompt_text=10010403, anchor_entity=1212998, anchor_type=MapEntityType.Region, facing_angle=0.0, max_distance=0.0, human_or_hollow_only=True, line_intersects=1211990, boss_version=True)
    IfConditionTrue(0, input_condition=1)
    RotateToFaceEntity(PLAYER, 1212997)
    ForceAnimation(PLAYER, 7410, wait_for_completion=True)
    Restart()


@NeverRestart
def Event11215021():
    """ 11215021: Event 11215021 """
    IfFlagOff(1, 11210002)
    IfFlagOn(1, 11215023)
    IfCharacterType(1, PLAYER, CharacterType.WhitePhantom)
    IfDialogPromptActivated(1, prompt_text=10010403, anchor_entity=1212998, anchor_type=MapEntityType.Region, facing_angle=0.0, max_distance=0.0, human_or_hollow_only=False, line_intersects=1211990)
    IfConditionTrue(0, input_condition=1)
    RotateToFaceEntity(PLAYER, 1212997)
    ForceAnimation(PLAYER, 7410)
    Restart()


@NeverRestart
def Event11215022():
    """ 11215022: Event 11215022 """
    SkipLinesIfThisEventOn(3)
    IfFlagOff(1, 11210002)
    IfCharacterInsideRegion(1, PLAYER, region=1212996)
    IfConditionTrue(0, input_condition=1)
    SkipLinesIfClient(2)
    NotifyBossBattleStart()
    SetNetworkUpdateAuthority(1210840, UpdateAuthority.Forced)
    IfCharacterType(2, PLAYER, CharacterType.BlackPhantom)
    SkipLinesIfConditionFalse(1, 2)
    IfFlagOn(0, 703)
    ActivateMultiplayerBuffs(1210840)


@NeverRestart
def Event11215027():
    """ 11215027: Event 11215027 """
    IfFlagOn(1, 11215020)
    IfCharacterInsideRegion(1, PLAYER, region=1212996)
    IfHost(1)
    IfConditionTrue(0, input_condition=1)
    SkipLinesIfMultiplayer(2)
    PlayCutscene(120140, skippable=True, fade_out=False, player_id=PLAYER, move_to_region=1212022, move_to_map=OOLACILE)
    SkipLines(4)
    SkipLinesIfClient(2)
    PlayCutscene(120140, skippable=False, fade_out=False, player_id=PLAYER, move_to_region=1212022, move_to_map=OOLACILE)
    SkipLines(1)
    PlayCutscene(120140, skippable=False, fade_out=False, player_id=PLAYER)
    WaitFrames(1)
    EnableFlag(11210031)


@RestartOnRest
def Event11215026():
    """ 11215026: Event 11215026 """
    DisableNetworkSync()
    IfCharacterInsideRegion(0, PLAYER, region=1212021)
    EnableInvincibility(PLAYER)
    Wait(2.0)
    DisableInvincibility(PLAYER)


@RestartOnRest
def Event11215023():
    """ 11215023: Event 11215023 """
    EndIfFlagOn(17)
    SkipLinesIfThisEventOn(3)
    DisableAI(1210840)
    IfCharacterInsideRegion(0, PLAYER, region=1212021)
    EnableAI(1210840)
    EnableBossHealthBar(1210840, name=4500, slot=0)


@NeverRestart
def Event11215024():
    """ 11215024: Event 11215024 """
    DisableNetworkSync()
    IfFlagOff(1, 11210002)
    IfFlagOn(1, 11215023)
    SkipLinesIfHost(3)
    IfFlagOn(1, 11215021)
    IfCharacterInsideRegion(1, PLAYER, region=1212996)
    SkipLines(1)
    IfCharacterInsideRegion(1, PLAYER, region=1212990)
    IfConditionTrue(0, input_condition=1)
    EnableMapSound(1213802)


@NeverRestart
def Event11215025():
    """ 11215025: Event 11215025 """
    DisableNetworkSync()
    IfFlagOn(1, 11215024)
    IfFlagOn(1, 11210002)
    IfConditionTrue(0, input_condition=1)
    DisableMapSound(1213802)


@NeverRestart
def Event11210002():
    """ 11210002: Event 11210002 """
    DisableObject(1211950)
    DisableObject(1211950)
    SkipLinesIfThisEventOff(4)
    DisableCharacter(1210840)
    Kill(1210840, award_souls=False)
    EnableObject(1211950)
    End()
    IfHealthLessThanOrEqual(0, 1210840, 0.0)
    Wait(1.0)
    PlaySoundEffect(anchor_entity=1210840, sound_type=SoundType.s_SFX, sound_id=777777777)
    IfCharacterDead(0, 1210840)
    EnableFlag(11210002)
    EnableFlag(17)
    KillBoss(1210840)
    DisableObject(1211990)
    DeleteFX(1211991, erase_root_only=True)
    DeleteFX(1213100, erase_root_only=True)
    CreateTemporaryFX(90014, anchor_entity=1211950, anchor_type=MapEntityType.Object, model_point=-1)
    Wait(2.0)
    EnableObject(1211950)
    RegisterBonfire(11210992, obj=1211950, reaction_distance=2.0, reaction_angle=180.0, initial_kindle_level=0)


@NeverRestart
def Event11215250(ARG_0_3: int, ARG_4_7: int):
    """ 11215250: Event 11215250 """
    DeleteFX(ARG_4_7, erase_root_only=False)
    SkipLinesIfFlagOff(2, 11210002)
    DisableObject(ARG_0_3)
    End()
    IfObjectDestroyed(-1, ARG_0_3)
    IfCharacterDead(-1, 1210840)
    IfConditionTrue(0, input_condition=-1)
    DestroyObject(ARG_0_3, slot=1)
    ForceAnimation(ARG_0_3, 0, wait_for_completion=True)
    DisableObject(ARG_0_3)


@RestartOnRest
def Event11215060():
    """ 11215060: Event 11215060 """
    IfFlagOn(1, 11210592)
    IfFlagOff(1, 11210004)
    IfDialogPromptActivated(1, prompt_text=10010403, anchor_entity=1212908, anchor_type=MapEntityType.Region, facing_angle=0.0, max_distance=0.0, human_or_hollow_only=True, line_intersects=1211690, boss_version=True)
    IfConditionTrue(0, input_condition=1)
    RotateToFaceEntity(PLAYER, 1212907)
    ForceAnimation(PLAYER, 7410, wait_for_completion=True)
    Restart()


@NeverRestart
def Event11215061():
    """ 11215061: Event 11215061 """
    IfFlagOn(1, 11210592)
    IfFlagOff(1, 11210004)
    IfFlagOn(1, 11215062)
    IfCharacterType(1, PLAYER, CharacterType.WhitePhantom)
    IfDialogPromptActivated(1, prompt_text=10010403, anchor_entity=1212908, anchor_type=MapEntityType.Region, facing_angle=0.0, max_distance=0.0, human_or_hollow_only=False, line_intersects=1211690)
    IfConditionTrue(0, input_condition=1)
    RotateToFaceEntity(PLAYER, 1212907)
    ForceAnimation(PLAYER, 7410)
    Restart()


@NeverRestart
def Event11215062():
    """ 11215062: Event 11215062 """
    SkipLinesIfThisEventOn(4)
    IfFlagOn(1, 11210592)
    IfFlagOff(1, 11210004)
    IfCharacterInsideRegion(1, PLAYER, region=1212909)
    IfConditionTrue(0, input_condition=1)
    SkipLinesIfClient(2)
    NotifyBossBattleStart()
    SetNetworkUpdateAuthority(1210401, UpdateAuthority.Forced)
    ActivateMultiplayerBuffs(1210401)


@RestartOnRest
def Event11215063():
    """ 11215063: Event 11215063 """
    EnableInvincibility(1210401)
    SkipLinesIfThisEventOn(9)
    DisableAI(1210401)
    IfFlagOn(1, 11215062)
    IfCharacterInsideRegion(1, PLAYER, region=1212906)
    IfStandingOnHitbox(-1, 1213003)
    IfStandingOnHitbox(-1, 1213004)
    IfStandingOnHitbox(-1, 1213009)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    EnableAI(1210401)
    DisableInvincibility(1210401)
    EnableBossHealthBar(1210401, name=4510, slot=0)
    EnableHitbox(1213001)


@NeverRestart
def Event11215064():
    """ 11215064: Event 11215064 """
    DisableNetworkSync()
    IfFlagOff(1, 11210004)
    IfFlagOn(1, 11215063)
    SkipLinesIfHost(2)
    IfFlagOn(1, 11215061)
    IfFlagOn(1, 11215067)
    IfCharacterInsideRegion(1, PLAYER, region=1212900)
    IfConditionTrue(0, input_condition=1)
    EnableMapSound(1213803)


@NeverRestart
def Event11215065():
    """ 11215065: Event 11215065 """
    DisableNetworkSync()
    IfFlagOn(1, 11215064)
    IfFlagOn(1, 11210004)
    IfConditionTrue(0, input_condition=1)
    DisableMapSound(1213803)


@NeverRestart
def Event11215066():
    """ 11215066: Event 11215066 """
    DisableNetworkSync()
    IfFlagOn(1, 11210592)
    IfFlagOff(1, 11210004)
    IfFlagOn(1, 11215062)
    IfCharacterType(1, PLAYER, CharacterType.WhitePhantom)
    IfDialogPromptActivated(1, prompt_text=10010403, anchor_entity=1212908, anchor_type=MapEntityType.Region, facing_angle=0.0, max_distance=0.0, human_or_hollow_only=False, line_intersects=1211690)
    IfConditionTrue(0, input_condition=1)
    WaitFrames(75)
    EnableFlag(11215067)


@NeverRestart
def Event11210005():
    """ 11210005: Event 11210005 """
    EndIfThisEventOn()
    IfHealthLessThanOrEqual(0, 1210401, 0.0)
    Wait(1.0)
    PlaySoundEffect(anchor_entity=1210401, sound_type=SoundType.s_SFX, sound_id=777777777)
    IfCharacterDead(0, 1210401)
    EnableFlag(11210004)
    EnableFlag(11210005)
    EnableFlag(121)
    KillBoss(1210401)
    DisableObject(1211690)
    DeleteFX(1211691, erase_root_only=True)
    DisableHitbox(1213001)


@NeverRestart
def Event11210340():
    """ 11210340: Event 11210340 """
    SkipLinesIfThisEventOff(3)
    EndIfFlagOn(11210341)
    Move(6760, destination=1212331, destination_type=MapEntityType.Region, model_point=-1, copy_draw_hitbox=6760)
    End()
    IfHost(1)
    IfEntityWithinDistance(-1, 6760, 10000, radius=7.0)
    IfAttacked(-1, 6760, attacking_character=10000)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    ForceAnimation(6760, 7003, wait_for_completion=True)
    DisableCharacter(6760)
    Move(6760, destination=1212331, destination_type=MapEntityType.Region, model_point=-1, copy_draw_hitbox=6760)
    EnableCharacter(6760)


@NeverRestart
def Event11210341():
    """ 11210341: Event 11210341 """
    SkipLinesIfThisEventSlotOff(2)
    Move(6760, destination=1212332, destination_type=MapEntityType.Region, model_point=-1, copy_draw_hitbox=6760)
    End()
    IfHost(1)
    IfFlagOn(1, 11210340)
    IfEntityWithinDistance(-1, 6760, 10000, radius=12.0)
    IfAttacked(-1, 6760, attacking_character=10000)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    ForceAnimation(6760, 7003, wait_for_completion=True)
    DisableCharacter(6760)
    Move(6760, destination=1212332, destination_type=MapEntityType.Region, model_point=-1, copy_draw_hitbox=6760)
    EnableCharacter(6760)


@NeverRestart
def Event11210345():
    """ 11210345: Event 11210345 """
    SkipLinesIfThisEventOff(3)
    DisableCharacter(6760)
    DeleteFX(1213125, erase_root_only=False)
    End()
    IfHost(1)
    IfFlagOn(1, 11210341)
    IfEntityWithinDistance(-1, 6760, 10000, radius=12.0)
    IfAttacked(-1, 6760, attacking_character=10000)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    ForceAnimation(6760, 7003, wait_for_completion=True)
    DisableCharacter(6760)
    DeleteFX(1213125, erase_root_only=True)


@NeverRestart
def Event11210346():
    """ 11210346: Event 11210346 """
    DisableNetworkSync()
    IfFlagOff(1, 11210345)
    IfCharacterInsideRegion(1, PLAYER, region=1212335)
    IfFlagOn(2, 11210345)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(2)
    AddSpecialEffect(PLAYER, 4161)
    Restart()


@NeverRestart
def Event11210347():
    """ 11210347: Event 11210347 """
    SkipLinesIfFlagOn(1, 11215045)
    SkipLinesIfFlagOff(2, 11210345)
    DisableObject(1211250)
    End()
    IfHost(1)
    IfCharacterInsideRegion(1, PLAYER, region=1212336)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(11215045)
    EndIfObjectDestroyed(1211250)
    DisableObjectInvulnerability(1211250)
    DestroyObject(1211250, slot=1)
    ForceAnimation(1211250, 0)
    PlaySoundEffect(anchor_entity=1211250, sound_type=SoundType.o_Object, sound_id=262000000)


@NeverRestart
def Event11210025():
    """ 11210025: Event 11210025 """
    SkipLinesIfThisEventOff(2)
    DisableObject(1211240)
    End()
    IfObjectDestroyed(0, 1211240)
    End()


@RestartOnRest
def Event11210310(ARG_0_3: int, ARG_4_7: int):
    """ 11210310: Event 11210310 """
    SkipLinesIfThisEventSlotOff(3)
    DisableCharacter(ARG_0_3)
    Kill(ARG_0_3, award_souls=False)
    End()
    IfCharacterDead(0, ARG_0_3)
    EnableFlag(ARG_4_7)


@NeverRestart
def Event11210330(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int):
    """ 11210330: Event 11210330 """
    IfFlagRangeAllOn(0, (ARG_0_3, ARG_4_7))
    EnableFlag(ARG_8_11)


@NeverRestart
def Event11210021():
    """ 11210021: Event 11210021 """
    DisableAI(1210502)
    EnableInvincibility(1210502)
    SkipLinesIfFlagOff(5, 11210330)
    DisableCharacter(1210502)
    DropMandatoryTreasure(1210502)
    DeleteFX(1213110, erase_root_only=False)
    DisableObject(1211230)
    End()
    IfFlagOn(0, 11210330)
    Wait(6.0)
    ForceAnimation(1210502, 7010, wait_for_completion=True)
    DisableCharacter(1210502)
    DropMandatoryTreasure(1210502)
    DeleteFX(1213110, erase_root_only=True)
    DisableObject(1211230)


@RestartOnRest
def Event11215040():
    """ 11215040: Event 11215040 """
    DisableAI(1210500)
    DisableCharacter(1210500)
    IfFlagOff(1, 17)
    IfFlagOn(1, 11210021)
    IfCharacterHuman(1, PLAYER)
    IfDialogPromptActivated(1, prompt_text=50000000, anchor_entity=1212300, anchor_type=MapEntityType.Region, facing_angle=0.0, max_distance=0.0, model_point=0, human_or_hollow_only=True)
    IfConditionTrue(0, input_condition=1)
    DisplayBattlefieldMessage(140010, display_location_index=0)
    SkipLinesIfClient(1)
    ForceAnimation(1210501, 7008)
    WaitFrames(30)
    DisableCharacter(1210501)
    EnableFlag(11215042)
    DeleteFX(1213100, erase_root_only=True)
    Wait(10.0)
    EnableCharacter(1210500)
    EnableAI(1210500)
    SetTeamType(1210500, TeamType.WhitePhantom)
    ForceAnimation(1210500, 7004)
    SkipLinesIfClient(2)
    DisplayBattlefieldMessage(20001110, display_location_index=0)
    SkipLines(1)
    DisplayBattlefieldMessage(20001111, display_location_index=0)
    WaitFrames(140)


@RestartOnRest
def Event11215041():
    """ 11215041: Event 11215041 """
    DisableCharacter(1210501)
    DisableAI(1210501)
    DisableAnimations(1210501)
    EndIfClient()
    IfFlagOn(1, 11210021)
    IfFlagOff(1, 17)
    IfCharacterInsideRegion(1, PLAYER, region=1212300)
    IfCharacterHuman(1, PLAYER)
    IfConditionTrue(0, input_condition=1)
    EndIfFlagOn(11215042)
    EnableCharacter(1210501)
    ForceAnimation(1210501, 7006, wait_for_completion=True)
    ForceAnimation(1210501, 7007, loop=True)
    IfCharacterOutsideRegion(2, PLAYER, region=1212300)
    IfFlagOn(2, 11215020)
    IfConditionTrue(0, input_condition=2)
    ForceAnimation(1210501, 7008, wait_for_completion=True)
    DisableCharacter(1210501)
    Restart()


@RestartOnRest
def Event11215044():
    """ 11215044: Event 11215044 """
    DeleteFX(1213100, erase_root_only=True)
    EndIfClient()
    IfFlagOff(1, 17)
    IfFlagOn(1, 11210021)
    IfCharacterHuman(1, PLAYER)
    IfConditionTrue(0, input_condition=1)
    CreateFX(1213100)
    IfFlagOff(2, 17)
    IfFlagOn(2, 11210021)
    IfCharacterHuman(2, PLAYER)
    IfConditionFalse(0, input_condition=2)
    Restart()


@NeverRestart
def Event11210020():
    """ 11210020: Event 11210020 """
    EndIfFlagOn(17)
    IfCharacterDead(1, 1210840)
    IfCharacterAlive(1, 1210500)
    IfFlagOn(1, 11215040)
    IfCharacterDead(2, 1210500)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionTrue(5, 2)
    DisableAI(1210500)
    WaitFrames(120)
    ForceAnimation(1210500, 7005, wait_for_completion=True)
    DisableCharacter(1210500)
    End()
    DisplayBattlefieldMessage(20001115, display_location_index=0)


@RestartOnRest
def Event11215043():
    """ 11215043: Event 11215043 """
    SkipLinesIfThisEventOn(1)
    IfHealthLessThanOrEqual(0, 1210500, 0.30000001192092896)
    AddSpecialEffect(1210500, 5401)


@RestartOnRest
def Event11215100():
    """ 11215100: Event 11215100 """
    EndIfThisEventOn()
    DisableAI(1210100)
    IfCharacterType(7, PLAYER, CharacterType.BlackPhantom)
    IfConditionFalse(3, input_condition=7)
    IfCharacterInsideRegion(3, PLAYER, region=1212502)
    IfConditionTrue(-3, input_condition=3)
    IfAttacked(-3, 1210100, attacking_character=10000)
    IfConditionTrue(1, input_condition=-3)
    IfConditionFalse(2, input_condition=7)
    IfCharacterInsideRegion(2, PLAYER, region=1212500)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    SetStandbyAnimationSettings(1210100, cancel_animation=9060)
    EnableAI(1210100)
    EndIfFinishedConditionTrue(1)
    SetNest(1210100, 1212501)
    AICommand(1210100, command_id=10, slot=0)
    ReplanAI(1210100)
    Wait(6.0)
    IfCharacterInsideRegion(-2, PLAYER, region=1212502)
    IfAttacked(-2, 1210100, attacking_character=10000)
    IfConditionTrue(0, input_condition=-2)
    AICommand(1210100, command_id=-1, slot=0)
    ReplanAI(1210100)


@RestartOnRest
def Event11215110(ARG_0_3: int, ARG_4_7: int, ARG_8_11: float, ARG_12_15: int):
    """ 11215110: Event 11215110 """
    SkipLinesIfThisEventSlotOff(2)
    ResetStandbyAnimationSettings(ARG_0_3)
    End()
    DisableAI(ARG_0_3)
    IfAttacked(-1, ARG_0_3, attacking_character=10000)
    IfCharacterInsideRegion(-1, PLAYER, region=ARG_4_7)
    IfCharacterInsideRegion(-1, PLAYER, region=ARG_12_15)
    IfEntityWithinDistance(-1, 10000, ARG_0_3, radius=ARG_8_11)
    IfCharacterType(7, PLAYER, CharacterType.BlackPhantom)
    IfConditionFalse(1, input_condition=7)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    EnableAI(ARG_0_3)
    SetStandbyAnimationSettings(ARG_0_3, cancel_animation=9060)


@RestartOnRest
def Event11215115(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int):
    """ 11215115: Event 11215115 """
    IfCharacterInsideRegion(0, ARG_0_3, region=ARG_4_7)
    SetNest(ARG_0_3, ARG_8_11)


@RestartOnRest
def Event11215120(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int, ARG_12_15: int):
    """ 11215120: Event 11215120 """
    SkipLinesIfThisEventOff(4)
    ResetStandbyAnimationSettings(ARG_0_3)
    ResetStandbyAnimationSettings(ARG_4_7)
    ResetStandbyAnimationSettings(ARG_8_11)
    End()
    DisableAI(ARG_0_3)
    DisableAI(ARG_4_7)
    DisableAI(ARG_8_11)
    IfHost(1)
    IfAttacked(-1, ARG_0_3, attacking_character=10000)
    IfAttacked(-1, ARG_4_7, attacking_character=10000)
    IfAttacked(-1, ARG_8_11, attacking_character=10000)
    SkipLinesIfClient(2)
    SkipLinesIfFlagOn(1, ARG_12_15)
    IfFlagOn(1, ARG_12_15)
    IfConditionTrue(-2, input_condition=-1)
    IfConditionTrue(-2, input_condition=1)
    IfConditionTrue(0, input_condition=-2)
    EnableAI(ARG_0_3)
    EnableAI(ARG_4_7)
    EnableAI(ARG_8_11)
    SetStandbyAnimationSettings(ARG_0_3, cancel_animation=9060)
    SetStandbyAnimationSettings(ARG_4_7, cancel_animation=9060)
    SetStandbyAnimationSettings(ARG_8_11, cancel_animation=9060)


@RestartOnRest
def Event11215130(ARG_0_3: int, ARG_4_7: int, ARG_8_11: float, ARG_12_15: float):
    """ 11215130: Event 11215130 """
    SkipLinesIfThisEventSlotOff(2)
    ResetStandbyAnimationSettings(ARG_0_3)
    End()
    IfEntityWithinDistance(-1, 10000, ARG_4_7, radius=ARG_8_11)
    IfAttacked(-1, 1210108, attacking_character=10000)
    IfAttacked(-1, 1210109, attacking_character=10000)
    IfAttacked(-1, 1210110, attacking_character=10000)
    IfCharacterType(7, PLAYER, CharacterType.BlackPhantom)
    IfConditionFalse(1, input_condition=7)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    Wait(ARG_12_15)
    SetStandbyAnimationSettings(ARG_0_3, cancel_animation=9060)


@RestartOnRest
def Event11215140(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int, ARG_12_15: int, ARG_16_19: int, ARG_20_23: int, ARG_24_27: int):
    """ 11215140: Event 11215140 """
    IfCharacterInsideRegion(1, ARG_0_3, region=ARG_4_7)
    IfFlagOff(1, ARG_16_19)
    IfHasAIStatus(1, ARG_0_3, ai_status=AIStatusType.Normal)
    IfCharacterInsideRegion(2, ARG_0_3, region=ARG_8_11)
    IfFlagOff(2, ARG_20_23)
    IfHasAIStatus(2, ARG_0_3, ai_status=AIStatusType.Normal)
    IfCharacterInsideRegion(3, ARG_0_3, region=ARG_12_15)
    IfFlagOff(3, ARG_24_27)
    IfHasAIStatus(3, ARG_0_3, ai_status=AIStatusType.Normal)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionFalse(3, 1)
    EnableFlag(ARG_16_19)
    DisableFlag(ARG_20_23)
    DisableFlag(ARG_24_27)
    SkipLinesIfFinishedConditionFalse(3, 2)
    DisableFlag(ARG_16_19)
    EnableFlag(ARG_20_23)
    DisableFlag(ARG_24_27)
    SkipLinesIfFinishedConditionFalse(3, 3)
    DisableFlag(ARG_16_19)
    DisableFlag(ARG_20_23)
    EnableFlag(ARG_24_27)
    ResetAnimation(ARG_0_3, disable_interpolation=False)
    ForceAnimation(ARG_0_3, 7000, skip_transition=True)
    WaitFrames(25)
    ForceAnimation(ARG_0_3, 9000, skip_transition=True)
    WaitFrames(190)
    ForceAnimation(ARG_0_3, 9060)
    WaitFrames(35)
    Restart()


@NeverRestart
def Event11210600(ARG_0_3: int, ARG_4_7: int):
    """ 11210600: Event 11210600 """
    SkipLinesIfThisEventSlotOff(4)
    EndOfAnimation(ARG_0_3, 0)
    DisableObjectActivation(ARG_0_3, obj_act_id=-1)
    EnableTreasure(ARG_0_3)
    End()
    DisableTreasure(ARG_0_3)
    IfObjectActivated(0, obj_act_id=ARG_4_7)
    WaitFrames(10)
    EnableTreasure(ARG_0_3)


@RestartOnRest
def Event11210350(ARG_0_3: int, ARG_4_7: int):
    """ 11210350: Event 11210350 """
    SkipLinesIfThisEventSlotOff(3)
    DisableCharacter(ARG_0_3)
    Kill(ARG_0_3, award_souls=False)
    End()
    IfCharacterDead(0, ARG_0_3)
    EndIfEqual(left=ARG_4_7, right=0)
    IfCharacterHuman(-7, PLAYER)
    IfCharacterHollow(-7, PLAYER)
    EndIfConditionFalse(-7)
    AwardItemLot(ARG_4_7, host_only=True)


@RestartOnRest
def Event11210150():
    """ 11210150: Event 11210150 """
    EndIfFlagOn(11210160)
    Move(1210350, destination=1212143, destination_type=MapEntityType.Region, model_point=-1, set_draw_hitbox=1213040)
    Move(1210350, destination=1212150, destination_type=MapEntityType.Region, model_point=-1, set_draw_hitbox=1213040)
    SetNest(1210350, 1212150)


@NeverRestart
def Event11210100():
    """ 11210100: Event 11210100 """
    SkipLinesIfFlagOff(1, 11210101)
    EndOfAnimation(1211000, 0)
    SkipLinesIfFlagOn(1, 11210101)
    EndOfAnimation(1211000, 10)
    IfFlagOff(1, 11210101)
    IfCharacterInsideRegion(1, PLAYER, region=1212101)
    IfFlagOn(1, 11210103)
    IfFlagOff(1, 11215220)
    IfFlagOn(2, 11210102)
    IfFlagOn(2, 11210101)
    IfCharacterInsideRegion(2, PLAYER, region=1212100)
    IfFlagOn(2, 11210103)
    IfFlagOff(2, 11215220)
    IfFlagOn(3, 11210102)
    IfFlagOff(3, 11210101)
    IfCharacterInsideRegion(3, PLAYER, region=1212102)
    IfFlagOn(3, 11210103)
    IfFlagOff(3, 11215220)
    IfFlagOn(4, 11210101)
    IfCharacterInsideRegion(4, PLAYER, region=1212103)
    IfFlagOn(4, 11210103)
    IfFlagOff(4, 11215220)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(-1, input_condition=4)
    IfConditionTrue(0, input_condition=-1)
    WaitForNetworkApproval(max_seconds=3.0)
    WaitFrames(0)
    EnableFlag(11215220)
    SkipLinesIfFinishedConditionTrue(25, 2)
    SkipLinesIfFinishedConditionTrue(24, 4)
    CreateTemporaryFX(120030, anchor_entity=1211001, anchor_type=MapEntityType.Object, model_point=101)
    EnableFlag(11210101)
    EnableFlag(11210102)
    CreateObjectFX(120029, obj=1211000, model_point=191)
    ForceAnimation(1211000, 0)
    WaitFrames(180)
    DeleteObjectFX(1211000, erase_root=False)
    SkipLinesIfFinishedConditionTrue(8, 1)
    IfAllPlayersOutsideRegion(-2, region=1212102)
    IfCharacterInsideRegion(5, PLAYER, region=1212103)
    IfHost(5)
    IfTimeElapsed(5, 1.0)
    IfConditionTrue(-2, input_condition=5)
    IfConditionTrue(0, input_condition=-2)
    DisableFlag(11215220)
    Restart()
    IfAllPlayersOutsideRegion(-2, region=1212100)
    IfCharacterInsideRegion(5, PLAYER, region=1212103)
    IfHost(5)
    IfTimeElapsed(5, 1.0)
    IfConditionTrue(-2, input_condition=5)
    IfConditionTrue(0, input_condition=-2)
    DisableFlag(11215220)
    Restart()
    CreateTemporaryFX(120030, anchor_entity=1211002, anchor_type=MapEntityType.Object, model_point=101)
    DisableFlag(11210101)
    CreateObjectFX(120029, obj=1211000, model_point=191)
    ForceAnimation(1211000, 10)
    WaitFrames(180)
    DeleteObjectFX(1211000, erase_root=False)
    SkipLinesIfFinishedConditionTrue(8, 2)
    IfAllPlayersOutsideRegion(-3, region=1212103)
    IfCharacterInsideRegion(6, PLAYER, region=1212102)
    IfHost(6)
    IfTimeElapsed(6, 1.0)
    IfConditionTrue(-3, input_condition=6)
    IfConditionTrue(0, input_condition=-3)
    DisableFlag(11215220)
    Restart()
    IfAllPlayersOutsideRegion(-3, region=1212101)
    IfCharacterInsideRegion(6, PLAYER, region=1212102)
    IfHost(6)
    IfTimeElapsed(6, 1.0)
    IfConditionTrue(-3, input_condition=6)
    IfConditionTrue(0, input_condition=-3)
    DisableFlag(11215220)
    Restart()


@NeverRestart
def Event11210103():
    """ 11210103: Event 11210103 """
    IfCharacterType(7, PLAYER, CharacterType.BlackPhantom)
    IfConditionFalse(1, input_condition=7)
    IfCharacterInsideRegion(1, PLAYER, region=1212104)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(11210103)


@NeverRestart
def Event11210110():
    """ 11210110: Event 11210110 """
    SkipLinesIfFlagOff(1, 11210111)
    EndOfAnimation(1211010, 11)
    SkipLinesIfFlagOn(1, 11210111)
    EndOfAnimation(1211010, 1)
    IfFlagOn(1, 11210111)
    IfCharacterInsideRegion(1, PLAYER, region=1212111)
    IfFlagOff(1, 11215221)
    IfFlagOff(2, 11210111)
    IfCharacterInsideRegion(2, PLAYER, region=1212110)
    IfFlagOff(2, 11215221)
    IfFlagOn(3, 11210111)
    IfCharacterInsideRegion(3, PLAYER, region=1212112)
    IfFlagOff(3, 11215221)
    IfFlagOff(4, 11210111)
    IfCharacterInsideRegion(4, PLAYER, region=1212113)
    IfFlagOff(4, 11215221)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(-1, input_condition=4)
    IfConditionTrue(0, input_condition=-1)
    WaitForNetworkApproval(max_seconds=3.0)
    WaitFrames(0)
    EnableFlag(11215221)
    SkipLinesIfFinishedConditionTrue(24, 2)
    SkipLinesIfFinishedConditionTrue(23, 4)
    CreateTemporaryFX(120030, anchor_entity=1211011, anchor_type=MapEntityType.Object, model_point=101)
    DisableFlag(11210111)
    CreateObjectFX(120029, obj=1211010, model_point=191)
    ForceAnimation(1211010, 1)
    WaitFrames(140)
    DeleteObjectFX(1211010, erase_root=False)
    SkipLinesIfFinishedConditionTrue(8, 1)
    IfAllPlayersOutsideRegion(-2, region=1212112)
    IfCharacterInsideRegion(5, PLAYER, region=1212113)
    IfHost(5)
    IfTimeElapsed(5, 1.0)
    IfConditionTrue(-2, input_condition=5)
    IfConditionTrue(0, input_condition=-2)
    DisableFlag(11215221)
    Restart()
    IfAllPlayersOutsideRegion(-2, region=1212110)
    IfCharacterInsideRegion(5, PLAYER, region=1212113)
    IfHost(5)
    IfTimeElapsed(5, 1.0)
    IfConditionTrue(-2, input_condition=5)
    IfConditionTrue(0, input_condition=-2)
    DisableFlag(11215221)
    Restart()
    CreateTemporaryFX(120030, anchor_entity=1211012, anchor_type=MapEntityType.Object, model_point=101)
    EnableFlag(11210111)
    CreateObjectFX(120029, obj=1211010, model_point=191)
    ForceAnimation(1211010, 11)
    WaitFrames(140)
    DeleteObjectFX(1211010, erase_root=False)
    SkipLinesIfFinishedConditionTrue(8, 2)
    IfAllPlayersOutsideRegion(-3, region=1212113)
    IfCharacterInsideRegion(6, PLAYER, region=1212112)
    IfHost(6)
    IfTimeElapsed(6, 1.0)
    IfConditionTrue(-3, input_condition=6)
    IfConditionTrue(0, input_condition=-3)
    DisableFlag(11215221)
    Restart()
    IfAllPlayersOutsideRegion(-3, region=1212111)
    IfCharacterInsideRegion(6, PLAYER, region=1212112)
    IfHost(6)
    IfTimeElapsed(6, 1.0)
    IfConditionTrue(-3, input_condition=6)
    IfConditionTrue(0, input_condition=-3)
    DisableFlag(11215221)
    Restart()


@NeverRestart
def Event11210120():
    """ 11210120: Event 11210120 """
    SkipLinesIfFlagOff(1, 11210121)
    EndOfAnimation(1211020, 2)
    SkipLinesIfFlagOn(1, 11210121)
    EndOfAnimation(1211020, 12)
    IfFlagOff(1, 11210121)
    IfCharacterInsideRegion(1, PLAYER, region=1212121)
    IfFlagOn(1, 11210123)
    IfFlagOff(1, 11215222)
    IfFlagOn(2, 11210122)
    IfFlagOn(2, 11210121)
    IfCharacterInsideRegion(2, PLAYER, region=1212120)
    IfFlagOn(2, 11210123)
    IfFlagOff(2, 11215222)
    IfFlagOn(3, 11210122)
    IfFlagOff(3, 11210121)
    IfCharacterInsideRegion(3, PLAYER, region=1212122)
    IfFlagOn(3, 11210123)
    IfFlagOff(3, 11215222)
    IfFlagOn(4, 11210121)
    IfCharacterInsideRegion(4, PLAYER, region=1212123)
    IfFlagOn(4, 11210123)
    IfFlagOff(4, 11215222)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(-1, input_condition=4)
    IfConditionTrue(0, input_condition=-1)
    WaitForNetworkApproval(max_seconds=3.0)
    WaitFrames(0)
    EnableFlag(11215222)
    SkipLinesIfFinishedConditionTrue(25, 2)
    SkipLinesIfFinishedConditionTrue(24, 4)
    CreateTemporaryFX(120030, anchor_entity=1211021, anchor_type=MapEntityType.Object, model_point=101)
    EnableFlag(11210121)
    EnableFlag(11210122)
    CreateObjectFX(120029, obj=1211020, model_point=191)
    ForceAnimation(1211020, 2)
    WaitFrames(140)
    DeleteObjectFX(1211020, erase_root=False)
    SkipLinesIfFinishedConditionTrue(8, 1)
    IfAllPlayersOutsideRegion(-2, region=1212122)
    IfCharacterInsideRegion(5, PLAYER, region=1212123)
    IfHost(5)
    IfTimeElapsed(5, 1.0)
    IfConditionTrue(-2, input_condition=5)
    IfConditionTrue(0, input_condition=-2)
    DisableFlag(11215222)
    Restart()
    IfAllPlayersOutsideRegion(-2, region=1212120)
    IfCharacterInsideRegion(5, PLAYER, region=1212123)
    IfHost(5)
    IfTimeElapsed(5, 1.0)
    IfConditionTrue(-2, input_condition=5)
    IfConditionTrue(0, input_condition=-2)
    DisableFlag(11215222)
    Restart()
    CreateTemporaryFX(120030, anchor_entity=1211022, anchor_type=MapEntityType.Object, model_point=101)
    DisableFlag(11210121)
    CreateObjectFX(120029, obj=1211020, model_point=191)
    ForceAnimation(1211020, 12)
    WaitFrames(140)
    DeleteObjectFX(1211020, erase_root=False)
    SkipLinesIfFinishedConditionTrue(8, 2)
    IfAllPlayersOutsideRegion(-3, region=1212123)
    IfCharacterInsideRegion(6, PLAYER, region=1212122)
    IfHost(6)
    IfTimeElapsed(6, 1.0)
    IfConditionTrue(-3, input_condition=6)
    IfConditionTrue(0, input_condition=-3)
    DisableFlag(11215222)
    Restart()
    IfAllPlayersOutsideRegion(-3, region=1212121)
    IfCharacterInsideRegion(6, PLAYER, region=1212122)
    IfHost(6)
    IfTimeElapsed(6, 1.0)
    IfConditionTrue(-3, input_condition=6)
    IfConditionTrue(0, input_condition=-3)
    DisableFlag(11215222)
    Restart()


@NeverRestart
def Event11210123():
    """ 11210123: Event 11210123 """
    IfCharacterType(7, PLAYER, CharacterType.BlackPhantom)
    IfConditionFalse(1, input_condition=7)
    IfCharacterInsideRegion(1, PLAYER, region=1212124)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(11210123)


@NeverRestart
def Event11210130():
    """ 11210130: Event 11210130 """
    SkipLinesIfFlagOff(1, 11210131)
    EndOfAnimation(1211030, 3)
    SkipLinesIfFlagOn(1, 11210131)
    EndOfAnimation(1211030, 13)
    IfFlagOff(1, 11210131)
    IfCharacterInsideRegion(1, PLAYER, region=1212131)
    IfFlagOn(1, 11210133)
    IfFlagOff(1, 11215223)
    IfFlagOn(2, 11210132)
    IfFlagOn(2, 11210131)
    IfCharacterInsideRegion(2, PLAYER, region=1212130)
    IfFlagOn(2, 11210133)
    IfFlagOff(2, 11215223)
    IfFlagOn(3, 11210132)
    IfFlagOff(3, 11210131)
    IfCharacterInsideRegion(3, PLAYER, region=1212132)
    IfFlagOn(3, 11210133)
    IfFlagOff(3, 11215223)
    IfFlagOn(4, 11210131)
    IfCharacterInsideRegion(4, PLAYER, region=1212133)
    IfFlagOn(4, 11210133)
    IfFlagOff(4, 11215223)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(-1, input_condition=4)
    IfConditionTrue(0, input_condition=-1)
    WaitForNetworkApproval(max_seconds=3.0)
    WaitFrames(0)
    EnableFlag(11215223)
    SkipLinesIfFinishedConditionTrue(25, 2)
    SkipLinesIfFinishedConditionTrue(24, 4)
    CreateTemporaryFX(120030, anchor_entity=1211031, anchor_type=MapEntityType.Object, model_point=101)
    EnableFlag(11210131)
    EnableFlag(11210132)
    CreateObjectFX(120029, obj=1211030, model_point=191)
    ForceAnimation(1211030, 3)
    WaitFrames(240)
    DeleteObjectFX(1211030, erase_root=False)
    SkipLinesIfFinishedConditionTrue(8, 1)
    IfAllPlayersOutsideRegion(-2, region=1212132)
    IfCharacterInsideRegion(5, PLAYER, region=1212133)
    IfHost(5)
    IfTimeElapsed(5, 1.0)
    IfConditionTrue(-2, input_condition=5)
    IfConditionTrue(0, input_condition=-2)
    DisableFlag(11215223)
    Restart()
    IfAllPlayersOutsideRegion(-2, region=1212130)
    IfCharacterInsideRegion(5, PLAYER, region=1212133)
    IfHost(5)
    IfTimeElapsed(5, 1.0)
    IfConditionTrue(-2, input_condition=5)
    IfConditionTrue(0, input_condition=-2)
    DisableFlag(11215223)
    Restart()
    CreateTemporaryFX(120030, anchor_entity=1211032, anchor_type=MapEntityType.Object, model_point=101)
    DisableFlag(11210131)
    CreateObjectFX(120029, obj=1211030, model_point=191)
    ForceAnimation(1211030, 13)
    WaitFrames(240)
    DeleteObjectFX(1211030, erase_root=False)
    SkipLinesIfFinishedConditionTrue(8, 2)
    IfAllPlayersOutsideRegion(-3, region=1212133)
    IfCharacterInsideRegion(6, PLAYER, region=1212132)
    IfHost(6)
    IfTimeElapsed(6, 1.0)
    IfConditionTrue(-3, input_condition=6)
    IfConditionTrue(0, input_condition=-3)
    DisableFlag(11215223)
    Restart()
    IfAllPlayersOutsideRegion(-3, region=1212131)
    IfCharacterInsideRegion(6, PLAYER, region=1212132)
    IfHost(6)
    IfTimeElapsed(6, 1.0)
    IfConditionTrue(-3, input_condition=6)
    IfConditionTrue(0, input_condition=-3)
    DisableFlag(11215223)
    Restart()


@NeverRestart
def Event11210133():
    """ 11210133: Event 11210133 """
    IfCharacterInsideRegion(0, PLAYER, region=1212134)
    EnableFlag(11210133)


@NeverRestart
def Event11210140():
    """ 11210140: Event 11210140 """
    SkipLinesIfFlagOff(1, 11210141)
    EndOfAnimation(1211040, 4)
    SkipLinesIfFlagOn(1, 11210141)
    EndOfAnimation(1211040, 14)
    IfFlagOff(1, 11210141)
    IfCharacterInsideRegion(1, PLAYER, region=1212141)
    IfFlagOff(1, 11215224)
    IfFlagOn(2, 11210141)
    IfCharacterInsideRegion(2, PLAYER, region=1212140)
    IfFlagOff(2, 11215224)
    IfFlagOff(3, 11210141)
    IfCharacterInsideRegion(3, PLAYER, region=1212142)
    IfFlagOff(3, 11215224)
    IfFlagOn(4, 11210141)
    IfCharacterInsideRegion(4, PLAYER, region=1212143)
    IfFlagOff(4, 11215224)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(-1, input_condition=4)
    IfConditionTrue(0, input_condition=-1)
    WaitForNetworkApproval(max_seconds=3.0)
    WaitFrames(0)
    EnableFlag(11215224)
    EnableFlag(11210160)
    SkipLinesIfFinishedConditionTrue(24, 2)
    SkipLinesIfFinishedConditionTrue(23, 4)
    CreateTemporaryFX(120030, anchor_entity=1211041, anchor_type=MapEntityType.Object, model_point=101)
    EnableFlag(11210141)
    CreateObjectFX(120029, obj=1211040, model_point=191)
    ForceAnimation(1211040, 4)
    WaitFrames(180)
    DeleteObjectFX(1211040, erase_root=False)
    SkipLinesIfFinishedConditionTrue(8, 1)
    IfAllPlayersOutsideRegion(-2, region=1212142)
    IfCharacterInsideRegion(5, PLAYER, region=1212143)
    IfHost(5)
    IfTimeElapsed(5, 1.0)
    IfConditionTrue(-2, input_condition=5)
    IfConditionTrue(0, input_condition=-2)
    DisableFlag(11215224)
    Restart()
    IfAllPlayersOutsideRegion(-2, region=1212140)
    IfCharacterInsideRegion(5, PLAYER, region=1212143)
    IfHost(5)
    IfTimeElapsed(5, 1.0)
    IfConditionTrue(-2, input_condition=5)
    IfConditionTrue(0, input_condition=-2)
    DisableFlag(11215224)
    Restart()
    CreateTemporaryFX(120030, anchor_entity=1211042, anchor_type=MapEntityType.Object, model_point=101)
    DisableFlag(11210141)
    CreateObjectFX(120029, obj=1211040, model_point=191)
    ForceAnimation(1211040, 14)
    WaitFrames(180)
    DeleteObjectFX(1211040, erase_root=False)
    SkipLinesIfFinishedConditionTrue(8, 2)
    IfAllPlayersOutsideRegion(-3, region=1212143)
    IfCharacterInsideRegion(6, PLAYER, region=1212142)
    IfHost(6)
    IfTimeElapsed(6, 1.0)
    IfConditionTrue(-3, input_condition=6)
    IfConditionTrue(0, input_condition=-3)
    DisableFlag(11215224)
    Restart()
    IfAllPlayersOutsideRegion(-3, region=1212141)
    IfCharacterInsideRegion(6, PLAYER, region=1212142)
    IfHost(6)
    IfTimeElapsed(6, 1.0)
    IfConditionTrue(-3, input_condition=6)
    IfConditionTrue(0, input_condition=-3)
    DisableFlag(11215224)
    Restart()


@NeverRestart
def Event11210170(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int):
    """ 11210170: Event 11210170 """
    DisableHitbox(ARG_4_7)
    SkipLinesIfNotEqual(1, left=ARG_0_3, right=11215220)
    IfAllPlayersOutsideRegion(1, region=1212100)
    IfCharacterInsideRegion(1, PLAYER, region=ARG_8_11)
    IfFlagOn(1, ARG_0_3)
    IfConditionTrue(0, input_condition=1)
    EnableHitbox(ARG_4_7)
    SkipLinesIfNotEqual(3, left=ARG_0_3, right=11215220)
    IfCharacterInsideRegion(7, PLAYER, region=1212100)
    IfTimeElapsed(7, 2.0)
    IfConditionTrue(-1, input_condition=7)
    IfAllPlayersOutsideRegion(-1, region=ARG_8_11)
    IfFlagOff(-1, ARG_0_3)
    IfConditionTrue(0, input_condition=-1)
    Wait(5.0)
    Restart()


@NeverRestart
def Event11210300():
    """ 11210300: Event 11210300 """
    EndIfClient()
    EndIfThisEventOn()
    IfObjectActivated(0, obj_act_id=11210650)
    EnableFlag(11210650)
    DisplayDialog(10010884, anchor_entity=1211120, display_distance=3.0, button_type=ButtonType.Yes_or_No, number_buttons=NumberButtons.NoButton)


@RestartOnRest
def Event11210050():
    """ 11210050: Event 11210050 """
    DisableGravity(1210400)
    EnableInvincibility(1210400)
    DisableCollision(1210400)
    DisableCharacter(1210400)
    SkipLinesIfClient(1)
    SetNetworkUpdateAuthority(1210400, UpdateAuthority.Forced)
    EndIfThisEventOn()
    IfCharacterInsideRegion(0, PLAYER, region=1212050)
    EnableFlag(11210050)
    SetNetworkUpdateRate(1210400, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableCharacter(1210400)
    Move(1210400, destination=1212051, destination_type=MapEntityType.Region, model_point=-1, set_draw_hitbox=1213000)
    ForceAnimation(1210400, 7000)
    WaitFrames(420)
    DisableCharacter(1210400)


@RestartOnRest
def Event11210051():
    """ 11210051: Event 11210051 """
    DisableAI(1210402)
    EnableImmortality(1210402)
    DisableGravity(1210402)
    DisableCollision(1210402)
    SkipLinesIfThisEventOn(1)
    DisableCharacter(1210402)
    SkipLinesIfClient(1)
    SetNetworkUpdateAuthority(1210402, UpdateAuthority.Forced)
    EndIfThisEventOn()
    IfCharacterInsideRegion(1, PLAYER, region=1212052)
    IfFlagOff(1, 11210535)
    IfConditionTrue(0, input_condition=1)
    SetNetworkUpdateRate(1210402, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableCharacter(1210402)
    ForceAnimation(1210402, 7006, skip_transition=True)
    WaitFrames(240)
    ForceAnimation(1210402, 7008, skip_transition=True)
    WaitFrames(194)
    EnableFlag(11210062)
    EnableFlag(11210069)
    End()


@RestartOnRest
def Event11210052():
    """ 11210052: Event 11210052 """
    SkipLinesIfFlagOff(3, 11210535)
    DisableFlagRange((11210063, 11210067))
    DisableCharacter(1210402)
    End()
    DisableFlagRange((11210070, 11210073))
    SkipLinesIfClient(1)
    EnableRandomFlagInRange((11210070, 11210073))
    EnableFlag(11210068)
    IfHealthLessThanOrEqual(1, 1210402, 0.009999999776482582)
    IfFlagOn(1, 11210062)
    IfFlagOff(1, 11210535)
    IfFlagOff(1, 11210067)
    IfFlagOn(-2, 11215056)
    IfFlagOn(-2, 11215058)
    IfConditionTrue(2, input_condition=-2)
    IfFlagOn(2, 11210062)
    IfFlagOff(2, 11210535)
    IfFlagOff(2, 11210067)
    IfFlagOn(-3, 11215055)
    IfFlagOn(-3, 11215057)
    IfConditionTrue(3, input_condition=-3)
    IfFlagOn(3, 11210062)
    IfFlagOff(3, 11210535)
    IfFlagOff(3, 11210067)
    IfConditionFalse(4, input_condition=1)
    IfConditionFalse(4, input_condition=2)
    IfConditionFalse(4, input_condition=3)
    IfFlagOn(4, 11210062)
    IfFlagOff(4, 11210535)
    IfFlagOff(4, 11210067)
    IfConditionTrue(-5, input_condition=1)
    IfConditionTrue(-5, input_condition=2)
    IfConditionTrue(-5, input_condition=3)
    IfConditionTrue(-5, input_condition=4)
    IfConditionTrue(0, input_condition=-5)
    SkipLinesIfFinishedConditionTrue(3, 1)
    SkipLinesIfFinishedConditionTrue(4, 2)
    SkipLinesIfFinishedConditionTrue(5, 3)
    SkipLinesIfFinishedConditionTrue(6, 4)
    EnableFlag(11210063)
    SkipLines(5)
    EnableFlag(11210065)
    SkipLines(3)
    EnableFlag(11210064)
    SkipLines(1)
    EnableFlag(11210066)
    EnableFlag(11210067)
    Restart()


@RestartOnRest
def Event11210053():
    """ 11210053: Event 11210053 """
    SkipLinesIfThisEventOff(3)
    DisableCharacter(1210401)
    DisableCharacter(1210402)
    End()
    IfFlagOn(1, 11210063)
    IfHost(1)
    IfConditionTrue(0, input_condition=1)
    ForceAnimation(1210402, 7004, skip_transition=True)
    WaitFrames(176)
    DisableCharacter(1210402)
    Kill(1210402, award_souls=True)


@RestartOnRest
def Event11210054():
    """ 11210054: Event 11210054 """
    IfFlagOff(1, 11210065)
    IfFlagOn(1, 11210064)
    IfHost(1)
    IfConditionTrue(0, input_condition=1)
    SkipLinesIfFlagOff(3, 11210069)
    ForceAnimation(1210402, 7010, skip_transition=True)
    WaitFrames(561)
    SkipLines(2)
    ForceAnimation(1210402, 7002, skip_transition=True)
    WaitFrames(461)
    IfHealthLessThanOrEqual(2, 1210402, 0.009999999776482582)
    SkipLinesIfConditionTrue(26, 2)
    SkipLinesIfFlagOn(3, 11210070)
    SkipLinesIfFlagOn(7, 11210071)
    SkipLinesIfFlagOn(12, 11210072)
    SkipLinesIfFlagOn(17, 11210073)
    WaitFrames(6)
    ForceAnimation(1210402, 7001, skip_transition=True)
    WaitFrames(269)
    DisableFlag(11210069)
    SkipLines(17)
    WaitFrames(6)
    ForceAnimation(1210402, 7008, skip_transition=True)
    WaitFrames(194)
    WaitFrames(60)
    EnableFlag(11210069)
    SkipLines(11)
    WaitFrames(6)
    ForceAnimation(1210402, 7008, skip_transition=True)
    WaitFrames(194)
    WaitFrames(120)
    EnableFlag(11210069)
    SkipLines(5)
    WaitFrames(6)
    ForceAnimation(1210402, 7008, skip_transition=True)
    WaitFrames(194)
    WaitFrames(180)
    EnableFlag(11210069)
    DisableFlag(11210067)
    DisableFlag(11210064)
    Restart()


@RestartOnRest
def Event11210055():
    """ 11210055: Event 11210055 """
    IfFlagOn(1, 11210065)
    IfHost(1)
    IfConditionTrue(0, input_condition=1)
    SkipLinesIfFlagOff(3, 11210069)
    ForceAnimation(1210402, 7011, skip_transition=True)
    WaitFrames(514)
    SkipLines(2)
    ForceAnimation(1210402, 7003, skip_transition=True)
    WaitFrames(414)
    IfHealthLessThanOrEqual(2, 1210402, 0.009999999776482582)
    SkipLinesIfConditionTrue(26, 2)
    SkipLinesIfFlagOn(3, 11210070)
    SkipLinesIfFlagOn(7, 11210071)
    SkipLinesIfFlagOn(12, 11210072)
    SkipLinesIfFlagOn(17, 11210073)
    WaitFrames(6)
    ForceAnimation(1210402, 7001, skip_transition=True)
    WaitFrames(269)
    DisableFlag(11210069)
    SkipLines(17)
    WaitFrames(6)
    ForceAnimation(1210402, 7008, skip_transition=True)
    WaitFrames(194)
    WaitFrames(60)
    EnableFlag(11210069)
    SkipLines(11)
    WaitFrames(6)
    ForceAnimation(1210402, 7008, skip_transition=True)
    WaitFrames(194)
    WaitFrames(120)
    EnableFlag(11210069)
    SkipLines(5)
    WaitFrames(6)
    ForceAnimation(1210402, 7008, skip_transition=True)
    WaitFrames(194)
    WaitFrames(180)
    EnableFlag(11210069)
    DisableFlag(11210067)
    DisableFlag(11210065)
    Restart()


@RestartOnRest
def Event11210056():
    """ 11210056: Event 11210056 """
    IfFlagOff(1, 11210064)
    IfFlagOff(1, 11210065)
    IfFlagOn(1, 11210066)
    IfHost(1)
    IfConditionTrue(0, input_condition=1)
    SkipLinesIfFlagOff(11, 11210069)
    ForceAnimation(1210402, 7009, skip_transition=True)
    WaitFrames(30)
    SkipLinesIfFlagOn(1, 11210070)
    WaitFrames(15)
    SkipLinesIfFlagOn(1, 11210071)
    WaitFrames(30)
    SkipLinesIfFlagOn(1, 11210072)
    WaitFrames(45)
    SkipLinesIfFlagOn(1, 11210073)
    WaitFrames(60)
    SkipLines(11)
    ForceAnimation(1210402, 7008, skip_transition=True)
    WaitFrames(200)
    SkipLinesIfFlagOn(1, 11210070)
    WaitFrames(15)
    SkipLinesIfFlagOn(1, 11210071)
    WaitFrames(30)
    SkipLinesIfFlagOn(1, 11210072)
    WaitFrames(45)
    SkipLinesIfFlagOn(1, 11210073)
    WaitFrames(60)
    EnableFlag(11210069)
    DisableFlag(11210067)
    DisableFlag(11210066)
    Restart()


@RestartOnRest
def Event11210057():
    """ 11210057: Event 11210057 """
    IfFlagOn(1, 11210070)
    IfFlagOn(1, 11210068)
    IfFlagOn(2, 11210071)
    IfFlagOn(2, 11210068)
    IfFlagOn(3, 11210072)
    IfFlagOn(3, 11210068)
    IfFlagOn(4, 11210073)
    IfFlagOn(4, 11210068)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(-1, input_condition=4)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionTrue(3, 1)
    SkipLinesIfFinishedConditionTrue(8, 2)
    SkipLinesIfFinishedConditionTrue(13, 3)
    SkipLinesIfFinishedConditionTrue(18, 4)
    EnableFlag(11210070)
    DisableFlag(11210071)
    DisableFlag(11210072)
    DisableFlag(11210073)
    DisableFlag(11210068)
    Restart()
    DisableFlag(11210070)
    EnableFlag(11210071)
    DisableFlag(11210072)
    DisableFlag(11210073)
    DisableFlag(11210068)
    Restart()
    DisableFlag(11210070)
    DisableFlag(11210071)
    EnableFlag(11210072)
    DisableFlag(11210073)
    DisableFlag(11210068)
    Restart()
    DisableFlag(11210070)
    DisableFlag(11210071)
    DisableFlag(11210072)
    EnableFlag(11210073)
    DisableFlag(11210068)
    Restart()


@RestartOnRest
def Event11210040():
    """ 11210040: Event 11210040 """
    IfHost(1)
    IfCharacterInsideRegion(-1, PLAYER, region=1212054)
    IfCharacterInsideRegion(-1, PLAYER, region=1212062)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(11215055)
    IfHost(2)
    IfCharacterOutsideRegion(2, PLAYER, region=1212054)
    IfCharacterOutsideRegion(2, PLAYER, region=1212062)
    IfConditionTrue(0, input_condition=2)
    DisableFlag(11215055)
    Restart()


@RestartOnRest
def Event11210041():
    """ 11210041: Event 11210041 """
    IfHost(1)
    IfCharacterInsideRegion(1, PLAYER, region=1212055)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(11215056)
    IfHost(2)
    IfCharacterOutsideRegion(2, PLAYER, region=1212055)
    IfConditionTrue(0, input_condition=2)
    DisableFlag(11215056)
    Restart()


@RestartOnRest
def Event11210042():
    """ 11210042: Event 11210042 """
    IfClient(1)
    IfCharacterType(1, PLAYER, CharacterType.WhitePhantom)
    IfCharacterInsideRegion(-1, PLAYER, region=1212054)
    IfCharacterInsideRegion(-1, PLAYER, region=1212062)
    IfConditionTrue(1, input_condition=-1)
    IfFramesElapsed(1, 30)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(11215057)
    WaitFrames(90)
    DisableFlag(11215057)
    Restart()


@RestartOnRest
def Event11210043():
    """ 11210043: Event 11210043 """
    IfClient(1)
    IfCharacterType(1, PLAYER, CharacterType.WhitePhantom)
    IfCharacterInsideRegion(1, PLAYER, region=1212055)
    IfFramesElapsed(1, 30)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(11215058)
    WaitFrames(90)
    DisableFlag(11215058)
    Restart()


@NeverRestart
def Event11210004():
    """ 11210004: Event 11210004 """
    SkipLinesIfThisEventOff(2)
    DisableCharacter(1210401)
    End()
    IfCharacterDead(-1, 1210401)
    IfCharacterDead(-1, 1210402)
    IfConditionTrue(0, input_condition=-1)
    EnableFlag(11210004)


@RestartOnRest
def Event11215050():
    """ 11215050: Event 11215050 """
    IfCharacterInsideRegion(1, PLAYER, region=1212057)
    IfCharacterInsideRegion(2, PLAYER, region=1212059)
    IfAllPlayersOutsideRegion(2, region=1212057)
    IfCharacterInsideRegion(3, PLAYER, region=1212058)
    IfAllPlayersOutsideRegion(3, region=1212057)
    IfAllPlayersOutsideRegion(3, region=1212059)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(4, input_condition=-1)
    IfFlagOn(4, 11215063)
    IfConditionTrue(0, input_condition=4)
    SkipLinesIfFinishedConditionTrue(2, 1)
    SkipLinesIfFinishedConditionTrue(3, 2)
    SkipLinesIfFinishedConditionTrue(4, 3)
    SetEventPoint(1210401, region=1212060, reaction_range=2.0)
    SkipLines(3)
    SetEventPoint(1210401, region=1212060, reaction_range=2.0)
    SkipLines(1)
    SetEventPoint(1210401, region=1212061, reaction_range=2.0)
    Wait(1.0)
    Restart()


@RestartOnRest
def Event11215051():
    """ 11215051: Event 11215051 """
    DisableCharacter(1210410)
    SkipLinesIfFlagOn(7, 11215054)
    SkipLinesIfThisEventSlotOff(4)
    SetDisplayMask(1210401, bit_index=0, switch_type=OnOffChange.On)
    SetHitboxMask(1210401, bit_index=1, switch_type=OnOffChange.Off)
    AICommand(1210401, command_id=20, slot=0)
    End()
    IfCharacterBackreadEnabled(0, 1210401)
    CreateNPCPart(1210401, npc_part_id=4510, part_index=NPCPartType.Part1, part_health=200, damage_correction=1.0, body_damage_correction=1.0, is_invincible=False, start_in_stop_state=False)
    DisableFlag(11215054)
    IfCharacterPartHealthLessThanOrEqual(1, 1210401, npc_part_id=4510, value=0)
    IfHealthLessThanOrEqual(2, 1210401, 0.0)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(2)
    SkipLinesIfFlagOff(3, 11215053)
    SetNPCPartHealth(1210401, npc_part_id=4510, desired_hp=10, overwrite_max=False)
    EnableFlag(11215054)
    Restart()
    Move(1210410, destination=1210401, destination_type=MapEntityType.Character, model_point=150, copy_draw_hitbox=1210401)
    EnableCharacter(1210410)
    ResetAnimation(1210401, disable_interpolation=False)
    ForceAnimation(1210401, 8000)
    ForceAnimation(1210410, 8100)
    SetDisplayMask(1210401, bit_index=0, switch_type=OnOffChange.On)
    SetHitboxMask(1210401, bit_index=1, switch_type=OnOffChange.Off)
    AddSpecialEffect(1210401, 5434)
    AICommand(1210401, command_id=20, slot=0)
    ReplanAI(1210401)
    IfCharacterHuman(-7, PLAYER)
    IfCharacterHollow(-7, PLAYER)
    EndIfConditionFalse(-7)
    AwardItemLot(45110000, host_only=True)


@RestartOnRest
def Event11215052():
    """ 11215052: Event 11215052 """
    IfHasTAEEvent(0, 1210401, tae_event_id=10)
    EnableFlag(11215053)
    IfHasTAEEvent(0, 1210401, tae_event_id=20)
    DisableFlag(11215053)
    Restart()


@RestartOnRest
def Event11215160(ARG_0_3: int):
    """ 11215160: Event 11215160 """
    IfHealthGreaterThan(1, ARG_0_3, 0.0)
    IfCharacterBackreadEnabled(1, ARG_0_3)
    IfCharacterHasSpecialEffect(1, ARG_0_3, 5421)
    IfCharacterType(2, PLAYER, CharacterType.BlackPhantom)
    IfConditionFalse(1, input_condition=2)
    IfDialogPromptActivated(1, prompt_text=10010400, anchor_entity=ARG_0_3, anchor_type=MapEntityType.Character, facing_angle=45.0, max_distance=1.2000000476837158, model_point=7, human_or_hollow_only=False)
    IfConditionTrue(0, input_condition=1)
    Move(PLAYER, destination=ARG_0_3, destination_type=MapEntityType.Character, model_point=100, copy_draw_hitbox=ARG_0_3)
    ForceAnimation(PLAYER, 7521)
    AICommand(ARG_0_3, command_id=10, slot=0)
    ReplanAI(ARG_0_3)
    Wait(0.10000000149011612)
    AICommand(ARG_0_3, command_id=-1, slot=0)
    Restart()


@RestartOnRest
def Event11215165(ARG_0_3: int):
    """ 11215165: Event 11215165 """
    IfCharacterDoesNotHaveSpecialEffect(1, ARG_0_3, 5420)
    IfAttacked(1, ARG_0_3, attacking_character=10000)
    IfConditionTrue(0, input_condition=1)
    CancelSpecialEffect(ARG_0_3, 3150)
    CancelSpecialEffect(ARG_0_3, 3151)
    IfCharacterBackreadDisabled(7, ARG_0_3)
    RestartIfConditionTrue(7)
    IfCharacterHasSpecialEffect(2, ARG_0_3, 5421)
    SkipLinesIfConditionFalse(1, 2)
    ForceAnimation(ARG_0_3, 3001, wait_for_completion=True)
    IfCharacterHasSpecialEffect(3, ARG_0_3, 5422)
    SkipLinesIfConditionFalse(1, 3)
    ForceAnimation(ARG_0_3, 3001, wait_for_completion=True)
    IfCharacterHasSpecialEffect(4, ARG_0_3, 5423)
    SkipLinesIfConditionFalse(1, 4)
    ForceAnimation(ARG_0_3, 3001, wait_for_completion=True)
    IfCharacterHasSpecialEffect(5, ARG_0_3, 5424)
    SkipLinesIfConditionFalse(1, 5)
    ForceAnimation(ARG_0_3, 3006, wait_for_completion=True)
    ReplanAI(ARG_0_3)
    CancelSpecialEffect(ARG_0_3, 3150)
    CancelSpecialEffect(ARG_0_3, 3151)
    Restart()


@RestartOnRest
def Event11215170(ARG_0_3: int):
    """ 11215170: Event 11215170 """
    IfCharacterHasSpecialEffect(1, ARG_0_3, 5421)
    IfCharacterHasSpecialEffect(1, ARG_0_3, 3150)
    IfCharacterHasSpecialEffect(2, ARG_0_3, 5420)
    IfCharacterHasSpecialEffect(2, ARG_0_3, 3150)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionTrue(5, 2)
    AICommand(ARG_0_3, command_id=200, slot=0)
    ReplanAI(ARG_0_3)
    Wait(0.10000000149011612)
    AICommand(ARG_0_3, command_id=-1, slot=0)
    SkipLines(4)
    AICommand(ARG_0_3, command_id=210, slot=0)
    ReplanAI(ARG_0_3)
    Wait(0.10000000149011612)
    AICommand(ARG_0_3, command_id=-1, slot=0)
    IfCharacterHasSpecialEffect(-2, ARG_0_3, 5420)
    IfCharacterHasSpecialEffect(-2, ARG_0_3, 5421)
    IfConditionTrue(0, input_condition=-2)
    Restart()


@RestartOnRest
def Event11215175(ARG_0_3: int):
    """ 11215175: Event 11215175 """
    IfCharacterHasSpecialEffect(1, ARG_0_3, 5422)
    IfCharacterDoesNotHaveSpecialEffect(1, ARG_0_3, 3150)
    IfCharacterHasSpecialEffect(2, ARG_0_3, 5423)
    IfCharacterDoesNotHaveSpecialEffect(2, ARG_0_3, 3150)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    CancelSpecialEffect(ARG_0_3, 3150)
    CancelSpecialEffect(ARG_0_3, 3151)
    SkipLinesIfFinishedConditionTrue(5, 2)
    AICommand(ARG_0_3, command_id=201, slot=0)
    ReplanAI(ARG_0_3)
    Wait(0.10000000149011612)
    AICommand(ARG_0_3, command_id=-1, slot=0)
    SkipLines(4)
    AICommand(ARG_0_3, command_id=211, slot=0)
    ReplanAI(ARG_0_3)
    Wait(0.10000000149011612)
    AICommand(ARG_0_3, command_id=-1, slot=0)
    IfCharacterHasSpecialEffect(-2, ARG_0_3, 5420)
    IfCharacterHasSpecialEffect(-2, ARG_0_3, 5421)
    IfConditionTrue(0, input_condition=-2)
    Restart()


@RestartOnRest
def Event11215180(ARG_0_3: int, ARG_4_7: int):
    """ 11215180: Event 11215180 """
    IfSingleplayer(1)
    IfCharacterInsideRegion(1, ARG_0_3, region=ARG_4_7)
    IfCharacterBackreadDisabled(1, ARG_0_3)
    IfConditionTrue(0, input_condition=1)
    AddSpecialEffect(ARG_0_3, 5421)
    ClearTargetList(ARG_0_3)
    ReplanAI(ARG_0_3)
    Move(ARG_0_3, destination=ARG_4_7, destination_type=MapEntityType.Region, model_point=-1, short_move=True)
    IfCharacterBackreadEnabled(0, ARG_0_3)
    Restart()


@RestartOnRest
def Event11210680(ARG_0_3: int):
    """ 11210680: Event 11210680 """
    SkipLinesIfThisEventSlotOff(2)
    DropMandatoryTreasure(ARG_0_3)
    End()
    IfCharacterDead(0, ARG_0_3)
    End()


@RestartOnRest
def Event11215185(ARG_0_3: int):
    """ 11215185: Event 11215185 """
    EndIfHost()
    IfCharacterBackreadDisabled(1, ARG_0_3)
    EndIfConditionTrue(1)
    ResetAnimation(ARG_0_3, disable_interpolation=True)
    ForceAnimation(ARG_0_3, 0)
    ReplanAI(ARG_0_3)


@NeverRestart
def Event11210200(ARG_0_3: int, ARG_4_7: int):
    """ 11210200: Event 11210200 """
    SkipLinesIfThisEventSlotOff(2)
    DisableObject(ARG_0_3)
    End()
    IfCharacterHasSpecialEffect(-1, PLAYER, 620)
    IfCharacterHasSpecialEffect(-1, PLAYER, 6950)
    IfSkullLanternActive(-1)
    IfConditionTrue(1, input_condition=-1)
    IfCharacterInsideRegion(1, PLAYER, region=ARG_4_7)
    IfConditionTrue(0, input_condition=1)
    PlaySoundEffect(anchor_entity=ARG_0_3, sound_type=SoundType.o_Object, sound_id=262000000)
    ForceAnimation(ARG_0_3, 1, wait_for_completion=True)
    DisableObject(ARG_0_3)


@NeverRestart
def Event11210205(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int):
    """ 11210205: Event 11210205 """
    DisableNetworkSync()
    IfCharacterInsideRegion(0, PLAYER, region=ARG_4_7)
    EndIfFlagOn(ARG_8_11)
    PlaySoundEffect(anchor_entity=ARG_0_3, sound_type=SoundType.o_Object, sound_id=120199999)
    Wait(2.0)
    Restart()


@NeverRestart
def Event11210230(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int, ARG_12_15: int):
    """ 11210230: Event 11210230 """
    SkipLinesIfThisEventSlotOff(4)
    EndOfAnimation(ARG_4_7, ARG_12_15)
    PostDestruction(ARG_0_3, slot=1)
    EnableTreasure(ARG_4_7)
    End()
    DisableTreasure(ARG_4_7)
    SkipLinesIfClient(1)
    CreateObjectFX(99005, obj=ARG_4_7, model_point=90)
    ForceAnimation(ARG_4_7, ARG_8_11, loop=True)
    IfObjectDestroyed(0, ARG_0_3)
    ForceAnimation(ARG_4_7, ARG_12_15, wait_for_completion=True)
    SkipLinesIfClient(1)
    DeleteObjectFX(ARG_4_7, erase_root=True)
    EnableTreasure(ARG_4_7)


@NeverRestart
def Event11210510(ARG_0_3: int, ARG_4_7: int):
    """ 11210510: Event 11210510 """
    IfHealthLessThanOrEqual(1, ARG_0_3, 0.8999999761581421)
    IfHealthGreaterThan(1, ARG_0_3, 0.0)
    IfAttacked(1, ARG_0_3, attacking_character=10000)
    IfFlagOn(2, ARG_4_7)
    IfThisEventSlotOn(2)
    IfFlagOn(3, ARG_4_7)
    IfThisEventSlotOff(3)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionFalse(2, 3)
    DisableCharacter(ARG_0_3)
    IfFlagOn(0, 703)
    EnableFlag(ARG_4_7)
    SetTeamTypeAndExitStandbyAnimation(ARG_0_3, TeamType.HostileAlly)
    SaveRequest()


@NeverRestart
def Event11210910():
    """ 11210910: Event 11210910 """
    SkipLinesIfThisEventOn(1)
    SetAIParamID(6720, 411001)
    IfFlagOn(0, 11210911)
    SetAIParamID(6720, 411000)


@NeverRestart
def Event11210912():
    """ 11210912: Event 11210912 """
    IfFlagOn(0, 1822)
    IfCharacterOutsideRegion(0, PLAYER, region=1212040)
    SetAIParamID(6720, 411001)
    SetNest(6720, 1212041)
    AICommand(6720, command_id=10, slot=0)
    ReplanAI(6720)
    IfCharacterInsideRegion(0, PLAYER, region=1212040)
    WaitFrames(30)
    SetAIParamID(6720, 411000)
    AICommand(6720, command_id=-1, slot=0)
    ReplanAI(6720)
    Restart()


@NeverRestart
def Event11210915():
    """ 11210915: Event 11210915 """
    EndIfFlagOn(1822)
    IfFlagOn(0, 1822)
    ForceAnimation(6720, 9060)


@NeverRestart
def Event11210520(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int, ARG_12_15: int):
    """ 11210520: Event 11210520 """
    SkipLinesIfThisEventSlotOff(2)
    DropMandatoryTreasure(ARG_0_3)
    End()
    IfHealthLessThanOrEqual(0, ARG_0_3, 0.0)
    DisableFlagRange((ARG_4_7, ARG_8_11))
    EnableFlag(ARG_12_15)


@NeverRestart
def Event11210530(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int, ARG_12_15: int):
    """ 11210530: Event 11210530 """
    IfFlagOff(1, 1822)
    IfFlagOn(1, 1820)
    IfFlagOn(1, 11210300)
    IfCharacterAlive(1, ARG_0_3)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((ARG_4_7, ARG_8_11))
    EnableFlag(ARG_12_15)


@NeverRestart
def Event11210535():
    """ 11210535: Event 11210535 """
    EndIfThisEventOn()
    DisableCharacter(1210401)
    IfFlagOn(1, 1821)
    IfFlagOn(1, 11210592)
    IfConditionTrue(0, input_condition=1)
    DisableFlag(121)
    SkipLinesIfMultiplayer(1)
    PlayCutscene(120100, skippable=True, fade_out=False, player_id=PLAYER)
    SkipLines(1)
    PlayCutscene(120100, skippable=False, fade_out=False, player_id=PLAYER)
    WaitFrames(1)
    EnableFlag(11210539)
    EnableCharacter(1210401)
    DisableCharacter(1210402)
    EnableObject(1211690)
    CreateFX(1211691)
    EnableHitbox(1213061)
    DisableHitbox(1213060)


@NeverRestart
def Event11210544():
    """ 11210544: Event 11210544 """
    IfObjectDestroyed(0, 1211130)
    DeleteFX(1213150, erase_root_only=True)


@NeverRestart
def Event11210531(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int, ARG_12_15: int):
    """ 11210531: Event 11210531 """
    IfHost(1)
    IfPlayerHasGood(1, 710, including_box=False)
    IfFlagOn(1, 1860)
    IfFlagOn(1, 11210001)
    IfConditionTrue(0, input_condition=1)
    EndIfThisEventOff()
    EnableCharacter(ARG_0_3)
    EnableObject(1211220)
    DisableFlagRange((ARG_4_7, ARG_8_11))
    EnableFlag(ARG_12_15)


@NeverRestart
def Event11210532(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int, ARG_12_15: int):
    """ 11210532: Event 11210532 """
    IfFlagOff(1, 1863)
    IfFlagOn(1, 1861)
    IfFlagOn(1, 11210590)
    IfCharacterAlive(1, ARG_0_3)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((ARG_4_7, ARG_8_11))
    EnableFlag(ARG_12_15)
    EnableCharacter(ARG_0_3)


@NeverRestart
def Event11210533(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int, ARG_12_15: int):
    """ 11210533: Event 11210533 """
    IfHost(1)
    IfFlagOff(1, 1863)
    IfFlagOff(1, 1865)
    IfFlagOn(1, 1862)
    IfCharacterBackreadDisabled(1, ARG_0_3)
    IfConditionTrue(0, input_condition=1)
    DisableCharacter(ARG_0_3)
    DisableFlagRange((ARG_4_7, ARG_8_11))
    EnableFlag(ARG_12_15)


@NeverRestart
def Event11210534(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int, ARG_12_15: int):
    """ 11210534: Event 11210534 """
    IfHost(1)
    IfFlagOff(1, 1863)
    IfFlagOff(1, 1864)
    IfFlagOff(1, 1865)
    IfFlagOn(1, 11210591)
    IfCharacterBackreadDisabled(1, ARG_0_3)
    IfConditionTrue(0, input_condition=1)
    DisableCharacter(ARG_0_3)
    DisableFlagRange((ARG_4_7, ARG_8_11))
    EnableFlag(ARG_12_15)


@NeverRestart
def Event11210543():
    """ 11210543: Event 11210543 """
    IfFlagOff(1, 11215210)
    IfCharacterInsideRegion(1, 6740, region=1212351)
    IfFlagOn(2, 11215210)
    IfCharacterInsideRegion(2, 6740, region=1212350)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionTrue(3, 2)
    EnableFlag(11215210)
    SetNest(6740, 1212353)
    Restart()
    DisableFlag(11215210)
    SetNest(6740, 1212352)
    Restart()


@NeverRestart
def Event11210540():
    """ 11210540: Event 11210540 """
    IfFlagOn(1, 1127)
    IfFlagOn(1, 11210002)
    IfConditionTrue(0, input_condition=1)
    SkipLinesIfFlagOn(2, 1126)
    SkipLinesIfFlagOn(1, 1125)
    DisableFlagRange((1120, 1139))
    DisableFlag(1127)
    EnableFlag(1128)
    Move(6700, destination=1210840, destination_type=MapEntityType.Character, model_point=30, copy_draw_hitbox=1210840)
    RequestAnimation(6700, 7915, loop=True, wait_for_completion=False)
    EnableCharacter(6700)


@NeverRestart
def Event11210541():
    """ 11210541: Event 11210541 """
    SkipLinesIfThisEventOff(2)
    DropMandatoryTreasure(6700)
    End()
    EnableImmortality(6700)
    IfHealthLessThanOrEqual(0, 6700, 0.009999999776482582)
    ForceAnimation(6700, 7917, wait_for_completion=True)
    DisableCharacter(6700)
    DisableImmortality(6700)
    Kill(6700, award_souls=True)
    Kill(6750, award_souls=False)
    DisableFlagRange((1120, 1139))
    EnableFlag(1125)


@NeverRestart
def Event11210542():
    """ 11210542: Event 11210542 """
    SkipLinesIfFlagOff(1, 11210541)
    End()
    IfAttacked(0, 6700, attacking_character=10000)
    ForceAnimation(6700, 7916, wait_for_completion=True)
    Restart()


@NeverRestart
def Event11210538():
    """ 11210538: Event 11210538 """
    SkipLinesIfThisEventOff(2)
    DropMandatoryTreasure(6750)
    End()
    IfFlagOn(0, 1125)
    DropMandatoryTreasure(6750)
    DisableFlagRange((1870, 1889))
    EnableFlag(1872)


@NeverRestart
def Event11215030(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int, ARG_12_15: int, ARG_16_19: int, ARG_20_23: int, ARG_24_27: int, ARG_28_31: int):
    """ 11215030: Event 11215030 """
    EndIfFlagOn(ARG_4_7)
    DisableCharacter(ARG_0_3)
    EndIfFlagOn(17)
    IfHost(1)
    IfCharacterHuman(1, PLAYER)
    IfFlagOff(1, ARG_12_15)
    IfFlagOff(1, 1842)
    IfCharacterInsideRegion(1, PLAYER, region=ARG_20_23)
    IfFlagOff(-1, ARG_8_11)
    IfFlagOn(2, ARG_8_11)
    IfFlagOn(-2, ARG_24_27)
    IfFlagOn(-2, ARG_28_31)
    IfConditionTrue(2, input_condition=-2)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    DisableCharacter(6730)
    EnableCharacter(ARG_0_3)
    DisplayBattlefieldMessage(20001100, display_location_index=0)
    SkipLinesIfThisEventSlotOn(3)
    CreateTemporaryFX(130, anchor_entity=ARG_16_19, anchor_type=MapEntityType.Region, model_point=-1)
    ForceAnimation(ARG_0_3, 7000)
    ReplanAI(ARG_0_3)
    EnableFlag(ARG_4_7)
    EnableFlag(11210536)


@NeverRestart
def Event11210900(ARG_0_3: int):
    """ 11210900: Event 11210900 """
    EndIfThisEventSlotOn()
    IfCharacterDead(0, ARG_0_3)
    DisplayBattlefieldMessage(20001105, display_location_index=0)
    EnableCharacter(6730)


@NeverRestart
def Event11210905(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int, ARG_12_15: int, ARG_16_19: int, ARG_20_23: int):
    """ 11210905: Event 11210905 """
    SkipLinesIfFlagOff(2, ARG_20_23)
    DisableCharacter(ARG_0_3)
    End()
    IfHost(1)
    IfFlagOn(1, ARG_4_7)
    IfFlagOff(1, ARG_16_19)
    IfCharacterInsideRegion(-1, PLAYER, region=1212084)
    IfCharacterInsideRegion(-1, PLAYER, region=1212085)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(ARG_20_23)
    ForceAnimation(ARG_0_3, 7001)
    WaitFrames(80)
    DisableCharacter(ARG_0_3)
    Move(ARG_0_3, destination=ARG_8_11, destination_type=MapEntityType.Region, model_point=-1, set_draw_hitbox=ARG_12_15)
    DisplayBattlefieldMessage(20001101, display_location_index=0)
    EnableCharacter(6730)


@NeverRestart
def Event11210700():
    """ 11210700: Event 11210700 """
    RunEvent(7999)
    RunEvent(7998)
    SkipLinesIfClient(1)
    DisableFlagRange((11215350, 11215360))
    DisableFlag(11215398)
    DisableFlagRange((11215342, 11215345))
    DeleteFX(1213403, erase_root_only=False)
    DeleteFX(1213404, erase_root_only=False)
    DeleteFX(1213405, erase_root_only=False)
    DeleteFX(1213406, erase_root_only=False)
    DeleteFX(1213407, erase_root_only=False)
    DeleteFX(1213408, erase_root_only=False)
    DeleteFX(1213409, erase_root_only=False)
    DeleteFX(1213410, erase_root_only=False)
    DeleteFX(1213411, erase_root_only=False)
    DeleteFX(1213412, erase_root_only=False)
    DeleteFX(1213416, erase_root_only=False)
    DeleteFX(1213417, erase_root_only=False)
    DeleteFX(1213418, erase_root_only=False)
    DeleteFX(1213419, erase_root_only=False)
    DeleteFX(1213420, erase_root_only=False)
    DeleteFX(1213421, erase_root_only=False)
    DeleteFX(1213422, erase_root_only=False)
    DeleteFX(1213423, erase_root_only=False)
    DeleteFX(1213424, erase_root_only=False)
    DeleteFX(1213425, erase_root_only=False)
    RunEvent(11210708)
    RunEvent(11210838)
    RunEvent(11210839)
    RunEvent(11210875)
    RunEvent(11210876)
    RunEvent(11210830)
    RunEvent(11210835, slot=0, args=(120.0, 60.0, 240.0, 120.0), arg_types='ffff')
    RunEvent(11210836)
    RunEvent(11210877)
    RunEvent(11210878)
    RunEvent(11215398)
    RunEvent(11210705)
    RunEvent(11210706)
    RunEvent(11210707)
    RunEvent(11210845)
    RunEvent(11210846)
    RunEvent(11210847)
    RunEvent(11210848)
    RunEvent(11210849)
    RunEvent(11210837)
    RunEvent(11210401)
    RunEvent(11210402)
    RunEvent(11210403)
    RunEvent(11210404, slot=0, args=(7200,))
    RunEvent(11210404, slot=1, args=(7450,))
    RunEvent(11210404, slot=2, args=(7700,))
    RunEvent(11210407)
    RunEvent(11210439)
    RunEvent(11210710, slot=0, args=(1211500, 1218215, 10010132, 1))
    RunEvent(11210710, slot=1, args=(1211501, 1218213, 10010134, 1))
    RunEvent(11210710, slot=2, args=(1211502, 1218211, 10010136, 1))
    RunEvent(11210710, slot=3, args=(1211503, 1218214, 10010131, 1))
    RunEvent(11210710, slot=4, args=(1211504, 1218212, 10010133, 1))
    RunEvent(11210710, slot=5, args=(1211505, 1218210, 10010135, 1))
    RunEvent(11210710, slot=6, args=(1211510, 1218200, 10010137, 0))
    RunEvent(11210710, slot=7, args=(1211511, 1218200, 10010137, 0))
    RunEvent(11210710, slot=8, args=(1211512, 1218200, 10010137, 0))
    RunEvent(11210710, slot=9, args=(1211513, 1218200, 10010137, 0))
    RunEvent(11210710, slot=10, args=(1211514, 1218200, 10010137, 0))
    RunEvent(11210710, slot=11, args=(1211515, 1218200, 10010137, 0))
    RunEvent(11210730, slot=0, args=(1212700, 4510))
    RunEvent(11210730, slot=1, args=(1212701, 4511))
    RunEvent(11210730, slot=2, args=(1212702, 4512))
    RunEvent(11210730, slot=3, args=(1212703, 4513))
    RunEvent(11210730, slot=4, args=(1212704, 4514))
    RunEvent(11210730, slot=5, args=(1212705, 4515))
    RunEvent(11210730, slot=6, args=(1212706, 4516))
    RunEvent(11210730, slot=7, args=(1212707, 4517))
    RunEvent(11210730, slot=8, args=(1212708, 4518))
    RunEvent(11210730, slot=9, args=(1212709, 4519))
    RunEvent(11210730, slot=10, args=(1212710, 4520))
    RunEvent(11210730, slot=11, args=(1212711, 4521))
    RunEvent(11210730, slot=12, args=(1212712, 4522))
    RunEvent(11210730, slot=13, args=(1212713, 4523))
    RunEvent(11210730, slot=14, args=(1212714, 4524))
    RunEvent(11210730, slot=15, args=(1212715, 4525))
    RunEvent(11210730, slot=16, args=(1212716, 4526))
    RunEvent(11210730, slot=17, args=(1212717, 4527))
    RunEvent(11210730, slot=18, args=(1212718, 4528))
    RunEvent(11210730, slot=19, args=(1212719, 4529))
    RunEvent(11210730, slot=20, args=(1212720, 4530))
    RunEvent(11210730, slot=21, args=(1212721, 4531))
    RunEvent(11210730, slot=22, args=(1212722, 4532))
    RunEvent(11210730, slot=23, args=(1212723, 4533))
    RunEvent(11210730, slot=24, args=(1212724, 4534))
    RunEvent(11210730, slot=25, args=(1212725, 4535))
    RunEvent(11210410, slot=0, args=(1212722, 11215350, 1213422, 11215355, 11215360))
    RunEvent(11210410, slot=1, args=(1212723, 11215351, 1213423, 11215356, 11215361))
    RunEvent(11210410, slot=2, args=(1212724, 11215352, 1213424, 11215357, 11215362))
    RunEvent(11210410, slot=3, args=(1212725, 11215353, 1213425, 11215358, 11215363))
    RunEvent(11210410, slot=4, args=(1212718, 11215350, 1213418, 11215355, 11215360))
    RunEvent(11210410, slot=5, args=(1212719, 11215351, 1213419, 11215356, 11215361))
    RunEvent(11210410, slot=6, args=(1212720, 11215352, 1213420, 11215357, 11215362))
    RunEvent(11210410, slot=7, args=(1212721, 11215353, 1213421, 11215358, 11215363))
    RunEvent(11210410, slot=8, args=(1212716, 11215350, 1213416, 11215355, 11215360))
    RunEvent(11210410, slot=9, args=(1212717, 11215352, 1213417, 11215357, 11215362))
    RunEvent(11210410, slot=10, args=(1212709, 11215350, 1213409, 11215355, 11215360))
    RunEvent(11210410, slot=11, args=(1212710, 11215351, 1213410, 11215356, 11215361))
    RunEvent(11210410, slot=12, args=(1212711, 11215352, 1213411, 11215357, 11215362))
    RunEvent(11210410, slot=13, args=(1212712, 11215353, 1213412, 11215358, 11215363))
    RunEvent(11210410, slot=14, args=(1212705, 11215350, 1213405, 11215355, 11215360))
    RunEvent(11210410, slot=15, args=(1212706, 11215351, 1213406, 11215356, 11215361))
    RunEvent(11210410, slot=16, args=(1212707, 11215352, 1213407, 11215357, 11215362))
    RunEvent(11210410, slot=17, args=(1212708, 11215353, 1213408, 11215358, 11215363))
    RunEvent(11210410, slot=18, args=(1212703, 11215350, 1213403, 11215355, 11215360))
    RunEvent(11210410, slot=19, args=(1212704, 11215352, 1213404, 11215357, 11215362))
    RunEvent(11210800, slot=0, args=(1212722, 11215350))
    RunEvent(11210800, slot=1, args=(1212723, 11215351))
    RunEvent(11210800, slot=2, args=(1212724, 11215352))
    RunEvent(11210800, slot=3, args=(1212725, 11215353))
    RunEvent(11210800, slot=4, args=(1212718, 11215350))
    RunEvent(11210800, slot=5, args=(1212719, 11215351))
    RunEvent(11210800, slot=6, args=(1212720, 11215352))
    RunEvent(11210800, slot=7, args=(1212721, 11215353))
    RunEvent(11210800, slot=8, args=(1212716, 11215350))
    RunEvent(11210800, slot=9, args=(1212717, 11215352))
    RunEvent(11210800, slot=10, args=(1212709, 11215350))
    RunEvent(11210800, slot=11, args=(1212710, 11215351))
    RunEvent(11210800, slot=12, args=(1212711, 11215352))
    RunEvent(11210800, slot=13, args=(1212712, 11215353))
    RunEvent(11210800, slot=14, args=(1212705, 11215350))
    RunEvent(11210800, slot=15, args=(1212706, 11215351))
    RunEvent(11210800, slot=16, args=(1212707, 11215352))
    RunEvent(11210800, slot=17, args=(1212708, 11215353))
    RunEvent(11210800, slot=18, args=(1212703, 11215350))
    RunEvent(11210800, slot=19, args=(1212704, 11215352))
    RunEvent(11210820, slot=0, args=(11215350, 11215360, 11210825, 0))
    RunEvent(11210820, slot=1, args=(11215351, 11215361, 11210825, 1))
    RunEvent(11210820, slot=2, args=(11215352, 11215362, 11210825, 2))
    RunEvent(11210820, slot=3, args=(11215353, 11215363, 11210825, 3))
    RunEvent(11210825, slot=0, args=(11215360, 11215370))
    RunEvent(11210825, slot=1, args=(11215361, 11215371))
    RunEvent(11210825, slot=2, args=(11215362, 11215372))
    RunEvent(11210825, slot=3, args=(11215363, 11215373))
    RunEvent(11210701, slot=0, args=(11215350, 11215300, 11215312, 11215318, 11215306))
    RunEvent(11210701, slot=1, args=(11215351, 11215306, 11215312, 11215318, 11215300))
    RunEvent(11210701, slot=2, args=(11215352, 11215312, 11215300, 11215306, 11215318))
    RunEvent(11210701, slot=3, args=(11215353, 11215318, 11215300, 11215306, 11215312))
    RunEvent(11210434)
    RunEvent(11210430, slot=0, args=(11215350, 11215300, 11215312))
    RunEvent(11210430, slot=1, args=(11215351, 11215306, 11215312))
    RunEvent(11210430, slot=2, args=(11215352, 11215312, 11215300))
    RunEvent(11210430, slot=3, args=(11215353, 11215318, 11215300))
    RunEvent(11210435, slot=0, args=(11215350, 11215300, 11215312, 11215318, 11215306))
    RunEvent(11210435, slot=1, args=(11215351, 11215306, 11215312, 11215318, 11215300))
    RunEvent(11210435, slot=2, args=(11215352, 11215312, 11215300, 11215306, 11215318))
    RunEvent(11210435, slot=3, args=(11215353, 11215318, 11215300, 11215306, 11215312))
    RunEvent(11210870, slot=0, args=(11215350, 11215300, 11215312, 11215318, 11215306))
    RunEvent(11210870, slot=1, args=(11215351, 11215306, 11215312, 11215318, 11215300))
    RunEvent(11210870, slot=2, args=(11215352, 11215312, 11215300, 11215306, 11215318))
    RunEvent(11210870, slot=3, args=(11215353, 11215318, 11215300, 11215306, 11215312))
    RunEvent(11210831, slot=0, args=(11215360, 11215300, 11215305))
    RunEvent(11210831, slot=1, args=(11215361, 11215306, 11215311))
    RunEvent(11210831, slot=2, args=(11215362, 11215312, 11215317))
    RunEvent(11210831, slot=3, args=(11215363, 11215318, 11215323))
    RunEvent(11210760, slot=0, args=(1212711, 1211520, 1213202, 11215372))
    RunEvent(11210760, slot=1, args=(1212712, 1211521, 1213203, 11215373))
    RunEvent(11210760, slot=2, args=(1212709, 1211522, 1213200, 11215370))
    RunEvent(11210760, slot=3, args=(1212710, 1211523, 1213201, 11215371))
    RunEvent(11210760, slot=4, args=(1212707, 1211530, 1213212, 11215372))
    RunEvent(11210760, slot=5, args=(1212708, 1211531, 1213213, 11215373))
    RunEvent(11210760, slot=6, args=(1212705, 1211532, 1213210, 11215370))
    RunEvent(11210760, slot=7, args=(1212706, 1211533, 1213211, 11215371))
    RunEvent(11210760, slot=8, args=(1212704, 1211540, 1213222, 11215372))
    RunEvent(11210760, slot=9, args=(1212703, 1211542, 1213220, 11215370))
    RunEvent(11210760, slot=10, args=(1212724, 1211550, 1213232, 11215372))
    RunEvent(11210760, slot=11, args=(1212725, 1211551, 1213233, 11215373))
    RunEvent(11210760, slot=12, args=(1212722, 1211552, 1213230, 11215370))
    RunEvent(11210760, slot=13, args=(1212723, 1211553, 1213231, 11215371))
    RunEvent(11210760, slot=14, args=(1212720, 1211560, 1213242, 11215372))
    RunEvent(11210760, slot=15, args=(1212721, 1211561, 1213243, 11215373))
    RunEvent(11210760, slot=16, args=(1212718, 1211562, 1213240, 11215370))
    RunEvent(11210760, slot=17, args=(1212719, 1211563, 1213241, 11215371))
    RunEvent(11210760, slot=18, args=(1212717, 1211570, 1213252, 11215372))
    RunEvent(11210760, slot=19, args=(1212716, 1211572, 1213250, 11215370))
    RunEvent(11210780, slot=0, args=(1212711, 1211420, 1213302, 11215362))
    RunEvent(11210780, slot=1, args=(1212712, 1211421, 1213303, 11215363))
    RunEvent(11210780, slot=2, args=(1212709, 1211422, 1213300, 11215360))
    RunEvent(11210780, slot=3, args=(1212710, 1211423, 1213301, 11215361))
    RunEvent(11210780, slot=4, args=(1212707, 1211430, 1213302, 11215362))
    RunEvent(11210780, slot=5, args=(1212708, 1211431, 1213303, 11215363))
    RunEvent(11210780, slot=6, args=(1212705, 1211432, 1213300, 11215360))
    RunEvent(11210780, slot=7, args=(1212706, 1211433, 1213301, 11215361))
    RunEvent(11210780, slot=8, args=(1212704, 1211440, 1213302, 11215362))
    RunEvent(11210780, slot=9, args=(1212703, 1211442, 1213300, 11215360))
    RunEvent(11210780, slot=10, args=(1212724, 1211450, 1213302, 11215362))
    RunEvent(11210780, slot=11, args=(1212725, 1211451, 1213303, 11215363))
    RunEvent(11210780, slot=12, args=(1212722, 1211452, 1213300, 11215360))
    RunEvent(11210780, slot=13, args=(1212723, 1211453, 1213301, 11215361))
    RunEvent(11210780, slot=14, args=(1212720, 1211460, 1213302, 11215362))
    RunEvent(11210780, slot=15, args=(1212721, 1211461, 1213303, 11215363))
    RunEvent(11210780, slot=16, args=(1212718, 1211462, 1213300, 11215360))
    RunEvent(11210780, slot=17, args=(1212719, 1211463, 1213301, 11215361))
    RunEvent(11210780, slot=18, args=(1212717, 1211470, 1213302, 11215362))
    RunEvent(11210780, slot=19, args=(1212716, 1211472, 1213300, 11215360))
    RunEvent(11210840, slot=0, args=(11215350, 11215370, 11215375, 11215300, 11215306, 150070))
    RunEvent(11210840, slot=1, args=(11215351, 11215371, 11215376, 11215306, 11215300, 150071))
    RunEvent(11210840, slot=2, args=(11215352, 11215372, 11215377, 11215312, 11215318, 150072))
    RunEvent(11210840, slot=3, args=(11215353, 11215373, 11215378, 11215318, 11215312, 150073))
    RunEvent(11210850, slot=0, args=(11215350, 11215375, 1212700, 1212703))
    RunEvent(11210850, slot=1, args=(11215352, 11215377, 1212700, 1212704))
    RunEvent(11210850, slot=2, args=(11215350, 11215375, 1212701, 1212705))
    RunEvent(11210850, slot=3, args=(11215351, 11215376, 1212701, 1212706))
    RunEvent(11210850, slot=4, args=(11215352, 11215377, 1212701, 1212707))
    RunEvent(11210850, slot=5, args=(11215353, 11215378, 1212701, 1212708))
    RunEvent(11210850, slot=6, args=(11215350, 11215375, 1212702, 1212709))
    RunEvent(11210850, slot=7, args=(11215351, 11215376, 1212702, 1212710))
    RunEvent(11210850, slot=8, args=(11215352, 11215377, 1212702, 1212711))
    RunEvent(11210850, slot=9, args=(11215353, 11215378, 1212702, 1212712))
    RunEvent(11210850, slot=10, args=(11215350, 11215375, 1212713, 1212716))
    RunEvent(11210850, slot=11, args=(11215352, 11215377, 1212713, 1212717))
    RunEvent(11210850, slot=12, args=(11215350, 11215375, 1212714, 1212718))
    RunEvent(11210850, slot=13, args=(11215351, 11215376, 1212714, 1212719))
    RunEvent(11210850, slot=14, args=(11215352, 11215377, 1212714, 1212720))
    RunEvent(11210850, slot=15, args=(11215353, 11215378, 1212714, 1212721))
    RunEvent(11210850, slot=16, args=(11215350, 11215375, 1212715, 1212722))
    RunEvent(11210850, slot=17, args=(11215351, 11215376, 1212715, 1212723))
    RunEvent(11210850, slot=18, args=(11215352, 11215377, 1212715, 1212724))
    RunEvent(11210850, slot=19, args=(11215353, 11215378, 1212715, 1212725))
    RunEvent(11210886, slot=0, args=(11215350, 11215375))
    RunEvent(11210886, slot=1, args=(11215351, 11215376))
    RunEvent(11210886, slot=2, args=(11215352, 11215377))
    RunEvent(11210886, slot=3, args=(11215353, 11215378))
    RunEvent(11210880, slot=0, args=(1212700, 1212703))
    RunEvent(11210880, slot=1, args=(1212701, 1212705))
    RunEvent(11210880, slot=2, args=(1212702, 1212709))
    RunEvent(11210880, slot=3, args=(1212713, 1212716))
    RunEvent(11210880, slot=4, args=(1212714, 1212718))
    RunEvent(11210880, slot=5, args=(1212715, 1212722))
    RunEvent(11210890, slot=0, args=(1212730, 1218215))
    RunEvent(11210890, slot=1, args=(1212731, 1218213))
    RunEvent(11210890, slot=2, args=(1212732, 1218211))
    RunEvent(11210890, slot=3, args=(1212733, 1218214))
    RunEvent(11210890, slot=4, args=(1212734, 1218212))
    RunEvent(11210890, slot=5, args=(1212735, 1218210))


@NeverRestart
def Event11210708():
    """ 11210708: Event 11210708 """
    EndIfThisEventOn()
    IfCharacterInsideRegion(-1, PLAYER, region=1212700)
    IfCharacterInsideRegion(-1, PLAYER, region=1212701)
    IfCharacterInsideRegion(-1, PLAYER, region=1212702)
    IfCharacterInsideRegion(-1, PLAYER, region=1212713)
    IfCharacterInsideRegion(-1, PLAYER, region=1212714)
    IfCharacterInsideRegion(-1, PLAYER, region=1212715)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    IfPlayerHasGood(2, 118, including_box=False)
    EndIfConditionTrue(2)
    AwardItemLot(2200, host_only=False)


@NeverRestart
def Event11210710(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int, ARG_12_15: int):
    """ 11210710: Event 11210710 """
    IfDialogPromptActivated(0, prompt_text=ARG_8_11, anchor_entity=ARG_0_3, anchor_type=MapEntityType.Object, facing_angle=180.0, max_distance=2.0, model_point=100, human_or_hollow_only=True)
    EnableFlag(11215341)
    EnableFlag(11210709)
    RotateToFaceEntity(PLAYER, ARG_0_3)
    ForceAnimation(PLAYER, 7114)
    Wait(0.699999988079071)
    CreateTemporaryFX(90021, anchor_entity=10000, anchor_type=MapEntityType.Character, model_point=17)
    Wait(1.5)
    IfHealthEqual(1, PLAYER, 0.0)
    EndIfConditionTrue(1)
    SkipLinesIfEqual(1, left=0, right=ARG_12_15)
    DisableFlagRange((7000, 7799))
    SkipLinesIfEqual(1, left=1, right=ARG_12_15)
    ArenaExitRequest()
    DisableFlagRange((8140, 8146))
    WarpToMap(game_map=OOLACILE, destination_player_id=ARG_4_7)


@NeverRestart
def Event11210730(ARG_0_3: int, ARG_4_7: int):
    """ 11210730: Event 11210730 """
    DisableNetworkSync()
    IfFlagOff(1, 11215390)
    IfFlagOff(1, 765)
    IfCharacterInsideRegion(1, PLAYER, region=ARG_0_3)
    IfConditionTrue(0, input_condition=1)
    AddSpecialEffect(PLAYER, ARG_4_7)
    WaitFrames(10)
    Restart()


@NeverRestart
def Event11210878():
    """ 11210878: Event 11210878 """
    DisableNetworkSync()
    IfCharacterInsideRegion(-1, PLAYER, region=1212700)
    IfCharacterInsideRegion(-1, PLAYER, region=1212701)
    IfCharacterInsideRegion(-1, PLAYER, region=1212702)
    IfCharacterInsideRegion(-1, PLAYER, region=1212713)
    IfCharacterInsideRegion(-1, PLAYER, region=1212714)
    IfCharacterInsideRegion(-1, PLAYER, region=1212715)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    AddSpecialEffect(PLAYER, 4610)
    SkipLinesIfFlagOn(1, 11215398)
    AddSpecialEffect(PLAYER, 4613)
    Wait(1.0)
    Restart()


@NeverRestart
def Event11215398():
    """ 11215398: Event 11215398 """
    DisableNetworkSync()
    IfCharacterInsideRegion(-1, PLAYER, region=1212740)
    IfCharacterInsideRegion(-1, PLAYER, region=1212741)
    IfConditionTrue(0, input_condition=-1)
    CancelSpecialEffect(PLAYER, 4613)
    Restart()


@NeverRestart
def Event11210875():
    """ 11210875: Event 11210875 """
    DisableNetworkSync()
    IfMultiplayer(1)
    IfCharacterInsideRegion(-1, PLAYER, region=1212703)
    IfCharacterInsideRegion(-1, PLAYER, region=1212704)
    IfCharacterInsideRegion(-1, PLAYER, region=1212705)
    IfCharacterInsideRegion(-1, PLAYER, region=1212706)
    IfCharacterInsideRegion(-1, PLAYER, region=1212707)
    IfCharacterInsideRegion(-1, PLAYER, region=1212708)
    IfCharacterInsideRegion(-1, PLAYER, region=1212709)
    IfCharacterInsideRegion(-1, PLAYER, region=1212710)
    IfCharacterInsideRegion(-1, PLAYER, region=1212711)
    IfCharacterInsideRegion(-1, PLAYER, region=1212712)
    IfCharacterInsideRegion(-1, PLAYER, region=1212716)
    IfCharacterInsideRegion(-1, PLAYER, region=1212717)
    IfCharacterInsideRegion(-1, PLAYER, region=1212718)
    IfCharacterInsideRegion(-1, PLAYER, region=1212719)
    IfCharacterInsideRegion(-1, PLAYER, region=1212720)
    IfCharacterInsideRegion(-1, PLAYER, region=1212721)
    IfCharacterInsideRegion(-1, PLAYER, region=1212722)
    IfCharacterInsideRegion(-1, PLAYER, region=1212723)
    IfCharacterInsideRegion(-1, PLAYER, region=1212724)
    IfCharacterInsideRegion(-1, PLAYER, region=1212725)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(11215394)
    EnableInvincibility(PLAYER)
    AddSpecialEffect(PLAYER, 90000)
    Wait(4.0)
    RestartEvent(11210876, slot=0)
    Restart()


@NeverRestart
def Event11210876():
    """ 11210876: Event 11210876 """
    DisableNetworkSync()
    IfFlagOn(0, 11215394)
    Wait(5.0)
    DisableFlag(11215394)
    SkipLinesIfFlagOn(2, 11215391)
    DisableInvincibility(PLAYER)
    CancelSpecialEffect(PLAYER, 90000)
    Restart()


@NeverRestart
def Event11210780(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int, ARG_12_15: int):
    """ 11210780: Event 11210780 """
    SkipLinesIfHost(1)
    SkipLinesIfFlagOn(9, ARG_12_15)
    EndOfAnimation(ARG_4_7, 1)
    DisableHitbox(ARG_8_11)
    IfMultiplayer(1)
    IfCharacterInsideRegion(-1, PLAYER, region=ARG_0_3)
    IfFlagOn(-1, ARG_12_15)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    EnableHitbox(ARG_8_11)
    ForceAnimation(ARG_4_7, 0, wait_for_completion=True)
    IfFlagOff(2, 11215340)
    IfSingleplayer(-2)
    IfFlagOff(3, ARG_12_15)
    IfAllPlayersOutsideRegion(3, region=ARG_0_3)
    IfConditionTrue(-2, input_condition=3)
    IfConditionTrue(2, input_condition=-2)
    IfConditionTrue(0, input_condition=2)
    ForceAnimation(ARG_4_7, 1, wait_for_completion=True)
    Restart()


@NeverRestart
def Event11210410(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int, ARG_12_15: int, ARG_16_19: int):
    """ 11210410: Event 11210410 """
    SkipLinesIfFlagOn(10, ARG_12_15)
    IfFlagOff(1, 765)
    IfFlagOff(1, 11215390)
    IfFlagOn(1, ARG_4_7)
    IfCharacterInsideRegion(1, PLAYER, region=ARG_0_3)
    IfFlagOn(5, ARG_16_19)
    IfFlagOff(5, 11215390)
    IfTimeElapsed(5, 15.0)
    IfConditionTrue(-2, input_condition=1)
    IfConditionTrue(-2, input_condition=5)
    IfConditionTrue(0, input_condition=-2)
    EnableFlag(ARG_12_15)
    SkipLinesIfMultiplayer(1)
    DisplayBattlefieldMessage(150000, display_location_index=1)
    CreateFX(ARG_8_11)
    SkipLinesIfFlagOff(11, ARG_12_15)
    IfFlagOn(2, ARG_4_7)
    IfCharacterOutsideRegion(2, PLAYER, region=ARG_0_3)
    IfMultiplayer(3)
    IfFlagOff(3, ARG_16_19)
    IfTimeElapsed(3, 5.0)
    IfSingleplayer(4)
    IfFlagOff(4, ARG_4_7)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(-1, input_condition=4)
    IfConditionTrue(0, input_condition=-1)
    DisableFlag(ARG_12_15)
    DeleteFX(ARG_8_11, erase_root_only=True)
    Restart()


@NeverRestart
def Event11210800(ARG_0_3: int, ARG_4_7: int):
    """ 11210800: Event 11210800 """
    DisableNetworkSync()
    IfCharacterInsideRegion(0, PLAYER, region=ARG_0_3)
    DisableFlagRange((11215350, 11215353))
    EnableFlag(ARG_4_7)
    IfFlagOff(0, ARG_4_7)
    Restart()


@NeverRestart
def Event11210820(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int, ARG_12_15: int):
    """ 11210820: Event 11210820 """
    IfMultiplayer(1)
    SkipLinesIfEqual(1, left=ARG_0_3, right=11215350)
    IfClient(1)
    IfFlagOn(1, ARG_0_3)
    IfTimeElapsed(1, 3.0)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(ARG_4_7)
    RestartEvent(ARG_8_11, slot=ARG_12_15)
    Restart()


@NeverRestart
def Event11210825(ARG_0_3: int, ARG_4_7: int):
    """ 11210825: Event 11210825 """
    DisableNetworkSync()
    IfFlagOn(1, ARG_0_3)
    IfTimeElapsed(1, 10.0)
    IfConditionTrue(0, input_condition=1)
    RestartIfFlagOn(ARG_4_7)
    DisableFlag(ARG_0_3)
    Restart()


@NeverRestart
def Event11210830():
    """ 11210830: Event 11210830 """
    IfCharacterInsideRegion(1, PLAYER, region=1212715)
    IfFlagRangeAllOn(1, (11215360, 11215363))
    IfCharacterInsideRegion(2, PLAYER, region=1212702)
    IfFlagRangeAllOn(2, (11215360, 11215363))
    IfCharacterInsideRegion(3, PLAYER, region=1212714)
    IfFlagRangeAllOn(3, (11215360, 11215363))
    IfCharacterInsideRegion(4, PLAYER, region=1212701)
    IfFlagRangeAllOn(4, (11215360, 11215363))
    IfCharacterInsideRegion(5, PLAYER, region=1212713)
    IfFlagOn(5, 11215360)
    IfFlagOn(5, 11215362)
    IfCharacterInsideRegion(6, PLAYER, region=1212700)
    IfFlagOn(6, 11215360)
    IfFlagOn(6, 11215362)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(-1, input_condition=4)
    IfConditionTrue(-1, input_condition=5)
    IfConditionTrue(-1, input_condition=6)
    IfConditionTrue(0, input_condition=-1)
    EnableFlag(11215340)
    SkipLinesIfFinishedConditionTrue(2, 3)
    SkipLinesIfFinishedConditionTrue(1, 4)
    SkipLines(1)
    EnableFlag(11215392)
    SkipLinesIfFinishedConditionTrue(2, 1)
    SkipLinesIfFinishedConditionTrue(1, 2)
    SkipLines(1)
    EnableFlag(11215395)
    Wait(8.0)
    SkipLinesIfFlagOn(3, 11215395)
    SkipLinesIfFlagOn(2, 11215392)
    DisplayBattlefieldMessage(150215, display_location_index=1)
    SkipLines(1)
    DisplayBattlefieldMessage(150205, display_location_index=1)
    Wait(2.0)
    EnableFlag(11215390)
    IfFlagOff(0, 11215390)
    Restart()


@NeverRestart
def Event11210831(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int):
    """ 11210831: Event 11210831 """
    IfHost(1)
    IfFlagOn(1, 11215390)
    IfFlagOff(1, ARG_0_3)
    IfFlagRangeAnyOff(1, (ARG_4_7, ARG_8_11))
    IfConditionTrue(0, input_condition=1)
    SkipLinesIfFlagOn(1, 11215392)
    EnableFlagRange((ARG_4_7, ARG_8_11))


@NeverRestart
def Event11210835(ARG_0_3: float, ARG_4_7: float, ARG_8_11: float, ARG_12_15: float):
    """ 11210835: Event 11210835 """
    DisableNetworkSync()
    IfHost(1)
    IfFlagOff(1, 11215391)
    IfFlagOn(1, 11215390)
    IfConditionTrue(0, input_condition=1)
    SkipLinesIfFlagOn(3, 11215395)
    SkipLinesIfFlagOn(2, 11215392)
    Wait(ARG_0_3)
    SkipLines(1)
    Wait(ARG_8_11)
    EnableFlag(11215396)
    SkipLinesIfFlagOn(3, 11215395)
    SkipLinesIfFlagOn(2, 11215392)
    Wait(ARG_4_7)
    SkipLines(1)
    Wait(ARG_12_15)
    IfFlagOff(0, 904)
    EnableFlag(11215391)
    Restart()


@NeverRestart
def Event11210836():
    """ 11210836: Event 11210836 """
    IfFlagOn(0, 11215396)
    EnableFlag(11215396)
    SkipLinesIfFlagOn(3, 11215395)
    SkipLinesIfFlagOn(2, 11215392)
    DisplayBattlefieldMessage(150115, display_location_index=0)
    SkipLines(1)
    DisplayBattlefieldMessage(150105, display_location_index=0)
    IfFlagOn(0, 11215391)
    EnableFlag(11215391)
    DisplayBattlefieldMessage(150300, display_location_index=0)
    IfFlagOff(0, 11215391)
    Restart()


@NeverRestart
def Event11210760(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int, ARG_12_15: int):
    """ 11210760: Event 11210760 """
    IfFlagOn(1, 11215390)
    IfFlagOff(1, ARG_12_15)
    IfCharacterInsideRegion(1, PLAYER, region=ARG_0_3)
    IfConditionTrue(0, input_condition=1)
    Wait(1.0)
    DisableHitbox(ARG_8_11)
    ForceAnimation(ARG_4_7, 1, wait_for_completion=True)
    EnableHitbox(ARG_8_11)
    Restart()


@NeverRestart
def Event11210840(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int, ARG_12_15: int, ARG_16_19: int, ARG_20_23: int):
    """ 11210840: Event 11210840 """
    IfFlagOn(1, ARG_0_3)
    IfFlagOn(1, 11215390)
    IfFlagOff(1, 11215391)
    IfHealthValueEqual(1, PLAYER, 1)
    IfConditionTrue(0, input_condition=1)
    EnableInvincibility(PLAYER)
    AddSpecialEffect(PLAYER, 101)
    AddSpecialEffect(PLAYER, 102)
    AddSpecialEffect(PLAYER, 103)
    AddSpecialEffect(PLAYER, 104)
    AddSpecialEffect(PLAYER, 4611)
    SkipLinesIfFlagOn(2, ARG_0_3)
    DisplayBattlefieldMessage(ARG_20_23, display_location_index=1)
    SkipLines(1)
    DisplayBattlefieldMessage(150023, display_location_index=1)
    IncrementEventValue(ARG_12_15, bit_count=6, max_value=63)
    SkipLinesIfFlagOff(1, 11215392)
    IncrementEventValue(ARG_16_19, bit_count=6, max_value=63)
    Wait(3.0)
    EnableFlag(ARG_4_7)
    EnableFlag(ARG_8_11)
    IfFlagOff(0, ARG_8_11)
    DisableFlag(ARG_8_11)
    SkipLinesIfFlagOn(1, ARG_0_3)
    DisableInvincibility(PLAYER)
    CancelSpecialEffect(PLAYER, 4611)
    ResetAnimation(PLAYER, disable_interpolation=True)
    ForceAnimation(PLAYER, 6950, wait_for_completion=True)
    DisableFlag(ARG_4_7)
    Restart()


@NeverRestart
def Event11210850(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int, ARG_12_15: int):
    """ 11210850: Event 11210850 """
    DisableNetworkSync()
    IfFlagOn(1, ARG_0_3)
    IfFlagOn(1, ARG_4_7)
    IfCharacterInsideRegion(1, PLAYER, region=ARG_8_11)
    IfConditionTrue(0, input_condition=1)
    PlayCutscene(120130, skippable=False, fade_out=False, move_to_region=ARG_12_15, move_to_map=OOLACILE)
    WaitFrames(1)
    EqualRecovery()
    DisableFlag(ARG_4_7)
    Restart()


@NeverRestart
def Event11210886(ARG_0_3: int, ARG_4_7: int):
    """ 11210886: Event 11210886 """
    IfFlagOn(1, ARG_0_3)
    IfFlagOn(1, ARG_4_7)
    IfConditionTrue(0, input_condition=1)
    SkipLinesIfFlagOn(1, ARG_0_3)
    DisableCharacter(PLAYER)
    IfFlagOn(2, ARG_0_3)
    IfFlagOff(2, ARG_4_7)
    IfTimeElapsed(2, 2.0)
    IfConditionTrue(0, input_condition=2)
    SkipLinesIfFlagOn(1, ARG_0_3)
    EnableCharacter(PLAYER)
    Restart()


@NeverRestart
def Event11210870(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int, ARG_12_15: int, ARG_16_19: int):
    """ 11210870: Event 11210870 """
    DisableNetworkSync()
    IfFlagOn(1, ARG_0_3)
    IfFlagOn(1, 11215390)
    IfFlagOn(1, 11215391)
    IfConditionTrue(0, input_condition=1)
    EnableInvincibility(PLAYER)
    AddSpecialEffect(PLAYER, 90000)
    Wait(6.0)
    EnableFlag(11215397)
    IfEventsComparison(2, ARG_4_7, 6, ComparisonType.LessThan, ARG_8_11, 6)
    IfEventsComparison(2, ARG_4_7, 6, ComparisonType.LessThan, ARG_12_15, 6)
    SkipLinesIfFlagOn(1, 11215392)
    IfEventsComparison(2, ARG_4_7, 6, ComparisonType.LessThan, ARG_16_19, 6)
    IfEventsComparison(-1, ARG_4_7, 6, ComparisonType.GreaterThan, ARG_8_11, 6)
    IfEventsComparison(-1, ARG_4_7, 6, ComparisonType.GreaterThan, ARG_12_15, 6)
    SkipLinesIfFlagOn(1, 11215392)
    IfEventsComparison(-1, ARG_4_7, 6, ComparisonType.GreaterThan, ARG_16_19, 6)
    IfEventsComparison(3, ARG_4_7, 6, ComparisonType.Equal, ARG_8_11, 6)
    SkipLinesIfFlagOn(8, 11215392)
    IfEventsComparison(3, ARG_4_7, 6, ComparisonType.LessThan, ARG_12_15, 6)
    IfEventsComparison(3, ARG_4_7, 6, ComparisonType.LessThan, ARG_16_19, 6)
    IfEventsComparison(4, ARG_4_7, 6, ComparisonType.LessThan, ARG_8_11, 6)
    IfEventsComparison(4, ARG_4_7, 6, ComparisonType.Equal, ARG_12_15, 6)
    IfEventsComparison(4, ARG_4_7, 6, ComparisonType.LessThan, ARG_16_19, 6)
    IfEventsComparison(5, ARG_4_7, 6, ComparisonType.LessThan, ARG_8_11, 6)
    IfEventsComparison(5, ARG_4_7, 6, ComparisonType.LessThan, ARG_12_15, 6)
    IfEventsComparison(5, ARG_4_7, 6, ComparisonType.Equal, ARG_16_19, 6)
    IfConditionTrue(-2, input_condition=3)
    IfConditionTrue(-2, input_condition=4)
    IfConditionTrue(-2, input_condition=5)
    SkipLinesIfConditionTrue(3, 2)
    SkipLinesIfConditionTrue(11, -1)
    SkipLinesIfConditionTrue(6, -2)
    SkipLines(5)
    EnableFlag(11215393)
    DisplayBanner(BannerType.YouWin)
    Wait(2.0)
    DisplayBattlefieldMessage(150050, display_location_index=1)
    SkipLines(29)
    DisplayBanner(BannerType.Draw)
    Wait(2.0)
    DisplayBattlefieldMessage(150055, display_location_index=1)
    SkipLines(18)
    ClearEventValue(7000, bit_count=10)
    ClearEventValue(7050, bit_count=10)
    ClearEventValue(7100, bit_count=10)
    ClearEventValue(7150, bit_count=10)
    ClearEventValue(7200, bit_count=10)
    ClearEventValue(7250, bit_count=10)
    ClearEventValue(7300, bit_count=10)
    ClearEventValue(7350, bit_count=10)
    ClearEventValue(7400, bit_count=10)
    ClearEventValue(7450, bit_count=10)
    ClearEventValue(7500, bit_count=10)
    ClearEventValue(7550, bit_count=10)
    ClearEventValue(7600, bit_count=10)
    ClearEventValue(7650, bit_count=10)
    ClearEventValue(7700, bit_count=10)
    DisplayBanner(BannerType.YouLose)
    Wait(2.0)
    DisplayBattlefieldMessage(150060, display_location_index=1)
    SkipLinesIfFlagOff(2, 11215392)
    ArenaRankingRequest2v2()
    SkipLines(4)
    SkipLinesIfFlagOff(2, 11215395)
    ArenaRankingRequestFFA()
    SkipLines(1)
    ArenaRankingRequest1v1()
    Wait(8.0)
    DisableInvincibility(PLAYER)
    CancelSpecialEffect(PLAYER, 90000)
    ArenaExitRequest()


@NeverRestart
def Event11210705():
    """ 11210705: Event 11210705 """
    DisableNetworkSync()
    IfFlagOff(1, 11215392)
    IfFlagOff(1, 11215395)
    IfFlagOn(1, 11215393)
    IfConditionTrue(0, input_condition=1)
    SkipLinesIfFlagOff(2, 11215380)
    IncrementEventValue(7000, bit_count=10, max_value=1000)
    IfEventsComparison(2, 7000, 10, ComparisonType.GreaterThan, 6000, 10)
    SkipLinesIfFlagOff(2, 11215381)
    IncrementEventValue(7050, bit_count=10, max_value=1000)
    IfEventsComparison(2, 7050, 10, ComparisonType.GreaterThan, 6050, 10)
    SkipLinesIfFlagOff(2, 11215382)
    IncrementEventValue(7100, bit_count=10, max_value=1000)
    IfEventsComparison(2, 7100, 10, ComparisonType.GreaterThan, 6100, 10)
    SkipLinesIfFlagOff(2, 11215383)
    IncrementEventValue(7150, bit_count=10, max_value=1000)
    IfEventsComparison(2, 7150, 10, ComparisonType.GreaterThan, 6150, 10)
    IncrementEventValue(7200, bit_count=10, max_value=1000)
    SkipLinesIfConditionTrue(3, 2)
    ArenaRankingRequest1v1()
    DisableFlag(11215393)
    Restart()
    SkipLinesIfFlagOff(1, 11215380)
    IncrementEventValue(6000, bit_count=10, max_value=1000)
    SkipLinesIfFlagOff(1, 11215381)
    IncrementEventValue(6050, bit_count=10, max_value=1000)
    SkipLinesIfFlagOff(1, 11215382)
    IncrementEventValue(6100, bit_count=10, max_value=1000)
    SkipLinesIfFlagOff(1, 11215383)
    IncrementEventValue(6150, bit_count=10, max_value=1000)
    IfEventsComparison(3, 7200, 10, ComparisonType.GreaterThan, 6200, 10)
    SkipLinesIfConditionFalse(1, 3)
    IncrementEventValue(6200, bit_count=10, max_value=1000)
    ArenaRankingRequest1v1()
    DisableFlag(11215393)
    Restart()


@NeverRestart
def Event11210706():
    """ 11210706: Event 11210706 """
    DisableNetworkSync()
    IfFlagOn(1, 11215392)
    IfFlagOff(1, 11215395)
    IfFlagOn(1, 11215393)
    IfConditionTrue(0, input_condition=1)
    SkipLinesIfFlagOff(2, 11215380)
    IncrementEventValue(7250, bit_count=10, max_value=1000)
    IfEventsComparison(2, 7250, 10, ComparisonType.GreaterThan, 6250, 10)
    SkipLinesIfFlagOff(2, 11215381)
    IncrementEventValue(7300, bit_count=10, max_value=1000)
    IfEventsComparison(2, 7300, 10, ComparisonType.GreaterThan, 6300, 10)
    SkipLinesIfFlagOff(2, 11215382)
    IncrementEventValue(7350, bit_count=10, max_value=1000)
    IfEventsComparison(2, 7350, 10, ComparisonType.GreaterThan, 6350, 10)
    SkipLinesIfFlagOff(2, 11215383)
    IncrementEventValue(7400, bit_count=10, max_value=1000)
    IfEventsComparison(2, 7400, 10, ComparisonType.GreaterThan, 6400, 10)
    IncrementEventValue(7450, bit_count=10, max_value=1000)
    SkipLinesIfConditionTrue(3, 2)
    ArenaRankingRequest2v2()
    DisableFlag(11215393)
    Restart()
    SkipLinesIfFlagOff(1, 11215380)
    IncrementEventValue(6250, bit_count=10, max_value=1000)
    SkipLinesIfFlagOff(1, 11215381)
    IncrementEventValue(6300, bit_count=10, max_value=1000)
    SkipLinesIfFlagOff(1, 11215382)
    IncrementEventValue(6350, bit_count=10, max_value=1000)
    SkipLinesIfFlagOff(1, 11215383)
    IncrementEventValue(6400, bit_count=10, max_value=1000)
    IfEventsComparison(3, 7450, 10, ComparisonType.GreaterThan, 6450, 10)
    SkipLinesIfConditionFalse(1, 3)
    IncrementEventValue(6450, bit_count=10, max_value=1000)
    ArenaRankingRequest2v2()
    DisableFlag(11215393)
    Restart()


@NeverRestart
def Event11210707():
    """ 11210707: Event 11210707 """
    DisableNetworkSync()
    IfFlagOff(1, 11215392)
    IfFlagOn(1, 11215395)
    IfFlagOn(1, 11215393)
    IfConditionTrue(0, input_condition=1)
    SkipLinesIfFlagOff(2, 11215380)
    IncrementEventValue(7500, bit_count=10, max_value=1000)
    IfEventsComparison(2, 7500, 10, ComparisonType.GreaterThan, 6500, 10)
    SkipLinesIfFlagOff(2, 11215381)
    IncrementEventValue(7550, bit_count=10, max_value=1000)
    IfEventsComparison(2, 7550, 10, ComparisonType.GreaterThan, 6550, 10)
    SkipLinesIfFlagOff(2, 11215382)
    IncrementEventValue(7600, bit_count=10, max_value=1000)
    IfEventsComparison(2, 7600, 10, ComparisonType.GreaterThan, 6600, 10)
    SkipLinesIfFlagOff(2, 11215383)
    IncrementEventValue(7650, bit_count=10, max_value=1000)
    IfEventsComparison(2, 7650, 10, ComparisonType.GreaterThan, 6650, 10)
    IncrementEventValue(7700, bit_count=10, max_value=1000)
    SkipLinesIfConditionTrue(3, 2)
    ArenaRankingRequestFFA()
    DisableFlag(11215393)
    Restart()
    SkipLinesIfFlagOff(1, 11215380)
    IncrementEventValue(6500, bit_count=10, max_value=1000)
    SkipLinesIfFlagOff(1, 11215381)
    IncrementEventValue(6550, bit_count=10, max_value=1000)
    SkipLinesIfFlagOff(1, 11215382)
    IncrementEventValue(6600, bit_count=10, max_value=1000)
    SkipLinesIfFlagOff(1, 11215383)
    IncrementEventValue(6650, bit_count=10, max_value=1000)
    IfEventsComparison(3, 7700, 10, ComparisonType.GreaterThan, 6700, 10)
    SkipLinesIfConditionFalse(1, 3)
    IncrementEventValue(6700, bit_count=10, max_value=1000)
    ArenaRankingRequestFFA()
    DisableFlag(11215393)
    Restart()


@NeverRestart
def Event11210838():
    """ 11210838: Event 11210838 """
    DisableNetworkSync()
    IfCharacterInsideRegion(-1, PLAYER, region=1212700)
    IfCharacterInsideRegion(-1, PLAYER, region=1212701)
    IfCharacterInsideRegion(-1, PLAYER, region=1212702)
    IfCharacterInsideRegion(-1, PLAYER, region=1212713)
    IfCharacterInsideRegion(-1, PLAYER, region=1212714)
    IfCharacterInsideRegion(-1, PLAYER, region=1212715)
    IfConditionTrue(0, input_condition=-1)
    EqualRecovery()


@NeverRestart
def Event11210839():
    """ 11210839: Event 11210839 """
    DisableNetworkSync()
    DisableFlagRange((8140, 8145))
    IfMultiplayer(1)
    IfCharacterInsideRegion(1, PLAYER, region=1212700)
    IfMultiplayer(2)
    IfCharacterInsideRegion(2, PLAYER, region=1212701)
    IfMultiplayer(3)
    IfCharacterInsideRegion(3, PLAYER, region=1212702)
    IfMultiplayer(4)
    IfCharacterInsideRegion(4, PLAYER, region=1212713)
    IfMultiplayer(5)
    IfCharacterInsideRegion(5, PLAYER, region=1212714)
    IfMultiplayer(6)
    IfCharacterInsideRegion(6, PLAYER, region=1212715)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(-1, input_condition=4)
    IfConditionTrue(-1, input_condition=5)
    IfConditionTrue(-1, input_condition=6)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionFalse(1, 1)
    EnableFlag(8145)
    SkipLinesIfFinishedConditionFalse(1, 2)
    EnableFlag(8143)
    SkipLinesIfFinishedConditionFalse(1, 3)
    EnableFlag(8141)
    SkipLinesIfFinishedConditionFalse(1, 4)
    EnableFlag(8144)
    SkipLinesIfFinishedConditionFalse(1, 5)
    EnableFlag(8142)
    SkipLinesIfFinishedConditionFalse(1, 6)
    EnableFlag(8140)


@NeverRestart
def Event11210877():
    """ 11210877: Event 11210877 """
    DisableNetworkSync()
    IfFlagOn(7, 11215390)
    IfFlagRangeAllOff(7, (11215380, 11215383))
    IfConditionTrue(0, input_condition=7)
    IfPlayerSoulLevelLessThanOrEqual(1, 50)
    SkipLinesIfConditionFalse(2, 1)
    EnableFlag(11215380)
    Restart()
    IfPlayerSoulLevelComparison(2, ComparisonType.GreaterThan, 50)
    IfPlayerSoulLevelLessThanOrEqual(2, 100)
    SkipLinesIfConditionFalse(2, 2)
    EnableFlag(11215381)
    Restart()
    IfPlayerSoulLevelComparison(3, ComparisonType.GreaterThan, 100)
    IfPlayerSoulLevelLessThanOrEqual(3, 200)
    SkipLinesIfConditionFalse(2, 3)
    EnableFlag(11215382)
    Restart()
    EnableFlag(11215383)
    Restart()


@NeverRestart
def Event11210880(ARG_0_3: int, ARG_4_7: int):
    """ 11210880: Event 11210880 """
    DisableNetworkSync()
    EndIfClient()
    IfHost(1)
    IfMultiplayer(1)
    IfFlagOff(1, 11215341)
    IfFlagOff(1, 11215390)
    IfCharacterInsideRegion(1, PLAYER, region=ARG_0_3)
    IfCharacterOutsideRegion(1, PLAYER, region=ARG_4_7)
    IfConditionTrue(0, input_condition=1)
    PlayCutscene(120130, skippable=False, fade_out=False, move_to_region=ARG_4_7, move_to_map=OOLACILE)
    WaitFrames(1)
    Restart()


@NeverRestart
def Event11210890(ARG_0_3: int, ARG_4_7: int):
    """ 11210890: Event 11210890 """
    DisableNetworkSync()
    IfFlagOn(1, 11215390)
    IfSingleplayer(1)
    IfCharacterInsideRegion(1, PLAYER, region=ARG_0_3)
    IfConditionTrue(0, input_condition=1)
    Wait(3.0)
    WarpToMap(game_map=OOLACILE, destination_player_id=ARG_4_7)
    Wait(3.0)
    Restart()


@NeverRestart
def Event11210701(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int, ARG_12_15: int, ARG_16_19: int):
    """ 11210701: Event 11210701 """
    IfFlagOff(-1, 11215396)
    IfFlagOn(-1, 11215397)
    IfConditionTrue(1, input_condition=-1)
    IfFlagOn(1, 11215390)
    IfFlagOn(1, ARG_0_3)
    IfFlagOff(2, 11215395)
    IfEventsComparison(2, ARG_4_7, 6, ComparisonType.LessThan, ARG_8_11, 6)
    IfFlagOn(3, 11215395)
    IfEventsComparison(3, ARG_4_7, 6, ComparisonType.LessThan, ARG_8_11, 6)
    IfEventsComparison(3, ARG_4_7, 6, ComparisonType.LessThan, ARG_12_15, 6)
    IfEventsComparison(3, ARG_4_7, 6, ComparisonType.LessThan, ARG_16_19, 6)
    IfConditionTrue(-2, input_condition=2)
    IfConditionTrue(-2, input_condition=3)
    IfConditionTrue(1, input_condition=-2)
    IfFlagOn(4, 11215342)
    IfFlagOn(5, 11215343)
    IfFlagOn(6, 11215344)
    IfFlagOn(7, 11215345)
    IfConditionTrue(0, input_condition=1)
    SkipLinesIfFinishedConditionFalse(1, 4)
    AddSpecialEffect(PLAYER, 4615)
    SkipLinesIfFinishedConditionFalse(1, 5)
    AddSpecialEffect(PLAYER, 4616)
    SkipLinesIfFinishedConditionFalse(1, 6)
    AddSpecialEffect(PLAYER, 4617)
    SkipLinesIfFinishedConditionFalse(1, 7)
    AddSpecialEffect(PLAYER, 4618)
    SkipLinesIfFinishedConditionTrue(4, 4)
    SkipLinesIfFinishedConditionTrue(3, 5)
    SkipLinesIfFinishedConditionTrue(2, 6)
    SkipLinesIfFinishedConditionTrue(1, 7)
    AddSpecialEffect(PLAYER, 4612)
    Wait(5.0)
    Restart()


@NeverRestart
def Event11210430(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int):
    """ 11210430: Event 11210430 """
    IfFlagOff(-1, 11215396)
    IfFlagOn(-1, 11215397)
    IfConditionTrue(1, input_condition=-1)
    IfFlagOn(1, 11215390)
    IfFlagOn(1, ARG_0_3)
    IfFlagOff(2, 11215395)
    IfEventsComparison(2, ARG_4_7, 6, ComparisonType.Equal, ARG_8_11, 6)
    IfConditionTrue(1, input_condition=2)
    IfFlagOn(-3, 11215399)
    IfFlagOn(-3, 11215397)
    IfConditionTrue(1, input_condition=-3)
    IfConditionTrue(0, input_condition=1)
    AddSpecialEffect(PLAYER, 4614)
    Wait(5.0)
    Restart()


@NeverRestart
def Event11210435(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int, ARG_12_15: int, ARG_16_19: int):
    """ 11210435: Event 11210435 """
    IfFlagOn(1, 11215390)
    IfFlagOn(2, 11215390)
    IfFlagOn(3, 11215390)
    IfFlagOn(4, 11215390)
    IfFlagOn(5, 11215390)
    IfFlagOn(6, 11215390)
    IfFlagOn(7, 11215390)
    IfFlagOn(1, ARG_0_3)
    IfFlagOn(2, ARG_0_3)
    IfFlagOn(3, ARG_0_3)
    IfFlagOn(4, ARG_0_3)
    IfFlagOn(5, ARG_0_3)
    IfFlagOn(6, ARG_0_3)
    IfFlagOn(7, ARG_0_3)
    IfFlagOn(1, 11215395)
    IfFlagOn(2, 11215395)
    IfFlagOn(3, 11215395)
    IfFlagOn(4, 11215395)
    IfFlagOn(5, 11215395)
    IfFlagOn(6, 11215395)
    IfFlagOn(7, 11215395)
    IfFlagOn(-1, 11215399)
    IfFlagOn(-1, 11215397)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(2, input_condition=-1)
    IfConditionTrue(3, input_condition=-1)
    IfConditionTrue(4, input_condition=-1)
    IfConditionTrue(5, input_condition=-1)
    IfConditionTrue(6, input_condition=-1)
    IfConditionTrue(7, input_condition=-1)
    IfFlagOff(-2, 11215396)
    IfFlagOn(-2, 11215397)
    IfConditionTrue(1, input_condition=-2)
    IfConditionTrue(2, input_condition=-2)
    IfConditionTrue(3, input_condition=-2)
    IfConditionTrue(4, input_condition=-2)
    IfConditionTrue(5, input_condition=-2)
    IfConditionTrue(6, input_condition=-2)
    IfConditionTrue(7, input_condition=-2)
    IfEventsComparison(1, ARG_4_7, 6, ComparisonType.Equal, ARG_8_11, 6)
    IfEventsComparison(1, ARG_4_7, 6, ComparisonType.Equal, ARG_12_15, 6)
    IfEventsComparison(1, ARG_4_7, 6, ComparisonType.Equal, ARG_16_19, 6)
    IfEventsComparison(2, ARG_4_7, 6, ComparisonType.Equal, ARG_8_11, 6)
    IfEventsComparison(2, ARG_4_7, 6, ComparisonType.LessThan, ARG_12_15, 6)
    IfEventsComparison(2, ARG_4_7, 6, ComparisonType.LessThan, ARG_16_19, 6)
    IfEventsComparison(3, ARG_4_7, 6, ComparisonType.LessThan, ARG_8_11, 6)
    IfEventsComparison(3, ARG_4_7, 6, ComparisonType.Equal, ARG_12_15, 6)
    IfEventsComparison(3, ARG_4_7, 6, ComparisonType.LessThan, ARG_16_19, 6)
    IfEventsComparison(4, ARG_4_7, 6, ComparisonType.LessThan, ARG_8_11, 6)
    IfEventsComparison(4, ARG_4_7, 6, ComparisonType.LessThan, ARG_12_15, 6)
    IfEventsComparison(4, ARG_4_7, 6, ComparisonType.Equal, ARG_16_19, 6)
    IfEventsComparison(5, ARG_4_7, 6, ComparisonType.Equal, ARG_8_11, 6)
    IfEventsComparison(5, ARG_4_7, 6, ComparisonType.Equal, ARG_12_15, 6)
    IfEventsComparison(5, ARG_4_7, 6, ComparisonType.LessThan, ARG_16_19, 6)
    IfEventsComparison(6, ARG_4_7, 6, ComparisonType.LessThan, ARG_8_11, 6)
    IfEventsComparison(6, ARG_4_7, 6, ComparisonType.Equal, ARG_12_15, 6)
    IfEventsComparison(6, ARG_4_7, 6, ComparisonType.Equal, ARG_16_19, 6)
    IfEventsComparison(7, ARG_4_7, 6, ComparisonType.Equal, ARG_8_11, 6)
    IfEventsComparison(7, ARG_4_7, 6, ComparisonType.LessThan, ARG_12_15, 6)
    IfEventsComparison(7, ARG_4_7, 6, ComparisonType.Equal, ARG_16_19, 6)
    IfConditionTrue(-7, input_condition=1)
    IfConditionTrue(-7, input_condition=2)
    IfConditionTrue(-7, input_condition=3)
    IfConditionTrue(-7, input_condition=4)
    IfConditionTrue(-7, input_condition=4)
    IfConditionTrue(-7, input_condition=5)
    IfConditionTrue(-7, input_condition=6)
    IfConditionTrue(-7, input_condition=7)
    IfConditionTrue(0, input_condition=-7)
    AddSpecialEffect(PLAYER, 4614)
    Wait(5.0)
    Restart()


@NeverRestart
def Event11210434():
    """ 11210434: Event 11210434 """
    EnableFlag(11215399)
    End()
    IfFlagOn(1, 11215390)
    IfFlagOff(1, 11215392)
    IfFlagOff(1, 11215395)
    IfFlagRangeAnyOn(-2, (11215300, 11215305))
    IfFlagRangeAnyOn(-2, (11215312, 11215317))
    IfConditionTrue(1, input_condition=-2)
    IfFlagOn(2, 11215390)
    IfFlagOn(-1, 11215392)
    IfFlagOn(-1, 11215395)
    IfConditionTrue(2, input_condition=-1)
    IfFlagRangeAnyOn(-3, (11215300, 11215305))
    IfFlagRangeAnyOn(-3, (11215306, 11215311))
    IfFlagRangeAnyOn(-3, (11215312, 11215317))
    IfFlagRangeAnyOn(-3, (11215318, 11215323))
    IfConditionTrue(2, input_condition=-3)
    IfConditionTrue(-7, input_condition=1)
    IfConditionTrue(-7, input_condition=2)
    IfConditionTrue(0, input_condition=-7)
    EnableFlag(11215399)


@NeverRestart
def Event11210845():
    """ 11210845: Event 11210845 """
    IfFlagOn(1, 11215350)
    IfFlagOn(1, 11215390)
    IfConditionTrue(0, input_condition=1)
    ArenaSetNametag1(10000)


@NeverRestart
def Event11210846():
    """ 11210846: Event 11210846 """
    IfFlagOn(1, 11215351)
    IfFlagOn(1, 11215390)
    IfConditionTrue(0, input_condition=1)
    ArenaSetNametag2(10000)


@NeverRestart
def Event11210847():
    """ 11210847: Event 11210847 """
    IfFlagOn(1, 11215352)
    IfFlagOn(1, 11215390)
    IfConditionTrue(0, input_condition=1)
    ArenaSetNametag3(10000)


@NeverRestart
def Event11210848():
    """ 11210848: Event 11210848 """
    IfFlagOn(1, 11215353)
    IfFlagOn(1, 11215390)
    IfConditionTrue(0, input_condition=1)
    ArenaSetNametag4(10000)


@NeverRestart
def Event11210849():
    """ 11210849: Event 11210849 """
    DisableNetworkSync()
    IfCharacterHasSpecialEffect(0, PLAYER, 17)
    EnableFlag(8146)
    SkipLinesIfClient(2)
    DisplayArenaDissolutionMessage(150030)
    SkipLines(1)
    DisplayArenaDissolutionMessage(150031)
    Wait(1.0)
    SkipLinesIfFlagOn(4, 11215390)
    ArenaExitRequest()
    Wait(3.0)
    WarpToMap(game_map=OOLACILE, destination_player_id=1218146)
    Restart()
    ArenaExitRequest()
    Wait(3.0)
    Restart()


@NeverRestart
def Event11210837():
    """ 11210837: Event 11210837 """
    IfHost(1)
    IfMultiplayer(1)
    IfFlagOn(1, 8146)
    IfClient(2)
    IfMultiplayer(2)
    IfFlagOn(2, 8146)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFlagOff(1, 8146)
    IfFlagOff(0, 8146)
    SkipLinesIfFinishedConditionTrue(2, 2)
    DisplayArenaDissolutionMessage(150040)
    Restart()
    DisplayArenaDissolutionMessage(20000437)
    Restart()


@NeverRestart
def Event11210401():
    """ 11210401: Event 11210401 """
    DisableNetworkSync()
    IfMultiplayer(1)
    IfTrueFlagCountGreaterThanOrEqual(1, 2, (11215360, 11215363))
    IfCharacterHasSpecialEffect(1, PLAYER, 4613)
    IfFlagOff(1, 11215340)
    IfConditionTrue(0, input_condition=1)
    Wait(15.0)
    RestartIfFlagOn(11215340)
    RestartIfSingleplayer()
    DisplayBattlefieldMessage(150001, display_location_index=1)
    Restart()


@NeverRestart
def Event11210402():
    """ 11210402: Event 11210402 """
    DisableNetworkSync()
    IfCharacterInsideRegion(-1, PLAYER, region=1212700)
    IfCharacterInsideRegion(-1, PLAYER, region=1212701)
    IfCharacterInsideRegion(-1, PLAYER, region=1212702)
    IfCharacterInsideRegion(-1, PLAYER, region=1212713)
    IfCharacterInsideRegion(-1, PLAYER, region=1212714)
    IfCharacterInsideRegion(-1, PLAYER, region=1212715)
    IfConditionTrue(1, input_condition=-1)
    IfCharacterHasSpecialEffect(-2, PLAYER, 2320)
    IfCharacterHasSpecialEffect(-2, PLAYER, 2330)
    IfConditionTrue(1, input_condition=-2)
    IfConditionTrue(0, input_condition=1)
    CancelSpecialEffect(PLAYER, 2320)
    CancelSpecialEffect(PLAYER, 2330)
    Restart()


@NeverRestart
def Event11210403():
    """ 11210403: Event 11210403 """
    DisableNetworkSync()
    IfSingleplayer(1)
    IfFlagOn(1, 765)
    IfCharacterInsideRegion(-1, PLAYER, region=1212703)
    IfCharacterInsideRegion(-1, PLAYER, region=1212704)
    IfCharacterInsideRegion(-1, PLAYER, region=1212705)
    IfCharacterInsideRegion(-1, PLAYER, region=1212706)
    IfCharacterInsideRegion(-1, PLAYER, region=1212707)
    IfCharacterInsideRegion(-1, PLAYER, region=1212708)
    IfCharacterInsideRegion(-1, PLAYER, region=1212709)
    IfCharacterInsideRegion(-1, PLAYER, region=1212710)
    IfCharacterInsideRegion(-1, PLAYER, region=1212711)
    IfCharacterInsideRegion(-1, PLAYER, region=1212712)
    IfCharacterInsideRegion(-1, PLAYER, region=1212716)
    IfCharacterInsideRegion(-1, PLAYER, region=1212717)
    IfCharacterInsideRegion(-1, PLAYER, region=1212718)
    IfCharacterInsideRegion(-1, PLAYER, region=1212719)
    IfCharacterInsideRegion(-1, PLAYER, region=1212720)
    IfCharacterInsideRegion(-1, PLAYER, region=1212721)
    IfCharacterInsideRegion(-1, PLAYER, region=1212722)
    IfCharacterInsideRegion(-1, PLAYER, region=1212723)
    IfCharacterInsideRegion(-1, PLAYER, region=1212724)
    IfCharacterInsideRegion(-1, PLAYER, region=1212725)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    DisplayDialog(150400, anchor_entity=-1, display_distance=5.0, button_type=ButtonType.OK_or_Cancel, number_buttons=NumberButtons.OneButton)
    Wait(10.0)
    Restart()


@NeverRestart
def Event11210404(ARG_0_3: int):
    """ 11210404: Event 11210404 """
    DisableNetworkSync()
    IfFlagOn(0, 11215340)
    IfEventValueComparison(1, ARG_0_3, bit_count=10, comparison_type=ComparisonType.LessThan, value=10)
    IfEventValueComparison(2, ARG_0_3, bit_count=10, comparison_type=ComparisonType.GreaterThanOrEqual, value=10)
    IfEventValueComparison(2, ARG_0_3, bit_count=10, comparison_type=ComparisonType.LessThan, value=30)
    IfEventValueComparison(3, ARG_0_3, bit_count=10, comparison_type=ComparisonType.GreaterThanOrEqual, value=30)
    IfEventValueComparison(3, ARG_0_3, bit_count=10, comparison_type=ComparisonType.LessThan, value=50)
    IfEventValueComparison(4, ARG_0_3, bit_count=10, comparison_type=ComparisonType.GreaterThanOrEqual, value=50)
    IfEventValueComparison(4, ARG_0_3, bit_count=10, comparison_type=ComparisonType.LessThan, value=100)
    IfEventValueComparison(5, ARG_0_3, bit_count=10, comparison_type=ComparisonType.GreaterThanOrEqual, value=100)
    SkipLinesIfConditionFalse(1, 2)
    EnableFlag(11215342)
    SkipLinesIfConditionFalse(1, 3)
    EnableFlag(11215343)
    SkipLinesIfConditionFalse(1, 4)
    EnableFlag(11215344)
    SkipLinesIfConditionFalse(1, 5)
    EnableFlag(11215345)


@NeverRestart
def Event11210407():
    """ 11210407: Event 11210407 """
    DisableNetworkSync()
    SkipLinesIfFlagOff(2, 11210709)
    DisableFlag(11210709)
    End()
    EndIfMultiplayer()
    IfCharacterInsideRegion(-1, PLAYER, region=1212700)
    IfCharacterInsideRegion(-1, PLAYER, region=1212713)
    IfCharacterInsideRegion(-1, PLAYER, region=1212701)
    IfCharacterInsideRegion(-1, PLAYER, region=1212714)
    IfCharacterInsideRegion(-1, PLAYER, region=1212702)
    IfCharacterInsideRegion(-1, PLAYER, region=1212715)
    EndIfConditionFalse(-1)
    Wait(2.0)
    RunEvent(11216300)
    RunEvent(11216301)
    RunEvent(11216200, slot=0, args=(1, 60000001), arg_types='Ii')
    RunEvent(11216200, slot=1, args=(2, 60000002), arg_types='Ii')
    RunEvent(11216200, slot=2, args=(3, 60000003), arg_types='Ii')
    RunEvent(11216200, slot=3, args=(4, 60000004), arg_types='Ii')
    RunEvent(11216200, slot=4, args=(5, 60000005), arg_types='Ii')
    RunEvent(11216200, slot=5, args=(6, 60000006), arg_types='Ii')
    RunEvent(11216200, slot=6, args=(7, 60000007), arg_types='Ii')
    RunEvent(11216200, slot=7, args=(8, 60000008), arg_types='Ii')
    RunEvent(11216200, slot=8, args=(9, 60000009), arg_types='Ii')
    RunEvent(11216200, slot=9, args=(10, 60000010), arg_types='Ii')
    RunEvent(11216200, slot=10, args=(11, 60000011), arg_types='Ii')
    RunEvent(11216200, slot=11, args=(12, 60000012), arg_types='Ii')
    RunEvent(11216200, slot=12, args=(13, 60000013), arg_types='Ii')
    RunEvent(11216200, slot=13, args=(14, 60000014), arg_types='Ii')
    RunEvent(11216200, slot=14, args=(15, 60000015), arg_types='Ii')
    RunEvent(11216200, slot=15, args=(16, 60000016), arg_types='Ii')
    RunEvent(11216200, slot=16, args=(17, 60000017), arg_types='Ii')
    RunEvent(11216200, slot=17, args=(18, 60000018), arg_types='Ii')
    RunEvent(11216200, slot=18, args=(19, 60000019), arg_types='Ii')
    RunEvent(11216200, slot=19, args=(20, 60000020), arg_types='Ii')
    RunEvent(11216200, slot=20, args=(21, 60000021), arg_types='Ii')
    RunEvent(11216200, slot=21, args=(22, 60000022), arg_types='Ii')
    RunEvent(11216200, slot=22, args=(23, 60000023), arg_types='Ii')
    RunEvent(11216200, slot=23, args=(24, 60000024), arg_types='Ii')
    RunEvent(11216200, slot=24, args=(25, 60000025), arg_types='Ii')
    RunEvent(11216200, slot=25, args=(26, 60000026), arg_types='Ii')
    RunEvent(11216200, slot=26, args=(27, 60000027), arg_types='Ii')
    RunEvent(11216200, slot=27, args=(28, 60000028), arg_types='Ii')
    RunEvent(11216200, slot=28, args=(29, 60000029), arg_types='Ii')
    RunEvent(11216200, slot=29, args=(30, 60000030), arg_types='Ii')
    RunEvent(11216200, slot=30, args=(31, 60000031), arg_types='Ii')
    RunEvent(11216200, slot=31, args=(32, 60000032), arg_types='Ii')
    RunEvent(11216200, slot=32, args=(33, 60000033), arg_types='Ii')
    RunEvent(11216200, slot=33, args=(34, 60000034), arg_types='Ii')
    RunEvent(11216200, slot=34, args=(35, 60000035), arg_types='Ii')
    RunEvent(11216200, slot=35, args=(36, 60000036), arg_types='Ii')
    RunEvent(11216200, slot=36, args=(37, 60000037), arg_types='Ii')
    RunEvent(11216200, slot=37, args=(38, 60000038), arg_types='Ii')
    RunEvent(11216200, slot=38, args=(39, 60000039), arg_types='Ii')
    RunEvent(11216200, slot=39, args=(40, 60000040), arg_types='Ii')
    RunEvent(11216200, slot=40, args=(41, 60000041), arg_types='Ii')
    RunEvent(11216200, slot=41, args=(42, 60000042), arg_types='Ii')
    RunEvent(11216200, slot=42, args=(43, 60000043), arg_types='Ii')
    RunEvent(11216200, slot=43, args=(44, 60000044), arg_types='Ii')
    RunEvent(11216200, slot=44, args=(45, 60000045), arg_types='Ii')
    RunEvent(11216200, slot=45, args=(46, 60000046), arg_types='Ii')
    RunEvent(11216200, slot=46, args=(47, 60000047), arg_types='Ii')
    RunEvent(11216200, slot=47, args=(48, 60000048), arg_types='Ii')
    RunEvent(11216200, slot=48, args=(49, 60000049), arg_types='Ii')
    RunEvent(11216200, slot=49, args=(50, 60000050), arg_types='Ii')
    RunEvent(11216200, slot=50, args=(51, 60000051), arg_types='Ii')
    RunEvent(11216200, slot=51, args=(52, 60000052), arg_types='Ii')
    RunEvent(11216200, slot=52, args=(53, 60000053), arg_types='Ii')
    RunEvent(11216200, slot=53, args=(54, 60000054), arg_types='Ii')
    RunEvent(11216200, slot=54, args=(55, 60000055), arg_types='Ii')
    RunEvent(11216200, slot=55, args=(56, 60000056), arg_types='Ii')
    RunEvent(11216200, slot=56, args=(57, 60000057), arg_types='Ii')
    RunEvent(11216200, slot=57, args=(58, 60000058), arg_types='Ii')
    RunEvent(11216200, slot=58, args=(59, 60000059), arg_types='Ii')
    RunEvent(11216200, slot=59, args=(60, 60000060), arg_types='Ii')
    RunEvent(11216200, slot=60, args=(61, 60000061), arg_types='Ii')
    RunEvent(11216200, slot=61, args=(62, 60000062), arg_types='Ii')
    RunEvent(11216200, slot=62, args=(63, 60000063), arg_types='Ii')
    RunEvent(11216200, slot=63, args=(64, 60000064), arg_types='Ii')
    RunEvent(11216200, slot=64, args=(65, 60000065), arg_types='Ii')
    RunEvent(11216200, slot=65, args=(66, 60000066), arg_types='Ii')
    RunEvent(11216200, slot=66, args=(67, 60000067), arg_types='Ii')
    RunEvent(11216200, slot=67, args=(68, 60000068), arg_types='Ii')
    RunEvent(11216200, slot=68, args=(69, 60000069), arg_types='Ii')
    RunEvent(11216200, slot=69, args=(70, 60000070), arg_types='Ii')
    RunEvent(11216200, slot=70, args=(71, 60000071), arg_types='Ii')
    RunEvent(11216200, slot=71, args=(72, 60000072), arg_types='Ii')
    RunEvent(11216200, slot=72, args=(73, 60000073), arg_types='Ii')
    RunEvent(11216200, slot=73, args=(74, 60000074), arg_types='Ii')
    RunEvent(11216200, slot=74, args=(75, 60000075), arg_types='Ii')
    RunEvent(11216200, slot=75, args=(76, 60000076), arg_types='Ii')
    RunEvent(11216200, slot=76, args=(77, 60000077), arg_types='Ii')
    RunEvent(11216200, slot=77, args=(78, 60000078), arg_types='Ii')
    RunEvent(11216200, slot=78, args=(79, 60000079), arg_types='Ii')
    RunEvent(11216200, slot=79, args=(80, 60000080), arg_types='Ii')
    RunEvent(11216200, slot=80, args=(81, 60000081), arg_types='Ii')
    RunEvent(11216200, slot=81, args=(82, 60000082), arg_types='Ii')
    RunEvent(11216200, slot=82, args=(83, 60000083), arg_types='Ii')
    RunEvent(11216200, slot=83, args=(84, 60000084), arg_types='Ii')
    RunEvent(11216200, slot=84, args=(85, 60000085), arg_types='Ii')
    RunEvent(11216200, slot=85, args=(86, 60000086), arg_types='Ii')
    RunEvent(11216200, slot=86, args=(87, 60000087), arg_types='Ii')
    RunEvent(11216200, slot=87, args=(88, 60000088), arg_types='Ii')
    RunEvent(11216200, slot=88, args=(89, 60000089), arg_types='Ii')
    RunEvent(11216200, slot=89, args=(90, 60000090), arg_types='Ii')
    RunEvent(11216200, slot=90, args=(91, 60000091), arg_types='Ii')
    RunEvent(11216200, slot=91, args=(92, 60000092), arg_types='Ii')
    RunEvent(11216200, slot=92, args=(93, 60000093), arg_types='Ii')
    RunEvent(11216200, slot=93, args=(94, 60000094), arg_types='Ii')
    RunEvent(11216200, slot=94, args=(95, 60000095), arg_types='Ii')
    RunEvent(11216200, slot=95, args=(96, 60000096), arg_types='Ii')
    RunEvent(11216200, slot=96, args=(97, 60000097), arg_types='Ii')
    RunEvent(11216200, slot=97, args=(98, 60000098), arg_types='Ii')
    RunEvent(11216200, slot=98, args=(99, 60000099), arg_types='Ii')
    RunEvent(11216200, slot=99, args=(100, 60000100), arg_types='Ii')


@NeverRestart
def Event11216200(ARG_0_3: uint, ARG_4_7: int):
    """ 11216200: Event 11216200 """
    DisableNetworkSync()
    IfEventValueEqual(-1, 7200, bit_count=10, value=ARG_0_3)
    IfEventValueEqual(-1, 7450, bit_count=10, value=ARG_0_3)
    IfEventValueEqual(-1, 7700, bit_count=10, value=ARG_0_3)
    EndIfConditionFalse(-1)
    DisplayStatus(ARG_4_7, pad_enabled=True)


@NeverRestart
def Event11216300():
    """ 11216300: Event 11216300 """
    DisableNetworkSync()
    IfEventValueEqual(1, 7200, bit_count=10, value=0)
    IfEventValueEqual(1, 7450, bit_count=10, value=0)
    IfEventValueEqual(1, 7700, bit_count=10, value=0)
    EndIfConditionFalse(1)
    DisplayStatus(60000000, pad_enabled=True)


@NeverRestart
def Event11216301():
    """ 11216301: Event 11216301 """
    DisableNetworkSync()
    IfEventValueGreaterThan(-1, 7200, bit_count=10, value=100)
    IfEventValueGreaterThan(-1, 7450, bit_count=10, value=100)
    IfEventValueGreaterThan(-1, 7700, bit_count=10, value=100)
    EndIfConditionFalse(-1)
    DisplayStatus(59999999, pad_enabled=True)


@NeverRestart
def Event11210439():
    """ 11210439: Event 11210439 """
    EndIfClient()
    IfCharacterInsideRegion(-1, PLAYER, region=1212700)
    IfCharacterInsideRegion(-1, PLAYER, region=1212701)
    IfCharacterInsideRegion(-1, PLAYER, region=1212702)
    IfCharacterInsideRegion(-1, PLAYER, region=1212713)
    IfCharacterInsideRegion(-1, PLAYER, region=1212714)
    IfCharacterInsideRegion(-1, PLAYER, region=1212715)
    EndIfConditionFalse(-1)
    SetTeamType(PLAYER, TeamType.Human)


@NeverRestart
def Event7999():
    """ 7999: Event 7999 """
    DisableNetworkSync()
    IfFlagOn(1, 905)
    IfFlagOn(2, 906)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFlagOn(3, 906)
    DisableFlag(905)
    AddSpecialEffect(PLAYER, 4611)
    Restart()
    DisableFlag(906)
    AddSpecialEffect(PLAYER, 4612)
    Restart()


@NeverRestart
def Event7998():
    """ 7998: Event 7998 """
    IfFlagOn(1, 5100)
    IfFlagOn(2, 5101)
    IfFlagOn(3, 5102)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    DisableFlagRange((5100, 5102))
    SkipLinesIfFinishedConditionFalse(1, 1)
    IncrementEventValue(7200, bit_count=10, max_value=1000)
    SkipLinesIfFinishedConditionFalse(1, 2)
    IncrementEventValue(7450, bit_count=10, max_value=1000)
    SkipLinesIfFinishedConditionFalse(1, 3)
    IncrementEventValue(7700, bit_count=10, max_value=1000)
    Restart()