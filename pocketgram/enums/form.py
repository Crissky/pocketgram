from enum import Enum
from typing import TYPE_CHECKING, Union

if TYPE_CHECKING:
    from pocketgram.pocket_monster import PocketMonster


class FormEnum(Enum):
    '''Enum que representa as formas que determinados Monstrinhos
    podem assumir.
    '''

    _10_FORME = '10% Forme'
    _50_FORME = '50% Forme'
    ALOLAN = 'Alolan {pocket_monster}'
    ALTERED_FORME = 'Altered Forme'
    AMPED_FORM = 'Amped Form'
    AQUA_BREED = 'Aqua Breed'
    ARIA_FORME = 'Aria Forme'
    ASH = 'Ash-{pocket_monster}'
    ATTACK_FORME = 'Attack Forme'
    AVERAGE_SIZE = 'Average Size'
    BAILE_STYLE = 'Baile Style'
    BLACK = 'Black {pocket_monster}'
    BLADE_FORME = 'Blade Forme'
    BLAZE_BREED = 'Blaze Breed'
    BLOODMOON = 'Bloodmoon'
    BLUE_PLUMAGE = 'Blue Plumage'
    BLUE_STRIPED_FORM = 'Blue-Striped Form'
    CHEST_FORM = 'Chest Form'
    COMBAT_BREED = 'Combat Breed'
    COMPLETE_FORME = 'Complete Forme'
    CORE_FORM = 'Core Form'
    CORNERSTONE_MASK = 'Cornerstone Mask'
    CROWNED_SHIELD = 'Crowned Shield'
    CROWNED_SWORD = 'Crowned Sword'
    CURLY_FORM = 'Curly Form'
    DAWN_WINGS = 'Dawn Wings {pocket_monster}'
    DEFENSE_FORME = 'Defense Forme'
    DROOPY_FORM = 'Droopy Form'
    DUSK_FORM = 'Dusk Form'
    DUSK_MANE = 'Dusk Mane {pocket_monster}'
    ETERNAMAX = 'Eternamax'
    FAMILY_OF_FOUR = 'Family of Four'
    FAMILY_OF_THREE = 'Family of Three'
    FAN = 'Fan {pocket_monster}'
    FEMALE = 'Female'
    FROST = 'Frost {pocket_monster}'
    FULL_BELLY_MODE = 'Full Belly Mode'
    GALARIAN_STANDARD_MODE = 'Galarian Standard Mode'
    GALARIAN_ZEN_MODE = 'Galarian Zen Mode'
    GALARIAN = 'Galarian {pocket_monster}'
    GREEN_PLUMAGE = 'Green Plumage'
    HANGRY_MODE = 'Hangry Mode'
    HEARTHFLAME_MASK = 'Hearthflame Mask'
    HEAT = 'Heat {pocket_monster}'
    HERO_FORM = 'Hero Form'
    HERO_OF_MANY_BATTLES = 'Hero of Many Battles'
    HISUIAN = 'Hisuian {pocket_monster}'
    ICE_FACE = 'Ice Face'
    ICE_RIDER = 'Ice Rider'
    INCARNATE_FORME = 'Incarnate Forme'
    LAND_FORME = 'Land Forme'
    LARGE_SIZE = 'Large Size'
    LOW_KEY_FORM = 'Low Key Form'
    MALE = 'Male'
    MEGA = 'Mega {pocket_monster}'
    MEGA_X = 'Mega {pocket_monster} X'
    MEGA_Y = 'Mega {pocket_monster} Y'
    METEOR_FORM = 'Meteor Form'
    MIDDAY_FORM = 'Midday Form'
    MIDNIGHT_FORM = 'Midnight Form'
    MOW = 'Mow {pocket_monster}'
    NOICE_FACE = 'Noice Face'
    NORMAL_FORM = 'Normal Form'
    NORMAL_FORME = 'Normal Forme'
    ORDINARY_FORM = 'Ordinary Form'
    ORIGIN_FORME = 'Origin Forme'
    OWN_TEMPO = 'Own Tempo {pocket_monster}'
    PAU_STYLE = 'Pa\'u Style'
    PALDEAN = 'Paldean {pocket_monster}'
    PARTNER = 'Partner {pocket_monster}'
    PIROUETTE_FORME = 'Pirouette Forme'
    PLANT_CLOAK = 'Plant Cloak'
    POM_POM_STYLE = 'Pom-Pom Style'
    PRIMAL = 'Primal {pocket_monster}'
    RAINY_FORM = 'Rainy Form'
    RAPID_STRIKE_STYLE = 'Rapid Strike Style'
    RED_STRIPED_FORM = 'Red-Striped Form'
    RESOLUTE_FORM = 'Resolute Form'
    ROAMING_FORM = 'Roaming Form'
    SANDY_CLOAK = 'Sandy Cloak'
    SCHOOL_FORM = 'School Form'
    SENSU_STYLE = 'Sensu Style'
    SHADOW_RIDER = 'Shadow Rider'
    SHIELD_FORME = 'Shield Forme'
    SINGLE_STRIKE_STYLE = 'Single Strike Style'
    SKY_FORME = 'Sky Forme'
    SMALL_SIZE = 'Small Size'
    SNOWY_FORM = 'Snowy Form'
    SOLO_FORM = 'Solo Form'
    SPEED_FORME = 'Speed Forme'
    STANDARD_MODE = 'Standard Mode'
    STELLAR_FORM = 'Stellar Form'
    STRETCHY_FORM = 'Stretchy Form'
    SUNNY_FORM = 'Sunny Form'
    SUPER_SIZE = 'Super Size'
    TEAL_MASK = 'Teal Mask'
    TERASTAL_FORM = 'Terastal Form'
    THERIAN_FORME = 'Therian Forme'
    THREE_SEGMENT_FORM = 'Three-Segment Form'
    TRASH_CLOAK = 'Trash Cloak'
    TWO_SEGMENT_FORM = 'Two-Segment Form'
    ULTRA = 'Ultra {pocket_monster}'
    WASH = 'Wash {pocket_monster}'
    WELLSPRING_MASK = 'Wellspring Mask'
    WHITE_PLUMAGE = 'White Plumage'
    WHITE = 'White {pocket_monster}'
    WHITE_STRIPED_FORM = 'White-Striped Form'
    YELLOW_PLUMAGE = 'Yellow Plumage'
    ZEN_MODE = 'Zen Mode'
    ZERO_FORM = 'Zero Form'
    CONFINED = '{pocket_monster} Confined'
    UNBOUND = '{pocket_monster} Unbound'

    def get_formated_value(
        self,
        pocket_monster: Union['PocketMonster', str]
    ) -> str:
        if not isinstance(pocket_monster, str):
            pocket_monster = pocket_monster.name

        return self.value.format(pocket_monster=pocket_monster)
