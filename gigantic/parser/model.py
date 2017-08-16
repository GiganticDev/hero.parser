# encoding: utf-8


"""
Definition of the class attributes like this as
empty strings or default values is _completely_ pointless and very
stupid considering the base resource class inherits from dict.
I'm just doing it for documentation reasons, to sort of
1:1 map the data we expect with whats in the ini files.
This will be cleaned up once I polish this utility.
"""

class Resource(dict):  # Abstraction, no real sections in the ini
    """
    Grab Any Resource reference for each Hero.
    This includes references like
    _Cooldown_Upgrade
    """
    resourceid = None  # puAdept4_Cooldown_Upgrade, Adept, etc etc

    def __repr__(self):
        return self.resourceid


class UIResource(Resource):  # Abstraction, no real sections in the ini
    """ Grab Resources used by the character (essentiall summons) """
    uiresourceid = ''  # Adept, AdeptGhost, etc


class Skill(UIResource):  # [ResourceID RxSkillProvider]
    """ Grab All Available Skills for the Hero """
    heroarchetypename = ''  # Adept, same as HeroArchetypeName in Archetype
    skillname = ''  # Skill1, Skill2, Skill3, or Skill3 typically


class Upgrade(Resource):  # Abstraction, no real sections in the ini
    """ Display Upgrades Paths, and information regarding each upgrade. """
    heroname = ''  # Adept, same as HeroArchetypeName
    upgradetier = ''  # ESUT_Upgrade1, ESUT_Upgrade1_SubUpgrade1, ESUT_Upgrade2, ESUT_Upgrade2_SubUpgrade1, ESUT_None, etc
    minherolevel = 0  # 1 or 5?
    upgradepathcategory = ''  # UPC_Offense, UPC_Defense, UPC_BurstDamage, UPC_Healing, UPC_Sustain, UPC_Mobility, UPC_AntiDebuffs


class SkillUpgrade(Upgrade):  # [ResourceID RxSkillUpgradeProvider]
    skillupgradecategory = ''  # EUC_Skill1Upgrade where Skill1 is the 'SkillName' of the skill
    skillindex = 0  # Not sure what it corresponds to, have seen anywhere from 11-34


class PassiveUpgrade(Resource):  # [ResourceID RxPassiveUpgradeProvider]
    passiveupgradecategory = ''  # EUC_UnlockedDuringClash
    passiveiconidentifier = ''  # AttackFocus
    passiveindex = 0  # 4, 5, 6?


class UpgradePath(Resource): # [ResourceID RxUpgradePathProvider]
    setname = ''  # up_Adept_Default
    upgradetype = ''  # UPT_Skill1_U1
    groupindex = 0  # 0 - 15 in increments of 1?

    def __repr__(self):
        return str(self.setname)


class SummonProvider(UIResource):  # [ResourceID RxSummonProvider]
    providerpawnclasspath = ''  # "RxGameContent.RxPawn_AdeptAttacker"
    summonbehaviortreename = ''  # "BT_AdeptAttacker"
    creatorid = ''  # Adept (Maybe HeroArchetypeName?)


class Archetype(UIResource):  # [HeroArchetypeName RxHeroProvider]
    heroarchetypename = ''  # Adept_Pawn_Arch
    providerpawnclasspath = ''  # "RxGameContent.RxPawn_Adept"
    datasortpriority = 1700  # 1700
    primarytraitpath = ''  # tp_Duelist
    secondarytraitpath = ''  # tp_helper
    attackstat = 0  # 50
    defensestat = 0  # 60
    mobilitystat = 0  # 30
    utilitystat = 0  # 80
    playdifficulty = 0  # 5
    playstyle = 0  # 14
    baseuireticlespreadmultiplier = 1.0  # 1.0f
    lowhealthtriggerpercent = 40.0  # 40.0f
    lowhealthrecoveredpercent = 43.0  # 43.3f
    lowstaminatriggerpercent = 25.0  # 25.0f
    lowstaminarecoveredpercent = 30.0  # 30.0f

    def __repr__(self):
        return self.heroarchetypename


class_section_map = {
    'RxHeroProvider': Archetype,
    # 'RxSummonProvider': SummonProvider,
    'RxSkillProvider': Skill,
    'RxSkillUpgradeProvider': SkillUpgrade,
    # 'RxPassiveUpgradeProvider': PassiveUpgrade,
    # 'RxUpgradePathProvider': UpgradePath,
}
