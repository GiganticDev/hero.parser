# encoding: utf-8

from marrow.schema import Attribute, Container

from gigantic.dao.base import DAO
from gigantic.dao.relationship import Relationship


log = __import__('logging').getLogger(__name__)


class Resource(DAO):
	id = Attribute('resourceid')  # puAdept4_Cooldown_Upgrade, Adept, etc etc


class UIResource(Resource):  # Abstraction, no real sections in the ini
	ui_id = Attribute('uiresource')  # Adept, AdeptGhost, etc


class Hero(UIResource):  # [HeroArchetypeName RxHeroProvider]
	__section__ = 'RxHeroProvider'
	
	name = Attribute('heroarchetypename')  # Adept_Pawn_Arch
	
	pawn_class_path = Attribute('providerpawnclasspath')  # "RxGameContent.RxPawn_Adept"
	sort_priority = Attribute('datasortpriority')  # 1700
	
	primary_trait_path = Attribute('primarytraitpath')  # tp_Duelist
	secondary_trait_path = Attribute('secondarytraitpath')  # tp_helper
	
	attack = Attribute('attackstat')  # 50
	defenese = Attribute('defensestat')  # 60
	mobility = Attribute('mobilitystat')  # 30
	utility = Attribute('utilitystat')  # 80
	difficulty = Attribute('playdifficulty')  # 5
	style = Attribute('playstyle')  # 14
	reticle_spread = Attribute('baseuireticlespreadmultiplier')  # 1.0f
	
	health_min_trigger = Attribute('lowhealthtriggerpercent')  # 40.0f
	health_recover_trigger = Attribute('lowhealthrecoveredpercent')  # 43.3f
	
	stamina_min_trigger = Attribute('lowstaminatriggerpercent')  # 25.0f
	stamina_recover_trigger = Attribute('lowstaminarecoveredpercent')  # 30.0f


class Skill(UIResource):  # [ResourceID RxSkillProvider]
	__section__ = 'RxSkillProvider'
	
	hero = Relationship('heroarchetypename', resource=Hero)
	# hero_id = Attribute('heroarchetypename')  # Adept, same as HeroArchetypeName in Archetype
	name = Attribute('skillname')  # Skill1, Skill2, Skill3, or Skill3 typically


class Upgrade(Resource):  # Abstraction, no real sections in the ini
	hero = Relationship('heroname', resource=Hero)
	tier = Attribute('upgradetier')  # ESUT_Upgrade1, ESUT_Upgrade1_SubUpgrade1, ESUT_Upgrade2, ESUT_Upgrade2_SubUpgrade1, ESUT_None, etc
	min_level = Attribute('minherolevel')  # 1 or 5?
	path_category = Attribute('upgradepathcategory')  # UPC_Offense, UPC_Defense, UPC_BurstDamage, UPC_Healing, UPC_Sustain, UPC_Mobility, UPC_AntiDebuffs


class SkillUpgrade(Upgrade):  # [ResourceID RxSkillUpgradeProvider]
	__section__ = 'RxSkillUpgradeProvider'
	
	skill_category = Attribute('skillupgradecategory')  # EUC_Skill1Upgrade where Skill1 is the 'SkillName' of the skill
	index = Attribute('skillindex')  # Not sure what it corresponds to, have seen anywhere from 11-34


class PassiveUpgrade(Upgrade):  # [ResourceID RxPassiveUpgradeProvider]
	__section__ = 'RxPassiveUpgradeProvider'
	
	category = Attribute('passiveupgradecategory')  # EUC_UnlockedDuringClash
	icon_id = Attribute('passiveiconidentifier')  # AttackFocus
	index = Attribute('passiveindex')  # 4, 5, 6?


class UpgradePath(Container): # [ResourceID RxUpgradePathProvider]
	__section__ = 'RxUpgradePathProvider'
	
	set_name = Attribute('setname')  # up_Adept_Default
	type = Attribute('upgradetype')  # UPT_Skill1_U1
	group_index = Attribute('groupindex')  # 0 - 15 in increments of 1?


class Summon(UIResource):  # [ResourceID RxSummonProvider]
	__section__ = 'RxSummonProvider'
	
	pawn_class_path = Attribute('providerpawnclasspath')  # "RxGameContent.RxPawn_AdeptAttacker"
	behavior_tree_name = Attribute('summonbehaviortreename')  # "BT_AdeptAttacker"
	creator_id = Attribute('creatorid')  # Adept (Maybe HeroArchetypeName?)