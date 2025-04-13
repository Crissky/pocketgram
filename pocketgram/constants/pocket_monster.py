from pocketgram.enums._types import TypesEnum
from pocketgram.enums.pocket_monster import PocketMonsterParamEnum
from pocketgram.enums.stats import StatsEnum
from pocketgram.enums.form import FormEnum


POCKET_MONSTERS_DICT = {
    "0001": {
        None: {
            PocketMonsterParamEnum.NAME: "Bulbasaur",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.GRASS,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.POISON,
            StatsEnum.HP: 45,
            StatsEnum.ATTACK: 49,
            StatsEnum.DEFENSE: 49,
            StatsEnum.SPECIAL_ATTACK: 65,
            StatsEnum.SPECIAL_DEFENSE: 65,
            StatsEnum.SPEED: 45
        }
    },
    "0002": {
        None: {
            PocketMonsterParamEnum.NAME: "Ivysaur",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.GRASS,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.POISON,
            StatsEnum.HP: 60,
            StatsEnum.ATTACK: 62,
            StatsEnum.DEFENSE: 63,
            StatsEnum.SPECIAL_ATTACK: 80,
            StatsEnum.SPECIAL_DEFENSE: 80,
            StatsEnum.SPEED: 60
        }
    },
    "0003": {
        None: {
            PocketMonsterParamEnum.NAME: "Venusaur",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.GRASS,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.POISON,
            StatsEnum.HP: 80,
            StatsEnum.ATTACK: 82,
            StatsEnum.DEFENSE: 83,
            StatsEnum.SPECIAL_ATTACK: 100,
            StatsEnum.SPECIAL_DEFENSE: 100,
            StatsEnum.SPEED: 80
        },
        FormEnum.MEGA: {
            PocketMonsterParamEnum.NAME: "Venusaur",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.GRASS,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.POISON,
            StatsEnum.HP: 80,
            StatsEnum.ATTACK: 100,
            StatsEnum.DEFENSE: 123,
            StatsEnum.SPECIAL_ATTACK: 122,
            StatsEnum.SPECIAL_DEFENSE: 120,
            StatsEnum.SPEED: 80
        }
    },
    "0004": {
        None: {
            PocketMonsterParamEnum.NAME: "Charmander",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.FIRE,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 39,
            StatsEnum.ATTACK: 52,
            StatsEnum.DEFENSE: 43,
            StatsEnum.SPECIAL_ATTACK: 60,
            StatsEnum.SPECIAL_DEFENSE: 50,
            StatsEnum.SPEED: 65
        }
    },
    "0005": {
        None: {
            PocketMonsterParamEnum.NAME: "Charmeleon",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.FIRE,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 58,
            StatsEnum.ATTACK: 64,
            StatsEnum.DEFENSE: 58,
            StatsEnum.SPECIAL_ATTACK: 80,
            StatsEnum.SPECIAL_DEFENSE: 65,
            StatsEnum.SPEED: 80
        }
    },
    "0006": {
        None: {
            PocketMonsterParamEnum.NAME: "Charizard",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.FIRE,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.FLYING,
            StatsEnum.HP: 78,
            StatsEnum.ATTACK: 84,
            StatsEnum.DEFENSE: 78,
            StatsEnum.SPECIAL_ATTACK: 109,
            StatsEnum.SPECIAL_DEFENSE: 85,
            StatsEnum.SPEED: 100
        },
        FormEnum.MEGA_X: {
            PocketMonsterParamEnum.NAME: "Charizard",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.FIRE,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.DRAGON,
            StatsEnum.HP: 78,
            StatsEnum.ATTACK: 130,
            StatsEnum.DEFENSE: 111,
            StatsEnum.SPECIAL_ATTACK: 130,
            StatsEnum.SPECIAL_DEFENSE: 85,
            StatsEnum.SPEED: 100
        },
        FormEnum.MEGA_Y: {
            PocketMonsterParamEnum.NAME: "Charizard",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.FIRE,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.FLYING,
            StatsEnum.HP: 78,
            StatsEnum.ATTACK: 104,
            StatsEnum.DEFENSE: 78,
            StatsEnum.SPECIAL_ATTACK: 159,
            StatsEnum.SPECIAL_DEFENSE: 115,
            StatsEnum.SPEED: 100
        }
    },
    "0007": {
        None: {
            PocketMonsterParamEnum.NAME: "Squirtle",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.WATER,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 44,
            StatsEnum.ATTACK: 48,
            StatsEnum.DEFENSE: 65,
            StatsEnum.SPECIAL_ATTACK: 50,
            StatsEnum.SPECIAL_DEFENSE: 64,
            StatsEnum.SPEED: 43
        }
    },
    "0008": {
        None: {
            PocketMonsterParamEnum.NAME: "Wartortle",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.WATER,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 59,
            StatsEnum.ATTACK: 63,
            StatsEnum.DEFENSE: 80,
            StatsEnum.SPECIAL_ATTACK: 65,
            StatsEnum.SPECIAL_DEFENSE: 80,
            StatsEnum.SPEED: 58
        }
    },
    "0009": {
        None: {
            PocketMonsterParamEnum.NAME: "Blastoise",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.WATER,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 79,
            StatsEnum.ATTACK: 83,
            StatsEnum.DEFENSE: 100,
            StatsEnum.SPECIAL_ATTACK: 85,
            StatsEnum.SPECIAL_DEFENSE: 105,
            StatsEnum.SPEED: 78
        },
        FormEnum.MEGA: {
            PocketMonsterParamEnum.NAME: "Blastoise",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.WATER,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 79,
            StatsEnum.ATTACK: 103,
            StatsEnum.DEFENSE: 120,
            StatsEnum.SPECIAL_ATTACK: 135,
            StatsEnum.SPECIAL_DEFENSE: 115,
            StatsEnum.SPEED: 78
        }
    },
    "0010": {
        None: {
            PocketMonsterParamEnum.NAME: "Caterpie",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.BUG,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 45,
            StatsEnum.ATTACK: 30,
            StatsEnum.DEFENSE: 35,
            StatsEnum.SPECIAL_ATTACK: 20,
            StatsEnum.SPECIAL_DEFENSE: 20,
            StatsEnum.SPEED: 45
        }
    },
    "0011": {
        None: {
            PocketMonsterParamEnum.NAME: "Metapod",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.BUG,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 50,
            StatsEnum.ATTACK: 20,
            StatsEnum.DEFENSE: 55,
            StatsEnum.SPECIAL_ATTACK: 25,
            StatsEnum.SPECIAL_DEFENSE: 25,
            StatsEnum.SPEED: 30
        }
    },
    "0012": {
        None: {
            PocketMonsterParamEnum.NAME: "Butterfree",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.BUG,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.FLYING,
            StatsEnum.HP: 60,
            StatsEnum.ATTACK: 45,
            StatsEnum.DEFENSE: 50,
            StatsEnum.SPECIAL_ATTACK: 90,
            StatsEnum.SPECIAL_DEFENSE: 80,
            StatsEnum.SPEED: 70
        }
    },
    "0013": {
        None: {
            PocketMonsterParamEnum.NAME: "Weedle",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.BUG,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.POISON,
            StatsEnum.HP: 40,
            StatsEnum.ATTACK: 35,
            StatsEnum.DEFENSE: 30,
            StatsEnum.SPECIAL_ATTACK: 20,
            StatsEnum.SPECIAL_DEFENSE: 20,
            StatsEnum.SPEED: 50
        }
    },
    "0014": {
        None: {
            PocketMonsterParamEnum.NAME: "Kakuna",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.BUG,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.POISON,
            StatsEnum.HP: 45,
            StatsEnum.ATTACK: 25,
            StatsEnum.DEFENSE: 50,
            StatsEnum.SPECIAL_ATTACK: 25,
            StatsEnum.SPECIAL_DEFENSE: 25,
            StatsEnum.SPEED: 35
        }
    },
    "0015": {
        None: {
            PocketMonsterParamEnum.NAME: "Beedrill",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.BUG,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.POISON,
            StatsEnum.HP: 65,
            StatsEnum.ATTACK: 90,
            StatsEnum.DEFENSE: 40,
            StatsEnum.SPECIAL_ATTACK: 45,
            StatsEnum.SPECIAL_DEFENSE: 80,
            StatsEnum.SPEED: 75
        },
        FormEnum.MEGA: {
            PocketMonsterParamEnum.NAME: "Beedrill",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.BUG,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.POISON,
            StatsEnum.HP: 65,
            StatsEnum.ATTACK: 150,
            StatsEnum.DEFENSE: 40,
            StatsEnum.SPECIAL_ATTACK: 15,
            StatsEnum.SPECIAL_DEFENSE: 80,
            StatsEnum.SPEED: 145
        }
    },
    "0016": {
        None: {
            PocketMonsterParamEnum.NAME: "Pidgey",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.NORMAL,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.FLYING,
            StatsEnum.HP: 40,
            StatsEnum.ATTACK: 45,
            StatsEnum.DEFENSE: 40,
            StatsEnum.SPECIAL_ATTACK: 35,
            StatsEnum.SPECIAL_DEFENSE: 35,
            StatsEnum.SPEED: 56
        }
    },
    "0017": {
        None: {
            PocketMonsterParamEnum.NAME: "Pidgeotto",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.NORMAL,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.FLYING,
            StatsEnum.HP: 63,
            StatsEnum.ATTACK: 60,
            StatsEnum.DEFENSE: 55,
            StatsEnum.SPECIAL_ATTACK: 50,
            StatsEnum.SPECIAL_DEFENSE: 50,
            StatsEnum.SPEED: 71
        }
    },
    "0018": {
        None: {
            PocketMonsterParamEnum.NAME: "Pidgeot",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.NORMAL,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.FLYING,
            StatsEnum.HP: 83,
            StatsEnum.ATTACK: 80,
            StatsEnum.DEFENSE: 75,
            StatsEnum.SPECIAL_ATTACK: 70,
            StatsEnum.SPECIAL_DEFENSE: 70,
            StatsEnum.SPEED: 101
        },
        FormEnum.MEGA: {
            PocketMonsterParamEnum.NAME: "Pidgeot",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.NORMAL,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.FLYING,
            StatsEnum.HP: 83,
            StatsEnum.ATTACK: 80,
            StatsEnum.DEFENSE: 80,
            StatsEnum.SPECIAL_ATTACK: 135,
            StatsEnum.SPECIAL_DEFENSE: 80,
            StatsEnum.SPEED: 121
        }
    },
    "0019": {
        None: {
            PocketMonsterParamEnum.NAME: "Rattata",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.NORMAL,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 30,
            StatsEnum.ATTACK: 56,
            StatsEnum.DEFENSE: 35,
            StatsEnum.SPECIAL_ATTACK: 25,
            StatsEnum.SPECIAL_DEFENSE: 35,
            StatsEnum.SPEED: 72
        },
        FormEnum.ALOLAN: {
            PocketMonsterParamEnum.NAME: "Rattata",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.DARK,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.NORMAL,
            StatsEnum.HP: 30,
            StatsEnum.ATTACK: 56,
            StatsEnum.DEFENSE: 35,
            StatsEnum.SPECIAL_ATTACK: 25,
            StatsEnum.SPECIAL_DEFENSE: 35,
            StatsEnum.SPEED: 72
        }
    },
    "0020": {
        None: {
            PocketMonsterParamEnum.NAME: "Raticate",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.NORMAL,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 55,
            StatsEnum.ATTACK: 81,
            StatsEnum.DEFENSE: 60,
            StatsEnum.SPECIAL_ATTACK: 50,
            StatsEnum.SPECIAL_DEFENSE: 70,
            StatsEnum.SPEED: 97
        },
        FormEnum.ALOLAN: {
            PocketMonsterParamEnum.NAME: "Raticate",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.DARK,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.NORMAL,
            StatsEnum.HP: 75,
            StatsEnum.ATTACK: 71,
            StatsEnum.DEFENSE: 70,
            StatsEnum.SPECIAL_ATTACK: 40,
            StatsEnum.SPECIAL_DEFENSE: 80,
            StatsEnum.SPEED: 77
        }
    },
    "0021": {
        None: {
            PocketMonsterParamEnum.NAME: "Spearow",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.NORMAL,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.FLYING,
            StatsEnum.HP: 40,
            StatsEnum.ATTACK: 60,
            StatsEnum.DEFENSE: 30,
            StatsEnum.SPECIAL_ATTACK: 31,
            StatsEnum.SPECIAL_DEFENSE: 31,
            StatsEnum.SPEED: 70
        }
    },
    "0022": {
        None: {
            PocketMonsterParamEnum.NAME: "Fearow",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.NORMAL,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.FLYING,
            StatsEnum.HP: 65,
            StatsEnum.ATTACK: 90,
            StatsEnum.DEFENSE: 65,
            StatsEnum.SPECIAL_ATTACK: 61,
            StatsEnum.SPECIAL_DEFENSE: 61,
            StatsEnum.SPEED: 100
        }
    },
    "0023": {
        None: {
            PocketMonsterParamEnum.NAME: "Ekans",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.POISON,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 35,
            StatsEnum.ATTACK: 60,
            StatsEnum.DEFENSE: 44,
            StatsEnum.SPECIAL_ATTACK: 40,
            StatsEnum.SPECIAL_DEFENSE: 54,
            StatsEnum.SPEED: 55
        }
    },
    "0024": {
        None: {
            PocketMonsterParamEnum.NAME: "Arbok",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.POISON,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 60,
            StatsEnum.ATTACK: 95,
            StatsEnum.DEFENSE: 69,
            StatsEnum.SPECIAL_ATTACK: 65,
            StatsEnum.SPECIAL_DEFENSE: 79,
            StatsEnum.SPEED: 80
        }
    },
    "0025": {
        None: {
            PocketMonsterParamEnum.NAME: "Pikachu",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.ELECTRIC,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 35,
            StatsEnum.ATTACK: 55,
            StatsEnum.DEFENSE: 40,
            StatsEnum.SPECIAL_ATTACK: 50,
            StatsEnum.SPECIAL_DEFENSE: 50,
            StatsEnum.SPEED: 90
        },
        FormEnum.PARTNER: {
            PocketMonsterParamEnum.NAME: "Pikachu",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.ELECTRIC,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 45,
            StatsEnum.ATTACK: 80,
            StatsEnum.DEFENSE: 50,
            StatsEnum.SPECIAL_ATTACK: 75,
            StatsEnum.SPECIAL_DEFENSE: 60,
            StatsEnum.SPEED: 120
        }
    },
    "0026": {
        None: {
            PocketMonsterParamEnum.NAME: "Raichu",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.ELECTRIC,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 60,
            StatsEnum.ATTACK: 90,
            StatsEnum.DEFENSE: 55,
            StatsEnum.SPECIAL_ATTACK: 90,
            StatsEnum.SPECIAL_DEFENSE: 80,
            StatsEnum.SPEED: 110
        },
        FormEnum.ALOLAN: {
            PocketMonsterParamEnum.NAME: "Raichu",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.ELECTRIC,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.PSYCHIC,
            StatsEnum.HP: 60,
            StatsEnum.ATTACK: 85,
            StatsEnum.DEFENSE: 50,
            StatsEnum.SPECIAL_ATTACK: 95,
            StatsEnum.SPECIAL_DEFENSE: 85,
            StatsEnum.SPEED: 110
        }
    },
    "0027": {
        None: {
            PocketMonsterParamEnum.NAME: "Sandshrew",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.GROUND,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 50,
            StatsEnum.ATTACK: 75,
            StatsEnum.DEFENSE: 85,
            StatsEnum.SPECIAL_ATTACK: 20,
            StatsEnum.SPECIAL_DEFENSE: 30,
            StatsEnum.SPEED: 40
        },
        FormEnum.ALOLAN: {
            PocketMonsterParamEnum.NAME: "Sandshrew",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.ICE,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.STEEL,
            StatsEnum.HP: 50,
            StatsEnum.ATTACK: 75,
            StatsEnum.DEFENSE: 90,
            StatsEnum.SPECIAL_ATTACK: 10,
            StatsEnum.SPECIAL_DEFENSE: 35,
            StatsEnum.SPEED: 40
        }
    },
    "0028": {
        None: {
            PocketMonsterParamEnum.NAME: "Sandslash",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.GROUND,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 75,
            StatsEnum.ATTACK: 100,
            StatsEnum.DEFENSE: 110,
            StatsEnum.SPECIAL_ATTACK: 45,
            StatsEnum.SPECIAL_DEFENSE: 55,
            StatsEnum.SPEED: 65
        },
        FormEnum.ALOLAN: {
            PocketMonsterParamEnum.NAME: "Sandslash",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.ICE,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.STEEL,
            StatsEnum.HP: 75,
            StatsEnum.ATTACK: 100,
            StatsEnum.DEFENSE: 120,
            StatsEnum.SPECIAL_ATTACK: 25,
            StatsEnum.SPECIAL_DEFENSE: 65,
            StatsEnum.SPEED: 65
        }
    },
    "0029": {
        None: {
            PocketMonsterParamEnum.NAME: "Nidoran♀",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.POISON,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 55,
            StatsEnum.ATTACK: 47,
            StatsEnum.DEFENSE: 52,
            StatsEnum.SPECIAL_ATTACK: 40,
            StatsEnum.SPECIAL_DEFENSE: 40,
            StatsEnum.SPEED: 41
        }
    },
    "0030": {
        None: {
            PocketMonsterParamEnum.NAME: "Nidorina",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.POISON,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 70,
            StatsEnum.ATTACK: 62,
            StatsEnum.DEFENSE: 67,
            StatsEnum.SPECIAL_ATTACK: 55,
            StatsEnum.SPECIAL_DEFENSE: 55,
            StatsEnum.SPEED: 56
        }
    },
    "0031": {
        None: {
            PocketMonsterParamEnum.NAME: "Nidoqueen",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.POISON,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.GROUND,
            StatsEnum.HP: 90,
            StatsEnum.ATTACK: 92,
            StatsEnum.DEFENSE: 87,
            StatsEnum.SPECIAL_ATTACK: 75,
            StatsEnum.SPECIAL_DEFENSE: 85,
            StatsEnum.SPEED: 76
        }
    },
    "0032": {
        None: {
            PocketMonsterParamEnum.NAME: "Nidoran♂",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.POISON,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 46,
            StatsEnum.ATTACK: 57,
            StatsEnum.DEFENSE: 40,
            StatsEnum.SPECIAL_ATTACK: 40,
            StatsEnum.SPECIAL_DEFENSE: 40,
            StatsEnum.SPEED: 50
        }
    },
    "0033": {
        None: {
            PocketMonsterParamEnum.NAME: "Nidorino",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.POISON,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 61,
            StatsEnum.ATTACK: 72,
            StatsEnum.DEFENSE: 57,
            StatsEnum.SPECIAL_ATTACK: 55,
            StatsEnum.SPECIAL_DEFENSE: 55,
            StatsEnum.SPEED: 65
        }
    },
    "0034": {
        None: {
            PocketMonsterParamEnum.NAME: "Nidoking",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.POISON,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.GROUND,
            StatsEnum.HP: 81,
            StatsEnum.ATTACK: 102,
            StatsEnum.DEFENSE: 77,
            StatsEnum.SPECIAL_ATTACK: 85,
            StatsEnum.SPECIAL_DEFENSE: 75,
            StatsEnum.SPEED: 85
        }
    },
    "0035": {
        None: {
            PocketMonsterParamEnum.NAME: "Clefairy",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.FAIRY,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 70,
            StatsEnum.ATTACK: 45,
            StatsEnum.DEFENSE: 48,
            StatsEnum.SPECIAL_ATTACK: 60,
            StatsEnum.SPECIAL_DEFENSE: 65,
            StatsEnum.SPEED: 35
        }
    },
    "0036": {
        None: {
            PocketMonsterParamEnum.NAME: "Clefable",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.FAIRY,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 95,
            StatsEnum.ATTACK: 70,
            StatsEnum.DEFENSE: 73,
            StatsEnum.SPECIAL_ATTACK: 95,
            StatsEnum.SPECIAL_DEFENSE: 90,
            StatsEnum.SPEED: 60
        }
    },
    "0037": {
        None: {
            PocketMonsterParamEnum.NAME: "Vulpix",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.FIRE,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 38,
            StatsEnum.ATTACK: 41,
            StatsEnum.DEFENSE: 40,
            StatsEnum.SPECIAL_ATTACK: 50,
            StatsEnum.SPECIAL_DEFENSE: 65,
            StatsEnum.SPEED: 65
        },
        FormEnum.ALOLAN: {
            PocketMonsterParamEnum.NAME: "Vulpix",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.ICE,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 38,
            StatsEnum.ATTACK: 41,
            StatsEnum.DEFENSE: 40,
            StatsEnum.SPECIAL_ATTACK: 50,
            StatsEnum.SPECIAL_DEFENSE: 65,
            StatsEnum.SPEED: 65
        }
    },
    "0038": {
        None: {
            PocketMonsterParamEnum.NAME: "Ninetales",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.FIRE,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 73,
            StatsEnum.ATTACK: 76,
            StatsEnum.DEFENSE: 75,
            StatsEnum.SPECIAL_ATTACK: 81,
            StatsEnum.SPECIAL_DEFENSE: 100,
            StatsEnum.SPEED: 100
        },
        FormEnum.ALOLAN: {
            PocketMonsterParamEnum.NAME: "Ninetales",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.ICE,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.FAIRY,
            StatsEnum.HP: 73,
            StatsEnum.ATTACK: 67,
            StatsEnum.DEFENSE: 75,
            StatsEnum.SPECIAL_ATTACK: 81,
            StatsEnum.SPECIAL_DEFENSE: 100,
            StatsEnum.SPEED: 109
        }
    },
    "0039": {
        None: {
            PocketMonsterParamEnum.NAME: "Jigglypuff",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.NORMAL,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.FAIRY,
            StatsEnum.HP: 115,
            StatsEnum.ATTACK: 45,
            StatsEnum.DEFENSE: 20,
            StatsEnum.SPECIAL_ATTACK: 45,
            StatsEnum.SPECIAL_DEFENSE: 25,
            StatsEnum.SPEED: 20
        }
    },
    "0040": {
        None: {
            PocketMonsterParamEnum.NAME: "Wigglytuff",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.NORMAL,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.FAIRY,
            StatsEnum.HP: 140,
            StatsEnum.ATTACK: 70,
            StatsEnum.DEFENSE: 45,
            StatsEnum.SPECIAL_ATTACK: 85,
            StatsEnum.SPECIAL_DEFENSE: 50,
            StatsEnum.SPEED: 45
        }
    },
    "0041": {
        None: {
            PocketMonsterParamEnum.NAME: "Zubat",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.POISON,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.FLYING,
            StatsEnum.HP: 40,
            StatsEnum.ATTACK: 45,
            StatsEnum.DEFENSE: 35,
            StatsEnum.SPECIAL_ATTACK: 30,
            StatsEnum.SPECIAL_DEFENSE: 40,
            StatsEnum.SPEED: 55
        }
    },
    "0042": {
        None: {
            PocketMonsterParamEnum.NAME: "Golbat",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.POISON,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.FLYING,
            StatsEnum.HP: 75,
            StatsEnum.ATTACK: 80,
            StatsEnum.DEFENSE: 70,
            StatsEnum.SPECIAL_ATTACK: 65,
            StatsEnum.SPECIAL_DEFENSE: 75,
            StatsEnum.SPEED: 90
        }
    },
    "0043": {
        None: {
            PocketMonsterParamEnum.NAME: "Oddish",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.GRASS,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.POISON,
            StatsEnum.HP: 45,
            StatsEnum.ATTACK: 50,
            StatsEnum.DEFENSE: 55,
            StatsEnum.SPECIAL_ATTACK: 75,
            StatsEnum.SPECIAL_DEFENSE: 65,
            StatsEnum.SPEED: 30
        }
    },
    "0044": {
        None: {
            PocketMonsterParamEnum.NAME: "Gloom",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.GRASS,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.POISON,
            StatsEnum.HP: 60,
            StatsEnum.ATTACK: 65,
            StatsEnum.DEFENSE: 70,
            StatsEnum.SPECIAL_ATTACK: 85,
            StatsEnum.SPECIAL_DEFENSE: 75,
            StatsEnum.SPEED: 40
        }
    },
    "0045": {
        None: {
            PocketMonsterParamEnum.NAME: "Vileplume",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.GRASS,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.POISON,
            StatsEnum.HP: 75,
            StatsEnum.ATTACK: 80,
            StatsEnum.DEFENSE: 85,
            StatsEnum.SPECIAL_ATTACK: 110,
            StatsEnum.SPECIAL_DEFENSE: 90,
            StatsEnum.SPEED: 50
        }
    },
    "0046": {
        None: {
            PocketMonsterParamEnum.NAME: "Paras",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.BUG,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.GRASS,
            StatsEnum.HP: 35,
            StatsEnum.ATTACK: 70,
            StatsEnum.DEFENSE: 55,
            StatsEnum.SPECIAL_ATTACK: 45,
            StatsEnum.SPECIAL_DEFENSE: 55,
            StatsEnum.SPEED: 25
        }
    },
    "0047": {
        None: {
            PocketMonsterParamEnum.NAME: "Parasect",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.BUG,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.GRASS,
            StatsEnum.HP: 60,
            StatsEnum.ATTACK: 95,
            StatsEnum.DEFENSE: 80,
            StatsEnum.SPECIAL_ATTACK: 60,
            StatsEnum.SPECIAL_DEFENSE: 80,
            StatsEnum.SPEED: 30
        }
    },
    "0048": {
        None: {
            PocketMonsterParamEnum.NAME: "Venonat",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.BUG,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.POISON,
            StatsEnum.HP: 60,
            StatsEnum.ATTACK: 55,
            StatsEnum.DEFENSE: 50,
            StatsEnum.SPECIAL_ATTACK: 40,
            StatsEnum.SPECIAL_DEFENSE: 55,
            StatsEnum.SPEED: 45
        }
    },
    "0049": {
        None: {
            PocketMonsterParamEnum.NAME: "Venomoth",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.BUG,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.POISON,
            StatsEnum.HP: 70,
            StatsEnum.ATTACK: 65,
            StatsEnum.DEFENSE: 60,
            StatsEnum.SPECIAL_ATTACK: 90,
            StatsEnum.SPECIAL_DEFENSE: 75,
            StatsEnum.SPEED: 90
        }
    },
    "0050": {
        None: {
            PocketMonsterParamEnum.NAME: "Diglett",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.GROUND,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 10,
            StatsEnum.ATTACK: 55,
            StatsEnum.DEFENSE: 25,
            StatsEnum.SPECIAL_ATTACK: 35,
            StatsEnum.SPECIAL_DEFENSE: 45,
            StatsEnum.SPEED: 95
        },
        FormEnum.ALOLAN: {
            PocketMonsterParamEnum.NAME: "Diglett",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.GROUND,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.STEEL,
            StatsEnum.HP: 10,
            StatsEnum.ATTACK: 55,
            StatsEnum.DEFENSE: 30,
            StatsEnum.SPECIAL_ATTACK: 35,
            StatsEnum.SPECIAL_DEFENSE: 45,
            StatsEnum.SPEED: 90
        }
    },
    "0051": {
        None: {
            PocketMonsterParamEnum.NAME: "Dugtrio",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.GROUND,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 35,
            StatsEnum.ATTACK: 100,
            StatsEnum.DEFENSE: 50,
            StatsEnum.SPECIAL_ATTACK: 50,
            StatsEnum.SPECIAL_DEFENSE: 70,
            StatsEnum.SPEED: 120
        },
        FormEnum.ALOLAN: {
            PocketMonsterParamEnum.NAME: "Dugtrio",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.GROUND,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.STEEL,
            StatsEnum.HP: 35,
            StatsEnum.ATTACK: 100,
            StatsEnum.DEFENSE: 60,
            StatsEnum.SPECIAL_ATTACK: 50,
            StatsEnum.SPECIAL_DEFENSE: 70,
            StatsEnum.SPEED: 110
        }
    },
    "0052": {
        None: {
            PocketMonsterParamEnum.NAME: "Meowth",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.NORMAL,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 40,
            StatsEnum.ATTACK: 45,
            StatsEnum.DEFENSE: 35,
            StatsEnum.SPECIAL_ATTACK: 40,
            StatsEnum.SPECIAL_DEFENSE: 40,
            StatsEnum.SPEED: 90
        },
        FormEnum.ALOLAN: {
            PocketMonsterParamEnum.NAME: "Meowth",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.DARK,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 40,
            StatsEnum.ATTACK: 35,
            StatsEnum.DEFENSE: 35,
            StatsEnum.SPECIAL_ATTACK: 50,
            StatsEnum.SPECIAL_DEFENSE: 40,
            StatsEnum.SPEED: 90
        },
        FormEnum.GALARIAN: {
            PocketMonsterParamEnum.NAME: "Meowth",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.STEEL,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 50,
            StatsEnum.ATTACK: 65,
            StatsEnum.DEFENSE: 55,
            StatsEnum.SPECIAL_ATTACK: 40,
            StatsEnum.SPECIAL_DEFENSE: 40,
            StatsEnum.SPEED: 40
        }
    },
    "0053": {
        None: {
            PocketMonsterParamEnum.NAME: "Persian",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.NORMAL,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 65,
            StatsEnum.ATTACK: 70,
            StatsEnum.DEFENSE: 60,
            StatsEnum.SPECIAL_ATTACK: 65,
            StatsEnum.SPECIAL_DEFENSE: 65,
            StatsEnum.SPEED: 115
        },
        FormEnum.ALOLAN: {
            PocketMonsterParamEnum.NAME: "Persian",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.DARK,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 65,
            StatsEnum.ATTACK: 60,
            StatsEnum.DEFENSE: 60,
            StatsEnum.SPECIAL_ATTACK: 75,
            StatsEnum.SPECIAL_DEFENSE: 65,
            StatsEnum.SPEED: 115
        }
    },
    "0054": {
        None: {
            PocketMonsterParamEnum.NAME: "Psyduck",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.WATER,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 50,
            StatsEnum.ATTACK: 52,
            StatsEnum.DEFENSE: 48,
            StatsEnum.SPECIAL_ATTACK: 65,
            StatsEnum.SPECIAL_DEFENSE: 50,
            StatsEnum.SPEED: 55
        }
    },
    "0055": {
        None: {
            PocketMonsterParamEnum.NAME: "Golduck",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.WATER,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 80,
            StatsEnum.ATTACK: 82,
            StatsEnum.DEFENSE: 78,
            StatsEnum.SPECIAL_ATTACK: 95,
            StatsEnum.SPECIAL_DEFENSE: 80,
            StatsEnum.SPEED: 85
        }
    },
    "0056": {
        None: {
            PocketMonsterParamEnum.NAME: "Mankey",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.FIGHTING,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 40,
            StatsEnum.ATTACK: 80,
            StatsEnum.DEFENSE: 35,
            StatsEnum.SPECIAL_ATTACK: 35,
            StatsEnum.SPECIAL_DEFENSE: 45,
            StatsEnum.SPEED: 70
        }
    },
    "0057": {
        None: {
            PocketMonsterParamEnum.NAME: "Primeape",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.FIGHTING,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 65,
            StatsEnum.ATTACK: 105,
            StatsEnum.DEFENSE: 60,
            StatsEnum.SPECIAL_ATTACK: 60,
            StatsEnum.SPECIAL_DEFENSE: 70,
            StatsEnum.SPEED: 95
        }
    },
    "0058": {
        None: {
            PocketMonsterParamEnum.NAME: "Growlithe",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.FIRE,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 55,
            StatsEnum.ATTACK: 70,
            StatsEnum.DEFENSE: 45,
            StatsEnum.SPECIAL_ATTACK: 70,
            StatsEnum.SPECIAL_DEFENSE: 50,
            StatsEnum.SPEED: 60
        },
        FormEnum.HISUIAN: {
            PocketMonsterParamEnum.NAME: "Growlithe",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.FIRE,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.ROCK,
            StatsEnum.HP: 60,
            StatsEnum.ATTACK: 75,
            StatsEnum.DEFENSE: 45,
            StatsEnum.SPECIAL_ATTACK: 65,
            StatsEnum.SPECIAL_DEFENSE: 50,
            StatsEnum.SPEED: 55
        }
    },
    "0059": {
        None: {
            PocketMonsterParamEnum.NAME: "Arcanine",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.FIRE,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 90,
            StatsEnum.ATTACK: 110,
            StatsEnum.DEFENSE: 80,
            StatsEnum.SPECIAL_ATTACK: 100,
            StatsEnum.SPECIAL_DEFENSE: 80,
            StatsEnum.SPEED: 95
        },
        FormEnum.HISUIAN: {
            PocketMonsterParamEnum.NAME: "Arcanine",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.FIRE,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.ROCK,
            StatsEnum.HP: 95,
            StatsEnum.ATTACK: 115,
            StatsEnum.DEFENSE: 80,
            StatsEnum.SPECIAL_ATTACK: 95,
            StatsEnum.SPECIAL_DEFENSE: 80,
            StatsEnum.SPEED: 90
        }
    },
    "0060": {
        None: {
            PocketMonsterParamEnum.NAME: "Poliwag",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.WATER,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 40,
            StatsEnum.ATTACK: 50,
            StatsEnum.DEFENSE: 40,
            StatsEnum.SPECIAL_ATTACK: 40,
            StatsEnum.SPECIAL_DEFENSE: 40,
            StatsEnum.SPEED: 90
        }
    },
    "0061": {
        None: {
            PocketMonsterParamEnum.NAME: "Poliwhirl",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.WATER,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 65,
            StatsEnum.ATTACK: 65,
            StatsEnum.DEFENSE: 65,
            StatsEnum.SPECIAL_ATTACK: 50,
            StatsEnum.SPECIAL_DEFENSE: 50,
            StatsEnum.SPEED: 90
        }
    },
    "0062": {
        None: {
            PocketMonsterParamEnum.NAME: "Poliwrath",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.WATER,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.FIGHTING,
            StatsEnum.HP: 90,
            StatsEnum.ATTACK: 95,
            StatsEnum.DEFENSE: 95,
            StatsEnum.SPECIAL_ATTACK: 70,
            StatsEnum.SPECIAL_DEFENSE: 90,
            StatsEnum.SPEED: 70
        }
    },
    "0063": {
        None: {
            PocketMonsterParamEnum.NAME: "Abra",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.PSYCHIC,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 25,
            StatsEnum.ATTACK: 20,
            StatsEnum.DEFENSE: 15,
            StatsEnum.SPECIAL_ATTACK: 105,
            StatsEnum.SPECIAL_DEFENSE: 55,
            StatsEnum.SPEED: 90
        }
    },
    "0064": {
        None: {
            PocketMonsterParamEnum.NAME: "Kadabra",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.PSYCHIC,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 40,
            StatsEnum.ATTACK: 35,
            StatsEnum.DEFENSE: 30,
            StatsEnum.SPECIAL_ATTACK: 120,
            StatsEnum.SPECIAL_DEFENSE: 70,
            StatsEnum.SPEED: 105
        }
    },
    "0065": {
        None: {
            PocketMonsterParamEnum.NAME: "Alakazam",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.PSYCHIC,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 55,
            StatsEnum.ATTACK: 50,
            StatsEnum.DEFENSE: 45,
            StatsEnum.SPECIAL_ATTACK: 135,
            StatsEnum.SPECIAL_DEFENSE: 95,
            StatsEnum.SPEED: 120
        },
        FormEnum.MEGA: {
            PocketMonsterParamEnum.NAME: "Alakazam",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.PSYCHIC,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 55,
            StatsEnum.ATTACK: 50,
            StatsEnum.DEFENSE: 65,
            StatsEnum.SPECIAL_ATTACK: 175,
            StatsEnum.SPECIAL_DEFENSE: 105,
            StatsEnum.SPEED: 150
        }
    },
    "0066": {
        None: {
            PocketMonsterParamEnum.NAME: "Machop",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.FIGHTING,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 70,
            StatsEnum.ATTACK: 80,
            StatsEnum.DEFENSE: 50,
            StatsEnum.SPECIAL_ATTACK: 35,
            StatsEnum.SPECIAL_DEFENSE: 35,
            StatsEnum.SPEED: 35
        }
    },
    "0067": {
        None: {
            PocketMonsterParamEnum.NAME: "Machoke",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.FIGHTING,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 80,
            StatsEnum.ATTACK: 100,
            StatsEnum.DEFENSE: 70,
            StatsEnum.SPECIAL_ATTACK: 50,
            StatsEnum.SPECIAL_DEFENSE: 60,
            StatsEnum.SPEED: 45
        }
    },
    "0068": {
        None: {
            PocketMonsterParamEnum.NAME: "Machamp",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.FIGHTING,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 90,
            StatsEnum.ATTACK: 130,
            StatsEnum.DEFENSE: 80,
            StatsEnum.SPECIAL_ATTACK: 65,
            StatsEnum.SPECIAL_DEFENSE: 85,
            StatsEnum.SPEED: 55
        }
    },
    "0069": {
        None: {
            PocketMonsterParamEnum.NAME: "Bellsprout",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.GRASS,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.POISON,
            StatsEnum.HP: 50,
            StatsEnum.ATTACK: 75,
            StatsEnum.DEFENSE: 35,
            StatsEnum.SPECIAL_ATTACK: 70,
            StatsEnum.SPECIAL_DEFENSE: 30,
            StatsEnum.SPEED: 40
        }
    },
    "0070": {
        None: {
            PocketMonsterParamEnum.NAME: "Weepinbell",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.GRASS,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.POISON,
            StatsEnum.HP: 65,
            StatsEnum.ATTACK: 90,
            StatsEnum.DEFENSE: 50,
            StatsEnum.SPECIAL_ATTACK: 85,
            StatsEnum.SPECIAL_DEFENSE: 45,
            StatsEnum.SPEED: 55
        }
    },
    "0071": {
        None: {
            PocketMonsterParamEnum.NAME: "Victreebel",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.GRASS,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.POISON,
            StatsEnum.HP: 80,
            StatsEnum.ATTACK: 105,
            StatsEnum.DEFENSE: 65,
            StatsEnum.SPECIAL_ATTACK: 100,
            StatsEnum.SPECIAL_DEFENSE: 70,
            StatsEnum.SPEED: 70
        }
    },
    "0072": {
        None: {
            PocketMonsterParamEnum.NAME: "Tentacool",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.WATER,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.POISON,
            StatsEnum.HP: 40,
            StatsEnum.ATTACK: 40,
            StatsEnum.DEFENSE: 35,
            StatsEnum.SPECIAL_ATTACK: 50,
            StatsEnum.SPECIAL_DEFENSE: 100,
            StatsEnum.SPEED: 70
        }
    },
    "0073": {
        None: {
            PocketMonsterParamEnum.NAME: "Tentacruel",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.WATER,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.POISON,
            StatsEnum.HP: 80,
            StatsEnum.ATTACK: 70,
            StatsEnum.DEFENSE: 65,
            StatsEnum.SPECIAL_ATTACK: 80,
            StatsEnum.SPECIAL_DEFENSE: 120,
            StatsEnum.SPEED: 100
        }
    },
    "0074": {
        None: {
            PocketMonsterParamEnum.NAME: "Geodude",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.ROCK,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.GROUND,
            StatsEnum.HP: 40,
            StatsEnum.ATTACK: 80,
            StatsEnum.DEFENSE: 100,
            StatsEnum.SPECIAL_ATTACK: 30,
            StatsEnum.SPECIAL_DEFENSE: 30,
            StatsEnum.SPEED: 20
        },
        FormEnum.ALOLAN: {
            PocketMonsterParamEnum.NAME: "Geodude",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.ROCK,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.ELECTRIC,
            StatsEnum.HP: 40,
            StatsEnum.ATTACK: 80,
            StatsEnum.DEFENSE: 100,
            StatsEnum.SPECIAL_ATTACK: 30,
            StatsEnum.SPECIAL_DEFENSE: 30,
            StatsEnum.SPEED: 20
        }
    },
    "0075": {
        None: {
            PocketMonsterParamEnum.NAME: "Graveler",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.ROCK,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.GROUND,
            StatsEnum.HP: 55,
            StatsEnum.ATTACK: 95,
            StatsEnum.DEFENSE: 115,
            StatsEnum.SPECIAL_ATTACK: 45,
            StatsEnum.SPECIAL_DEFENSE: 45,
            StatsEnum.SPEED: 35
        },
        FormEnum.ALOLAN: {
            PocketMonsterParamEnum.NAME: "Graveler",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.ROCK,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.ELECTRIC,
            StatsEnum.HP: 55,
            StatsEnum.ATTACK: 95,
            StatsEnum.DEFENSE: 115,
            StatsEnum.SPECIAL_ATTACK: 45,
            StatsEnum.SPECIAL_DEFENSE: 45,
            StatsEnum.SPEED: 35
        }
    },
    "0076": {
        None: {
            PocketMonsterParamEnum.NAME: "Golem",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.ROCK,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.GROUND,
            StatsEnum.HP: 80,
            StatsEnum.ATTACK: 120,
            StatsEnum.DEFENSE: 130,
            StatsEnum.SPECIAL_ATTACK: 55,
            StatsEnum.SPECIAL_DEFENSE: 65,
            StatsEnum.SPEED: 45
        },
        FormEnum.ALOLAN: {
            PocketMonsterParamEnum.NAME: "Golem",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.ROCK,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.ELECTRIC,
            StatsEnum.HP: 80,
            StatsEnum.ATTACK: 120,
            StatsEnum.DEFENSE: 130,
            StatsEnum.SPECIAL_ATTACK: 55,
            StatsEnum.SPECIAL_DEFENSE: 65,
            StatsEnum.SPEED: 45
        }
    },
    "0077": {
        None: {
            PocketMonsterParamEnum.NAME: "Ponyta",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.FIRE,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 50,
            StatsEnum.ATTACK: 85,
            StatsEnum.DEFENSE: 55,
            StatsEnum.SPECIAL_ATTACK: 65,
            StatsEnum.SPECIAL_DEFENSE: 65,
            StatsEnum.SPEED: 90
        },
        FormEnum.GALARIAN: {
            PocketMonsterParamEnum.NAME: "Ponyta",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.PSYCHIC,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 50,
            StatsEnum.ATTACK: 85,
            StatsEnum.DEFENSE: 55,
            StatsEnum.SPECIAL_ATTACK: 65,
            StatsEnum.SPECIAL_DEFENSE: 65,
            StatsEnum.SPEED: 90
        }
    },
    "0078": {
        None: {
            PocketMonsterParamEnum.NAME: "Rapidash",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.FIRE,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 65,
            StatsEnum.ATTACK: 100,
            StatsEnum.DEFENSE: 70,
            StatsEnum.SPECIAL_ATTACK: 80,
            StatsEnum.SPECIAL_DEFENSE: 80,
            StatsEnum.SPEED: 105
        },
        FormEnum.GALARIAN: {
            PocketMonsterParamEnum.NAME: "Rapidash",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.PSYCHIC,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.FAIRY,
            StatsEnum.HP: 65,
            StatsEnum.ATTACK: 100,
            StatsEnum.DEFENSE: 70,
            StatsEnum.SPECIAL_ATTACK: 80,
            StatsEnum.SPECIAL_DEFENSE: 80,
            StatsEnum.SPEED: 105
        }
    },
    "0079": {
        None: {
            PocketMonsterParamEnum.NAME: "Slowpoke",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.WATER,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.PSYCHIC,
            StatsEnum.HP: 90,
            StatsEnum.ATTACK: 65,
            StatsEnum.DEFENSE: 65,
            StatsEnum.SPECIAL_ATTACK: 40,
            StatsEnum.SPECIAL_DEFENSE: 40,
            StatsEnum.SPEED: 15
        },
        FormEnum.GALARIAN: {
            PocketMonsterParamEnum.NAME: "Slowpoke",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.PSYCHIC,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 90,
            StatsEnum.ATTACK: 65,
            StatsEnum.DEFENSE: 65,
            StatsEnum.SPECIAL_ATTACK: 40,
            StatsEnum.SPECIAL_DEFENSE: 40,
            StatsEnum.SPEED: 15
        }
    },
    "0080": {
        None: {
            PocketMonsterParamEnum.NAME: "Slowbro",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.WATER,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.PSYCHIC,
            StatsEnum.HP: 95,
            StatsEnum.ATTACK: 75,
            StatsEnum.DEFENSE: 110,
            StatsEnum.SPECIAL_ATTACK: 100,
            StatsEnum.SPECIAL_DEFENSE: 80,
            StatsEnum.SPEED: 30
        },
        FormEnum.MEGA: {
            PocketMonsterParamEnum.NAME: "Slowbro",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.WATER,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.PSYCHIC,
            StatsEnum.HP: 95,
            StatsEnum.ATTACK: 75,
            StatsEnum.DEFENSE: 180,
            StatsEnum.SPECIAL_ATTACK: 130,
            StatsEnum.SPECIAL_DEFENSE: 80,
            StatsEnum.SPEED: 30
        },
        FormEnum.GALARIAN: {
            PocketMonsterParamEnum.NAME: "Slowbro",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.POISON,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.PSYCHIC,
            StatsEnum.HP: 95,
            StatsEnum.ATTACK: 100,
            StatsEnum.DEFENSE: 95,
            StatsEnum.SPECIAL_ATTACK: 100,
            StatsEnum.SPECIAL_DEFENSE: 70,
            StatsEnum.SPEED: 30
        }
    },
    "0081": {
        None: {
            PocketMonsterParamEnum.NAME: "Magnemite",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.ELECTRIC,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.STEEL,
            StatsEnum.HP: 25,
            StatsEnum.ATTACK: 35,
            StatsEnum.DEFENSE: 70,
            StatsEnum.SPECIAL_ATTACK: 95,
            StatsEnum.SPECIAL_DEFENSE: 55,
            StatsEnum.SPEED: 45
        }
    },
    "0082": {
        None: {
            PocketMonsterParamEnum.NAME: "Magneton",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.ELECTRIC,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.STEEL,
            StatsEnum.HP: 50,
            StatsEnum.ATTACK: 60,
            StatsEnum.DEFENSE: 95,
            StatsEnum.SPECIAL_ATTACK: 120,
            StatsEnum.SPECIAL_DEFENSE: 70,
            StatsEnum.SPEED: 70
        }
    },
    "0083": {
        None: {
            PocketMonsterParamEnum.NAME: "Farfetch'd",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.NORMAL,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.FLYING,
            StatsEnum.HP: 52,
            StatsEnum.ATTACK: 90,
            StatsEnum.DEFENSE: 55,
            StatsEnum.SPECIAL_ATTACK: 58,
            StatsEnum.SPECIAL_DEFENSE: 62,
            StatsEnum.SPEED: 60
        },
        FormEnum.GALARIAN: {
            PocketMonsterParamEnum.NAME: "Farfetch'd",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.FIGHTING,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 52,
            StatsEnum.ATTACK: 95,
            StatsEnum.DEFENSE: 55,
            StatsEnum.SPECIAL_ATTACK: 58,
            StatsEnum.SPECIAL_DEFENSE: 62,
            StatsEnum.SPEED: 55
        }
    },
    "0084": {
        None: {
            PocketMonsterParamEnum.NAME: "Doduo",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.NORMAL,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.FLYING,
            StatsEnum.HP: 35,
            StatsEnum.ATTACK: 85,
            StatsEnum.DEFENSE: 45,
            StatsEnum.SPECIAL_ATTACK: 35,
            StatsEnum.SPECIAL_DEFENSE: 35,
            StatsEnum.SPEED: 75
        }
    },
    "0085": {
        None: {
            PocketMonsterParamEnum.NAME: "Dodrio",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.NORMAL,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.FLYING,
            StatsEnum.HP: 60,
            StatsEnum.ATTACK: 110,
            StatsEnum.DEFENSE: 70,
            StatsEnum.SPECIAL_ATTACK: 60,
            StatsEnum.SPECIAL_DEFENSE: 60,
            StatsEnum.SPEED: 110
        }
    },
    "0086": {
        None: {
            PocketMonsterParamEnum.NAME: "Seel",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.WATER,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 65,
            StatsEnum.ATTACK: 45,
            StatsEnum.DEFENSE: 55,
            StatsEnum.SPECIAL_ATTACK: 45,
            StatsEnum.SPECIAL_DEFENSE: 70,
            StatsEnum.SPEED: 45
        }
    },
    "0087": {
        None: {
            PocketMonsterParamEnum.NAME: "Dewgong",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.WATER,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.ICE,
            StatsEnum.HP: 90,
            StatsEnum.ATTACK: 70,
            StatsEnum.DEFENSE: 80,
            StatsEnum.SPECIAL_ATTACK: 70,
            StatsEnum.SPECIAL_DEFENSE: 95,
            StatsEnum.SPEED: 70
        }
    },
    "0088": {
        None: {
            PocketMonsterParamEnum.NAME: "Grimer",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.POISON,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 80,
            StatsEnum.ATTACK: 80,
            StatsEnum.DEFENSE: 50,
            StatsEnum.SPECIAL_ATTACK: 40,
            StatsEnum.SPECIAL_DEFENSE: 50,
            StatsEnum.SPEED: 25
        },
        FormEnum.ALOLAN: {
            PocketMonsterParamEnum.NAME: "Grimer",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.POISON,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.DARK,
            StatsEnum.HP: 80,
            StatsEnum.ATTACK: 80,
            StatsEnum.DEFENSE: 50,
            StatsEnum.SPECIAL_ATTACK: 40,
            StatsEnum.SPECIAL_DEFENSE: 50,
            StatsEnum.SPEED: 25
        }
    },
    "0089": {
        None: {
            PocketMonsterParamEnum.NAME: "Muk",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.POISON,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 105,
            StatsEnum.ATTACK: 105,
            StatsEnum.DEFENSE: 75,
            StatsEnum.SPECIAL_ATTACK: 65,
            StatsEnum.SPECIAL_DEFENSE: 100,
            StatsEnum.SPEED: 50
        },
        FormEnum.ALOLAN: {
            PocketMonsterParamEnum.NAME: "Muk",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.POISON,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.DARK,
            StatsEnum.HP: 105,
            StatsEnum.ATTACK: 105,
            StatsEnum.DEFENSE: 75,
            StatsEnum.SPECIAL_ATTACK: 65,
            StatsEnum.SPECIAL_DEFENSE: 100,
            StatsEnum.SPEED: 50
        }
    },
    "0090": {
        None: {
            PocketMonsterParamEnum.NAME: "Shellder",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.WATER,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 30,
            StatsEnum.ATTACK: 65,
            StatsEnum.DEFENSE: 100,
            StatsEnum.SPECIAL_ATTACK: 45,
            StatsEnum.SPECIAL_DEFENSE: 25,
            StatsEnum.SPEED: 40
        }
    },
    "0091": {
        None: {
            PocketMonsterParamEnum.NAME: "Cloyster",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.WATER,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.ICE,
            StatsEnum.HP: 50,
            StatsEnum.ATTACK: 95,
            StatsEnum.DEFENSE: 180,
            StatsEnum.SPECIAL_ATTACK: 85,
            StatsEnum.SPECIAL_DEFENSE: 45,
            StatsEnum.SPEED: 70
        }
    },
    "0092": {
        None: {
            PocketMonsterParamEnum.NAME: "Gastly",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.GHOST,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.POISON,
            StatsEnum.HP: 30,
            StatsEnum.ATTACK: 35,
            StatsEnum.DEFENSE: 30,
            StatsEnum.SPECIAL_ATTACK: 100,
            StatsEnum.SPECIAL_DEFENSE: 35,
            StatsEnum.SPEED: 80
        }
    },
    "0093": {
        None: {
            PocketMonsterParamEnum.NAME: "Haunter",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.GHOST,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.POISON,
            StatsEnum.HP: 45,
            StatsEnum.ATTACK: 50,
            StatsEnum.DEFENSE: 45,
            StatsEnum.SPECIAL_ATTACK: 115,
            StatsEnum.SPECIAL_DEFENSE: 55,
            StatsEnum.SPEED: 95
        }
    },
    "0094": {
        None: {
            PocketMonsterParamEnum.NAME: "Gengar",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.GHOST,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.POISON,
            StatsEnum.HP: 60,
            StatsEnum.ATTACK: 65,
            StatsEnum.DEFENSE: 60,
            StatsEnum.SPECIAL_ATTACK: 130,
            StatsEnum.SPECIAL_DEFENSE: 75,
            StatsEnum.SPEED: 110
        },
        FormEnum.MEGA: {
            PocketMonsterParamEnum.NAME: "Gengar",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.GHOST,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.POISON,
            StatsEnum.HP: 60,
            StatsEnum.ATTACK: 65,
            StatsEnum.DEFENSE: 80,
            StatsEnum.SPECIAL_ATTACK: 170,
            StatsEnum.SPECIAL_DEFENSE: 95,
            StatsEnum.SPEED: 130
        }
    },
    "0095": {
        None: {
            PocketMonsterParamEnum.NAME: "Onix",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.ROCK,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.GROUND,
            StatsEnum.HP: 35,
            StatsEnum.ATTACK: 45,
            StatsEnum.DEFENSE: 160,
            StatsEnum.SPECIAL_ATTACK: 30,
            StatsEnum.SPECIAL_DEFENSE: 45,
            StatsEnum.SPEED: 70
        }
    },
    "0096": {
        None: {
            PocketMonsterParamEnum.NAME: "Drowzee",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.PSYCHIC,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 60,
            StatsEnum.ATTACK: 48,
            StatsEnum.DEFENSE: 45,
            StatsEnum.SPECIAL_ATTACK: 43,
            StatsEnum.SPECIAL_DEFENSE: 90,
            StatsEnum.SPEED: 42
        }
    },
    "0097": {
        None: {
            PocketMonsterParamEnum.NAME: "Hypno",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.PSYCHIC,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 85,
            StatsEnum.ATTACK: 73,
            StatsEnum.DEFENSE: 70,
            StatsEnum.SPECIAL_ATTACK: 73,
            StatsEnum.SPECIAL_DEFENSE: 115,
            StatsEnum.SPEED: 67
        }
    },
    "0098": {
        None: {
            PocketMonsterParamEnum.NAME: "Krabby",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.WATER,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 30,
            StatsEnum.ATTACK: 105,
            StatsEnum.DEFENSE: 90,
            StatsEnum.SPECIAL_ATTACK: 25,
            StatsEnum.SPECIAL_DEFENSE: 25,
            StatsEnum.SPEED: 50
        }
    },
    "0099": {
        None: {
            PocketMonsterParamEnum.NAME: "Kingler",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.WATER,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 55,
            StatsEnum.ATTACK: 130,
            StatsEnum.DEFENSE: 115,
            StatsEnum.SPECIAL_ATTACK: 50,
            StatsEnum.SPECIAL_DEFENSE: 50,
            StatsEnum.SPEED: 75
        }
    },
    "0100": {
        None: {
            PocketMonsterParamEnum.NAME: "Voltorb",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.ELECTRIC,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 40,
            StatsEnum.ATTACK: 30,
            StatsEnum.DEFENSE: 50,
            StatsEnum.SPECIAL_ATTACK: 55,
            StatsEnum.SPECIAL_DEFENSE: 55,
            StatsEnum.SPEED: 100
        },
        FormEnum.HISUIAN: {
            PocketMonsterParamEnum.NAME: "Voltorb",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.ELECTRIC,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.GRASS,
            StatsEnum.HP: 40,
            StatsEnum.ATTACK: 30,
            StatsEnum.DEFENSE: 50,
            StatsEnum.SPECIAL_ATTACK: 55,
            StatsEnum.SPECIAL_DEFENSE: 55,
            StatsEnum.SPEED: 100
        }
    },
    "0101": {
        None: {
            PocketMonsterParamEnum.NAME: "Electrode",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.ELECTRIC,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 60,
            StatsEnum.ATTACK: 50,
            StatsEnum.DEFENSE: 70,
            StatsEnum.SPECIAL_ATTACK: 80,
            StatsEnum.SPECIAL_DEFENSE: 80,
            StatsEnum.SPEED: 150
        },
        FormEnum.HISUIAN: {
            PocketMonsterParamEnum.NAME: "Electrode",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.ELECTRIC,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.GRASS,
            StatsEnum.HP: 60,
            StatsEnum.ATTACK: 50,
            StatsEnum.DEFENSE: 70,
            StatsEnum.SPECIAL_ATTACK: 80,
            StatsEnum.SPECIAL_DEFENSE: 80,
            StatsEnum.SPEED: 150
        }
    },
    "0102": {
        None: {
            PocketMonsterParamEnum.NAME: "Exeggcute",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.GRASS,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.PSYCHIC,
            StatsEnum.HP: 60,
            StatsEnum.ATTACK: 40,
            StatsEnum.DEFENSE: 80,
            StatsEnum.SPECIAL_ATTACK: 60,
            StatsEnum.SPECIAL_DEFENSE: 45,
            StatsEnum.SPEED: 40
        }
    },
    "0103": {
        None: {
            PocketMonsterParamEnum.NAME: "Exeggutor",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.GRASS,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.PSYCHIC,
            StatsEnum.HP: 95,
            StatsEnum.ATTACK: 95,
            StatsEnum.DEFENSE: 85,
            StatsEnum.SPECIAL_ATTACK: 125,
            StatsEnum.SPECIAL_DEFENSE: 75,
            StatsEnum.SPEED: 55
        },
        FormEnum.ALOLAN: {
            PocketMonsterParamEnum.NAME: "Exeggutor",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.GRASS,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.DRAGON,
            StatsEnum.HP: 95,
            StatsEnum.ATTACK: 105,
            StatsEnum.DEFENSE: 85,
            StatsEnum.SPECIAL_ATTACK: 125,
            StatsEnum.SPECIAL_DEFENSE: 75,
            StatsEnum.SPEED: 45
        }
    },
    "0104": {
        None: {
            PocketMonsterParamEnum.NAME: "Cubone",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.GROUND,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 50,
            StatsEnum.ATTACK: 50,
            StatsEnum.DEFENSE: 95,
            StatsEnum.SPECIAL_ATTACK: 40,
            StatsEnum.SPECIAL_DEFENSE: 50,
            StatsEnum.SPEED: 35
        }
    },
    "0105": {
        None: {
            PocketMonsterParamEnum.NAME: "Marowak",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.GROUND,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 60,
            StatsEnum.ATTACK: 80,
            StatsEnum.DEFENSE: 110,
            StatsEnum.SPECIAL_ATTACK: 50,
            StatsEnum.SPECIAL_DEFENSE: 80,
            StatsEnum.SPEED: 45
        },
        FormEnum.ALOLAN: {
            PocketMonsterParamEnum.NAME: "Marowak",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.FIRE,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.GHOST,
            StatsEnum.HP: 60,
            StatsEnum.ATTACK: 80,
            StatsEnum.DEFENSE: 110,
            StatsEnum.SPECIAL_ATTACK: 50,
            StatsEnum.SPECIAL_DEFENSE: 80,
            StatsEnum.SPEED: 45
        }
    },
    "0106": {
        None: {
            PocketMonsterParamEnum.NAME: "Hitmonlee",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.FIGHTING,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 50,
            StatsEnum.ATTACK: 120,
            StatsEnum.DEFENSE: 53,
            StatsEnum.SPECIAL_ATTACK: 35,
            StatsEnum.SPECIAL_DEFENSE: 110,
            StatsEnum.SPEED: 87
        }
    },
    "0107": {
        None: {
            PocketMonsterParamEnum.NAME: "Hitmonchan",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.FIGHTING,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 50,
            StatsEnum.ATTACK: 105,
            StatsEnum.DEFENSE: 79,
            StatsEnum.SPECIAL_ATTACK: 35,
            StatsEnum.SPECIAL_DEFENSE: 110,
            StatsEnum.SPEED: 76
        }
    },
    "0108": {
        None: {
            PocketMonsterParamEnum.NAME: "Lickitung",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.NORMAL,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 90,
            StatsEnum.ATTACK: 55,
            StatsEnum.DEFENSE: 75,
            StatsEnum.SPECIAL_ATTACK: 60,
            StatsEnum.SPECIAL_DEFENSE: 75,
            StatsEnum.SPEED: 30
        }
    },
    "0109": {
        None: {
            PocketMonsterParamEnum.NAME: "Koffing",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.POISON,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 40,
            StatsEnum.ATTACK: 65,
            StatsEnum.DEFENSE: 95,
            StatsEnum.SPECIAL_ATTACK: 60,
            StatsEnum.SPECIAL_DEFENSE: 45,
            StatsEnum.SPEED: 35
        }
    },
    "0110": {
        None: {
            PocketMonsterParamEnum.NAME: "Weezing",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.POISON,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 65,
            StatsEnum.ATTACK: 90,
            StatsEnum.DEFENSE: 120,
            StatsEnum.SPECIAL_ATTACK: 85,
            StatsEnum.SPECIAL_DEFENSE: 70,
            StatsEnum.SPEED: 60
        },
        FormEnum.GALARIAN: {
            PocketMonsterParamEnum.NAME: "Weezing",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.POISON,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.FAIRY,
            StatsEnum.HP: 65,
            StatsEnum.ATTACK: 90,
            StatsEnum.DEFENSE: 120,
            StatsEnum.SPECIAL_ATTACK: 85,
            StatsEnum.SPECIAL_DEFENSE: 70,
            StatsEnum.SPEED: 60
        }
    },
    "0111": {
        None: {
            PocketMonsterParamEnum.NAME: "Rhyhorn",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.GROUND,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.ROCK,
            StatsEnum.HP: 80,
            StatsEnum.ATTACK: 85,
            StatsEnum.DEFENSE: 95,
            StatsEnum.SPECIAL_ATTACK: 30,
            StatsEnum.SPECIAL_DEFENSE: 30,
            StatsEnum.SPEED: 25
        }
    },
    "0112": {
        None: {
            PocketMonsterParamEnum.NAME: "Rhydon",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.GROUND,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.ROCK,
            StatsEnum.HP: 105,
            StatsEnum.ATTACK: 130,
            StatsEnum.DEFENSE: 120,
            StatsEnum.SPECIAL_ATTACK: 45,
            StatsEnum.SPECIAL_DEFENSE: 45,
            StatsEnum.SPEED: 40
        }
    },
    "0113": {
        None: {
            PocketMonsterParamEnum.NAME: "Chansey",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.NORMAL,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 250,
            StatsEnum.ATTACK: 5,
            StatsEnum.DEFENSE: 5,
            StatsEnum.SPECIAL_ATTACK: 35,
            StatsEnum.SPECIAL_DEFENSE: 105,
            StatsEnum.SPEED: 50
        }
    },
    "0114": {
        None: {
            PocketMonsterParamEnum.NAME: "Tangela",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.GRASS,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 65,
            StatsEnum.ATTACK: 55,
            StatsEnum.DEFENSE: 115,
            StatsEnum.SPECIAL_ATTACK: 100,
            StatsEnum.SPECIAL_DEFENSE: 40,
            StatsEnum.SPEED: 60
        }
    },
    "0115": {
        None: {
            PocketMonsterParamEnum.NAME: "Kangaskhan",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.NORMAL,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 105,
            StatsEnum.ATTACK: 95,
            StatsEnum.DEFENSE: 80,
            StatsEnum.SPECIAL_ATTACK: 40,
            StatsEnum.SPECIAL_DEFENSE: 80,
            StatsEnum.SPEED: 90
        },
        FormEnum.MEGA: {
            PocketMonsterParamEnum.NAME: "Kangaskhan",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.NORMAL,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 105,
            StatsEnum.ATTACK: 125,
            StatsEnum.DEFENSE: 100,
            StatsEnum.SPECIAL_ATTACK: 60,
            StatsEnum.SPECIAL_DEFENSE: 100,
            StatsEnum.SPEED: 100
        }
    },
    "0116": {
        None: {
            PocketMonsterParamEnum.NAME: "Horsea",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.WATER,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 30,
            StatsEnum.ATTACK: 40,
            StatsEnum.DEFENSE: 70,
            StatsEnum.SPECIAL_ATTACK: 70,
            StatsEnum.SPECIAL_DEFENSE: 25,
            StatsEnum.SPEED: 60
        }
    },
    "0117": {
        None: {
            PocketMonsterParamEnum.NAME: "Seadra",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.WATER,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 55,
            StatsEnum.ATTACK: 65,
            StatsEnum.DEFENSE: 95,
            StatsEnum.SPECIAL_ATTACK: 95,
            StatsEnum.SPECIAL_DEFENSE: 45,
            StatsEnum.SPEED: 85
        }
    },
    "0118": {
        None: {
            PocketMonsterParamEnum.NAME: "Goldeen",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.WATER,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 45,
            StatsEnum.ATTACK: 67,
            StatsEnum.DEFENSE: 60,
            StatsEnum.SPECIAL_ATTACK: 35,
            StatsEnum.SPECIAL_DEFENSE: 50,
            StatsEnum.SPEED: 63
        }
    },
    "0119": {
        None: {
            PocketMonsterParamEnum.NAME: "Seaking",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.WATER,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 80,
            StatsEnum.ATTACK: 92,
            StatsEnum.DEFENSE: 65,
            StatsEnum.SPECIAL_ATTACK: 65,
            StatsEnum.SPECIAL_DEFENSE: 80,
            StatsEnum.SPEED: 68
        }
    },
    "0120": {
        None: {
            PocketMonsterParamEnum.NAME: "Staryu",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.WATER,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 30,
            StatsEnum.ATTACK: 45,
            StatsEnum.DEFENSE: 55,
            StatsEnum.SPECIAL_ATTACK: 70,
            StatsEnum.SPECIAL_DEFENSE: 55,
            StatsEnum.SPEED: 85
        }
    },
    "0121": {
        None: {
            PocketMonsterParamEnum.NAME: "Starmie",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.WATER,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.PSYCHIC,
            StatsEnum.HP: 60,
            StatsEnum.ATTACK: 75,
            StatsEnum.DEFENSE: 85,
            StatsEnum.SPECIAL_ATTACK: 100,
            StatsEnum.SPECIAL_DEFENSE: 85,
            StatsEnum.SPEED: 115
        }
    },
    "0122": {
        None: {
            PocketMonsterParamEnum.NAME: "Mr. Mime",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.PSYCHIC,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.FAIRY,
            StatsEnum.HP: 40,
            StatsEnum.ATTACK: 45,
            StatsEnum.DEFENSE: 65,
            StatsEnum.SPECIAL_ATTACK: 100,
            StatsEnum.SPECIAL_DEFENSE: 120,
            StatsEnum.SPEED: 90
        },
        FormEnum.GALARIAN: {
            PocketMonsterParamEnum.NAME: "Mr. Mime",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.ICE,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.PSYCHIC,
            StatsEnum.HP: 50,
            StatsEnum.ATTACK: 65,
            StatsEnum.DEFENSE: 65,
            StatsEnum.SPECIAL_ATTACK: 90,
            StatsEnum.SPECIAL_DEFENSE: 90,
            StatsEnum.SPEED: 100
        }
    },
    "0123": {
        None: {
            PocketMonsterParamEnum.NAME: "Scyther",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.BUG,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.FLYING,
            StatsEnum.HP: 70,
            StatsEnum.ATTACK: 110,
            StatsEnum.DEFENSE: 80,
            StatsEnum.SPECIAL_ATTACK: 55,
            StatsEnum.SPECIAL_DEFENSE: 80,
            StatsEnum.SPEED: 105
        }
    },
    "0124": {
        None: {
            PocketMonsterParamEnum.NAME: "Jynx",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.ICE,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.PSYCHIC,
            StatsEnum.HP: 65,
            StatsEnum.ATTACK: 50,
            StatsEnum.DEFENSE: 35,
            StatsEnum.SPECIAL_ATTACK: 115,
            StatsEnum.SPECIAL_DEFENSE: 95,
            StatsEnum.SPEED: 95
        }
    },
    "0125": {
        None: {
            PocketMonsterParamEnum.NAME: "Electabuzz",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.ELECTRIC,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 65,
            StatsEnum.ATTACK: 83,
            StatsEnum.DEFENSE: 57,
            StatsEnum.SPECIAL_ATTACK: 95,
            StatsEnum.SPECIAL_DEFENSE: 85,
            StatsEnum.SPEED: 105
        }
    },
    "0126": {
        None: {
            PocketMonsterParamEnum.NAME: "Magmar",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.FIRE,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 65,
            StatsEnum.ATTACK: 95,
            StatsEnum.DEFENSE: 57,
            StatsEnum.SPECIAL_ATTACK: 100,
            StatsEnum.SPECIAL_DEFENSE: 85,
            StatsEnum.SPEED: 93
        }
    },
    "0127": {
        None: {
            PocketMonsterParamEnum.NAME: "Pinsir",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.BUG,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 65,
            StatsEnum.ATTACK: 125,
            StatsEnum.DEFENSE: 100,
            StatsEnum.SPECIAL_ATTACK: 55,
            StatsEnum.SPECIAL_DEFENSE: 70,
            StatsEnum.SPEED: 85
        },
        FormEnum.MEGA: {
            PocketMonsterParamEnum.NAME: "Pinsir",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.BUG,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.FLYING,
            StatsEnum.HP: 65,
            StatsEnum.ATTACK: 155,
            StatsEnum.DEFENSE: 120,
            StatsEnum.SPECIAL_ATTACK: 65,
            StatsEnum.SPECIAL_DEFENSE: 90,
            StatsEnum.SPEED: 105
        }
    },
    "0128": {
        None: {
            PocketMonsterParamEnum.NAME: "Tauros",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.NORMAL,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 75,
            StatsEnum.ATTACK: 100,
            StatsEnum.DEFENSE: 95,
            StatsEnum.SPECIAL_ATTACK: 40,
            StatsEnum.SPECIAL_DEFENSE: 70,
            StatsEnum.SPEED: 110
        },
        FormEnum.COMBAT_BREED: {
            PocketMonsterParamEnum.NAME: "Tauros",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.FIGHTING,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 75,
            StatsEnum.ATTACK: 110,
            StatsEnum.DEFENSE: 105,
            StatsEnum.SPECIAL_ATTACK: 30,
            StatsEnum.SPECIAL_DEFENSE: 70,
            StatsEnum.SPEED: 100
        },
        FormEnum.BLAZE_BREED: {
            PocketMonsterParamEnum.NAME: "Tauros",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.FIGHTING,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.FIRE,
            StatsEnum.HP: 75,
            StatsEnum.ATTACK: 110,
            StatsEnum.DEFENSE: 105,
            StatsEnum.SPECIAL_ATTACK: 30,
            StatsEnum.SPECIAL_DEFENSE: 70,
            StatsEnum.SPEED: 100
        },
        FormEnum.AQUA_BREED: {
            PocketMonsterParamEnum.NAME: "Tauros",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.FIGHTING,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.WATER,
            StatsEnum.HP: 75,
            StatsEnum.ATTACK: 110,
            StatsEnum.DEFENSE: 105,
            StatsEnum.SPECIAL_ATTACK: 30,
            StatsEnum.SPECIAL_DEFENSE: 70,
            StatsEnum.SPEED: 100
        }
    },
    "0129": {
        None: {
            PocketMonsterParamEnum.NAME: "Magikarp",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.WATER,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 20,
            StatsEnum.ATTACK: 10,
            StatsEnum.DEFENSE: 55,
            StatsEnum.SPECIAL_ATTACK: 15,
            StatsEnum.SPECIAL_DEFENSE: 20,
            StatsEnum.SPEED: 80
        }
    },
    "0130": {
        None: {
            PocketMonsterParamEnum.NAME: "Gyarados",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.WATER,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.FLYING,
            StatsEnum.HP: 95,
            StatsEnum.ATTACK: 125,
            StatsEnum.DEFENSE: 79,
            StatsEnum.SPECIAL_ATTACK: 60,
            StatsEnum.SPECIAL_DEFENSE: 100,
            StatsEnum.SPEED: 81
        },
        FormEnum.MEGA: {
            PocketMonsterParamEnum.NAME: "Gyarados",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.WATER,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.DARK,
            StatsEnum.HP: 95,
            StatsEnum.ATTACK: 155,
            StatsEnum.DEFENSE: 109,
            StatsEnum.SPECIAL_ATTACK: 70,
            StatsEnum.SPECIAL_DEFENSE: 130,
            StatsEnum.SPEED: 81
        }
    },
    "0131": {
        None: {
            PocketMonsterParamEnum.NAME: "Lapras",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.WATER,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.ICE,
            StatsEnum.HP: 130,
            StatsEnum.ATTACK: 85,
            StatsEnum.DEFENSE: 80,
            StatsEnum.SPECIAL_ATTACK: 85,
            StatsEnum.SPECIAL_DEFENSE: 95,
            StatsEnum.SPEED: 60
        }
    },
    "0132": {
        None: {
            PocketMonsterParamEnum.NAME: "Ditto",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.NORMAL,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 48,
            StatsEnum.ATTACK: 48,
            StatsEnum.DEFENSE: 48,
            StatsEnum.SPECIAL_ATTACK: 48,
            StatsEnum.SPECIAL_DEFENSE: 48,
            StatsEnum.SPEED: 48
        }
    },
    "0133": {
        None: {
            PocketMonsterParamEnum.NAME: "Eevee",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.NORMAL,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 55,
            StatsEnum.ATTACK: 55,
            StatsEnum.DEFENSE: 50,
            StatsEnum.SPECIAL_ATTACK: 45,
            StatsEnum.SPECIAL_DEFENSE: 65,
            StatsEnum.SPEED: 55
        },
        FormEnum.PARTNER: {
            PocketMonsterParamEnum.NAME: "Eevee",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.NORMAL,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 65,
            StatsEnum.ATTACK: 75,
            StatsEnum.DEFENSE: 70,
            StatsEnum.SPECIAL_ATTACK: 65,
            StatsEnum.SPECIAL_DEFENSE: 85,
            StatsEnum.SPEED: 75
        }
    },
    "0134": {
        None: {
            PocketMonsterParamEnum.NAME: "Vaporeon",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.WATER,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 130,
            StatsEnum.ATTACK: 65,
            StatsEnum.DEFENSE: 60,
            StatsEnum.SPECIAL_ATTACK: 110,
            StatsEnum.SPECIAL_DEFENSE: 95,
            StatsEnum.SPEED: 65
        }
    },
    "0135": {
        None: {
            PocketMonsterParamEnum.NAME: "Jolteon",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.ELECTRIC,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 65,
            StatsEnum.ATTACK: 65,
            StatsEnum.DEFENSE: 60,
            StatsEnum.SPECIAL_ATTACK: 110,
            StatsEnum.SPECIAL_DEFENSE: 95,
            StatsEnum.SPEED: 130
        }
    },
    "0136": {
        None: {
            PocketMonsterParamEnum.NAME: "Flareon",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.FIRE,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 65,
            StatsEnum.ATTACK: 130,
            StatsEnum.DEFENSE: 60,
            StatsEnum.SPECIAL_ATTACK: 95,
            StatsEnum.SPECIAL_DEFENSE: 110,
            StatsEnum.SPEED: 65
        }
    },
    "0137": {
        None: {
            PocketMonsterParamEnum.NAME: "Porygon",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.NORMAL,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 65,
            StatsEnum.ATTACK: 60,
            StatsEnum.DEFENSE: 70,
            StatsEnum.SPECIAL_ATTACK: 85,
            StatsEnum.SPECIAL_DEFENSE: 75,
            StatsEnum.SPEED: 40
        }
    },
    "0138": {
        None: {
            PocketMonsterParamEnum.NAME: "Omanyte",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.ROCK,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.WATER,
            StatsEnum.HP: 35,
            StatsEnum.ATTACK: 40,
            StatsEnum.DEFENSE: 100,
            StatsEnum.SPECIAL_ATTACK: 90,
            StatsEnum.SPECIAL_DEFENSE: 55,
            StatsEnum.SPEED: 35
        }
    },
    "0139": {
        None: {
            PocketMonsterParamEnum.NAME: "Omastar",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.ROCK,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.WATER,
            StatsEnum.HP: 70,
            StatsEnum.ATTACK: 60,
            StatsEnum.DEFENSE: 125,
            StatsEnum.SPECIAL_ATTACK: 115,
            StatsEnum.SPECIAL_DEFENSE: 70,
            StatsEnum.SPEED: 55
        }
    },
    "0140": {
        None: {
            PocketMonsterParamEnum.NAME: "Kabuto",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.ROCK,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.WATER,
            StatsEnum.HP: 30,
            StatsEnum.ATTACK: 80,
            StatsEnum.DEFENSE: 90,
            StatsEnum.SPECIAL_ATTACK: 55,
            StatsEnum.SPECIAL_DEFENSE: 45,
            StatsEnum.SPEED: 55
        }
    },
    "0141": {
        None: {
            PocketMonsterParamEnum.NAME: "Kabutops",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.ROCK,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.WATER,
            StatsEnum.HP: 60,
            StatsEnum.ATTACK: 115,
            StatsEnum.DEFENSE: 105,
            StatsEnum.SPECIAL_ATTACK: 65,
            StatsEnum.SPECIAL_DEFENSE: 70,
            StatsEnum.SPEED: 80
        }
    },
    "0142": {
        None: {
            PocketMonsterParamEnum.NAME: "Aerodactyl",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.ROCK,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.FLYING,
            StatsEnum.HP: 80,
            StatsEnum.ATTACK: 105,
            StatsEnum.DEFENSE: 65,
            StatsEnum.SPECIAL_ATTACK: 60,
            StatsEnum.SPECIAL_DEFENSE: 75,
            StatsEnum.SPEED: 130
        },
        FormEnum.MEGA: {
            PocketMonsterParamEnum.NAME: "Aerodactyl",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.ROCK,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.FLYING,
            StatsEnum.HP: 80,
            StatsEnum.ATTACK: 135,
            StatsEnum.DEFENSE: 85,
            StatsEnum.SPECIAL_ATTACK: 70,
            StatsEnum.SPECIAL_DEFENSE: 95,
            StatsEnum.SPEED: 150
        }
    },
    "0143": {
        None: {
            PocketMonsterParamEnum.NAME: "Snorlax",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.NORMAL,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 160,
            StatsEnum.ATTACK: 110,
            StatsEnum.DEFENSE: 65,
            StatsEnum.SPECIAL_ATTACK: 65,
            StatsEnum.SPECIAL_DEFENSE: 110,
            StatsEnum.SPEED: 30
        }
    },
    "0144": {
        None: {
            PocketMonsterParamEnum.NAME: "Articuno",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.ICE,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.FLYING,
            StatsEnum.HP: 90,
            StatsEnum.ATTACK: 85,
            StatsEnum.DEFENSE: 100,
            StatsEnum.SPECIAL_ATTACK: 95,
            StatsEnum.SPECIAL_DEFENSE: 125,
            StatsEnum.SPEED: 85
        },
        FormEnum.GALARIAN: {
            PocketMonsterParamEnum.NAME: "Articuno",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.PSYCHIC,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.FLYING,
            StatsEnum.HP: 90,
            StatsEnum.ATTACK: 85,
            StatsEnum.DEFENSE: 85,
            StatsEnum.SPECIAL_ATTACK: 125,
            StatsEnum.SPECIAL_DEFENSE: 100,
            StatsEnum.SPEED: 95
        }
    },
    "0145": {
        None: {
            PocketMonsterParamEnum.NAME: "Zapdos",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.ELECTRIC,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.FLYING,
            StatsEnum.HP: 90,
            StatsEnum.ATTACK: 90,
            StatsEnum.DEFENSE: 85,
            StatsEnum.SPECIAL_ATTACK: 125,
            StatsEnum.SPECIAL_DEFENSE: 90,
            StatsEnum.SPEED: 100
        },
        FormEnum.GALARIAN: {
            PocketMonsterParamEnum.NAME: "Zapdos",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.FIGHTING,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.FLYING,
            StatsEnum.HP: 90,
            StatsEnum.ATTACK: 125,
            StatsEnum.DEFENSE: 90,
            StatsEnum.SPECIAL_ATTACK: 85,
            StatsEnum.SPECIAL_DEFENSE: 90,
            StatsEnum.SPEED: 100
        }
    },
    "0146": {
        None: {
            PocketMonsterParamEnum.NAME: "Moltres",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.FIRE,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.FLYING,
            StatsEnum.HP: 90,
            StatsEnum.ATTACK: 100,
            StatsEnum.DEFENSE: 90,
            StatsEnum.SPECIAL_ATTACK: 125,
            StatsEnum.SPECIAL_DEFENSE: 85,
            StatsEnum.SPEED: 90
        },
        FormEnum.GALARIAN: {
            PocketMonsterParamEnum.NAME: "Moltres",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.DARK,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.FLYING,
            StatsEnum.HP: 90,
            StatsEnum.ATTACK: 85,
            StatsEnum.DEFENSE: 90,
            StatsEnum.SPECIAL_ATTACK: 100,
            StatsEnum.SPECIAL_DEFENSE: 125,
            StatsEnum.SPEED: 90
        }
    },
    "0147": {
        None: {
            PocketMonsterParamEnum.NAME: "Dratini",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.DRAGON,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 41,
            StatsEnum.ATTACK: 64,
            StatsEnum.DEFENSE: 45,
            StatsEnum.SPECIAL_ATTACK: 50,
            StatsEnum.SPECIAL_DEFENSE: 50,
            StatsEnum.SPEED: 50
        }
    },
    "0148": {
        None: {
            PocketMonsterParamEnum.NAME: "Dragonair",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.DRAGON,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 61,
            StatsEnum.ATTACK: 84,
            StatsEnum.DEFENSE: 65,
            StatsEnum.SPECIAL_ATTACK: 70,
            StatsEnum.SPECIAL_DEFENSE: 70,
            StatsEnum.SPEED: 70
        }
    },
    "0149": {
        None: {
            PocketMonsterParamEnum.NAME: "Dragonite",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.DRAGON,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.FLYING,
            StatsEnum.HP: 91,
            StatsEnum.ATTACK: 134,
            StatsEnum.DEFENSE: 95,
            StatsEnum.SPECIAL_ATTACK: 100,
            StatsEnum.SPECIAL_DEFENSE: 100,
            StatsEnum.SPEED: 80
        }
    },
    "0150": {
        None: {
            PocketMonsterParamEnum.NAME: "Mewtwo",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.PSYCHIC,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 106,
            StatsEnum.ATTACK: 110,
            StatsEnum.DEFENSE: 90,
            StatsEnum.SPECIAL_ATTACK: 154,
            StatsEnum.SPECIAL_DEFENSE: 90,
            StatsEnum.SPEED: 130
        },
        FormEnum.MEGA_X: {
            PocketMonsterParamEnum.NAME: "Mewtwo",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.PSYCHIC,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.FIGHTING,
            StatsEnum.HP: 106,
            StatsEnum.ATTACK: 190,
            StatsEnum.DEFENSE: 100,
            StatsEnum.SPECIAL_ATTACK: 154,
            StatsEnum.SPECIAL_DEFENSE: 100,
            StatsEnum.SPEED: 130
        },
        FormEnum.MEGA_Y: {
            PocketMonsterParamEnum.NAME: "Mewtwo",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.PSYCHIC,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 106,
            StatsEnum.ATTACK: 150,
            StatsEnum.DEFENSE: 70,
            StatsEnum.SPECIAL_ATTACK: 194,
            StatsEnum.SPECIAL_DEFENSE: 120,
            StatsEnum.SPEED: 140
        }
    },
    "0151": {
        None: {
            PocketMonsterParamEnum.NAME: "Mew",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.PSYCHIC,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 100,
            StatsEnum.ATTACK: 100,
            StatsEnum.DEFENSE: 100,
            StatsEnum.SPECIAL_ATTACK: 100,
            StatsEnum.SPECIAL_DEFENSE: 100,
            StatsEnum.SPEED: 100
        }
    },
    "0152": {
        None: {
            PocketMonsterParamEnum.NAME: "Chikorita",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.GRASS,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 45,
            StatsEnum.ATTACK: 49,
            StatsEnum.DEFENSE: 65,
            StatsEnum.SPECIAL_ATTACK: 49,
            StatsEnum.SPECIAL_DEFENSE: 65,
            StatsEnum.SPEED: 45
        }
    },
    "0153": {
        None: {
            PocketMonsterParamEnum.NAME: "Bayleef",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.GRASS,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 60,
            StatsEnum.ATTACK: 62,
            StatsEnum.DEFENSE: 80,
            StatsEnum.SPECIAL_ATTACK: 63,
            StatsEnum.SPECIAL_DEFENSE: 80,
            StatsEnum.SPEED: 60
        }
    },
    "0154": {
        None: {
            PocketMonsterParamEnum.NAME: "Meganium",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.GRASS,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 80,
            StatsEnum.ATTACK: 82,
            StatsEnum.DEFENSE: 100,
            StatsEnum.SPECIAL_ATTACK: 83,
            StatsEnum.SPECIAL_DEFENSE: 100,
            StatsEnum.SPEED: 80
        }
    },
    "0155": {
        None: {
            PocketMonsterParamEnum.NAME: "Cyndaquil",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.FIRE,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 39,
            StatsEnum.ATTACK: 52,
            StatsEnum.DEFENSE: 43,
            StatsEnum.SPECIAL_ATTACK: 60,
            StatsEnum.SPECIAL_DEFENSE: 50,
            StatsEnum.SPEED: 65
        }
    },
    "0156": {
        None: {
            PocketMonsterParamEnum.NAME: "Quilava",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.FIRE,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 58,
            StatsEnum.ATTACK: 64,
            StatsEnum.DEFENSE: 58,
            StatsEnum.SPECIAL_ATTACK: 80,
            StatsEnum.SPECIAL_DEFENSE: 65,
            StatsEnum.SPEED: 80
        }
    },
    "0157": {
        None: {
            PocketMonsterParamEnum.NAME: "Typhlosion",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.FIRE,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 78,
            StatsEnum.ATTACK: 84,
            StatsEnum.DEFENSE: 78,
            StatsEnum.SPECIAL_ATTACK: 109,
            StatsEnum.SPECIAL_DEFENSE: 85,
            StatsEnum.SPEED: 100
        },
        FormEnum.HISUIAN: {
            PocketMonsterParamEnum.NAME: "Typhlosion",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.FIRE,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.GHOST,
            StatsEnum.HP: 73,
            StatsEnum.ATTACK: 84,
            StatsEnum.DEFENSE: 78,
            StatsEnum.SPECIAL_ATTACK: 119,
            StatsEnum.SPECIAL_DEFENSE: 85,
            StatsEnum.SPEED: 95
        }
    },
    "0158": {
        None: {
            PocketMonsterParamEnum.NAME: "Totodile",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.WATER,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 50,
            StatsEnum.ATTACK: 65,
            StatsEnum.DEFENSE: 64,
            StatsEnum.SPECIAL_ATTACK: 44,
            StatsEnum.SPECIAL_DEFENSE: 48,
            StatsEnum.SPEED: 43
        }
    },
    "0159": {
        None: {
            PocketMonsterParamEnum.NAME: "Croconaw",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.WATER,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 65,
            StatsEnum.ATTACK: 80,
            StatsEnum.DEFENSE: 80,
            StatsEnum.SPECIAL_ATTACK: 59,
            StatsEnum.SPECIAL_DEFENSE: 63,
            StatsEnum.SPEED: 58
        }
    },
    "0160": {
        None: {
            PocketMonsterParamEnum.NAME: "Feraligatr",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.WATER,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 85,
            StatsEnum.ATTACK: 105,
            StatsEnum.DEFENSE: 100,
            StatsEnum.SPECIAL_ATTACK: 79,
            StatsEnum.SPECIAL_DEFENSE: 83,
            StatsEnum.SPEED: 78
        }
    },
    "0161": {
        None: {
            PocketMonsterParamEnum.NAME: "Sentret",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.NORMAL,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 35,
            StatsEnum.ATTACK: 46,
            StatsEnum.DEFENSE: 34,
            StatsEnum.SPECIAL_ATTACK: 35,
            StatsEnum.SPECIAL_DEFENSE: 45,
            StatsEnum.SPEED: 20
        }
    },
    "0162": {
        None: {
            PocketMonsterParamEnum.NAME: "Furret",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.NORMAL,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 85,
            StatsEnum.ATTACK: 76,
            StatsEnum.DEFENSE: 64,
            StatsEnum.SPECIAL_ATTACK: 45,
            StatsEnum.SPECIAL_DEFENSE: 55,
            StatsEnum.SPEED: 90
        }
    },
    "0163": {
        None: {
            PocketMonsterParamEnum.NAME: "Hoothoot",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.NORMAL,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.FLYING,
            StatsEnum.HP: 60,
            StatsEnum.ATTACK: 30,
            StatsEnum.DEFENSE: 30,
            StatsEnum.SPECIAL_ATTACK: 36,
            StatsEnum.SPECIAL_DEFENSE: 56,
            StatsEnum.SPEED: 50
        }
    },
    "0164": {
        None: {
            PocketMonsterParamEnum.NAME: "Noctowl",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.NORMAL,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.FLYING,
            StatsEnum.HP: 100,
            StatsEnum.ATTACK: 50,
            StatsEnum.DEFENSE: 50,
            StatsEnum.SPECIAL_ATTACK: 86,
            StatsEnum.SPECIAL_DEFENSE: 96,
            StatsEnum.SPEED: 70
        }
    },
    "0165": {
        None: {
            PocketMonsterParamEnum.NAME: "Ledyba",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.BUG,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.FLYING,
            StatsEnum.HP: 40,
            StatsEnum.ATTACK: 20,
            StatsEnum.DEFENSE: 30,
            StatsEnum.SPECIAL_ATTACK: 40,
            StatsEnum.SPECIAL_DEFENSE: 80,
            StatsEnum.SPEED: 55
        }
    },
    "0166": {
        None: {
            PocketMonsterParamEnum.NAME: "Ledian",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.BUG,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.FLYING,
            StatsEnum.HP: 55,
            StatsEnum.ATTACK: 35,
            StatsEnum.DEFENSE: 50,
            StatsEnum.SPECIAL_ATTACK: 55,
            StatsEnum.SPECIAL_DEFENSE: 110,
            StatsEnum.SPEED: 85
        }
    },
    "0167": {
        None: {
            PocketMonsterParamEnum.NAME: "Spinarak",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.BUG,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.POISON,
            StatsEnum.HP: 40,
            StatsEnum.ATTACK: 60,
            StatsEnum.DEFENSE: 40,
            StatsEnum.SPECIAL_ATTACK: 40,
            StatsEnum.SPECIAL_DEFENSE: 40,
            StatsEnum.SPEED: 30
        }
    },
    "0168": {
        None: {
            PocketMonsterParamEnum.NAME: "Ariados",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.BUG,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.POISON,
            StatsEnum.HP: 70,
            StatsEnum.ATTACK: 90,
            StatsEnum.DEFENSE: 70,
            StatsEnum.SPECIAL_ATTACK: 60,
            StatsEnum.SPECIAL_DEFENSE: 70,
            StatsEnum.SPEED: 40
        }
    },
    "0169": {
        None: {
            PocketMonsterParamEnum.NAME: "Crobat",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.POISON,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.FLYING,
            StatsEnum.HP: 85,
            StatsEnum.ATTACK: 90,
            StatsEnum.DEFENSE: 80,
            StatsEnum.SPECIAL_ATTACK: 70,
            StatsEnum.SPECIAL_DEFENSE: 80,
            StatsEnum.SPEED: 130
        }
    },
    "0170": {
        None: {
            PocketMonsterParamEnum.NAME: "Chinchou",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.WATER,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.ELECTRIC,
            StatsEnum.HP: 75,
            StatsEnum.ATTACK: 38,
            StatsEnum.DEFENSE: 38,
            StatsEnum.SPECIAL_ATTACK: 56,
            StatsEnum.SPECIAL_DEFENSE: 56,
            StatsEnum.SPEED: 67
        }
    },
    "0171": {
        None: {
            PocketMonsterParamEnum.NAME: "Lanturn",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.WATER,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.ELECTRIC,
            StatsEnum.HP: 125,
            StatsEnum.ATTACK: 58,
            StatsEnum.DEFENSE: 58,
            StatsEnum.SPECIAL_ATTACK: 76,
            StatsEnum.SPECIAL_DEFENSE: 76,
            StatsEnum.SPEED: 67
        }
    },
    "0172": {
        None: {
            PocketMonsterParamEnum.NAME: "Pichu",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.ELECTRIC,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 20,
            StatsEnum.ATTACK: 40,
            StatsEnum.DEFENSE: 15,
            StatsEnum.SPECIAL_ATTACK: 35,
            StatsEnum.SPECIAL_DEFENSE: 35,
            StatsEnum.SPEED: 60
        }
    },
    "0173": {
        None: {
            PocketMonsterParamEnum.NAME: "Cleffa",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.FAIRY,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 50,
            StatsEnum.ATTACK: 25,
            StatsEnum.DEFENSE: 28,
            StatsEnum.SPECIAL_ATTACK: 45,
            StatsEnum.SPECIAL_DEFENSE: 55,
            StatsEnum.SPEED: 15
        }
    },
    "0174": {
        None: {
            PocketMonsterParamEnum.NAME: "Igglybuff",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.NORMAL,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.FAIRY,
            StatsEnum.HP: 90,
            StatsEnum.ATTACK: 30,
            StatsEnum.DEFENSE: 15,
            StatsEnum.SPECIAL_ATTACK: 40,
            StatsEnum.SPECIAL_DEFENSE: 20,
            StatsEnum.SPEED: 15
        }
    },
    "0175": {
        None: {
            PocketMonsterParamEnum.NAME: "Togepi",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.FAIRY,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 35,
            StatsEnum.ATTACK: 20,
            StatsEnum.DEFENSE: 65,
            StatsEnum.SPECIAL_ATTACK: 40,
            StatsEnum.SPECIAL_DEFENSE: 65,
            StatsEnum.SPEED: 20
        }
    },
    "0176": {
        None: {
            PocketMonsterParamEnum.NAME: "Togetic",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.FAIRY,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.FLYING,
            StatsEnum.HP: 55,
            StatsEnum.ATTACK: 40,
            StatsEnum.DEFENSE: 85,
            StatsEnum.SPECIAL_ATTACK: 80,
            StatsEnum.SPECIAL_DEFENSE: 105,
            StatsEnum.SPEED: 40
        }
    },
    "0177": {
        None: {
            PocketMonsterParamEnum.NAME: "Natu",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.PSYCHIC,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.FLYING,
            StatsEnum.HP: 40,
            StatsEnum.ATTACK: 50,
            StatsEnum.DEFENSE: 45,
            StatsEnum.SPECIAL_ATTACK: 70,
            StatsEnum.SPECIAL_DEFENSE: 45,
            StatsEnum.SPEED: 70
        }
    },
    "0178": {
        None: {
            PocketMonsterParamEnum.NAME: "Xatu",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.PSYCHIC,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.FLYING,
            StatsEnum.HP: 65,
            StatsEnum.ATTACK: 75,
            StatsEnum.DEFENSE: 70,
            StatsEnum.SPECIAL_ATTACK: 95,
            StatsEnum.SPECIAL_DEFENSE: 70,
            StatsEnum.SPEED: 95
        }
    },
    "0179": {
        None: {
            PocketMonsterParamEnum.NAME: "Mareep",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.ELECTRIC,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 55,
            StatsEnum.ATTACK: 40,
            StatsEnum.DEFENSE: 40,
            StatsEnum.SPECIAL_ATTACK: 65,
            StatsEnum.SPECIAL_DEFENSE: 45,
            StatsEnum.SPEED: 35
        }
    },
    "0180": {
        None: {
            PocketMonsterParamEnum.NAME: "Flaaffy",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.ELECTRIC,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 70,
            StatsEnum.ATTACK: 55,
            StatsEnum.DEFENSE: 55,
            StatsEnum.SPECIAL_ATTACK: 80,
            StatsEnum.SPECIAL_DEFENSE: 60,
            StatsEnum.SPEED: 45
        }
    },
    "0181": {
        None: {
            PocketMonsterParamEnum.NAME: "Ampharos",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.ELECTRIC,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 90,
            StatsEnum.ATTACK: 75,
            StatsEnum.DEFENSE: 85,
            StatsEnum.SPECIAL_ATTACK: 115,
            StatsEnum.SPECIAL_DEFENSE: 90,
            StatsEnum.SPEED: 55
        },
        FormEnum.MEGA: {
            PocketMonsterParamEnum.NAME: "Ampharos",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.ELECTRIC,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.DRAGON,
            StatsEnum.HP: 90,
            StatsEnum.ATTACK: 95,
            StatsEnum.DEFENSE: 105,
            StatsEnum.SPECIAL_ATTACK: 165,
            StatsEnum.SPECIAL_DEFENSE: 110,
            StatsEnum.SPEED: 45
        }
    },
    "0182": {
        None: {
            PocketMonsterParamEnum.NAME: "Bellossom",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.GRASS,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 75,
            StatsEnum.ATTACK: 80,
            StatsEnum.DEFENSE: 95,
            StatsEnum.SPECIAL_ATTACK: 90,
            StatsEnum.SPECIAL_DEFENSE: 100,
            StatsEnum.SPEED: 50
        }
    },
    "0183": {
        None: {
            PocketMonsterParamEnum.NAME: "Marill",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.WATER,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.FAIRY,
            StatsEnum.HP: 70,
            StatsEnum.ATTACK: 20,
            StatsEnum.DEFENSE: 50,
            StatsEnum.SPECIAL_ATTACK: 20,
            StatsEnum.SPECIAL_DEFENSE: 50,
            StatsEnum.SPEED: 40
        }
    },
    "0184": {
        None: {
            PocketMonsterParamEnum.NAME: "Azumarill",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.WATER,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.FAIRY,
            StatsEnum.HP: 100,
            StatsEnum.ATTACK: 50,
            StatsEnum.DEFENSE: 80,
            StatsEnum.SPECIAL_ATTACK: 60,
            StatsEnum.SPECIAL_DEFENSE: 80,
            StatsEnum.SPEED: 50
        }
    },
    "0185": {
        None: {
            PocketMonsterParamEnum.NAME: "Sudowoodo",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.ROCK,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 70,
            StatsEnum.ATTACK: 100,
            StatsEnum.DEFENSE: 115,
            StatsEnum.SPECIAL_ATTACK: 30,
            StatsEnum.SPECIAL_DEFENSE: 65,
            StatsEnum.SPEED: 30
        }
    },
    "0186": {
        None: {
            PocketMonsterParamEnum.NAME: "Politoed",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.WATER,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 90,
            StatsEnum.ATTACK: 75,
            StatsEnum.DEFENSE: 75,
            StatsEnum.SPECIAL_ATTACK: 90,
            StatsEnum.SPECIAL_DEFENSE: 100,
            StatsEnum.SPEED: 70
        }
    },
    "0187": {
        None: {
            PocketMonsterParamEnum.NAME: "Hoppip",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.GRASS,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.FLYING,
            StatsEnum.HP: 35,
            StatsEnum.ATTACK: 35,
            StatsEnum.DEFENSE: 40,
            StatsEnum.SPECIAL_ATTACK: 35,
            StatsEnum.SPECIAL_DEFENSE: 55,
            StatsEnum.SPEED: 50
        }
    },
    "0188": {
        None: {
            PocketMonsterParamEnum.NAME: "Skiploom",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.GRASS,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.FLYING,
            StatsEnum.HP: 55,
            StatsEnum.ATTACK: 45,
            StatsEnum.DEFENSE: 50,
            StatsEnum.SPECIAL_ATTACK: 45,
            StatsEnum.SPECIAL_DEFENSE: 65,
            StatsEnum.SPEED: 80
        }
    },
    "0189": {
        None: {
            PocketMonsterParamEnum.NAME: "Jumpluff",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.GRASS,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.FLYING,
            StatsEnum.HP: 75,
            StatsEnum.ATTACK: 55,
            StatsEnum.DEFENSE: 70,
            StatsEnum.SPECIAL_ATTACK: 55,
            StatsEnum.SPECIAL_DEFENSE: 95,
            StatsEnum.SPEED: 110
        }
    },
    "0190": {
        None: {
            PocketMonsterParamEnum.NAME: "Aipom",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.NORMAL,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 55,
            StatsEnum.ATTACK: 70,
            StatsEnum.DEFENSE: 55,
            StatsEnum.SPECIAL_ATTACK: 40,
            StatsEnum.SPECIAL_DEFENSE: 55,
            StatsEnum.SPEED: 85
        }
    },
    "0191": {
        None: {
            PocketMonsterParamEnum.NAME: "Sunkern",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.GRASS,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 30,
            StatsEnum.ATTACK: 30,
            StatsEnum.DEFENSE: 30,
            StatsEnum.SPECIAL_ATTACK: 30,
            StatsEnum.SPECIAL_DEFENSE: 30,
            StatsEnum.SPEED: 30
        }
    },
    "0192": {
        None: {
            PocketMonsterParamEnum.NAME: "Sunflora",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.GRASS,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 75,
            StatsEnum.ATTACK: 75,
            StatsEnum.DEFENSE: 55,
            StatsEnum.SPECIAL_ATTACK: 105,
            StatsEnum.SPECIAL_DEFENSE: 85,
            StatsEnum.SPEED: 30
        }
    },
    "0193": {
        None: {
            PocketMonsterParamEnum.NAME: "Yanma",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.BUG,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.FLYING,
            StatsEnum.HP: 65,
            StatsEnum.ATTACK: 65,
            StatsEnum.DEFENSE: 45,
            StatsEnum.SPECIAL_ATTACK: 75,
            StatsEnum.SPECIAL_DEFENSE: 45,
            StatsEnum.SPEED: 95
        }
    },
    "0194": {
        None: {
            PocketMonsterParamEnum.NAME: "Wooper",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.WATER,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.GROUND,
            StatsEnum.HP: 55,
            StatsEnum.ATTACK: 45,
            StatsEnum.DEFENSE: 45,
            StatsEnum.SPECIAL_ATTACK: 25,
            StatsEnum.SPECIAL_DEFENSE: 25,
            StatsEnum.SPEED: 15
        },
        FormEnum.PALDEAN: {
            PocketMonsterParamEnum.NAME: "Wooper",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.POISON,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.GROUND,
            StatsEnum.HP: 55,
            StatsEnum.ATTACK: 45,
            StatsEnum.DEFENSE: 45,
            StatsEnum.SPECIAL_ATTACK: 25,
            StatsEnum.SPECIAL_DEFENSE: 25,
            StatsEnum.SPEED: 15
        }
    },
    "0195": {
        None: {
            PocketMonsterParamEnum.NAME: "Quagsire",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.WATER,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.GROUND,
            StatsEnum.HP: 95,
            StatsEnum.ATTACK: 85,
            StatsEnum.DEFENSE: 85,
            StatsEnum.SPECIAL_ATTACK: 65,
            StatsEnum.SPECIAL_DEFENSE: 65,
            StatsEnum.SPEED: 35
        }
    },
    "0196": {
        None: {
            PocketMonsterParamEnum.NAME: "Espeon",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.PSYCHIC,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 65,
            StatsEnum.ATTACK: 65,
            StatsEnum.DEFENSE: 60,
            StatsEnum.SPECIAL_ATTACK: 130,
            StatsEnum.SPECIAL_DEFENSE: 95,
            StatsEnum.SPEED: 110
        }
    },
    "0197": {
        None: {
            PocketMonsterParamEnum.NAME: "Umbreon",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.DARK,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 95,
            StatsEnum.ATTACK: 65,
            StatsEnum.DEFENSE: 110,
            StatsEnum.SPECIAL_ATTACK: 60,
            StatsEnum.SPECIAL_DEFENSE: 130,
            StatsEnum.SPEED: 65
        }
    },
    "0198": {
        None: {
            PocketMonsterParamEnum.NAME: "Murkrow",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.DARK,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.FLYING,
            StatsEnum.HP: 60,
            StatsEnum.ATTACK: 85,
            StatsEnum.DEFENSE: 42,
            StatsEnum.SPECIAL_ATTACK: 85,
            StatsEnum.SPECIAL_DEFENSE: 42,
            StatsEnum.SPEED: 91
        }
    },
    "0199": {
        None: {
            PocketMonsterParamEnum.NAME: "Slowking",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.WATER,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.PSYCHIC,
            StatsEnum.HP: 95,
            StatsEnum.ATTACK: 75,
            StatsEnum.DEFENSE: 80,
            StatsEnum.SPECIAL_ATTACK: 100,
            StatsEnum.SPECIAL_DEFENSE: 110,
            StatsEnum.SPEED: 30
        },
        FormEnum.GALARIAN: {
            PocketMonsterParamEnum.NAME: "Slowking",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.POISON,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.PSYCHIC,
            StatsEnum.HP: 95,
            StatsEnum.ATTACK: 65,
            StatsEnum.DEFENSE: 80,
            StatsEnum.SPECIAL_ATTACK: 110,
            StatsEnum.SPECIAL_DEFENSE: 110,
            StatsEnum.SPEED: 30
        }
    },
    "0200": {
        None: {
            PocketMonsterParamEnum.NAME: "Misdreavus",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.GHOST,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 60,
            StatsEnum.ATTACK: 60,
            StatsEnum.DEFENSE: 60,
            StatsEnum.SPECIAL_ATTACK: 85,
            StatsEnum.SPECIAL_DEFENSE: 85,
            StatsEnum.SPEED: 85
        }
    },
    "0201": {
        None: {
            PocketMonsterParamEnum.NAME: "Unown",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.PSYCHIC,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 48,
            StatsEnum.ATTACK: 72,
            StatsEnum.DEFENSE: 48,
            StatsEnum.SPECIAL_ATTACK: 72,
            StatsEnum.SPECIAL_DEFENSE: 48,
            StatsEnum.SPEED: 48
        }
    },
    "0202": {
        None: {
            PocketMonsterParamEnum.NAME: "Wobbuffet",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.PSYCHIC,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 190,
            StatsEnum.ATTACK: 33,
            StatsEnum.DEFENSE: 58,
            StatsEnum.SPECIAL_ATTACK: 33,
            StatsEnum.SPECIAL_DEFENSE: 58,
            StatsEnum.SPEED: 33
        }
    },
    "0203": {
        None: {
            PocketMonsterParamEnum.NAME: "Girafarig",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.NORMAL,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.PSYCHIC,
            StatsEnum.HP: 70,
            StatsEnum.ATTACK: 80,
            StatsEnum.DEFENSE: 65,
            StatsEnum.SPECIAL_ATTACK: 90,
            StatsEnum.SPECIAL_DEFENSE: 65,
            StatsEnum.SPEED: 85
        }
    },
    "0204": {
        None: {
            PocketMonsterParamEnum.NAME: "Pineco",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.BUG,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 50,
            StatsEnum.ATTACK: 65,
            StatsEnum.DEFENSE: 90,
            StatsEnum.SPECIAL_ATTACK: 35,
            StatsEnum.SPECIAL_DEFENSE: 35,
            StatsEnum.SPEED: 15
        }
    },
    "0205": {
        None: {
            PocketMonsterParamEnum.NAME: "Forretress",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.BUG,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.STEEL,
            StatsEnum.HP: 75,
            StatsEnum.ATTACK: 90,
            StatsEnum.DEFENSE: 140,
            StatsEnum.SPECIAL_ATTACK: 60,
            StatsEnum.SPECIAL_DEFENSE: 60,
            StatsEnum.SPEED: 40
        }
    },
    "0206": {
        None: {
            PocketMonsterParamEnum.NAME: "Dunsparce",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.NORMAL,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 100,
            StatsEnum.ATTACK: 70,
            StatsEnum.DEFENSE: 70,
            StatsEnum.SPECIAL_ATTACK: 65,
            StatsEnum.SPECIAL_DEFENSE: 65,
            StatsEnum.SPEED: 45
        }
    },
    "0207": {
        None: {
            PocketMonsterParamEnum.NAME: "Gligar",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.GROUND,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.FLYING,
            StatsEnum.HP: 65,
            StatsEnum.ATTACK: 75,
            StatsEnum.DEFENSE: 105,
            StatsEnum.SPECIAL_ATTACK: 35,
            StatsEnum.SPECIAL_DEFENSE: 65,
            StatsEnum.SPEED: 85
        }
    },
    "0208": {
        None: {
            PocketMonsterParamEnum.NAME: "Steelix",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.STEEL,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.GROUND,
            StatsEnum.HP: 75,
            StatsEnum.ATTACK: 85,
            StatsEnum.DEFENSE: 200,
            StatsEnum.SPECIAL_ATTACK: 55,
            StatsEnum.SPECIAL_DEFENSE: 65,
            StatsEnum.SPEED: 30
        },
        FormEnum.MEGA: {
            PocketMonsterParamEnum.NAME: "Steelix",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.STEEL,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.GROUND,
            StatsEnum.HP: 75,
            StatsEnum.ATTACK: 125,
            StatsEnum.DEFENSE: 230,
            StatsEnum.SPECIAL_ATTACK: 55,
            StatsEnum.SPECIAL_DEFENSE: 95,
            StatsEnum.SPEED: 30
        }
    },
    "0209": {
        None: {
            PocketMonsterParamEnum.NAME: "Snubbull",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.FAIRY,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 60,
            StatsEnum.ATTACK: 80,
            StatsEnum.DEFENSE: 50,
            StatsEnum.SPECIAL_ATTACK: 40,
            StatsEnum.SPECIAL_DEFENSE: 40,
            StatsEnum.SPEED: 30
        }
    },
    "0210": {
        None: {
            PocketMonsterParamEnum.NAME: "Granbull",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.FAIRY,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 90,
            StatsEnum.ATTACK: 120,
            StatsEnum.DEFENSE: 75,
            StatsEnum.SPECIAL_ATTACK: 60,
            StatsEnum.SPECIAL_DEFENSE: 60,
            StatsEnum.SPEED: 45
        }
    },
    "0211": {
        None: {
            PocketMonsterParamEnum.NAME: "Qwilfish",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.WATER,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.POISON,
            StatsEnum.HP: 65,
            StatsEnum.ATTACK: 95,
            StatsEnum.DEFENSE: 85,
            StatsEnum.SPECIAL_ATTACK: 55,
            StatsEnum.SPECIAL_DEFENSE: 55,
            StatsEnum.SPEED: 85
        },
        FormEnum.HISUIAN: {
            PocketMonsterParamEnum.NAME: "Qwilfish",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.DARK,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.POISON,
            StatsEnum.HP: 65,
            StatsEnum.ATTACK: 95,
            StatsEnum.DEFENSE: 85,
            StatsEnum.SPECIAL_ATTACK: 55,
            StatsEnum.SPECIAL_DEFENSE: 55,
            StatsEnum.SPEED: 85
        }
    },
    "0212": {
        None: {
            PocketMonsterParamEnum.NAME: "Scizor",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.BUG,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.STEEL,
            StatsEnum.HP: 70,
            StatsEnum.ATTACK: 130,
            StatsEnum.DEFENSE: 100,
            StatsEnum.SPECIAL_ATTACK: 55,
            StatsEnum.SPECIAL_DEFENSE: 80,
            StatsEnum.SPEED: 65
        },
        FormEnum.MEGA: {
            PocketMonsterParamEnum.NAME: "Scizor",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.BUG,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.STEEL,
            StatsEnum.HP: 70,
            StatsEnum.ATTACK: 150,
            StatsEnum.DEFENSE: 140,
            StatsEnum.SPECIAL_ATTACK: 65,
            StatsEnum.SPECIAL_DEFENSE: 100,
            StatsEnum.SPEED: 75
        }
    },
    "0213": {
        None: {
            PocketMonsterParamEnum.NAME: "Shuckle",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.BUG,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.ROCK,
            StatsEnum.HP: 20,
            StatsEnum.ATTACK: 10,
            StatsEnum.DEFENSE: 230,
            StatsEnum.SPECIAL_ATTACK: 10,
            StatsEnum.SPECIAL_DEFENSE: 230,
            StatsEnum.SPEED: 5
        }
    },
    "0214": {
        None: {
            PocketMonsterParamEnum.NAME: "Heracross",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.BUG,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.FIGHTING,
            StatsEnum.HP: 80,
            StatsEnum.ATTACK: 125,
            StatsEnum.DEFENSE: 75,
            StatsEnum.SPECIAL_ATTACK: 40,
            StatsEnum.SPECIAL_DEFENSE: 95,
            StatsEnum.SPEED: 85
        },
        FormEnum.MEGA: {
            PocketMonsterParamEnum.NAME: "Heracross",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.BUG,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.FIGHTING,
            StatsEnum.HP: 80,
            StatsEnum.ATTACK: 185,
            StatsEnum.DEFENSE: 115,
            StatsEnum.SPECIAL_ATTACK: 40,
            StatsEnum.SPECIAL_DEFENSE: 105,
            StatsEnum.SPEED: 75
        }
    },
    "0215": {
        None: {
            PocketMonsterParamEnum.NAME: "Sneasel",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.DARK,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.ICE,
            StatsEnum.HP: 55,
            StatsEnum.ATTACK: 95,
            StatsEnum.DEFENSE: 55,
            StatsEnum.SPECIAL_ATTACK: 35,
            StatsEnum.SPECIAL_DEFENSE: 75,
            StatsEnum.SPEED: 115
        },
        FormEnum.HISUIAN: {
            PocketMonsterParamEnum.NAME: "Sneasel",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.FIGHTING,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.POISON,
            StatsEnum.HP: 55,
            StatsEnum.ATTACK: 95,
            StatsEnum.DEFENSE: 55,
            StatsEnum.SPECIAL_ATTACK: 35,
            StatsEnum.SPECIAL_DEFENSE: 75,
            StatsEnum.SPEED: 115
        }
    },
    "0216": {
        None: {
            PocketMonsterParamEnum.NAME: "Teddiursa",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.NORMAL,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 60,
            StatsEnum.ATTACK: 80,
            StatsEnum.DEFENSE: 50,
            StatsEnum.SPECIAL_ATTACK: 50,
            StatsEnum.SPECIAL_DEFENSE: 50,
            StatsEnum.SPEED: 40
        }
    },
    "0217": {
        None: {
            PocketMonsterParamEnum.NAME: "Ursaring",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.NORMAL,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 90,
            StatsEnum.ATTACK: 130,
            StatsEnum.DEFENSE: 75,
            StatsEnum.SPECIAL_ATTACK: 75,
            StatsEnum.SPECIAL_DEFENSE: 75,
            StatsEnum.SPEED: 55
        }
    },
    "0218": {
        None: {
            PocketMonsterParamEnum.NAME: "Slugma",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.FIRE,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 40,
            StatsEnum.ATTACK: 40,
            StatsEnum.DEFENSE: 40,
            StatsEnum.SPECIAL_ATTACK: 70,
            StatsEnum.SPECIAL_DEFENSE: 40,
            StatsEnum.SPEED: 20
        }
    },
    "0219": {
        None: {
            PocketMonsterParamEnum.NAME: "Magcargo",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.FIRE,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.ROCK,
            StatsEnum.HP: 60,
            StatsEnum.ATTACK: 50,
            StatsEnum.DEFENSE: 120,
            StatsEnum.SPECIAL_ATTACK: 90,
            StatsEnum.SPECIAL_DEFENSE: 80,
            StatsEnum.SPEED: 30
        }
    },
    "0220": {
        None: {
            PocketMonsterParamEnum.NAME: "Swinub",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.ICE,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.GROUND,
            StatsEnum.HP: 50,
            StatsEnum.ATTACK: 50,
            StatsEnum.DEFENSE: 40,
            StatsEnum.SPECIAL_ATTACK: 30,
            StatsEnum.SPECIAL_DEFENSE: 30,
            StatsEnum.SPEED: 50
        }
    },
    "0221": {
        None: {
            PocketMonsterParamEnum.NAME: "Piloswine",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.ICE,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.GROUND,
            StatsEnum.HP: 100,
            StatsEnum.ATTACK: 100,
            StatsEnum.DEFENSE: 80,
            StatsEnum.SPECIAL_ATTACK: 60,
            StatsEnum.SPECIAL_DEFENSE: 60,
            StatsEnum.SPEED: 50
        }
    },
    "0222": {
        None: {
            PocketMonsterParamEnum.NAME: "Corsola",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.WATER,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.ROCK,
            StatsEnum.HP: 65,
            StatsEnum.ATTACK: 55,
            StatsEnum.DEFENSE: 95,
            StatsEnum.SPECIAL_ATTACK: 65,
            StatsEnum.SPECIAL_DEFENSE: 95,
            StatsEnum.SPEED: 35
        },
        FormEnum.GALARIAN: {
            PocketMonsterParamEnum.NAME: "Corsola",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.GHOST,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 60,
            StatsEnum.ATTACK: 55,
            StatsEnum.DEFENSE: 100,
            StatsEnum.SPECIAL_ATTACK: 65,
            StatsEnum.SPECIAL_DEFENSE: 100,
            StatsEnum.SPEED: 30
        }
    },
    "0223": {
        None: {
            PocketMonsterParamEnum.NAME: "Remoraid",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.WATER,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 35,
            StatsEnum.ATTACK: 65,
            StatsEnum.DEFENSE: 35,
            StatsEnum.SPECIAL_ATTACK: 65,
            StatsEnum.SPECIAL_DEFENSE: 35,
            StatsEnum.SPEED: 65
        }
    },
    "0224": {
        None: {
            PocketMonsterParamEnum.NAME: "Octillery",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.WATER,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 75,
            StatsEnum.ATTACK: 105,
            StatsEnum.DEFENSE: 75,
            StatsEnum.SPECIAL_ATTACK: 105,
            StatsEnum.SPECIAL_DEFENSE: 75,
            StatsEnum.SPEED: 45
        }
    },
    "0225": {
        None: {
            PocketMonsterParamEnum.NAME: "Delibird",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.ICE,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.FLYING,
            StatsEnum.HP: 45,
            StatsEnum.ATTACK: 55,
            StatsEnum.DEFENSE: 45,
            StatsEnum.SPECIAL_ATTACK: 65,
            StatsEnum.SPECIAL_DEFENSE: 45,
            StatsEnum.SPEED: 75
        }
    },
    "0226": {
        None: {
            PocketMonsterParamEnum.NAME: "Mantine",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.WATER,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.FLYING,
            StatsEnum.HP: 85,
            StatsEnum.ATTACK: 40,
            StatsEnum.DEFENSE: 70,
            StatsEnum.SPECIAL_ATTACK: 80,
            StatsEnum.SPECIAL_DEFENSE: 140,
            StatsEnum.SPEED: 70
        }
    },
    "0227": {
        None: {
            PocketMonsterParamEnum.NAME: "Skarmory",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.STEEL,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.FLYING,
            StatsEnum.HP: 65,
            StatsEnum.ATTACK: 80,
            StatsEnum.DEFENSE: 140,
            StatsEnum.SPECIAL_ATTACK: 40,
            StatsEnum.SPECIAL_DEFENSE: 70,
            StatsEnum.SPEED: 70
        }
    },
    "0228": {
        None: {
            PocketMonsterParamEnum.NAME: "Houndour",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.DARK,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.FIRE,
            StatsEnum.HP: 45,
            StatsEnum.ATTACK: 60,
            StatsEnum.DEFENSE: 30,
            StatsEnum.SPECIAL_ATTACK: 80,
            StatsEnum.SPECIAL_DEFENSE: 50,
            StatsEnum.SPEED: 65
        }
    },
    "0229": {
        None: {
            PocketMonsterParamEnum.NAME: "Houndoom",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.DARK,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.FIRE,
            StatsEnum.HP: 75,
            StatsEnum.ATTACK: 90,
            StatsEnum.DEFENSE: 50,
            StatsEnum.SPECIAL_ATTACK: 110,
            StatsEnum.SPECIAL_DEFENSE: 80,
            StatsEnum.SPEED: 95
        },
        FormEnum.MEGA: {
            PocketMonsterParamEnum.NAME: "Houndoom",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.DARK,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.FIRE,
            StatsEnum.HP: 75,
            StatsEnum.ATTACK: 90,
            StatsEnum.DEFENSE: 90,
            StatsEnum.SPECIAL_ATTACK: 140,
            StatsEnum.SPECIAL_DEFENSE: 90,
            StatsEnum.SPEED: 115
        }
    },
    "0230": {
        None: {
            PocketMonsterParamEnum.NAME: "Kingdra",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.WATER,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.DRAGON,
            StatsEnum.HP: 75,
            StatsEnum.ATTACK: 95,
            StatsEnum.DEFENSE: 95,
            StatsEnum.SPECIAL_ATTACK: 95,
            StatsEnum.SPECIAL_DEFENSE: 95,
            StatsEnum.SPEED: 85
        }
    },
    "0231": {
        None: {
            PocketMonsterParamEnum.NAME: "Phanpy",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.GROUND,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 90,
            StatsEnum.ATTACK: 60,
            StatsEnum.DEFENSE: 60,
            StatsEnum.SPECIAL_ATTACK: 40,
            StatsEnum.SPECIAL_DEFENSE: 40,
            StatsEnum.SPEED: 40
        }
    },
    "0232": {
        None: {
            PocketMonsterParamEnum.NAME: "Donphan",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.GROUND,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 90,
            StatsEnum.ATTACK: 120,
            StatsEnum.DEFENSE: 120,
            StatsEnum.SPECIAL_ATTACK: 60,
            StatsEnum.SPECIAL_DEFENSE: 60,
            StatsEnum.SPEED: 50
        }
    },
    "0233": {
        None: {
            PocketMonsterParamEnum.NAME: "Porygon2",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.NORMAL,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 85,
            StatsEnum.ATTACK: 80,
            StatsEnum.DEFENSE: 90,
            StatsEnum.SPECIAL_ATTACK: 105,
            StatsEnum.SPECIAL_DEFENSE: 95,
            StatsEnum.SPEED: 60
        }
    },
    "0234": {
        None: {
            PocketMonsterParamEnum.NAME: "Stantler",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.NORMAL,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 73,
            StatsEnum.ATTACK: 95,
            StatsEnum.DEFENSE: 62,
            StatsEnum.SPECIAL_ATTACK: 85,
            StatsEnum.SPECIAL_DEFENSE: 65,
            StatsEnum.SPEED: 85
        }
    },
    "0235": {
        None: {
            PocketMonsterParamEnum.NAME: "Smeargle",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.NORMAL,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 55,
            StatsEnum.ATTACK: 20,
            StatsEnum.DEFENSE: 35,
            StatsEnum.SPECIAL_ATTACK: 20,
            StatsEnum.SPECIAL_DEFENSE: 45,
            StatsEnum.SPEED: 75
        }
    },
    "0236": {
        None: {
            PocketMonsterParamEnum.NAME: "Tyrogue",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.FIGHTING,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 35,
            StatsEnum.ATTACK: 35,
            StatsEnum.DEFENSE: 35,
            StatsEnum.SPECIAL_ATTACK: 35,
            StatsEnum.SPECIAL_DEFENSE: 35,
            StatsEnum.SPEED: 35
        }
    },
    "0237": {
        None: {
            PocketMonsterParamEnum.NAME: "Hitmontop",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.FIGHTING,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 50,
            StatsEnum.ATTACK: 95,
            StatsEnum.DEFENSE: 95,
            StatsEnum.SPECIAL_ATTACK: 35,
            StatsEnum.SPECIAL_DEFENSE: 110,
            StatsEnum.SPEED: 70
        }
    },
    "0238": {
        None: {
            PocketMonsterParamEnum.NAME: "Smoochum",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.ICE,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.PSYCHIC,
            StatsEnum.HP: 45,
            StatsEnum.ATTACK: 30,
            StatsEnum.DEFENSE: 15,
            StatsEnum.SPECIAL_ATTACK: 85,
            StatsEnum.SPECIAL_DEFENSE: 65,
            StatsEnum.SPEED: 65
        }
    },
    "0239": {
        None: {
            PocketMonsterParamEnum.NAME: "Elekid",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.ELECTRIC,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 45,
            StatsEnum.ATTACK: 63,
            StatsEnum.DEFENSE: 37,
            StatsEnum.SPECIAL_ATTACK: 65,
            StatsEnum.SPECIAL_DEFENSE: 55,
            StatsEnum.SPEED: 95
        }
    },
    "0240": {
        None: {
            PocketMonsterParamEnum.NAME: "Magby",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.FIRE,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 45,
            StatsEnum.ATTACK: 75,
            StatsEnum.DEFENSE: 37,
            StatsEnum.SPECIAL_ATTACK: 70,
            StatsEnum.SPECIAL_DEFENSE: 55,
            StatsEnum.SPEED: 83
        }
    },
    "0241": {
        None: {
            PocketMonsterParamEnum.NAME: "Miltank",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.NORMAL,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 95,
            StatsEnum.ATTACK: 80,
            StatsEnum.DEFENSE: 105,
            StatsEnum.SPECIAL_ATTACK: 40,
            StatsEnum.SPECIAL_DEFENSE: 70,
            StatsEnum.SPEED: 100
        }
    },
    "0242": {
        None: {
            PocketMonsterParamEnum.NAME: "Blissey",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.NORMAL,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 255,
            StatsEnum.ATTACK: 10,
            StatsEnum.DEFENSE: 10,
            StatsEnum.SPECIAL_ATTACK: 75,
            StatsEnum.SPECIAL_DEFENSE: 135,
            StatsEnum.SPEED: 55
        }
    },
    "0243": {
        None: {
            PocketMonsterParamEnum.NAME: "Raikou",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.ELECTRIC,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 90,
            StatsEnum.ATTACK: 85,
            StatsEnum.DEFENSE: 75,
            StatsEnum.SPECIAL_ATTACK: 115,
            StatsEnum.SPECIAL_DEFENSE: 100,
            StatsEnum.SPEED: 115
        }
    },
    "0244": {
        None: {
            PocketMonsterParamEnum.NAME: "Entei",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.FIRE,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 115,
            StatsEnum.ATTACK: 115,
            StatsEnum.DEFENSE: 85,
            StatsEnum.SPECIAL_ATTACK: 90,
            StatsEnum.SPECIAL_DEFENSE: 75,
            StatsEnum.SPEED: 100
        }
    },
    "0245": {
        None: {
            PocketMonsterParamEnum.NAME: "Suicune",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.WATER,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 100,
            StatsEnum.ATTACK: 75,
            StatsEnum.DEFENSE: 115,
            StatsEnum.SPECIAL_ATTACK: 90,
            StatsEnum.SPECIAL_DEFENSE: 115,
            StatsEnum.SPEED: 85
        }
    },
    "0246": {
        None: {
            PocketMonsterParamEnum.NAME: "Larvitar",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.ROCK,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.GROUND,
            StatsEnum.HP: 50,
            StatsEnum.ATTACK: 64,
            StatsEnum.DEFENSE: 50,
            StatsEnum.SPECIAL_ATTACK: 45,
            StatsEnum.SPECIAL_DEFENSE: 50,
            StatsEnum.SPEED: 41
        }
    },
    "0247": {
        None: {
            PocketMonsterParamEnum.NAME: "Pupitar",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.ROCK,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.GROUND,
            StatsEnum.HP: 70,
            StatsEnum.ATTACK: 84,
            StatsEnum.DEFENSE: 70,
            StatsEnum.SPECIAL_ATTACK: 65,
            StatsEnum.SPECIAL_DEFENSE: 70,
            StatsEnum.SPEED: 51
        }
    },
    "0248": {
        None: {
            PocketMonsterParamEnum.NAME: "Tyranitar",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.ROCK,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.DARK,
            StatsEnum.HP: 100,
            StatsEnum.ATTACK: 134,
            StatsEnum.DEFENSE: 110,
            StatsEnum.SPECIAL_ATTACK: 95,
            StatsEnum.SPECIAL_DEFENSE: 100,
            StatsEnum.SPEED: 61
        },
        FormEnum.MEGA: {
            PocketMonsterParamEnum.NAME: "Tyranitar",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.ROCK,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.DARK,
            StatsEnum.HP: 100,
            StatsEnum.ATTACK: 164,
            StatsEnum.DEFENSE: 150,
            StatsEnum.SPECIAL_ATTACK: 95,
            StatsEnum.SPECIAL_DEFENSE: 120,
            StatsEnum.SPEED: 71
        }
    },
    "0249": {
        None: {
            PocketMonsterParamEnum.NAME: "Lugia",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.PSYCHIC,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.FLYING,
            StatsEnum.HP: 106,
            StatsEnum.ATTACK: 90,
            StatsEnum.DEFENSE: 130,
            StatsEnum.SPECIAL_ATTACK: 90,
            StatsEnum.SPECIAL_DEFENSE: 154,
            StatsEnum.SPEED: 110
        }
    },
    "0250": {
        None: {
            PocketMonsterParamEnum.NAME: "Ho-oh",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.FIRE,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.FLYING,
            StatsEnum.HP: 106,
            StatsEnum.ATTACK: 130,
            StatsEnum.DEFENSE: 90,
            StatsEnum.SPECIAL_ATTACK: 110,
            StatsEnum.SPECIAL_DEFENSE: 154,
            StatsEnum.SPEED: 90
        }
    },
    "0251": {
        None: {
            PocketMonsterParamEnum.NAME: "Celebi",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.PSYCHIC,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.GRASS,
            StatsEnum.HP: 100,
            StatsEnum.ATTACK: 100,
            StatsEnum.DEFENSE: 100,
            StatsEnum.SPECIAL_ATTACK: 100,
            StatsEnum.SPECIAL_DEFENSE: 100,
            StatsEnum.SPEED: 100
        }
    },
    "0252": {
        None: {
            PocketMonsterParamEnum.NAME: "Treecko",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.GRASS,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 40,
            StatsEnum.ATTACK: 45,
            StatsEnum.DEFENSE: 35,
            StatsEnum.SPECIAL_ATTACK: 65,
            StatsEnum.SPECIAL_DEFENSE: 55,
            StatsEnum.SPEED: 70
        }
    },
    "0253": {
        None: {
            PocketMonsterParamEnum.NAME: "Grovyle",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.GRASS,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 50,
            StatsEnum.ATTACK: 65,
            StatsEnum.DEFENSE: 45,
            StatsEnum.SPECIAL_ATTACK: 85,
            StatsEnum.SPECIAL_DEFENSE: 65,
            StatsEnum.SPEED: 95
        }
    },
    "0254": {
        None: {
            PocketMonsterParamEnum.NAME: "Sceptile",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.GRASS,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 70,
            StatsEnum.ATTACK: 85,
            StatsEnum.DEFENSE: 65,
            StatsEnum.SPECIAL_ATTACK: 105,
            StatsEnum.SPECIAL_DEFENSE: 85,
            StatsEnum.SPEED: 120
        },
        FormEnum.MEGA: {
            PocketMonsterParamEnum.NAME: "Sceptile",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.GRASS,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.DRAGON,
            StatsEnum.HP: 70,
            StatsEnum.ATTACK: 110,
            StatsEnum.DEFENSE: 75,
            StatsEnum.SPECIAL_ATTACK: 145,
            StatsEnum.SPECIAL_DEFENSE: 85,
            StatsEnum.SPEED: 145
        }
    },
    "0255": {
        None: {
            PocketMonsterParamEnum.NAME: "Torchic",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.FIRE,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 45,
            StatsEnum.ATTACK: 60,
            StatsEnum.DEFENSE: 40,
            StatsEnum.SPECIAL_ATTACK: 70,
            StatsEnum.SPECIAL_DEFENSE: 50,
            StatsEnum.SPEED: 45
        }
    },
    "0256": {
        None: {
            PocketMonsterParamEnum.NAME: "Combusken",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.FIRE,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.FIGHTING,
            StatsEnum.HP: 60,
            StatsEnum.ATTACK: 85,
            StatsEnum.DEFENSE: 60,
            StatsEnum.SPECIAL_ATTACK: 85,
            StatsEnum.SPECIAL_DEFENSE: 60,
            StatsEnum.SPEED: 55
        }
    },
    "0257": {
        None: {
            PocketMonsterParamEnum.NAME: "Blaziken",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.FIRE,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.FIGHTING,
            StatsEnum.HP: 80,
            StatsEnum.ATTACK: 120,
            StatsEnum.DEFENSE: 70,
            StatsEnum.SPECIAL_ATTACK: 110,
            StatsEnum.SPECIAL_DEFENSE: 70,
            StatsEnum.SPEED: 80
        },
        FormEnum.MEGA: {
            PocketMonsterParamEnum.NAME: "Blaziken",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.FIRE,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.FIGHTING,
            StatsEnum.HP: 80,
            StatsEnum.ATTACK: 160,
            StatsEnum.DEFENSE: 80,
            StatsEnum.SPECIAL_ATTACK: 130,
            StatsEnum.SPECIAL_DEFENSE: 80,
            StatsEnum.SPEED: 100
        }
    },
    "0258": {
        None: {
            PocketMonsterParamEnum.NAME: "Mudkip",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.WATER,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 50,
            StatsEnum.ATTACK: 70,
            StatsEnum.DEFENSE: 50,
            StatsEnum.SPECIAL_ATTACK: 50,
            StatsEnum.SPECIAL_DEFENSE: 50,
            StatsEnum.SPEED: 40
        }
    },
    "0259": {
        None: {
            PocketMonsterParamEnum.NAME: "Marshtomp",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.WATER,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.GROUND,
            StatsEnum.HP: 70,
            StatsEnum.ATTACK: 85,
            StatsEnum.DEFENSE: 70,
            StatsEnum.SPECIAL_ATTACK: 60,
            StatsEnum.SPECIAL_DEFENSE: 70,
            StatsEnum.SPEED: 50
        }
    },
    "0260": {
        None: {
            PocketMonsterParamEnum.NAME: "Swampert",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.WATER,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.GROUND,
            StatsEnum.HP: 100,
            StatsEnum.ATTACK: 110,
            StatsEnum.DEFENSE: 90,
            StatsEnum.SPECIAL_ATTACK: 85,
            StatsEnum.SPECIAL_DEFENSE: 90,
            StatsEnum.SPEED: 60
        },
        FormEnum.MEGA: {
            PocketMonsterParamEnum.NAME: "Swampert",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.WATER,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.GROUND,
            StatsEnum.HP: 100,
            StatsEnum.ATTACK: 150,
            StatsEnum.DEFENSE: 110,
            StatsEnum.SPECIAL_ATTACK: 95,
            StatsEnum.SPECIAL_DEFENSE: 110,
            StatsEnum.SPEED: 70
        }
    },
    "0261": {
        None: {
            PocketMonsterParamEnum.NAME: "Poochyena",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.DARK,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 35,
            StatsEnum.ATTACK: 55,
            StatsEnum.DEFENSE: 35,
            StatsEnum.SPECIAL_ATTACK: 30,
            StatsEnum.SPECIAL_DEFENSE: 30,
            StatsEnum.SPEED: 35
        }
    },
    "0262": {
        None: {
            PocketMonsterParamEnum.NAME: "Mightyena",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.DARK,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 70,
            StatsEnum.ATTACK: 90,
            StatsEnum.DEFENSE: 70,
            StatsEnum.SPECIAL_ATTACK: 60,
            StatsEnum.SPECIAL_DEFENSE: 60,
            StatsEnum.SPEED: 70
        }
    },
    "0263": {
        None: {
            PocketMonsterParamEnum.NAME: "Zigzagoon",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.NORMAL,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 38,
            StatsEnum.ATTACK: 30,
            StatsEnum.DEFENSE: 41,
            StatsEnum.SPECIAL_ATTACK: 30,
            StatsEnum.SPECIAL_DEFENSE: 41,
            StatsEnum.SPEED: 60
        },
        FormEnum.GALARIAN: {
            PocketMonsterParamEnum.NAME: "Zigzagoon",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.DARK,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.NORMAL,
            StatsEnum.HP: 38,
            StatsEnum.ATTACK: 30,
            StatsEnum.DEFENSE: 41,
            StatsEnum.SPECIAL_ATTACK: 30,
            StatsEnum.SPECIAL_DEFENSE: 41,
            StatsEnum.SPEED: 60
        }
    },
    "0264": {
        None: {
            PocketMonsterParamEnum.NAME: "Linoone",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.NORMAL,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 78,
            StatsEnum.ATTACK: 70,
            StatsEnum.DEFENSE: 61,
            StatsEnum.SPECIAL_ATTACK: 50,
            StatsEnum.SPECIAL_DEFENSE: 61,
            StatsEnum.SPEED: 100
        },
        FormEnum.GALARIAN: {
            PocketMonsterParamEnum.NAME: "Linoone",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.DARK,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.NORMAL,
            StatsEnum.HP: 78,
            StatsEnum.ATTACK: 70,
            StatsEnum.DEFENSE: 61,
            StatsEnum.SPECIAL_ATTACK: 50,
            StatsEnum.SPECIAL_DEFENSE: 61,
            StatsEnum.SPEED: 100
        }
    },
    "0265": {
        None: {
            PocketMonsterParamEnum.NAME: "Wurmple",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.BUG,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 45,
            StatsEnum.ATTACK: 45,
            StatsEnum.DEFENSE: 35,
            StatsEnum.SPECIAL_ATTACK: 20,
            StatsEnum.SPECIAL_DEFENSE: 30,
            StatsEnum.SPEED: 20
        }
    },
    "0266": {
        None: {
            PocketMonsterParamEnum.NAME: "Silcoon",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.BUG,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 50,
            StatsEnum.ATTACK: 35,
            StatsEnum.DEFENSE: 55,
            StatsEnum.SPECIAL_ATTACK: 25,
            StatsEnum.SPECIAL_DEFENSE: 25,
            StatsEnum.SPEED: 15
        }
    },
    "0267": {
        None: {
            PocketMonsterParamEnum.NAME: "Beautifly",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.BUG,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.FLYING,
            StatsEnum.HP: 60,
            StatsEnum.ATTACK: 70,
            StatsEnum.DEFENSE: 50,
            StatsEnum.SPECIAL_ATTACK: 100,
            StatsEnum.SPECIAL_DEFENSE: 50,
            StatsEnum.SPEED: 65
        }
    },
    "0268": {
        None: {
            PocketMonsterParamEnum.NAME: "Cascoon",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.BUG,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 50,
            StatsEnum.ATTACK: 35,
            StatsEnum.DEFENSE: 55,
            StatsEnum.SPECIAL_ATTACK: 25,
            StatsEnum.SPECIAL_DEFENSE: 25,
            StatsEnum.SPEED: 15
        }
    },
    "0269": {
        None: {
            PocketMonsterParamEnum.NAME: "Dustox",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.BUG,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.POISON,
            StatsEnum.HP: 60,
            StatsEnum.ATTACK: 50,
            StatsEnum.DEFENSE: 70,
            StatsEnum.SPECIAL_ATTACK: 50,
            StatsEnum.SPECIAL_DEFENSE: 90,
            StatsEnum.SPEED: 65
        }
    },
    "0270": {
        None: {
            PocketMonsterParamEnum.NAME: "Lotad",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.WATER,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.GRASS,
            StatsEnum.HP: 40,
            StatsEnum.ATTACK: 30,
            StatsEnum.DEFENSE: 30,
            StatsEnum.SPECIAL_ATTACK: 40,
            StatsEnum.SPECIAL_DEFENSE: 50,
            StatsEnum.SPEED: 30
        }
    },
    "0271": {
        None: {
            PocketMonsterParamEnum.NAME: "Lombre",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.WATER,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.GRASS,
            StatsEnum.HP: 60,
            StatsEnum.ATTACK: 50,
            StatsEnum.DEFENSE: 50,
            StatsEnum.SPECIAL_ATTACK: 60,
            StatsEnum.SPECIAL_DEFENSE: 70,
            StatsEnum.SPEED: 50
        }
    },
    "0272": {
        None: {
            PocketMonsterParamEnum.NAME: "Ludicolo",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.WATER,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.GRASS,
            StatsEnum.HP: 80,
            StatsEnum.ATTACK: 70,
            StatsEnum.DEFENSE: 70,
            StatsEnum.SPECIAL_ATTACK: 90,
            StatsEnum.SPECIAL_DEFENSE: 100,
            StatsEnum.SPEED: 70
        }
    },
    "0273": {
        None: {
            PocketMonsterParamEnum.NAME: "Seedot",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.GRASS,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 40,
            StatsEnum.ATTACK: 40,
            StatsEnum.DEFENSE: 50,
            StatsEnum.SPECIAL_ATTACK: 30,
            StatsEnum.SPECIAL_DEFENSE: 30,
            StatsEnum.SPEED: 30
        }
    },
    "0274": {
        None: {
            PocketMonsterParamEnum.NAME: "Nuzleaf",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.GRASS,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.DARK,
            StatsEnum.HP: 70,
            StatsEnum.ATTACK: 70,
            StatsEnum.DEFENSE: 40,
            StatsEnum.SPECIAL_ATTACK: 60,
            StatsEnum.SPECIAL_DEFENSE: 40,
            StatsEnum.SPEED: 60
        }
    },
    "0275": {
        None: {
            PocketMonsterParamEnum.NAME: "Shiftry",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.GRASS,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.DARK,
            StatsEnum.HP: 90,
            StatsEnum.ATTACK: 100,
            StatsEnum.DEFENSE: 60,
            StatsEnum.SPECIAL_ATTACK: 90,
            StatsEnum.SPECIAL_DEFENSE: 60,
            StatsEnum.SPEED: 80
        }
    },
    "0276": {
        None: {
            PocketMonsterParamEnum.NAME: "Taillow",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.NORMAL,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.FLYING,
            StatsEnum.HP: 40,
            StatsEnum.ATTACK: 55,
            StatsEnum.DEFENSE: 30,
            StatsEnum.SPECIAL_ATTACK: 30,
            StatsEnum.SPECIAL_DEFENSE: 30,
            StatsEnum.SPEED: 85
        }
    },
    "0277": {
        None: {
            PocketMonsterParamEnum.NAME: "Swellow",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.NORMAL,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.FLYING,
            StatsEnum.HP: 60,
            StatsEnum.ATTACK: 85,
            StatsEnum.DEFENSE: 60,
            StatsEnum.SPECIAL_ATTACK: 75,
            StatsEnum.SPECIAL_DEFENSE: 50,
            StatsEnum.SPEED: 125
        }
    },
    "0278": {
        None: {
            PocketMonsterParamEnum.NAME: "Wingull",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.WATER,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.FLYING,
            StatsEnum.HP: 40,
            StatsEnum.ATTACK: 30,
            StatsEnum.DEFENSE: 30,
            StatsEnum.SPECIAL_ATTACK: 55,
            StatsEnum.SPECIAL_DEFENSE: 30,
            StatsEnum.SPEED: 85
        }
    },
    "0279": {
        None: {
            PocketMonsterParamEnum.NAME: "Pelipper",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.WATER,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.FLYING,
            StatsEnum.HP: 60,
            StatsEnum.ATTACK: 50,
            StatsEnum.DEFENSE: 100,
            StatsEnum.SPECIAL_ATTACK: 95,
            StatsEnum.SPECIAL_DEFENSE: 70,
            StatsEnum.SPEED: 65
        }
    },
    "0280": {
        None: {
            PocketMonsterParamEnum.NAME: "Ralts",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.PSYCHIC,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.FAIRY,
            StatsEnum.HP: 28,
            StatsEnum.ATTACK: 25,
            StatsEnum.DEFENSE: 25,
            StatsEnum.SPECIAL_ATTACK: 45,
            StatsEnum.SPECIAL_DEFENSE: 35,
            StatsEnum.SPEED: 40
        }
    },
    "0281": {
        None: {
            PocketMonsterParamEnum.NAME: "Kirlia",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.PSYCHIC,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.FAIRY,
            StatsEnum.HP: 38,
            StatsEnum.ATTACK: 35,
            StatsEnum.DEFENSE: 35,
            StatsEnum.SPECIAL_ATTACK: 65,
            StatsEnum.SPECIAL_DEFENSE: 55,
            StatsEnum.SPEED: 50
        }
    },
    "0282": {
        None: {
            PocketMonsterParamEnum.NAME: "Gardevoir",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.PSYCHIC,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.FAIRY,
            StatsEnum.HP: 68,
            StatsEnum.ATTACK: 65,
            StatsEnum.DEFENSE: 65,
            StatsEnum.SPECIAL_ATTACK: 125,
            StatsEnum.SPECIAL_DEFENSE: 115,
            StatsEnum.SPEED: 80
        },
        FormEnum.MEGA: {
            PocketMonsterParamEnum.NAME: "Gardevoir",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.PSYCHIC,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.FAIRY,
            StatsEnum.HP: 68,
            StatsEnum.ATTACK: 85,
            StatsEnum.DEFENSE: 65,
            StatsEnum.SPECIAL_ATTACK: 165,
            StatsEnum.SPECIAL_DEFENSE: 135,
            StatsEnum.SPEED: 100
        }
    },
    "0283": {
        None: {
            PocketMonsterParamEnum.NAME: "Surskit",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.BUG,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.WATER,
            StatsEnum.HP: 40,
            StatsEnum.ATTACK: 30,
            StatsEnum.DEFENSE: 32,
            StatsEnum.SPECIAL_ATTACK: 50,
            StatsEnum.SPECIAL_DEFENSE: 52,
            StatsEnum.SPEED: 65
        }
    },
    "0284": {
        None: {
            PocketMonsterParamEnum.NAME: "Masquerain",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.BUG,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.FLYING,
            StatsEnum.HP: 70,
            StatsEnum.ATTACK: 60,
            StatsEnum.DEFENSE: 62,
            StatsEnum.SPECIAL_ATTACK: 100,
            StatsEnum.SPECIAL_DEFENSE: 82,
            StatsEnum.SPEED: 80
        }
    },
    "0285": {
        None: {
            PocketMonsterParamEnum.NAME: "Shroomish",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.GRASS,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 60,
            StatsEnum.ATTACK: 40,
            StatsEnum.DEFENSE: 60,
            StatsEnum.SPECIAL_ATTACK: 40,
            StatsEnum.SPECIAL_DEFENSE: 60,
            StatsEnum.SPEED: 35
        }
    },
    "0286": {
        None: {
            PocketMonsterParamEnum.NAME: "Breloom",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.GRASS,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.FIGHTING,
            StatsEnum.HP: 60,
            StatsEnum.ATTACK: 130,
            StatsEnum.DEFENSE: 80,
            StatsEnum.SPECIAL_ATTACK: 60,
            StatsEnum.SPECIAL_DEFENSE: 60,
            StatsEnum.SPEED: 70
        }
    },
    "0287": {
        None: {
            PocketMonsterParamEnum.NAME: "Slakoth",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.NORMAL,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 60,
            StatsEnum.ATTACK: 60,
            StatsEnum.DEFENSE: 60,
            StatsEnum.SPECIAL_ATTACK: 35,
            StatsEnum.SPECIAL_DEFENSE: 35,
            StatsEnum.SPEED: 30
        }
    },
    "0288": {
        None: {
            PocketMonsterParamEnum.NAME: "Vigoroth",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.NORMAL,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 80,
            StatsEnum.ATTACK: 80,
            StatsEnum.DEFENSE: 80,
            StatsEnum.SPECIAL_ATTACK: 55,
            StatsEnum.SPECIAL_DEFENSE: 55,
            StatsEnum.SPEED: 90
        }
    },
    "0289": {
        None: {
            PocketMonsterParamEnum.NAME: "Slaking",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.NORMAL,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 150,
            StatsEnum.ATTACK: 160,
            StatsEnum.DEFENSE: 100,
            StatsEnum.SPECIAL_ATTACK: 95,
            StatsEnum.SPECIAL_DEFENSE: 65,
            StatsEnum.SPEED: 100
        }
    },
    "0290": {
        None: {
            PocketMonsterParamEnum.NAME: "Nincada",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.BUG,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.GROUND,
            StatsEnum.HP: 31,
            StatsEnum.ATTACK: 45,
            StatsEnum.DEFENSE: 90,
            StatsEnum.SPECIAL_ATTACK: 30,
            StatsEnum.SPECIAL_DEFENSE: 30,
            StatsEnum.SPEED: 40
        }
    },
    "0291": {
        None: {
            PocketMonsterParamEnum.NAME: "Ninjask",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.BUG,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.FLYING,
            StatsEnum.HP: 61,
            StatsEnum.ATTACK: 90,
            StatsEnum.DEFENSE: 45,
            StatsEnum.SPECIAL_ATTACK: 50,
            StatsEnum.SPECIAL_DEFENSE: 50,
            StatsEnum.SPEED: 160
        }
    },
    "0292": {
        None: {
            PocketMonsterParamEnum.NAME: "Shedinja",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.BUG,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.GHOST,
            StatsEnum.HP: 1,
            StatsEnum.ATTACK: 90,
            StatsEnum.DEFENSE: 45,
            StatsEnum.SPECIAL_ATTACK: 30,
            StatsEnum.SPECIAL_DEFENSE: 30,
            StatsEnum.SPEED: 40
        }
    },
    "0293": {
        None: {
            PocketMonsterParamEnum.NAME: "Whismur",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.NORMAL,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 64,
            StatsEnum.ATTACK: 51,
            StatsEnum.DEFENSE: 23,
            StatsEnum.SPECIAL_ATTACK: 51,
            StatsEnum.SPECIAL_DEFENSE: 23,
            StatsEnum.SPEED: 28
        }
    },
    "0294": {
        None: {
            PocketMonsterParamEnum.NAME: "Loudred",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.NORMAL,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 84,
            StatsEnum.ATTACK: 71,
            StatsEnum.DEFENSE: 43,
            StatsEnum.SPECIAL_ATTACK: 71,
            StatsEnum.SPECIAL_DEFENSE: 43,
            StatsEnum.SPEED: 48
        }
    },
    "0295": {
        None: {
            PocketMonsterParamEnum.NAME: "Exploud",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.NORMAL,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 104,
            StatsEnum.ATTACK: 91,
            StatsEnum.DEFENSE: 63,
            StatsEnum.SPECIAL_ATTACK: 91,
            StatsEnum.SPECIAL_DEFENSE: 73,
            StatsEnum.SPEED: 68
        }
    },
    "0296": {
        None: {
            PocketMonsterParamEnum.NAME: "Makuhita",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.FIGHTING,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 72,
            StatsEnum.ATTACK: 60,
            StatsEnum.DEFENSE: 30,
            StatsEnum.SPECIAL_ATTACK: 20,
            StatsEnum.SPECIAL_DEFENSE: 30,
            StatsEnum.SPEED: 25
        }
    },
    "0297": {
        None: {
            PocketMonsterParamEnum.NAME: "Hariyama",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.FIGHTING,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 144,
            StatsEnum.ATTACK: 120,
            StatsEnum.DEFENSE: 60,
            StatsEnum.SPECIAL_ATTACK: 40,
            StatsEnum.SPECIAL_DEFENSE: 60,
            StatsEnum.SPEED: 50
        }
    },
    "0298": {
        None: {
            PocketMonsterParamEnum.NAME: "Azurill",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.NORMAL,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.FAIRY,
            StatsEnum.HP: 50,
            StatsEnum.ATTACK: 20,
            StatsEnum.DEFENSE: 40,
            StatsEnum.SPECIAL_ATTACK: 20,
            StatsEnum.SPECIAL_DEFENSE: 40,
            StatsEnum.SPEED: 20
        }
    },
    "0299": {
        None: {
            PocketMonsterParamEnum.NAME: "Nosepass",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.ROCK,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 30,
            StatsEnum.ATTACK: 45,
            StatsEnum.DEFENSE: 135,
            StatsEnum.SPECIAL_ATTACK: 45,
            StatsEnum.SPECIAL_DEFENSE: 90,
            StatsEnum.SPEED: 30
        }
    },
    "0300": {
        None: {
            PocketMonsterParamEnum.NAME: "Skitty",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.NORMAL,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 50,
            StatsEnum.ATTACK: 45,
            StatsEnum.DEFENSE: 45,
            StatsEnum.SPECIAL_ATTACK: 35,
            StatsEnum.SPECIAL_DEFENSE: 35,
            StatsEnum.SPEED: 50
        }
    },
    "0301": {
        None: {
            PocketMonsterParamEnum.NAME: "Delcatty",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.NORMAL,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 70,
            StatsEnum.ATTACK: 65,
            StatsEnum.DEFENSE: 65,
            StatsEnum.SPECIAL_ATTACK: 55,
            StatsEnum.SPECIAL_DEFENSE: 55,
            StatsEnum.SPEED: 90
        }
    },
    "0302": {
        None: {
            PocketMonsterParamEnum.NAME: "Sableye",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.DARK,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.GHOST,
            StatsEnum.HP: 50,
            StatsEnum.ATTACK: 75,
            StatsEnum.DEFENSE: 75,
            StatsEnum.SPECIAL_ATTACK: 65,
            StatsEnum.SPECIAL_DEFENSE: 65,
            StatsEnum.SPEED: 50
        },
        FormEnum.MEGA: {
            PocketMonsterParamEnum.NAME: "Sableye",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.DARK,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.GHOST,
            StatsEnum.HP: 50,
            StatsEnum.ATTACK: 85,
            StatsEnum.DEFENSE: 125,
            StatsEnum.SPECIAL_ATTACK: 85,
            StatsEnum.SPECIAL_DEFENSE: 115,
            StatsEnum.SPEED: 20
        }
    },
    "0303": {
        None: {
            PocketMonsterParamEnum.NAME: "Mawile",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.STEEL,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.FAIRY,
            StatsEnum.HP: 50,
            StatsEnum.ATTACK: 85,
            StatsEnum.DEFENSE: 85,
            StatsEnum.SPECIAL_ATTACK: 55,
            StatsEnum.SPECIAL_DEFENSE: 55,
            StatsEnum.SPEED: 50
        },
        FormEnum.MEGA: {
            PocketMonsterParamEnum.NAME: "Mawile",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.STEEL,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.FAIRY,
            StatsEnum.HP: 50,
            StatsEnum.ATTACK: 105,
            StatsEnum.DEFENSE: 125,
            StatsEnum.SPECIAL_ATTACK: 55,
            StatsEnum.SPECIAL_DEFENSE: 95,
            StatsEnum.SPEED: 50
        }
    },
    "0304": {
        None: {
            PocketMonsterParamEnum.NAME: "Aron",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.STEEL,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.ROCK,
            StatsEnum.HP: 50,
            StatsEnum.ATTACK: 70,
            StatsEnum.DEFENSE: 100,
            StatsEnum.SPECIAL_ATTACK: 40,
            StatsEnum.SPECIAL_DEFENSE: 40,
            StatsEnum.SPEED: 30
        }
    },
    "0305": {
        None: {
            PocketMonsterParamEnum.NAME: "Lairon",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.STEEL,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.ROCK,
            StatsEnum.HP: 60,
            StatsEnum.ATTACK: 90,
            StatsEnum.DEFENSE: 140,
            StatsEnum.SPECIAL_ATTACK: 50,
            StatsEnum.SPECIAL_DEFENSE: 50,
            StatsEnum.SPEED: 40
        }
    },
    "0306": {
        None: {
            PocketMonsterParamEnum.NAME: "Aggron",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.STEEL,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.ROCK,
            StatsEnum.HP: 70,
            StatsEnum.ATTACK: 110,
            StatsEnum.DEFENSE: 180,
            StatsEnum.SPECIAL_ATTACK: 60,
            StatsEnum.SPECIAL_DEFENSE: 60,
            StatsEnum.SPEED: 50
        },
        FormEnum.MEGA: {
            PocketMonsterParamEnum.NAME: "Aggron",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.STEEL,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 70,
            StatsEnum.ATTACK: 140,
            StatsEnum.DEFENSE: 230,
            StatsEnum.SPECIAL_ATTACK: 60,
            StatsEnum.SPECIAL_DEFENSE: 80,
            StatsEnum.SPEED: 50
        }
    },
    "0307": {
        None: {
            PocketMonsterParamEnum.NAME: "Meditite",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.FIGHTING,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.PSYCHIC,
            StatsEnum.HP: 30,
            StatsEnum.ATTACK: 40,
            StatsEnum.DEFENSE: 55,
            StatsEnum.SPECIAL_ATTACK: 40,
            StatsEnum.SPECIAL_DEFENSE: 55,
            StatsEnum.SPEED: 60
        }
    },
    "0308": {
        None: {
            PocketMonsterParamEnum.NAME: "Medicham",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.FIGHTING,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.PSYCHIC,
            StatsEnum.HP: 60,
            StatsEnum.ATTACK: 60,
            StatsEnum.DEFENSE: 75,
            StatsEnum.SPECIAL_ATTACK: 60,
            StatsEnum.SPECIAL_DEFENSE: 75,
            StatsEnum.SPEED: 80
        },
        FormEnum.MEGA: {
            PocketMonsterParamEnum.NAME: "Medicham",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.FIGHTING,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.PSYCHIC,
            StatsEnum.HP: 60,
            StatsEnum.ATTACK: 100,
            StatsEnum.DEFENSE: 85,
            StatsEnum.SPECIAL_ATTACK: 80,
            StatsEnum.SPECIAL_DEFENSE: 85,
            StatsEnum.SPEED: 100
        }
    },
    "0309": {
        None: {
            PocketMonsterParamEnum.NAME: "Electrike",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.ELECTRIC,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 40,
            StatsEnum.ATTACK: 45,
            StatsEnum.DEFENSE: 40,
            StatsEnum.SPECIAL_ATTACK: 65,
            StatsEnum.SPECIAL_DEFENSE: 40,
            StatsEnum.SPEED: 65
        }
    },
    "0310": {
        None: {
            PocketMonsterParamEnum.NAME: "Manectric",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.ELECTRIC,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 70,
            StatsEnum.ATTACK: 75,
            StatsEnum.DEFENSE: 60,
            StatsEnum.SPECIAL_ATTACK: 105,
            StatsEnum.SPECIAL_DEFENSE: 60,
            StatsEnum.SPEED: 105
        },
        FormEnum.MEGA: {
            PocketMonsterParamEnum.NAME: "Manectric",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.ELECTRIC,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 70,
            StatsEnum.ATTACK: 75,
            StatsEnum.DEFENSE: 80,
            StatsEnum.SPECIAL_ATTACK: 135,
            StatsEnum.SPECIAL_DEFENSE: 80,
            StatsEnum.SPEED: 135
        }
    },
    "0311": {
        None: {
            PocketMonsterParamEnum.NAME: "Plusle",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.ELECTRIC,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 60,
            StatsEnum.ATTACK: 50,
            StatsEnum.DEFENSE: 40,
            StatsEnum.SPECIAL_ATTACK: 85,
            StatsEnum.SPECIAL_DEFENSE: 75,
            StatsEnum.SPEED: 95
        }
    },
    "0312": {
        None: {
            PocketMonsterParamEnum.NAME: "Minun",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.ELECTRIC,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 60,
            StatsEnum.ATTACK: 40,
            StatsEnum.DEFENSE: 50,
            StatsEnum.SPECIAL_ATTACK: 75,
            StatsEnum.SPECIAL_DEFENSE: 85,
            StatsEnum.SPEED: 95
        }
    },
    "0313": {
        None: {
            PocketMonsterParamEnum.NAME: "Volbeat",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.BUG,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 65,
            StatsEnum.ATTACK: 73,
            StatsEnum.DEFENSE: 75,
            StatsEnum.SPECIAL_ATTACK: 47,
            StatsEnum.SPECIAL_DEFENSE: 85,
            StatsEnum.SPEED: 85
        }
    },
    "0314": {
        None: {
            PocketMonsterParamEnum.NAME: "Illumise",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.BUG,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 65,
            StatsEnum.ATTACK: 47,
            StatsEnum.DEFENSE: 75,
            StatsEnum.SPECIAL_ATTACK: 73,
            StatsEnum.SPECIAL_DEFENSE: 85,
            StatsEnum.SPEED: 85
        }
    },
    "0315": {
        None: {
            PocketMonsterParamEnum.NAME: "Roselia",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.GRASS,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.POISON,
            StatsEnum.HP: 50,
            StatsEnum.ATTACK: 60,
            StatsEnum.DEFENSE: 45,
            StatsEnum.SPECIAL_ATTACK: 100,
            StatsEnum.SPECIAL_DEFENSE: 80,
            StatsEnum.SPEED: 65
        }
    },
    "0316": {
        None: {
            PocketMonsterParamEnum.NAME: "Gulpin",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.POISON,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 70,
            StatsEnum.ATTACK: 43,
            StatsEnum.DEFENSE: 53,
            StatsEnum.SPECIAL_ATTACK: 43,
            StatsEnum.SPECIAL_DEFENSE: 53,
            StatsEnum.SPEED: 40
        }
    },
    "0317": {
        None: {
            PocketMonsterParamEnum.NAME: "Swalot",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.POISON,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 100,
            StatsEnum.ATTACK: 73,
            StatsEnum.DEFENSE: 83,
            StatsEnum.SPECIAL_ATTACK: 73,
            StatsEnum.SPECIAL_DEFENSE: 83,
            StatsEnum.SPEED: 55
        }
    },
    "0318": {
        None: {
            PocketMonsterParamEnum.NAME: "Carvanha",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.WATER,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.DARK,
            StatsEnum.HP: 45,
            StatsEnum.ATTACK: 90,
            StatsEnum.DEFENSE: 20,
            StatsEnum.SPECIAL_ATTACK: 65,
            StatsEnum.SPECIAL_DEFENSE: 20,
            StatsEnum.SPEED: 65
        }
    },
    "0319": {
        None: {
            PocketMonsterParamEnum.NAME: "Sharpedo",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.WATER,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.DARK,
            StatsEnum.HP: 70,
            StatsEnum.ATTACK: 120,
            StatsEnum.DEFENSE: 40,
            StatsEnum.SPECIAL_ATTACK: 95,
            StatsEnum.SPECIAL_DEFENSE: 40,
            StatsEnum.SPEED: 95
        },
        FormEnum.MEGA: {
            PocketMonsterParamEnum.NAME: "Sharpedo",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.WATER,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.DARK,
            StatsEnum.HP: 70,
            StatsEnum.ATTACK: 140,
            StatsEnum.DEFENSE: 70,
            StatsEnum.SPECIAL_ATTACK: 110,
            StatsEnum.SPECIAL_DEFENSE: 65,
            StatsEnum.SPEED: 105
        }
    },
    "0320": {
        None: {
            PocketMonsterParamEnum.NAME: "Wailmer",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.WATER,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 130,
            StatsEnum.ATTACK: 70,
            StatsEnum.DEFENSE: 35,
            StatsEnum.SPECIAL_ATTACK: 70,
            StatsEnum.SPECIAL_DEFENSE: 35,
            StatsEnum.SPEED: 60
        }
    },
    "0321": {
        None: {
            PocketMonsterParamEnum.NAME: "Wailord",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.WATER,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 170,
            StatsEnum.ATTACK: 90,
            StatsEnum.DEFENSE: 45,
            StatsEnum.SPECIAL_ATTACK: 90,
            StatsEnum.SPECIAL_DEFENSE: 45,
            StatsEnum.SPEED: 60
        }
    },
    "0322": {
        None: {
            PocketMonsterParamEnum.NAME: "Numel",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.FIRE,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.GROUND,
            StatsEnum.HP: 60,
            StatsEnum.ATTACK: 60,
            StatsEnum.DEFENSE: 40,
            StatsEnum.SPECIAL_ATTACK: 65,
            StatsEnum.SPECIAL_DEFENSE: 45,
            StatsEnum.SPEED: 35
        }
    },
    "0323": {
        None: {
            PocketMonsterParamEnum.NAME: "Camerupt",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.FIRE,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.GROUND,
            StatsEnum.HP: 70,
            StatsEnum.ATTACK: 100,
            StatsEnum.DEFENSE: 70,
            StatsEnum.SPECIAL_ATTACK: 105,
            StatsEnum.SPECIAL_DEFENSE: 75,
            StatsEnum.SPEED: 40
        },
        FormEnum.MEGA: {
            PocketMonsterParamEnum.NAME: "Camerupt",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.FIRE,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.GROUND,
            StatsEnum.HP: 70,
            StatsEnum.ATTACK: 120,
            StatsEnum.DEFENSE: 100,
            StatsEnum.SPECIAL_ATTACK: 145,
            StatsEnum.SPECIAL_DEFENSE: 105,
            StatsEnum.SPEED: 20
        }
    },
    "0324": {
        None: {
            PocketMonsterParamEnum.NAME: "Torkoal",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.FIRE,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 70,
            StatsEnum.ATTACK: 85,
            StatsEnum.DEFENSE: 140,
            StatsEnum.SPECIAL_ATTACK: 85,
            StatsEnum.SPECIAL_DEFENSE: 70,
            StatsEnum.SPEED: 20
        }
    },
    "0325": {
        None: {
            PocketMonsterParamEnum.NAME: "Spoink",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.PSYCHIC,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 60,
            StatsEnum.ATTACK: 25,
            StatsEnum.DEFENSE: 35,
            StatsEnum.SPECIAL_ATTACK: 70,
            StatsEnum.SPECIAL_DEFENSE: 80,
            StatsEnum.SPEED: 60
        }
    },
    "0326": {
        None: {
            PocketMonsterParamEnum.NAME: "Grumpig",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.PSYCHIC,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 80,
            StatsEnum.ATTACK: 45,
            StatsEnum.DEFENSE: 65,
            StatsEnum.SPECIAL_ATTACK: 90,
            StatsEnum.SPECIAL_DEFENSE: 110,
            StatsEnum.SPEED: 80
        }
    },
    "0327": {
        None: {
            PocketMonsterParamEnum.NAME: "Spinda",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.NORMAL,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 60,
            StatsEnum.ATTACK: 60,
            StatsEnum.DEFENSE: 60,
            StatsEnum.SPECIAL_ATTACK: 60,
            StatsEnum.SPECIAL_DEFENSE: 60,
            StatsEnum.SPEED: 60
        }
    },
    "0328": {
        None: {
            PocketMonsterParamEnum.NAME: "Trapinch",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.GROUND,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 45,
            StatsEnum.ATTACK: 100,
            StatsEnum.DEFENSE: 45,
            StatsEnum.SPECIAL_ATTACK: 45,
            StatsEnum.SPECIAL_DEFENSE: 45,
            StatsEnum.SPEED: 10
        }
    },
    "0329": {
        None: {
            PocketMonsterParamEnum.NAME: "Vibrava",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.GROUND,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.DRAGON,
            StatsEnum.HP: 50,
            StatsEnum.ATTACK: 70,
            StatsEnum.DEFENSE: 50,
            StatsEnum.SPECIAL_ATTACK: 50,
            StatsEnum.SPECIAL_DEFENSE: 50,
            StatsEnum.SPEED: 70
        }
    },
    "0330": {
        None: {
            PocketMonsterParamEnum.NAME: "Flygon",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.GROUND,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.DRAGON,
            StatsEnum.HP: 80,
            StatsEnum.ATTACK: 100,
            StatsEnum.DEFENSE: 80,
            StatsEnum.SPECIAL_ATTACK: 80,
            StatsEnum.SPECIAL_DEFENSE: 80,
            StatsEnum.SPEED: 100
        }
    },
    "0331": {
        None: {
            PocketMonsterParamEnum.NAME: "Cacnea",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.GRASS,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 50,
            StatsEnum.ATTACK: 85,
            StatsEnum.DEFENSE: 40,
            StatsEnum.SPECIAL_ATTACK: 85,
            StatsEnum.SPECIAL_DEFENSE: 40,
            StatsEnum.SPEED: 35
        }
    },
    "0332": {
        None: {
            PocketMonsterParamEnum.NAME: "Cacturne",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.GRASS,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.DARK,
            StatsEnum.HP: 70,
            StatsEnum.ATTACK: 115,
            StatsEnum.DEFENSE: 60,
            StatsEnum.SPECIAL_ATTACK: 115,
            StatsEnum.SPECIAL_DEFENSE: 60,
            StatsEnum.SPEED: 55
        }
    },
    "0333": {
        None: {
            PocketMonsterParamEnum.NAME: "Swablu",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.NORMAL,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.FLYING,
            StatsEnum.HP: 45,
            StatsEnum.ATTACK: 40,
            StatsEnum.DEFENSE: 60,
            StatsEnum.SPECIAL_ATTACK: 40,
            StatsEnum.SPECIAL_DEFENSE: 75,
            StatsEnum.SPEED: 50
        }
    },
    "0334": {
        None: {
            PocketMonsterParamEnum.NAME: "Altaria",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.DRAGON,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.FLYING,
            StatsEnum.HP: 75,
            StatsEnum.ATTACK: 70,
            StatsEnum.DEFENSE: 90,
            StatsEnum.SPECIAL_ATTACK: 70,
            StatsEnum.SPECIAL_DEFENSE: 105,
            StatsEnum.SPEED: 80
        },
        FormEnum.MEGA: {
            PocketMonsterParamEnum.NAME: "Altaria",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.DRAGON,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.FAIRY,
            StatsEnum.HP: 75,
            StatsEnum.ATTACK: 110,
            StatsEnum.DEFENSE: 110,
            StatsEnum.SPECIAL_ATTACK: 110,
            StatsEnum.SPECIAL_DEFENSE: 105,
            StatsEnum.SPEED: 80
        }
    },
    "0335": {
        None: {
            PocketMonsterParamEnum.NAME: "Zangoose",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.NORMAL,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 73,
            StatsEnum.ATTACK: 115,
            StatsEnum.DEFENSE: 60,
            StatsEnum.SPECIAL_ATTACK: 60,
            StatsEnum.SPECIAL_DEFENSE: 60,
            StatsEnum.SPEED: 90
        }
    },
    "0336": {
        None: {
            PocketMonsterParamEnum.NAME: "Seviper",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.POISON,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 73,
            StatsEnum.ATTACK: 100,
            StatsEnum.DEFENSE: 60,
            StatsEnum.SPECIAL_ATTACK: 100,
            StatsEnum.SPECIAL_DEFENSE: 60,
            StatsEnum.SPEED: 65
        }
    },
    "0337": {
        None: {
            PocketMonsterParamEnum.NAME: "Lunatone",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.ROCK,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.PSYCHIC,
            StatsEnum.HP: 90,
            StatsEnum.ATTACK: 55,
            StatsEnum.DEFENSE: 65,
            StatsEnum.SPECIAL_ATTACK: 95,
            StatsEnum.SPECIAL_DEFENSE: 85,
            StatsEnum.SPEED: 70
        }
    },
    "0338": {
        None: {
            PocketMonsterParamEnum.NAME: "Solrock",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.ROCK,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.PSYCHIC,
            StatsEnum.HP: 90,
            StatsEnum.ATTACK: 95,
            StatsEnum.DEFENSE: 85,
            StatsEnum.SPECIAL_ATTACK: 55,
            StatsEnum.SPECIAL_DEFENSE: 65,
            StatsEnum.SPEED: 70
        }
    },
    "0339": {
        None: {
            PocketMonsterParamEnum.NAME: "Barboach",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.WATER,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.GROUND,
            StatsEnum.HP: 50,
            StatsEnum.ATTACK: 48,
            StatsEnum.DEFENSE: 43,
            StatsEnum.SPECIAL_ATTACK: 46,
            StatsEnum.SPECIAL_DEFENSE: 41,
            StatsEnum.SPEED: 60
        }
    },
    "0340": {
        None: {
            PocketMonsterParamEnum.NAME: "Whiscash",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.WATER,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.GROUND,
            StatsEnum.HP: 110,
            StatsEnum.ATTACK: 78,
            StatsEnum.DEFENSE: 73,
            StatsEnum.SPECIAL_ATTACK: 76,
            StatsEnum.SPECIAL_DEFENSE: 71,
            StatsEnum.SPEED: 60
        }
    },
    "0341": {
        None: {
            PocketMonsterParamEnum.NAME: "Corphish",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.WATER,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 43,
            StatsEnum.ATTACK: 80,
            StatsEnum.DEFENSE: 65,
            StatsEnum.SPECIAL_ATTACK: 50,
            StatsEnum.SPECIAL_DEFENSE: 35,
            StatsEnum.SPEED: 35
        }
    },
    "0342": {
        None: {
            PocketMonsterParamEnum.NAME: "Crawdaunt",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.WATER,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.DARK,
            StatsEnum.HP: 63,
            StatsEnum.ATTACK: 120,
            StatsEnum.DEFENSE: 85,
            StatsEnum.SPECIAL_ATTACK: 90,
            StatsEnum.SPECIAL_DEFENSE: 55,
            StatsEnum.SPEED: 55
        }
    },
    "0343": {
        None: {
            PocketMonsterParamEnum.NAME: "Baltoy",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.GROUND,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.PSYCHIC,
            StatsEnum.HP: 40,
            StatsEnum.ATTACK: 40,
            StatsEnum.DEFENSE: 55,
            StatsEnum.SPECIAL_ATTACK: 40,
            StatsEnum.SPECIAL_DEFENSE: 70,
            StatsEnum.SPEED: 55
        }
    },
    "0344": {
        None: {
            PocketMonsterParamEnum.NAME: "Claydol",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.GROUND,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.PSYCHIC,
            StatsEnum.HP: 60,
            StatsEnum.ATTACK: 70,
            StatsEnum.DEFENSE: 105,
            StatsEnum.SPECIAL_ATTACK: 70,
            StatsEnum.SPECIAL_DEFENSE: 120,
            StatsEnum.SPEED: 75
        }
    },
    "0345": {
        None: {
            PocketMonsterParamEnum.NAME: "Lileep",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.ROCK,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.GRASS,
            StatsEnum.HP: 66,
            StatsEnum.ATTACK: 41,
            StatsEnum.DEFENSE: 77,
            StatsEnum.SPECIAL_ATTACK: 61,
            StatsEnum.SPECIAL_DEFENSE: 87,
            StatsEnum.SPEED: 23
        }
    },
    "0346": {
        None: {
            PocketMonsterParamEnum.NAME: "Cradily",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.ROCK,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.GRASS,
            StatsEnum.HP: 86,
            StatsEnum.ATTACK: 81,
            StatsEnum.DEFENSE: 97,
            StatsEnum.SPECIAL_ATTACK: 81,
            StatsEnum.SPECIAL_DEFENSE: 107,
            StatsEnum.SPEED: 43
        }
    },
    "0347": {
        None: {
            PocketMonsterParamEnum.NAME: "Anorith",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.ROCK,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.BUG,
            StatsEnum.HP: 45,
            StatsEnum.ATTACK: 95,
            StatsEnum.DEFENSE: 50,
            StatsEnum.SPECIAL_ATTACK: 40,
            StatsEnum.SPECIAL_DEFENSE: 50,
            StatsEnum.SPEED: 75
        }
    },
    "0348": {
        None: {
            PocketMonsterParamEnum.NAME: "Armaldo",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.ROCK,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.BUG,
            StatsEnum.HP: 75,
            StatsEnum.ATTACK: 125,
            StatsEnum.DEFENSE: 100,
            StatsEnum.SPECIAL_ATTACK: 70,
            StatsEnum.SPECIAL_DEFENSE: 80,
            StatsEnum.SPEED: 45
        }
    },
    "0349": {
        None: {
            PocketMonsterParamEnum.NAME: "Feebas",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.WATER,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 20,
            StatsEnum.ATTACK: 15,
            StatsEnum.DEFENSE: 20,
            StatsEnum.SPECIAL_ATTACK: 10,
            StatsEnum.SPECIAL_DEFENSE: 55,
            StatsEnum.SPEED: 80
        }
    },
    "0350": {
        None: {
            PocketMonsterParamEnum.NAME: "Milotic",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.WATER,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 95,
            StatsEnum.ATTACK: 60,
            StatsEnum.DEFENSE: 79,
            StatsEnum.SPECIAL_ATTACK: 100,
            StatsEnum.SPECIAL_DEFENSE: 125,
            StatsEnum.SPEED: 81
        }
    },
    "0351": {
        None: {
            PocketMonsterParamEnum.NAME: "Castform",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.NORMAL,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 70,
            StatsEnum.ATTACK: 70,
            StatsEnum.DEFENSE: 70,
            StatsEnum.SPECIAL_ATTACK: 70,
            StatsEnum.SPECIAL_DEFENSE: 70,
            StatsEnum.SPEED: 70
        },
        FormEnum.SUNNY_FORM: {
            PocketMonsterParamEnum.NAME: "Castform",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.FIRE,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 70,
            StatsEnum.ATTACK: 70,
            StatsEnum.DEFENSE: 70,
            StatsEnum.SPECIAL_ATTACK: 70,
            StatsEnum.SPECIAL_DEFENSE: 70,
            StatsEnum.SPEED: 70
        },
        FormEnum.RAINY_FORM: {
            PocketMonsterParamEnum.NAME: "Castform",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.WATER,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 70,
            StatsEnum.ATTACK: 70,
            StatsEnum.DEFENSE: 70,
            StatsEnum.SPECIAL_ATTACK: 70,
            StatsEnum.SPECIAL_DEFENSE: 70,
            StatsEnum.SPEED: 70
        },
        FormEnum.SNOWY_FORM: {
            PocketMonsterParamEnum.NAME: "Castform",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.ICE,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 70,
            StatsEnum.ATTACK: 70,
            StatsEnum.DEFENSE: 70,
            StatsEnum.SPECIAL_ATTACK: 70,
            StatsEnum.SPECIAL_DEFENSE: 70,
            StatsEnum.SPEED: 70
        }
    },
    "0352": {
        None: {
            PocketMonsterParamEnum.NAME: "Kecleon",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.NORMAL,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 60,
            StatsEnum.ATTACK: 90,
            StatsEnum.DEFENSE: 70,
            StatsEnum.SPECIAL_ATTACK: 60,
            StatsEnum.SPECIAL_DEFENSE: 120,
            StatsEnum.SPEED: 40
        }
    },
    "0353": {
        None: {
            PocketMonsterParamEnum.NAME: "Shuppet",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.GHOST,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 44,
            StatsEnum.ATTACK: 75,
            StatsEnum.DEFENSE: 35,
            StatsEnum.SPECIAL_ATTACK: 63,
            StatsEnum.SPECIAL_DEFENSE: 33,
            StatsEnum.SPEED: 45
        }
    },
    "0354": {
        None: {
            PocketMonsterParamEnum.NAME: "Banette",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.GHOST,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 64,
            StatsEnum.ATTACK: 115,
            StatsEnum.DEFENSE: 65,
            StatsEnum.SPECIAL_ATTACK: 83,
            StatsEnum.SPECIAL_DEFENSE: 63,
            StatsEnum.SPEED: 65
        },
        FormEnum.MEGA: {
            PocketMonsterParamEnum.NAME: "Banette",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.GHOST,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 64,
            StatsEnum.ATTACK: 165,
            StatsEnum.DEFENSE: 75,
            StatsEnum.SPECIAL_ATTACK: 93,
            StatsEnum.SPECIAL_DEFENSE: 83,
            StatsEnum.SPEED: 75
        }
    },
    "0355": {
        None: {
            PocketMonsterParamEnum.NAME: "Duskull",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.GHOST,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 20,
            StatsEnum.ATTACK: 40,
            StatsEnum.DEFENSE: 90,
            StatsEnum.SPECIAL_ATTACK: 30,
            StatsEnum.SPECIAL_DEFENSE: 90,
            StatsEnum.SPEED: 25
        }
    },
    "0356": {
        None: {
            PocketMonsterParamEnum.NAME: "Dusclops",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.GHOST,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 40,
            StatsEnum.ATTACK: 70,
            StatsEnum.DEFENSE: 130,
            StatsEnum.SPECIAL_ATTACK: 60,
            StatsEnum.SPECIAL_DEFENSE: 130,
            StatsEnum.SPEED: 25
        }
    },
    "0357": {
        None: {
            PocketMonsterParamEnum.NAME: "Tropius",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.GRASS,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.FLYING,
            StatsEnum.HP: 99,
            StatsEnum.ATTACK: 68,
            StatsEnum.DEFENSE: 83,
            StatsEnum.SPECIAL_ATTACK: 72,
            StatsEnum.SPECIAL_DEFENSE: 87,
            StatsEnum.SPEED: 51
        }
    },
    "0358": {
        None: {
            PocketMonsterParamEnum.NAME: "Chimecho",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.PSYCHIC,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 75,
            StatsEnum.ATTACK: 50,
            StatsEnum.DEFENSE: 80,
            StatsEnum.SPECIAL_ATTACK: 95,
            StatsEnum.SPECIAL_DEFENSE: 90,
            StatsEnum.SPEED: 65
        }
    },
    "0359": {
        None: {
            PocketMonsterParamEnum.NAME: "Absol",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.DARK,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 65,
            StatsEnum.ATTACK: 130,
            StatsEnum.DEFENSE: 60,
            StatsEnum.SPECIAL_ATTACK: 75,
            StatsEnum.SPECIAL_DEFENSE: 60,
            StatsEnum.SPEED: 75
        },
        FormEnum.MEGA: {
            PocketMonsterParamEnum.NAME: "Absol",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.DARK,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 65,
            StatsEnum.ATTACK: 150,
            StatsEnum.DEFENSE: 60,
            StatsEnum.SPECIAL_ATTACK: 115,
            StatsEnum.SPECIAL_DEFENSE: 60,
            StatsEnum.SPEED: 115
        }
    },
    "0360": {
        None: {
            PocketMonsterParamEnum.NAME: "Wynaut",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.PSYCHIC,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 95,
            StatsEnum.ATTACK: 23,
            StatsEnum.DEFENSE: 48,
            StatsEnum.SPECIAL_ATTACK: 23,
            StatsEnum.SPECIAL_DEFENSE: 48,
            StatsEnum.SPEED: 23
        }
    },
    "0361": {
        None: {
            PocketMonsterParamEnum.NAME: "Snorunt",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.ICE,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 50,
            StatsEnum.ATTACK: 50,
            StatsEnum.DEFENSE: 50,
            StatsEnum.SPECIAL_ATTACK: 50,
            StatsEnum.SPECIAL_DEFENSE: 50,
            StatsEnum.SPEED: 50
        }
    },
    "0362": {
        None: {
            PocketMonsterParamEnum.NAME: "Glalie",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.ICE,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 80,
            StatsEnum.ATTACK: 80,
            StatsEnum.DEFENSE: 80,
            StatsEnum.SPECIAL_ATTACK: 80,
            StatsEnum.SPECIAL_DEFENSE: 80,
            StatsEnum.SPEED: 80
        },
        FormEnum.MEGA: {
            PocketMonsterParamEnum.NAME: "Glalie",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.ICE,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 80,
            StatsEnum.ATTACK: 120,
            StatsEnum.DEFENSE: 80,
            StatsEnum.SPECIAL_ATTACK: 120,
            StatsEnum.SPECIAL_DEFENSE: 80,
            StatsEnum.SPEED: 100
        }
    },
    "0363": {
        None: {
            PocketMonsterParamEnum.NAME: "Spheal",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.ICE,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.WATER,
            StatsEnum.HP: 70,
            StatsEnum.ATTACK: 40,
            StatsEnum.DEFENSE: 50,
            StatsEnum.SPECIAL_ATTACK: 55,
            StatsEnum.SPECIAL_DEFENSE: 50,
            StatsEnum.SPEED: 25
        }
    },
    "0364": {
        None: {
            PocketMonsterParamEnum.NAME: "Sealeo",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.ICE,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.WATER,
            StatsEnum.HP: 90,
            StatsEnum.ATTACK: 60,
            StatsEnum.DEFENSE: 70,
            StatsEnum.SPECIAL_ATTACK: 75,
            StatsEnum.SPECIAL_DEFENSE: 70,
            StatsEnum.SPEED: 45
        }
    },
    "0365": {
        None: {
            PocketMonsterParamEnum.NAME: "Walrein",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.ICE,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.WATER,
            StatsEnum.HP: 110,
            StatsEnum.ATTACK: 80,
            StatsEnum.DEFENSE: 90,
            StatsEnum.SPECIAL_ATTACK: 95,
            StatsEnum.SPECIAL_DEFENSE: 90,
            StatsEnum.SPEED: 65
        }
    },
    "0366": {
        None: {
            PocketMonsterParamEnum.NAME: "Clamperl",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.WATER,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 35,
            StatsEnum.ATTACK: 64,
            StatsEnum.DEFENSE: 85,
            StatsEnum.SPECIAL_ATTACK: 74,
            StatsEnum.SPECIAL_DEFENSE: 55,
            StatsEnum.SPEED: 32
        }
    },
    "0367": {
        None: {
            PocketMonsterParamEnum.NAME: "Huntail",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.WATER,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 55,
            StatsEnum.ATTACK: 104,
            StatsEnum.DEFENSE: 105,
            StatsEnum.SPECIAL_ATTACK: 94,
            StatsEnum.SPECIAL_DEFENSE: 75,
            StatsEnum.SPEED: 52
        }
    },
    "0368": {
        None: {
            PocketMonsterParamEnum.NAME: "Gorebyss",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.WATER,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 55,
            StatsEnum.ATTACK: 84,
            StatsEnum.DEFENSE: 105,
            StatsEnum.SPECIAL_ATTACK: 114,
            StatsEnum.SPECIAL_DEFENSE: 75,
            StatsEnum.SPEED: 52
        }
    },
    "0369": {
        None: {
            PocketMonsterParamEnum.NAME: "Relicanth",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.WATER,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.ROCK,
            StatsEnum.HP: 100,
            StatsEnum.ATTACK: 90,
            StatsEnum.DEFENSE: 130,
            StatsEnum.SPECIAL_ATTACK: 45,
            StatsEnum.SPECIAL_DEFENSE: 65,
            StatsEnum.SPEED: 55
        }
    },
    "0370": {
        None: {
            PocketMonsterParamEnum.NAME: "Luvdisc",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.WATER,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 43,
            StatsEnum.ATTACK: 30,
            StatsEnum.DEFENSE: 55,
            StatsEnum.SPECIAL_ATTACK: 40,
            StatsEnum.SPECIAL_DEFENSE: 65,
            StatsEnum.SPEED: 97
        }
    },
    "0371": {
        None: {
            PocketMonsterParamEnum.NAME: "Bagon",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.DRAGON,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 45,
            StatsEnum.ATTACK: 75,
            StatsEnum.DEFENSE: 60,
            StatsEnum.SPECIAL_ATTACK: 40,
            StatsEnum.SPECIAL_DEFENSE: 30,
            StatsEnum.SPEED: 50
        }
    },
    "0372": {
        None: {
            PocketMonsterParamEnum.NAME: "Shelgon",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.DRAGON,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 65,
            StatsEnum.ATTACK: 95,
            StatsEnum.DEFENSE: 100,
            StatsEnum.SPECIAL_ATTACK: 60,
            StatsEnum.SPECIAL_DEFENSE: 50,
            StatsEnum.SPEED: 50
        }
    },
    "0373": {
        None: {
            PocketMonsterParamEnum.NAME: "Salamence",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.DRAGON,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.FLYING,
            StatsEnum.HP: 95,
            StatsEnum.ATTACK: 135,
            StatsEnum.DEFENSE: 80,
            StatsEnum.SPECIAL_ATTACK: 110,
            StatsEnum.SPECIAL_DEFENSE: 80,
            StatsEnum.SPEED: 100
        },
        FormEnum.MEGA: {
            PocketMonsterParamEnum.NAME: "Salamence",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.DRAGON,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.FLYING,
            StatsEnum.HP: 95,
            StatsEnum.ATTACK: 145,
            StatsEnum.DEFENSE: 130,
            StatsEnum.SPECIAL_ATTACK: 120,
            StatsEnum.SPECIAL_DEFENSE: 90,
            StatsEnum.SPEED: 120
        }
    },
    "0374": {
        None: {
            PocketMonsterParamEnum.NAME: "Beldum",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.STEEL,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.PSYCHIC,
            StatsEnum.HP: 40,
            StatsEnum.ATTACK: 55,
            StatsEnum.DEFENSE: 80,
            StatsEnum.SPECIAL_ATTACK: 35,
            StatsEnum.SPECIAL_DEFENSE: 60,
            StatsEnum.SPEED: 30
        }
    },
    "0375": {
        None: {
            PocketMonsterParamEnum.NAME: "Metang",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.STEEL,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.PSYCHIC,
            StatsEnum.HP: 60,
            StatsEnum.ATTACK: 75,
            StatsEnum.DEFENSE: 100,
            StatsEnum.SPECIAL_ATTACK: 55,
            StatsEnum.SPECIAL_DEFENSE: 80,
            StatsEnum.SPEED: 50
        }
    },
    "0376": {
        None: {
            PocketMonsterParamEnum.NAME: "Metagross",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.STEEL,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.PSYCHIC,
            StatsEnum.HP: 80,
            StatsEnum.ATTACK: 135,
            StatsEnum.DEFENSE: 130,
            StatsEnum.SPECIAL_ATTACK: 95,
            StatsEnum.SPECIAL_DEFENSE: 90,
            StatsEnum.SPEED: 70
        },
        FormEnum.MEGA: {
            PocketMonsterParamEnum.NAME: "Metagross",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.STEEL,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.PSYCHIC,
            StatsEnum.HP: 80,
            StatsEnum.ATTACK: 145,
            StatsEnum.DEFENSE: 150,
            StatsEnum.SPECIAL_ATTACK: 105,
            StatsEnum.SPECIAL_DEFENSE: 110,
            StatsEnum.SPEED: 110
        }
    },
    "0377": {
        None: {
            PocketMonsterParamEnum.NAME: "Regirock",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.ROCK,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 80,
            StatsEnum.ATTACK: 100,
            StatsEnum.DEFENSE: 200,
            StatsEnum.SPECIAL_ATTACK: 50,
            StatsEnum.SPECIAL_DEFENSE: 100,
            StatsEnum.SPEED: 50
        }
    },
    "0378": {
        None: {
            PocketMonsterParamEnum.NAME: "Regice",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.ICE,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 80,
            StatsEnum.ATTACK: 50,
            StatsEnum.DEFENSE: 100,
            StatsEnum.SPECIAL_ATTACK: 100,
            StatsEnum.SPECIAL_DEFENSE: 200,
            StatsEnum.SPEED: 50
        }
    },
    "0379": {
        None: {
            PocketMonsterParamEnum.NAME: "Registeel",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.STEEL,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 80,
            StatsEnum.ATTACK: 75,
            StatsEnum.DEFENSE: 150,
            StatsEnum.SPECIAL_ATTACK: 75,
            StatsEnum.SPECIAL_DEFENSE: 150,
            StatsEnum.SPEED: 50
        }
    },
    "0380": {
        None: {
            PocketMonsterParamEnum.NAME: "Latias",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.DRAGON,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.PSYCHIC,
            StatsEnum.HP: 80,
            StatsEnum.ATTACK: 80,
            StatsEnum.DEFENSE: 90,
            StatsEnum.SPECIAL_ATTACK: 110,
            StatsEnum.SPECIAL_DEFENSE: 130,
            StatsEnum.SPEED: 110
        },
        FormEnum.MEGA: {
            PocketMonsterParamEnum.NAME: "Latias",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.DRAGON,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.PSYCHIC,
            StatsEnum.HP: 80,
            StatsEnum.ATTACK: 100,
            StatsEnum.DEFENSE: 120,
            StatsEnum.SPECIAL_ATTACK: 140,
            StatsEnum.SPECIAL_DEFENSE: 150,
            StatsEnum.SPEED: 110
        }
    },
    "0381": {
        None: {
            PocketMonsterParamEnum.NAME: "Latios",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.DRAGON,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.PSYCHIC,
            StatsEnum.HP: 80,
            StatsEnum.ATTACK: 90,
            StatsEnum.DEFENSE: 80,
            StatsEnum.SPECIAL_ATTACK: 130,
            StatsEnum.SPECIAL_DEFENSE: 110,
            StatsEnum.SPEED: 110
        },
        FormEnum.MEGA: {
            PocketMonsterParamEnum.NAME: "Latios",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.DRAGON,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.PSYCHIC,
            StatsEnum.HP: 80,
            StatsEnum.ATTACK: 130,
            StatsEnum.DEFENSE: 100,
            StatsEnum.SPECIAL_ATTACK: 160,
            StatsEnum.SPECIAL_DEFENSE: 120,
            StatsEnum.SPEED: 110
        }
    },
    "0382": {
        None: {
            PocketMonsterParamEnum.NAME: "Kyogre",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.WATER,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 100,
            StatsEnum.ATTACK: 100,
            StatsEnum.DEFENSE: 90,
            StatsEnum.SPECIAL_ATTACK: 150,
            StatsEnum.SPECIAL_DEFENSE: 140,
            StatsEnum.SPEED: 90
        },
        FormEnum.PRIMAL: {
            PocketMonsterParamEnum.NAME: "Kyogre",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.WATER,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 100,
            StatsEnum.ATTACK: 150,
            StatsEnum.DEFENSE: 90,
            StatsEnum.SPECIAL_ATTACK: 180,
            StatsEnum.SPECIAL_DEFENSE: 160,
            StatsEnum.SPEED: 90
        }
    },
    "0383": {
        None: {
            PocketMonsterParamEnum.NAME: "Groudon",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.GROUND,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 100,
            StatsEnum.ATTACK: 150,
            StatsEnum.DEFENSE: 140,
            StatsEnum.SPECIAL_ATTACK: 100,
            StatsEnum.SPECIAL_DEFENSE: 90,
            StatsEnum.SPEED: 90
        },
        FormEnum.PRIMAL: {
            PocketMonsterParamEnum.NAME: "Groudon",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.GROUND,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.FIRE,
            StatsEnum.HP: 100,
            StatsEnum.ATTACK: 180,
            StatsEnum.DEFENSE: 160,
            StatsEnum.SPECIAL_ATTACK: 150,
            StatsEnum.SPECIAL_DEFENSE: 90,
            StatsEnum.SPEED: 90
        }
    },
    "0384": {
        None: {
            PocketMonsterParamEnum.NAME: "Rayquaza",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.DRAGON,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.FLYING,
            StatsEnum.HP: 105,
            StatsEnum.ATTACK: 150,
            StatsEnum.DEFENSE: 90,
            StatsEnum.SPECIAL_ATTACK: 150,
            StatsEnum.SPECIAL_DEFENSE: 90,
            StatsEnum.SPEED: 95
        },
        FormEnum.MEGA: {
            PocketMonsterParamEnum.NAME: "Rayquaza",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.DRAGON,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.FLYING,
            StatsEnum.HP: 105,
            StatsEnum.ATTACK: 180,
            StatsEnum.DEFENSE: 100,
            StatsEnum.SPECIAL_ATTACK: 180,
            StatsEnum.SPECIAL_DEFENSE: 100,
            StatsEnum.SPEED: 115
        }
    },
    "0385": {
        None: {
            PocketMonsterParamEnum.NAME: "Jirachi",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.STEEL,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.PSYCHIC,
            StatsEnum.HP: 100,
            StatsEnum.ATTACK: 100,
            StatsEnum.DEFENSE: 100,
            StatsEnum.SPECIAL_ATTACK: 100,
            StatsEnum.SPECIAL_DEFENSE: 100,
            StatsEnum.SPEED: 100
        }
    },
    "0386": {
        FormEnum.NORMAL_FORME: {
            PocketMonsterParamEnum.NAME: "Deoxys",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.PSYCHIC,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 50,
            StatsEnum.ATTACK: 150,
            StatsEnum.DEFENSE: 50,
            StatsEnum.SPECIAL_ATTACK: 150,
            StatsEnum.SPECIAL_DEFENSE: 50,
            StatsEnum.SPEED: 150
        },
        FormEnum.ATTACK_FORME: {
            PocketMonsterParamEnum.NAME: "Deoxys",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.PSYCHIC,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 50,
            StatsEnum.ATTACK: 180,
            StatsEnum.DEFENSE: 20,
            StatsEnum.SPECIAL_ATTACK: 180,
            StatsEnum.SPECIAL_DEFENSE: 20,
            StatsEnum.SPEED: 150
        },
        FormEnum.DEFENSE_FORME: {
            PocketMonsterParamEnum.NAME: "Deoxys",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.PSYCHIC,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 50,
            StatsEnum.ATTACK: 70,
            StatsEnum.DEFENSE: 160,
            StatsEnum.SPECIAL_ATTACK: 70,
            StatsEnum.SPECIAL_DEFENSE: 160,
            StatsEnum.SPEED: 90
        },
        FormEnum.SPEED_FORME: {
            PocketMonsterParamEnum.NAME: "Deoxys",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.PSYCHIC,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 50,
            StatsEnum.ATTACK: 95,
            StatsEnum.DEFENSE: 90,
            StatsEnum.SPECIAL_ATTACK: 95,
            StatsEnum.SPECIAL_DEFENSE: 90,
            StatsEnum.SPEED: 180
        }
    },
    "0387": {
        None: {
            PocketMonsterParamEnum.NAME: "Turtwig",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.GRASS,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 55,
            StatsEnum.ATTACK: 68,
            StatsEnum.DEFENSE: 64,
            StatsEnum.SPECIAL_ATTACK: 45,
            StatsEnum.SPECIAL_DEFENSE: 55,
            StatsEnum.SPEED: 31
        }
    },
    "0388": {
        None: {
            PocketMonsterParamEnum.NAME: "Grotle",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.GRASS,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 75,
            StatsEnum.ATTACK: 89,
            StatsEnum.DEFENSE: 85,
            StatsEnum.SPECIAL_ATTACK: 55,
            StatsEnum.SPECIAL_DEFENSE: 65,
            StatsEnum.SPEED: 36
        }
    },
    "0389": {
        None: {
            PocketMonsterParamEnum.NAME: "Torterra",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.GRASS,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.GROUND,
            StatsEnum.HP: 95,
            StatsEnum.ATTACK: 109,
            StatsEnum.DEFENSE: 105,
            StatsEnum.SPECIAL_ATTACK: 75,
            StatsEnum.SPECIAL_DEFENSE: 85,
            StatsEnum.SPEED: 56
        }
    },
    "0390": {
        None: {
            PocketMonsterParamEnum.NAME: "Chimchar",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.FIRE,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 44,
            StatsEnum.ATTACK: 58,
            StatsEnum.DEFENSE: 44,
            StatsEnum.SPECIAL_ATTACK: 58,
            StatsEnum.SPECIAL_DEFENSE: 44,
            StatsEnum.SPEED: 61
        }
    },
    "0391": {
        None: {
            PocketMonsterParamEnum.NAME: "Monferno",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.FIRE,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.FIGHTING,
            StatsEnum.HP: 64,
            StatsEnum.ATTACK: 78,
            StatsEnum.DEFENSE: 52,
            StatsEnum.SPECIAL_ATTACK: 78,
            StatsEnum.SPECIAL_DEFENSE: 52,
            StatsEnum.SPEED: 81
        }
    },
    "0392": {
        None: {
            PocketMonsterParamEnum.NAME: "Infernape",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.FIRE,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.FIGHTING,
            StatsEnum.HP: 76,
            StatsEnum.ATTACK: 104,
            StatsEnum.DEFENSE: 71,
            StatsEnum.SPECIAL_ATTACK: 104,
            StatsEnum.SPECIAL_DEFENSE: 71,
            StatsEnum.SPEED: 108
        }
    },
    "0393": {
        None: {
            PocketMonsterParamEnum.NAME: "Piplup",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.WATER,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 53,
            StatsEnum.ATTACK: 51,
            StatsEnum.DEFENSE: 53,
            StatsEnum.SPECIAL_ATTACK: 61,
            StatsEnum.SPECIAL_DEFENSE: 56,
            StatsEnum.SPEED: 40
        }
    },
    "0394": {
        None: {
            PocketMonsterParamEnum.NAME: "Prinplup",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.WATER,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 64,
            StatsEnum.ATTACK: 66,
            StatsEnum.DEFENSE: 68,
            StatsEnum.SPECIAL_ATTACK: 81,
            StatsEnum.SPECIAL_DEFENSE: 76,
            StatsEnum.SPEED: 50
        }
    },
    "0395": {
        None: {
            PocketMonsterParamEnum.NAME: "Empoleon",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.WATER,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.STEEL,
            StatsEnum.HP: 84,
            StatsEnum.ATTACK: 86,
            StatsEnum.DEFENSE: 88,
            StatsEnum.SPECIAL_ATTACK: 111,
            StatsEnum.SPECIAL_DEFENSE: 101,
            StatsEnum.SPEED: 60
        }
    },
    "0396": {
        None: {
            PocketMonsterParamEnum.NAME: "Starly",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.NORMAL,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.FLYING,
            StatsEnum.HP: 40,
            StatsEnum.ATTACK: 55,
            StatsEnum.DEFENSE: 30,
            StatsEnum.SPECIAL_ATTACK: 30,
            StatsEnum.SPECIAL_DEFENSE: 30,
            StatsEnum.SPEED: 60
        }
    },
    "0397": {
        None: {
            PocketMonsterParamEnum.NAME: "Staravia",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.NORMAL,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.FLYING,
            StatsEnum.HP: 55,
            StatsEnum.ATTACK: 75,
            StatsEnum.DEFENSE: 50,
            StatsEnum.SPECIAL_ATTACK: 40,
            StatsEnum.SPECIAL_DEFENSE: 40,
            StatsEnum.SPEED: 80
        }
    },
    "0398": {
        None: {
            PocketMonsterParamEnum.NAME: "Staraptor",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.NORMAL,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.FLYING,
            StatsEnum.HP: 85,
            StatsEnum.ATTACK: 120,
            StatsEnum.DEFENSE: 70,
            StatsEnum.SPECIAL_ATTACK: 50,
            StatsEnum.SPECIAL_DEFENSE: 60,
            StatsEnum.SPEED: 100
        }
    },
    "0399": {
        None: {
            PocketMonsterParamEnum.NAME: "Bidoof",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.NORMAL,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 59,
            StatsEnum.ATTACK: 45,
            StatsEnum.DEFENSE: 40,
            StatsEnum.SPECIAL_ATTACK: 35,
            StatsEnum.SPECIAL_DEFENSE: 40,
            StatsEnum.SPEED: 31
        }
    },
    "0400": {
        None: {
            PocketMonsterParamEnum.NAME: "Bibarel",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.NORMAL,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.WATER,
            StatsEnum.HP: 79,
            StatsEnum.ATTACK: 85,
            StatsEnum.DEFENSE: 60,
            StatsEnum.SPECIAL_ATTACK: 55,
            StatsEnum.SPECIAL_DEFENSE: 60,
            StatsEnum.SPEED: 71
        }
    },
    "0401": {
        None: {
            PocketMonsterParamEnum.NAME: "Kricketot",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.BUG,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 37,
            StatsEnum.ATTACK: 25,
            StatsEnum.DEFENSE: 41,
            StatsEnum.SPECIAL_ATTACK: 25,
            StatsEnum.SPECIAL_DEFENSE: 41,
            StatsEnum.SPEED: 25
        }
    },
    "0402": {
        None: {
            PocketMonsterParamEnum.NAME: "Kricketune",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.BUG,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 77,
            StatsEnum.ATTACK: 85,
            StatsEnum.DEFENSE: 51,
            StatsEnum.SPECIAL_ATTACK: 55,
            StatsEnum.SPECIAL_DEFENSE: 51,
            StatsEnum.SPEED: 65
        }
    },
    "0403": {
        None: {
            PocketMonsterParamEnum.NAME: "Shinx",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.ELECTRIC,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 45,
            StatsEnum.ATTACK: 65,
            StatsEnum.DEFENSE: 34,
            StatsEnum.SPECIAL_ATTACK: 40,
            StatsEnum.SPECIAL_DEFENSE: 34,
            StatsEnum.SPEED: 45
        }
    },
    "0404": {
        None: {
            PocketMonsterParamEnum.NAME: "Luxio",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.ELECTRIC,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 60,
            StatsEnum.ATTACK: 85,
            StatsEnum.DEFENSE: 49,
            StatsEnum.SPECIAL_ATTACK: 60,
            StatsEnum.SPECIAL_DEFENSE: 49,
            StatsEnum.SPEED: 60
        }
    },
    "0405": {
        None: {
            PocketMonsterParamEnum.NAME: "Luxray",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.ELECTRIC,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 80,
            StatsEnum.ATTACK: 120,
            StatsEnum.DEFENSE: 79,
            StatsEnum.SPECIAL_ATTACK: 95,
            StatsEnum.SPECIAL_DEFENSE: 79,
            StatsEnum.SPEED: 70
        }
    },
    "0406": {
        None: {
            PocketMonsterParamEnum.NAME: "Budew",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.GRASS,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.POISON,
            StatsEnum.HP: 40,
            StatsEnum.ATTACK: 30,
            StatsEnum.DEFENSE: 35,
            StatsEnum.SPECIAL_ATTACK: 50,
            StatsEnum.SPECIAL_DEFENSE: 70,
            StatsEnum.SPEED: 55
        }
    },
    "0407": {
        None: {
            PocketMonsterParamEnum.NAME: "Roserade",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.GRASS,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.POISON,
            StatsEnum.HP: 60,
            StatsEnum.ATTACK: 70,
            StatsEnum.DEFENSE: 65,
            StatsEnum.SPECIAL_ATTACK: 125,
            StatsEnum.SPECIAL_DEFENSE: 105,
            StatsEnum.SPEED: 90
        }
    },
    "0408": {
        None: {
            PocketMonsterParamEnum.NAME: "Cranidos",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.ROCK,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 67,
            StatsEnum.ATTACK: 125,
            StatsEnum.DEFENSE: 40,
            StatsEnum.SPECIAL_ATTACK: 30,
            StatsEnum.SPECIAL_DEFENSE: 30,
            StatsEnum.SPEED: 58
        }
    },
    "0409": {
        None: {
            PocketMonsterParamEnum.NAME: "Rampardos",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.ROCK,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 97,
            StatsEnum.ATTACK: 165,
            StatsEnum.DEFENSE: 60,
            StatsEnum.SPECIAL_ATTACK: 65,
            StatsEnum.SPECIAL_DEFENSE: 50,
            StatsEnum.SPEED: 58
        }
    },
    "0410": {
        None: {
            PocketMonsterParamEnum.NAME: "Shieldon",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.ROCK,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.STEEL,
            StatsEnum.HP: 30,
            StatsEnum.ATTACK: 42,
            StatsEnum.DEFENSE: 118,
            StatsEnum.SPECIAL_ATTACK: 42,
            StatsEnum.SPECIAL_DEFENSE: 88,
            StatsEnum.SPEED: 30
        }
    },
    "0411": {
        None: {
            PocketMonsterParamEnum.NAME: "Bastiodon",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.ROCK,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.STEEL,
            StatsEnum.HP: 60,
            StatsEnum.ATTACK: 52,
            StatsEnum.DEFENSE: 168,
            StatsEnum.SPECIAL_ATTACK: 47,
            StatsEnum.SPECIAL_DEFENSE: 138,
            StatsEnum.SPEED: 30
        }
    },
    "0412": {
        FormEnum.PLANT_CLOAK: {
            PocketMonsterParamEnum.NAME: "Burmy",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.BUG,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 40,
            StatsEnum.ATTACK: 29,
            StatsEnum.DEFENSE: 45,
            StatsEnum.SPECIAL_ATTACK: 29,
            StatsEnum.SPECIAL_DEFENSE: 45,
            StatsEnum.SPEED: 36
        },
        FormEnum.SANDY_CLOAK: {
            PocketMonsterParamEnum.NAME: "Burmy",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.BUG,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 40,
            StatsEnum.ATTACK: 29,
            StatsEnum.DEFENSE: 45,
            StatsEnum.SPECIAL_ATTACK: 29,
            StatsEnum.SPECIAL_DEFENSE: 45,
            StatsEnum.SPEED: 36
        },
        FormEnum.TRASH_CLOAK: {
            PocketMonsterParamEnum.NAME: "Burmy",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.BUG,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 40,
            StatsEnum.ATTACK: 29,
            StatsEnum.DEFENSE: 45,
            StatsEnum.SPECIAL_ATTACK: 29,
            StatsEnum.SPECIAL_DEFENSE: 45,
            StatsEnum.SPEED: 36
        }
    },
    "0413": {
        FormEnum.PLANT_CLOAK: {
            PocketMonsterParamEnum.NAME: "Wormadam",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.BUG,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.GRASS,
            StatsEnum.HP: 60,
            StatsEnum.ATTACK: 59,
            StatsEnum.DEFENSE: 85,
            StatsEnum.SPECIAL_ATTACK: 79,
            StatsEnum.SPECIAL_DEFENSE: 105,
            StatsEnum.SPEED: 36
        },
        FormEnum.SANDY_CLOAK: {
            PocketMonsterParamEnum.NAME: "Wormadam",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.BUG,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.GROUND,
            StatsEnum.HP: 60,
            StatsEnum.ATTACK: 79,
            StatsEnum.DEFENSE: 105,
            StatsEnum.SPECIAL_ATTACK: 59,
            StatsEnum.SPECIAL_DEFENSE: 85,
            StatsEnum.SPEED: 36
        },
        FormEnum.TRASH_CLOAK: {
            PocketMonsterParamEnum.NAME: "Wormadam",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.BUG,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.STEEL,
            StatsEnum.HP: 60,
            StatsEnum.ATTACK: 69,
            StatsEnum.DEFENSE: 95,
            StatsEnum.SPECIAL_ATTACK: 69,
            StatsEnum.SPECIAL_DEFENSE: 95,
            StatsEnum.SPEED: 36
        }
    },
    "0414": {
        None: {
            PocketMonsterParamEnum.NAME: "Mothim",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.BUG,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.FLYING,
            StatsEnum.HP: 70,
            StatsEnum.ATTACK: 94,
            StatsEnum.DEFENSE: 50,
            StatsEnum.SPECIAL_ATTACK: 94,
            StatsEnum.SPECIAL_DEFENSE: 50,
            StatsEnum.SPEED: 66
        }
    },
    "0415": {
        None: {
            PocketMonsterParamEnum.NAME: "Combee",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.BUG,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.FLYING,
            StatsEnum.HP: 30,
            StatsEnum.ATTACK: 30,
            StatsEnum.DEFENSE: 42,
            StatsEnum.SPECIAL_ATTACK: 30,
            StatsEnum.SPECIAL_DEFENSE: 42,
            StatsEnum.SPEED: 70
        }
    },
    "0416": {
        None: {
            PocketMonsterParamEnum.NAME: "Vespiquen",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.BUG,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.FLYING,
            StatsEnum.HP: 70,
            StatsEnum.ATTACK: 80,
            StatsEnum.DEFENSE: 102,
            StatsEnum.SPECIAL_ATTACK: 80,
            StatsEnum.SPECIAL_DEFENSE: 102,
            StatsEnum.SPEED: 40
        }
    },
    "0417": {
        None: {
            PocketMonsterParamEnum.NAME: "Pachirisu",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.ELECTRIC,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 60,
            StatsEnum.ATTACK: 45,
            StatsEnum.DEFENSE: 70,
            StatsEnum.SPECIAL_ATTACK: 45,
            StatsEnum.SPECIAL_DEFENSE: 90,
            StatsEnum.SPEED: 95
        }
    },
    "0418": {
        None: {
            PocketMonsterParamEnum.NAME: "Buizel",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.WATER,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 55,
            StatsEnum.ATTACK: 65,
            StatsEnum.DEFENSE: 35,
            StatsEnum.SPECIAL_ATTACK: 60,
            StatsEnum.SPECIAL_DEFENSE: 30,
            StatsEnum.SPEED: 85
        }
    },
    "0419": {
        None: {
            PocketMonsterParamEnum.NAME: "Floatzel",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.WATER,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 85,
            StatsEnum.ATTACK: 105,
            StatsEnum.DEFENSE: 55,
            StatsEnum.SPECIAL_ATTACK: 85,
            StatsEnum.SPECIAL_DEFENSE: 50,
            StatsEnum.SPEED: 115
        }
    },
    "0420": {
        None: {
            PocketMonsterParamEnum.NAME: "Cherubi",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.GRASS,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 45,
            StatsEnum.ATTACK: 35,
            StatsEnum.DEFENSE: 45,
            StatsEnum.SPECIAL_ATTACK: 62,
            StatsEnum.SPECIAL_DEFENSE: 53,
            StatsEnum.SPEED: 35
        }
    },
    "0421": {
        None: {
            PocketMonsterParamEnum.NAME: "Cherrim",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.GRASS,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 70,
            StatsEnum.ATTACK: 60,
            StatsEnum.DEFENSE: 70,
            StatsEnum.SPECIAL_ATTACK: 87,
            StatsEnum.SPECIAL_DEFENSE: 78,
            StatsEnum.SPEED: 85
        }
    },
    "0422": {
        None: {
            PocketMonsterParamEnum.NAME: "Shellos",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.WATER,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 76,
            StatsEnum.ATTACK: 48,
            StatsEnum.DEFENSE: 48,
            StatsEnum.SPECIAL_ATTACK: 57,
            StatsEnum.SPECIAL_DEFENSE: 62,
            StatsEnum.SPEED: 34
        }
    },
    "0423": {
        None: {
            PocketMonsterParamEnum.NAME: "Gastrodon",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.WATER,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.GROUND,
            StatsEnum.HP: 111,
            StatsEnum.ATTACK: 83,
            StatsEnum.DEFENSE: 68,
            StatsEnum.SPECIAL_ATTACK: 92,
            StatsEnum.SPECIAL_DEFENSE: 82,
            StatsEnum.SPEED: 39
        }
    },
    "0424": {
        None: {
            PocketMonsterParamEnum.NAME: "Ambipom",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.NORMAL,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 75,
            StatsEnum.ATTACK: 100,
            StatsEnum.DEFENSE: 66,
            StatsEnum.SPECIAL_ATTACK: 60,
            StatsEnum.SPECIAL_DEFENSE: 66,
            StatsEnum.SPEED: 115
        }
    },
    "0425": {
        None: {
            PocketMonsterParamEnum.NAME: "Drifloon",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.GHOST,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.FLYING,
            StatsEnum.HP: 90,
            StatsEnum.ATTACK: 50,
            StatsEnum.DEFENSE: 34,
            StatsEnum.SPECIAL_ATTACK: 60,
            StatsEnum.SPECIAL_DEFENSE: 44,
            StatsEnum.SPEED: 70
        }
    },
    "0426": {
        None: {
            PocketMonsterParamEnum.NAME: "Drifblim",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.GHOST,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.FLYING,
            StatsEnum.HP: 150,
            StatsEnum.ATTACK: 80,
            StatsEnum.DEFENSE: 44,
            StatsEnum.SPECIAL_ATTACK: 90,
            StatsEnum.SPECIAL_DEFENSE: 54,
            StatsEnum.SPEED: 80
        }
    },
    "0427": {
        None: {
            PocketMonsterParamEnum.NAME: "Buneary",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.NORMAL,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 55,
            StatsEnum.ATTACK: 66,
            StatsEnum.DEFENSE: 44,
            StatsEnum.SPECIAL_ATTACK: 44,
            StatsEnum.SPECIAL_DEFENSE: 56,
            StatsEnum.SPEED: 85
        }
    },
    "0428": {
        None: {
            PocketMonsterParamEnum.NAME: "Lopunny",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.NORMAL,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 65,
            StatsEnum.ATTACK: 76,
            StatsEnum.DEFENSE: 84,
            StatsEnum.SPECIAL_ATTACK: 54,
            StatsEnum.SPECIAL_DEFENSE: 96,
            StatsEnum.SPEED: 105
        },
        FormEnum.MEGA: {
            PocketMonsterParamEnum.NAME: "Lopunny",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.NORMAL,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.FIGHTING,
            StatsEnum.HP: 65,
            StatsEnum.ATTACK: 136,
            StatsEnum.DEFENSE: 94,
            StatsEnum.SPECIAL_ATTACK: 54,
            StatsEnum.SPECIAL_DEFENSE: 96,
            StatsEnum.SPEED: 135
        }
    },
    "0429": {
        None: {
            PocketMonsterParamEnum.NAME: "Mismagius",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.GHOST,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 60,
            StatsEnum.ATTACK: 60,
            StatsEnum.DEFENSE: 60,
            StatsEnum.SPECIAL_ATTACK: 105,
            StatsEnum.SPECIAL_DEFENSE: 105,
            StatsEnum.SPEED: 105
        }
    },
    "0430": {
        None: {
            PocketMonsterParamEnum.NAME: "Honchkrow",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.DARK,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.FLYING,
            StatsEnum.HP: 100,
            StatsEnum.ATTACK: 125,
            StatsEnum.DEFENSE: 52,
            StatsEnum.SPECIAL_ATTACK: 105,
            StatsEnum.SPECIAL_DEFENSE: 52,
            StatsEnum.SPEED: 71
        }
    },
    "0431": {
        None: {
            PocketMonsterParamEnum.NAME: "Glameow",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.NORMAL,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 49,
            StatsEnum.ATTACK: 55,
            StatsEnum.DEFENSE: 42,
            StatsEnum.SPECIAL_ATTACK: 42,
            StatsEnum.SPECIAL_DEFENSE: 37,
            StatsEnum.SPEED: 85
        }
    },
    "0432": {
        None: {
            PocketMonsterParamEnum.NAME: "Purugly",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.NORMAL,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 71,
            StatsEnum.ATTACK: 82,
            StatsEnum.DEFENSE: 64,
            StatsEnum.SPECIAL_ATTACK: 64,
            StatsEnum.SPECIAL_DEFENSE: 59,
            StatsEnum.SPEED: 112
        }
    },
    "0433": {
        None: {
            PocketMonsterParamEnum.NAME: "Chingling",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.PSYCHIC,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 45,
            StatsEnum.ATTACK: 30,
            StatsEnum.DEFENSE: 50,
            StatsEnum.SPECIAL_ATTACK: 65,
            StatsEnum.SPECIAL_DEFENSE: 50,
            StatsEnum.SPEED: 45
        }
    },
    "0434": {
        None: {
            PocketMonsterParamEnum.NAME: "Stunky",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.POISON,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.DARK,
            StatsEnum.HP: 63,
            StatsEnum.ATTACK: 63,
            StatsEnum.DEFENSE: 47,
            StatsEnum.SPECIAL_ATTACK: 41,
            StatsEnum.SPECIAL_DEFENSE: 41,
            StatsEnum.SPEED: 74
        }
    },
    "0435": {
        None: {
            PocketMonsterParamEnum.NAME: "Skuntank",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.POISON,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.DARK,
            StatsEnum.HP: 103,
            StatsEnum.ATTACK: 93,
            StatsEnum.DEFENSE: 67,
            StatsEnum.SPECIAL_ATTACK: 71,
            StatsEnum.SPECIAL_DEFENSE: 61,
            StatsEnum.SPEED: 84
        }
    },
    "0436": {
        None: {
            PocketMonsterParamEnum.NAME: "Bronzor",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.STEEL,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.PSYCHIC,
            StatsEnum.HP: 57,
            StatsEnum.ATTACK: 24,
            StatsEnum.DEFENSE: 86,
            StatsEnum.SPECIAL_ATTACK: 24,
            StatsEnum.SPECIAL_DEFENSE: 86,
            StatsEnum.SPEED: 23
        }
    },
    "0437": {
        None: {
            PocketMonsterParamEnum.NAME: "Bronzong",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.STEEL,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.PSYCHIC,
            StatsEnum.HP: 67,
            StatsEnum.ATTACK: 89,
            StatsEnum.DEFENSE: 116,
            StatsEnum.SPECIAL_ATTACK: 79,
            StatsEnum.SPECIAL_DEFENSE: 116,
            StatsEnum.SPEED: 33
        }
    },
    "0438": {
        None: {
            PocketMonsterParamEnum.NAME: "Bonsly",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.ROCK,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 50,
            StatsEnum.ATTACK: 80,
            StatsEnum.DEFENSE: 95,
            StatsEnum.SPECIAL_ATTACK: 10,
            StatsEnum.SPECIAL_DEFENSE: 45,
            StatsEnum.SPEED: 10
        }
    },
    "0439": {
        None: {
            PocketMonsterParamEnum.NAME: "Mime Jr.",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.PSYCHIC,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.FAIRY,
            StatsEnum.HP: 20,
            StatsEnum.ATTACK: 25,
            StatsEnum.DEFENSE: 45,
            StatsEnum.SPECIAL_ATTACK: 70,
            StatsEnum.SPECIAL_DEFENSE: 90,
            StatsEnum.SPEED: 60
        }
    },
    "0440": {
        None: {
            PocketMonsterParamEnum.NAME: "Happiny",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.NORMAL,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 100,
            StatsEnum.ATTACK: 5,
            StatsEnum.DEFENSE: 5,
            StatsEnum.SPECIAL_ATTACK: 15,
            StatsEnum.SPECIAL_DEFENSE: 65,
            StatsEnum.SPEED: 30
        }
    },
    "0441": {
        None: {
            PocketMonsterParamEnum.NAME: "Chatot",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.NORMAL,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.FLYING,
            StatsEnum.HP: 76,
            StatsEnum.ATTACK: 65,
            StatsEnum.DEFENSE: 45,
            StatsEnum.SPECIAL_ATTACK: 92,
            StatsEnum.SPECIAL_DEFENSE: 42,
            StatsEnum.SPEED: 91
        }
    },
    "0442": {
        None: {
            PocketMonsterParamEnum.NAME: "Spiritomb",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.GHOST,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.DARK,
            StatsEnum.HP: 50,
            StatsEnum.ATTACK: 92,
            StatsEnum.DEFENSE: 108,
            StatsEnum.SPECIAL_ATTACK: 92,
            StatsEnum.SPECIAL_DEFENSE: 108,
            StatsEnum.SPEED: 35
        }
    },
    "0443": {
        None: {
            PocketMonsterParamEnum.NAME: "Gible",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.DRAGON,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.GROUND,
            StatsEnum.HP: 58,
            StatsEnum.ATTACK: 70,
            StatsEnum.DEFENSE: 45,
            StatsEnum.SPECIAL_ATTACK: 40,
            StatsEnum.SPECIAL_DEFENSE: 45,
            StatsEnum.SPEED: 42
        }
    },
    "0444": {
        None: {
            PocketMonsterParamEnum.NAME: "Gabite",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.DRAGON,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.GROUND,
            StatsEnum.HP: 68,
            StatsEnum.ATTACK: 90,
            StatsEnum.DEFENSE: 65,
            StatsEnum.SPECIAL_ATTACK: 50,
            StatsEnum.SPECIAL_DEFENSE: 55,
            StatsEnum.SPEED: 82
        }
    },
    "0445": {
        None: {
            PocketMonsterParamEnum.NAME: "Garchomp",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.DRAGON,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.GROUND,
            StatsEnum.HP: 108,
            StatsEnum.ATTACK: 130,
            StatsEnum.DEFENSE: 95,
            StatsEnum.SPECIAL_ATTACK: 80,
            StatsEnum.SPECIAL_DEFENSE: 85,
            StatsEnum.SPEED: 102
        },
        FormEnum.MEGA: {
            PocketMonsterParamEnum.NAME: "Garchomp",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.DRAGON,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.GROUND,
            StatsEnum.HP: 108,
            StatsEnum.ATTACK: 170,
            StatsEnum.DEFENSE: 115,
            StatsEnum.SPECIAL_ATTACK: 120,
            StatsEnum.SPECIAL_DEFENSE: 95,
            StatsEnum.SPEED: 92
        }
    },
    "0446": {
        None: {
            PocketMonsterParamEnum.NAME: "Munchlax",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.NORMAL,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 135,
            StatsEnum.ATTACK: 85,
            StatsEnum.DEFENSE: 40,
            StatsEnum.SPECIAL_ATTACK: 40,
            StatsEnum.SPECIAL_DEFENSE: 85,
            StatsEnum.SPEED: 5
        }
    },
    "0447": {
        None: {
            PocketMonsterParamEnum.NAME: "Riolu",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.FIGHTING,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 40,
            StatsEnum.ATTACK: 70,
            StatsEnum.DEFENSE: 40,
            StatsEnum.SPECIAL_ATTACK: 35,
            StatsEnum.SPECIAL_DEFENSE: 40,
            StatsEnum.SPEED: 60
        }
    },
    "0448": {
        None: {
            PocketMonsterParamEnum.NAME: "Lucario",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.FIGHTING,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.STEEL,
            StatsEnum.HP: 70,
            StatsEnum.ATTACK: 110,
            StatsEnum.DEFENSE: 70,
            StatsEnum.SPECIAL_ATTACK: 115,
            StatsEnum.SPECIAL_DEFENSE: 70,
            StatsEnum.SPEED: 90
        },
        FormEnum.MEGA: {
            PocketMonsterParamEnum.NAME: "Lucario",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.FIGHTING,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.STEEL,
            StatsEnum.HP: 70,
            StatsEnum.ATTACK: 145,
            StatsEnum.DEFENSE: 88,
            StatsEnum.SPECIAL_ATTACK: 140,
            StatsEnum.SPECIAL_DEFENSE: 70,
            StatsEnum.SPEED: 112
        }
    },
    "0449": {
        None: {
            PocketMonsterParamEnum.NAME: "Hippopotas",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.GROUND,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 68,
            StatsEnum.ATTACK: 72,
            StatsEnum.DEFENSE: 78,
            StatsEnum.SPECIAL_ATTACK: 38,
            StatsEnum.SPECIAL_DEFENSE: 42,
            StatsEnum.SPEED: 32
        }
    },
    "0450": {
        None: {
            PocketMonsterParamEnum.NAME: "Hippowdon",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.GROUND,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 108,
            StatsEnum.ATTACK: 112,
            StatsEnum.DEFENSE: 118,
            StatsEnum.SPECIAL_ATTACK: 68,
            StatsEnum.SPECIAL_DEFENSE: 72,
            StatsEnum.SPEED: 47
        }
    },
    "0451": {
        None: {
            PocketMonsterParamEnum.NAME: "Skorupi",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.POISON,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.BUG,
            StatsEnum.HP: 40,
            StatsEnum.ATTACK: 50,
            StatsEnum.DEFENSE: 90,
            StatsEnum.SPECIAL_ATTACK: 30,
            StatsEnum.SPECIAL_DEFENSE: 55,
            StatsEnum.SPEED: 65
        }
    },
    "0452": {
        None: {
            PocketMonsterParamEnum.NAME: "Drapion",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.POISON,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.DARK,
            StatsEnum.HP: 70,
            StatsEnum.ATTACK: 90,
            StatsEnum.DEFENSE: 110,
            StatsEnum.SPECIAL_ATTACK: 60,
            StatsEnum.SPECIAL_DEFENSE: 75,
            StatsEnum.SPEED: 95
        }
    },
    "0453": {
        None: {
            PocketMonsterParamEnum.NAME: "Croagunk",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.POISON,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.FIGHTING,
            StatsEnum.HP: 48,
            StatsEnum.ATTACK: 61,
            StatsEnum.DEFENSE: 40,
            StatsEnum.SPECIAL_ATTACK: 61,
            StatsEnum.SPECIAL_DEFENSE: 40,
            StatsEnum.SPEED: 50
        }
    },
    "0454": {
        None: {
            PocketMonsterParamEnum.NAME: "Toxicroak",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.POISON,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.FIGHTING,
            StatsEnum.HP: 83,
            StatsEnum.ATTACK: 106,
            StatsEnum.DEFENSE: 65,
            StatsEnum.SPECIAL_ATTACK: 86,
            StatsEnum.SPECIAL_DEFENSE: 65,
            StatsEnum.SPEED: 85
        }
    },
    "0455": {
        None: {
            PocketMonsterParamEnum.NAME: "Carnivine",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.GRASS,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 74,
            StatsEnum.ATTACK: 100,
            StatsEnum.DEFENSE: 72,
            StatsEnum.SPECIAL_ATTACK: 90,
            StatsEnum.SPECIAL_DEFENSE: 72,
            StatsEnum.SPEED: 46
        }
    },
    "0456": {
        None: {
            PocketMonsterParamEnum.NAME: "Finneon",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.WATER,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 49,
            StatsEnum.ATTACK: 49,
            StatsEnum.DEFENSE: 56,
            StatsEnum.SPECIAL_ATTACK: 49,
            StatsEnum.SPECIAL_DEFENSE: 61,
            StatsEnum.SPEED: 66
        }
    },
    "0457": {
        None: {
            PocketMonsterParamEnum.NAME: "Lumineon",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.WATER,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 69,
            StatsEnum.ATTACK: 69,
            StatsEnum.DEFENSE: 76,
            StatsEnum.SPECIAL_ATTACK: 69,
            StatsEnum.SPECIAL_DEFENSE: 86,
            StatsEnum.SPEED: 91
        }
    },
    "0458": {
        None: {
            PocketMonsterParamEnum.NAME: "Mantyke",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.WATER,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.FLYING,
            StatsEnum.HP: 45,
            StatsEnum.ATTACK: 20,
            StatsEnum.DEFENSE: 50,
            StatsEnum.SPECIAL_ATTACK: 60,
            StatsEnum.SPECIAL_DEFENSE: 120,
            StatsEnum.SPEED: 50
        }
    },
    "0459": {
        None: {
            PocketMonsterParamEnum.NAME: "Snover",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.GRASS,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.ICE,
            StatsEnum.HP: 60,
            StatsEnum.ATTACK: 62,
            StatsEnum.DEFENSE: 50,
            StatsEnum.SPECIAL_ATTACK: 62,
            StatsEnum.SPECIAL_DEFENSE: 60,
            StatsEnum.SPEED: 40
        }
    },
    "0460": {
        None: {
            PocketMonsterParamEnum.NAME: "Abomasnow",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.GRASS,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.ICE,
            StatsEnum.HP: 90,
            StatsEnum.ATTACK: 92,
            StatsEnum.DEFENSE: 75,
            StatsEnum.SPECIAL_ATTACK: 92,
            StatsEnum.SPECIAL_DEFENSE: 85,
            StatsEnum.SPEED: 60
        },
        FormEnum.MEGA: {
            PocketMonsterParamEnum.NAME: "Abomasnow",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.GRASS,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.ICE,
            StatsEnum.HP: 90,
            StatsEnum.ATTACK: 132,
            StatsEnum.DEFENSE: 105,
            StatsEnum.SPECIAL_ATTACK: 132,
            StatsEnum.SPECIAL_DEFENSE: 105,
            StatsEnum.SPEED: 30
        }
    },
    "0461": {
        None: {
            PocketMonsterParamEnum.NAME: "Weavile",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.DARK,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.ICE,
            StatsEnum.HP: 70,
            StatsEnum.ATTACK: 120,
            StatsEnum.DEFENSE: 65,
            StatsEnum.SPECIAL_ATTACK: 45,
            StatsEnum.SPECIAL_DEFENSE: 85,
            StatsEnum.SPEED: 125
        }
    },
    "0462": {
        None: {
            PocketMonsterParamEnum.NAME: "Magnezone",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.ELECTRIC,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.STEEL,
            StatsEnum.HP: 70,
            StatsEnum.ATTACK: 70,
            StatsEnum.DEFENSE: 115,
            StatsEnum.SPECIAL_ATTACK: 130,
            StatsEnum.SPECIAL_DEFENSE: 90,
            StatsEnum.SPEED: 60
        }
    },
    "0463": {
        None: {
            PocketMonsterParamEnum.NAME: "Lickilicky",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.NORMAL,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 110,
            StatsEnum.ATTACK: 85,
            StatsEnum.DEFENSE: 95,
            StatsEnum.SPECIAL_ATTACK: 80,
            StatsEnum.SPECIAL_DEFENSE: 95,
            StatsEnum.SPEED: 50
        }
    },
    "0464": {
        None: {
            PocketMonsterParamEnum.NAME: "Rhyperior",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.GROUND,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.ROCK,
            StatsEnum.HP: 115,
            StatsEnum.ATTACK: 140,
            StatsEnum.DEFENSE: 130,
            StatsEnum.SPECIAL_ATTACK: 55,
            StatsEnum.SPECIAL_DEFENSE: 55,
            StatsEnum.SPEED: 40
        }
    },
    "0465": {
        None: {
            PocketMonsterParamEnum.NAME: "Tangrowth",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.GRASS,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 100,
            StatsEnum.ATTACK: 100,
            StatsEnum.DEFENSE: 125,
            StatsEnum.SPECIAL_ATTACK: 110,
            StatsEnum.SPECIAL_DEFENSE: 50,
            StatsEnum.SPEED: 50
        }
    },
    "0466": {
        None: {
            PocketMonsterParamEnum.NAME: "Electivire",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.ELECTRIC,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 75,
            StatsEnum.ATTACK: 123,
            StatsEnum.DEFENSE: 67,
            StatsEnum.SPECIAL_ATTACK: 95,
            StatsEnum.SPECIAL_DEFENSE: 85,
            StatsEnum.SPEED: 95
        }
    },
    "0467": {
        None: {
            PocketMonsterParamEnum.NAME: "Magmortar",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.FIRE,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 75,
            StatsEnum.ATTACK: 95,
            StatsEnum.DEFENSE: 67,
            StatsEnum.SPECIAL_ATTACK: 125,
            StatsEnum.SPECIAL_DEFENSE: 95,
            StatsEnum.SPEED: 83
        }
    },
    "0468": {
        None: {
            PocketMonsterParamEnum.NAME: "Togekiss",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.FAIRY,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.FLYING,
            StatsEnum.HP: 85,
            StatsEnum.ATTACK: 50,
            StatsEnum.DEFENSE: 95,
            StatsEnum.SPECIAL_ATTACK: 120,
            StatsEnum.SPECIAL_DEFENSE: 115,
            StatsEnum.SPEED: 80
        }
    },
    "0469": {
        None: {
            PocketMonsterParamEnum.NAME: "Yanmega",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.BUG,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.FLYING,
            StatsEnum.HP: 86,
            StatsEnum.ATTACK: 76,
            StatsEnum.DEFENSE: 86,
            StatsEnum.SPECIAL_ATTACK: 116,
            StatsEnum.SPECIAL_DEFENSE: 56,
            StatsEnum.SPEED: 95
        }
    },
    "0470": {
        None: {
            PocketMonsterParamEnum.NAME: "Leafeon",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.GRASS,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 65,
            StatsEnum.ATTACK: 110,
            StatsEnum.DEFENSE: 130,
            StatsEnum.SPECIAL_ATTACK: 60,
            StatsEnum.SPECIAL_DEFENSE: 65,
            StatsEnum.SPEED: 95
        }
    },
    "0471": {
        None: {
            PocketMonsterParamEnum.NAME: "Glaceon",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.ICE,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 65,
            StatsEnum.ATTACK: 60,
            StatsEnum.DEFENSE: 110,
            StatsEnum.SPECIAL_ATTACK: 130,
            StatsEnum.SPECIAL_DEFENSE: 95,
            StatsEnum.SPEED: 65
        }
    },
    "0472": {
        None: {
            PocketMonsterParamEnum.NAME: "Gliscor",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.GROUND,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.FLYING,
            StatsEnum.HP: 75,
            StatsEnum.ATTACK: 95,
            StatsEnum.DEFENSE: 125,
            StatsEnum.SPECIAL_ATTACK: 45,
            StatsEnum.SPECIAL_DEFENSE: 75,
            StatsEnum.SPEED: 95
        }
    },
    "0473": {
        None: {
            PocketMonsterParamEnum.NAME: "Mamoswine",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.ICE,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.GROUND,
            StatsEnum.HP: 110,
            StatsEnum.ATTACK: 130,
            StatsEnum.DEFENSE: 80,
            StatsEnum.SPECIAL_ATTACK: 70,
            StatsEnum.SPECIAL_DEFENSE: 60,
            StatsEnum.SPEED: 80
        }
    },
    "0474": {
        None: {
            PocketMonsterParamEnum.NAME: "Porygon-Z",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.NORMAL,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 85,
            StatsEnum.ATTACK: 80,
            StatsEnum.DEFENSE: 70,
            StatsEnum.SPECIAL_ATTACK: 135,
            StatsEnum.SPECIAL_DEFENSE: 75,
            StatsEnum.SPEED: 90
        }
    },
    "0475": {
        None: {
            PocketMonsterParamEnum.NAME: "Gallade",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.PSYCHIC,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.FIGHTING,
            StatsEnum.HP: 68,
            StatsEnum.ATTACK: 125,
            StatsEnum.DEFENSE: 65,
            StatsEnum.SPECIAL_ATTACK: 65,
            StatsEnum.SPECIAL_DEFENSE: 115,
            StatsEnum.SPEED: 80
        },
        FormEnum.MEGA: {
            PocketMonsterParamEnum.NAME: "Gallade",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.PSYCHIC,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.FIGHTING,
            StatsEnum.HP: 68,
            StatsEnum.ATTACK: 165,
            StatsEnum.DEFENSE: 95,
            StatsEnum.SPECIAL_ATTACK: 65,
            StatsEnum.SPECIAL_DEFENSE: 115,
            StatsEnum.SPEED: 110
        }
    },
    "0476": {
        None: {
            PocketMonsterParamEnum.NAME: "Probopass",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.ROCK,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.STEEL,
            StatsEnum.HP: 60,
            StatsEnum.ATTACK: 55,
            StatsEnum.DEFENSE: 145,
            StatsEnum.SPECIAL_ATTACK: 75,
            StatsEnum.SPECIAL_DEFENSE: 150,
            StatsEnum.SPEED: 40
        }
    },
    "0477": {
        None: {
            PocketMonsterParamEnum.NAME: "Dusknoir",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.GHOST,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 45,
            StatsEnum.ATTACK: 100,
            StatsEnum.DEFENSE: 135,
            StatsEnum.SPECIAL_ATTACK: 65,
            StatsEnum.SPECIAL_DEFENSE: 135,
            StatsEnum.SPEED: 45
        }
    },
    "0478": {
        None: {
            PocketMonsterParamEnum.NAME: "Froslass",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.ICE,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.GHOST,
            StatsEnum.HP: 70,
            StatsEnum.ATTACK: 80,
            StatsEnum.DEFENSE: 70,
            StatsEnum.SPECIAL_ATTACK: 80,
            StatsEnum.SPECIAL_DEFENSE: 70,
            StatsEnum.SPEED: 110
        }
    },
    "0479": {
        None: {
            PocketMonsterParamEnum.NAME: "Rotom",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.ELECTRIC,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.GHOST,
            StatsEnum.HP: 50,
            StatsEnum.ATTACK: 50,
            StatsEnum.DEFENSE: 77,
            StatsEnum.SPECIAL_ATTACK: 95,
            StatsEnum.SPECIAL_DEFENSE: 77,
            StatsEnum.SPEED: 91
        },
        FormEnum.HEAT: {
            PocketMonsterParamEnum.NAME: "Rotom",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.ELECTRIC,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.FIRE,
            StatsEnum.HP: 50,
            StatsEnum.ATTACK: 65,
            StatsEnum.DEFENSE: 107,
            StatsEnum.SPECIAL_ATTACK: 105,
            StatsEnum.SPECIAL_DEFENSE: 107,
            StatsEnum.SPEED: 86
        },
        FormEnum.WASH: {
            PocketMonsterParamEnum.NAME: "Rotom",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.ELECTRIC,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.WATER,
            StatsEnum.HP: 50,
            StatsEnum.ATTACK: 65,
            StatsEnum.DEFENSE: 107,
            StatsEnum.SPECIAL_ATTACK: 105,
            StatsEnum.SPECIAL_DEFENSE: 107,
            StatsEnum.SPEED: 86
        },
        FormEnum.FROST: {
            PocketMonsterParamEnum.NAME: "Rotom",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.ELECTRIC,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.ICE,
            StatsEnum.HP: 50,
            StatsEnum.ATTACK: 65,
            StatsEnum.DEFENSE: 107,
            StatsEnum.SPECIAL_ATTACK: 105,
            StatsEnum.SPECIAL_DEFENSE: 107,
            StatsEnum.SPEED: 86
        },
        FormEnum.FAN: {
            PocketMonsterParamEnum.NAME: "Rotom",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.ELECTRIC,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.FLYING,
            StatsEnum.HP: 50,
            StatsEnum.ATTACK: 65,
            StatsEnum.DEFENSE: 107,
            StatsEnum.SPECIAL_ATTACK: 105,
            StatsEnum.SPECIAL_DEFENSE: 107,
            StatsEnum.SPEED: 86
        },
        FormEnum.MOW: {
            PocketMonsterParamEnum.NAME: "Rotom",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.ELECTRIC,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.GRASS,
            StatsEnum.HP: 50,
            StatsEnum.ATTACK: 65,
            StatsEnum.DEFENSE: 107,
            StatsEnum.SPECIAL_ATTACK: 105,
            StatsEnum.SPECIAL_DEFENSE: 107,
            StatsEnum.SPEED: 86
        }
    },
    "0480": {
        None: {
            PocketMonsterParamEnum.NAME: "Uxie",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.PSYCHIC,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 75,
            StatsEnum.ATTACK: 75,
            StatsEnum.DEFENSE: 130,
            StatsEnum.SPECIAL_ATTACK: 75,
            StatsEnum.SPECIAL_DEFENSE: 130,
            StatsEnum.SPEED: 95
        }
    },
    "0481": {
        None: {
            PocketMonsterParamEnum.NAME: "Mesprit",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.PSYCHIC,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 80,
            StatsEnum.ATTACK: 105,
            StatsEnum.DEFENSE: 105,
            StatsEnum.SPECIAL_ATTACK: 105,
            StatsEnum.SPECIAL_DEFENSE: 105,
            StatsEnum.SPEED: 80
        }
    },
    "0482": {
        None: {
            PocketMonsterParamEnum.NAME: "Azelf",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.PSYCHIC,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 75,
            StatsEnum.ATTACK: 125,
            StatsEnum.DEFENSE: 70,
            StatsEnum.SPECIAL_ATTACK: 125,
            StatsEnum.SPECIAL_DEFENSE: 70,
            StatsEnum.SPEED: 115
        }
    },
    "0483": {
        None: {
            PocketMonsterParamEnum.NAME: "Dialga",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.STEEL,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.DRAGON,
            StatsEnum.HP: 100,
            StatsEnum.ATTACK: 120,
            StatsEnum.DEFENSE: 120,
            StatsEnum.SPECIAL_ATTACK: 150,
            StatsEnum.SPECIAL_DEFENSE: 100,
            StatsEnum.SPEED: 90
        },
        FormEnum.ORIGIN_FORME: {
            PocketMonsterParamEnum.NAME: "Dialga",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.STEEL,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.DRAGON,
            StatsEnum.HP: 100,
            StatsEnum.ATTACK: 100,
            StatsEnum.DEFENSE: 120,
            StatsEnum.SPECIAL_ATTACK: 150,
            StatsEnum.SPECIAL_DEFENSE: 120,
            StatsEnum.SPEED: 90
        }
    },
    "0484": {
        None: {
            PocketMonsterParamEnum.NAME: "Palkia",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.WATER,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.DRAGON,
            StatsEnum.HP: 90,
            StatsEnum.ATTACK: 120,
            StatsEnum.DEFENSE: 100,
            StatsEnum.SPECIAL_ATTACK: 150,
            StatsEnum.SPECIAL_DEFENSE: 120,
            StatsEnum.SPEED: 100
        },
        FormEnum.ORIGIN_FORME: {
            PocketMonsterParamEnum.NAME: "Palkia",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.WATER,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.DRAGON,
            StatsEnum.HP: 90,
            StatsEnum.ATTACK: 100,
            StatsEnum.DEFENSE: 100,
            StatsEnum.SPECIAL_ATTACK: 150,
            StatsEnum.SPECIAL_DEFENSE: 120,
            StatsEnum.SPEED: 120
        }
    },
    "0485": {
        None: {
            PocketMonsterParamEnum.NAME: "Heatran",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.FIRE,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.STEEL,
            StatsEnum.HP: 91,
            StatsEnum.ATTACK: 90,
            StatsEnum.DEFENSE: 106,
            StatsEnum.SPECIAL_ATTACK: 130,
            StatsEnum.SPECIAL_DEFENSE: 106,
            StatsEnum.SPEED: 77
        }
    },
    "0486": {
        None: {
            PocketMonsterParamEnum.NAME: "Regigigas",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.NORMAL,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 110,
            StatsEnum.ATTACK: 160,
            StatsEnum.DEFENSE: 110,
            StatsEnum.SPECIAL_ATTACK: 80,
            StatsEnum.SPECIAL_DEFENSE: 110,
            StatsEnum.SPEED: 100
        }
    },
    "0487": {
        FormEnum.ALTERED_FORME: {
            PocketMonsterParamEnum.NAME: "Giratina",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.GHOST,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.DRAGON,
            StatsEnum.HP: 150,
            StatsEnum.ATTACK: 100,
            StatsEnum.DEFENSE: 120,
            StatsEnum.SPECIAL_ATTACK: 100,
            StatsEnum.SPECIAL_DEFENSE: 120,
            StatsEnum.SPEED: 90
        },
        FormEnum.ORIGIN_FORME: {
            PocketMonsterParamEnum.NAME: "Giratina",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.GHOST,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.DRAGON,
            StatsEnum.HP: 150,
            StatsEnum.ATTACK: 120,
            StatsEnum.DEFENSE: 100,
            StatsEnum.SPECIAL_ATTACK: 120,
            StatsEnum.SPECIAL_DEFENSE: 100,
            StatsEnum.SPEED: 90
        }
    },
    "0488": {
        None: {
            PocketMonsterParamEnum.NAME: "Cresselia",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.PSYCHIC,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 120,
            StatsEnum.ATTACK: 70,
            StatsEnum.DEFENSE: 110,
            StatsEnum.SPECIAL_ATTACK: 75,
            StatsEnum.SPECIAL_DEFENSE: 120,
            StatsEnum.SPEED: 85
        }
    },
    "0489": {
        None: {
            PocketMonsterParamEnum.NAME: "Phione",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.WATER,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 80,
            StatsEnum.ATTACK: 80,
            StatsEnum.DEFENSE: 80,
            StatsEnum.SPECIAL_ATTACK: 80,
            StatsEnum.SPECIAL_DEFENSE: 80,
            StatsEnum.SPEED: 80
        }
    },
    "0490": {
        None: {
            PocketMonsterParamEnum.NAME: "Manaphy",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.WATER,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 100,
            StatsEnum.ATTACK: 100,
            StatsEnum.DEFENSE: 100,
            StatsEnum.SPECIAL_ATTACK: 100,
            StatsEnum.SPECIAL_DEFENSE: 100,
            StatsEnum.SPEED: 100
        }
    },
    "0491": {
        None: {
            PocketMonsterParamEnum.NAME: "Darkrai",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.DARK,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 70,
            StatsEnum.ATTACK: 90,
            StatsEnum.DEFENSE: 90,
            StatsEnum.SPECIAL_ATTACK: 135,
            StatsEnum.SPECIAL_DEFENSE: 90,
            StatsEnum.SPEED: 125
        }
    },
    "0492": {
        FormEnum.LAND_FORME: {
            PocketMonsterParamEnum.NAME: "Shaymin",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.GRASS,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 100,
            StatsEnum.ATTACK: 100,
            StatsEnum.DEFENSE: 100,
            StatsEnum.SPECIAL_ATTACK: 100,
            StatsEnum.SPECIAL_DEFENSE: 100,
            StatsEnum.SPEED: 100
        },
        FormEnum.SKY_FORME: {
            PocketMonsterParamEnum.NAME: "Shaymin",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.GRASS,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.FLYING,
            StatsEnum.HP: 100,
            StatsEnum.ATTACK: 103,
            StatsEnum.DEFENSE: 75,
            StatsEnum.SPECIAL_ATTACK: 120,
            StatsEnum.SPECIAL_DEFENSE: 75,
            StatsEnum.SPEED: 127
        }
    },
    "0493": {
        None: {
            PocketMonsterParamEnum.NAME: "Arceus",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.NORMAL,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 120,
            StatsEnum.ATTACK: 120,
            StatsEnum.DEFENSE: 120,
            StatsEnum.SPECIAL_ATTACK: 120,
            StatsEnum.SPECIAL_DEFENSE: 120,
            StatsEnum.SPEED: 120
        }
    },
    "0494": {
        None: {
            PocketMonsterParamEnum.NAME: "Victini",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.PSYCHIC,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.FIRE,
            StatsEnum.HP: 100,
            StatsEnum.ATTACK: 100,
            StatsEnum.DEFENSE: 100,
            StatsEnum.SPECIAL_ATTACK: 100,
            StatsEnum.SPECIAL_DEFENSE: 100,
            StatsEnum.SPEED: 100
        }
    },
    "0495": {
        None: {
            PocketMonsterParamEnum.NAME: "Snivy",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.GRASS,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 45,
            StatsEnum.ATTACK: 45,
            StatsEnum.DEFENSE: 55,
            StatsEnum.SPECIAL_ATTACK: 45,
            StatsEnum.SPECIAL_DEFENSE: 55,
            StatsEnum.SPEED: 63
        }
    },
    "0496": {
        None: {
            PocketMonsterParamEnum.NAME: "Servine",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.GRASS,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 60,
            StatsEnum.ATTACK: 60,
            StatsEnum.DEFENSE: 75,
            StatsEnum.SPECIAL_ATTACK: 60,
            StatsEnum.SPECIAL_DEFENSE: 75,
            StatsEnum.SPEED: 83
        }
    },
    "0497": {
        None: {
            PocketMonsterParamEnum.NAME: "Serperior",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.GRASS,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 75,
            StatsEnum.ATTACK: 75,
            StatsEnum.DEFENSE: 95,
            StatsEnum.SPECIAL_ATTACK: 75,
            StatsEnum.SPECIAL_DEFENSE: 95,
            StatsEnum.SPEED: 113
        }
    },
    "0498": {
        None: {
            PocketMonsterParamEnum.NAME: "Tepig",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.FIRE,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 65,
            StatsEnum.ATTACK: 63,
            StatsEnum.DEFENSE: 45,
            StatsEnum.SPECIAL_ATTACK: 45,
            StatsEnum.SPECIAL_DEFENSE: 45,
            StatsEnum.SPEED: 45
        }
    },
    "0499": {
        None: {
            PocketMonsterParamEnum.NAME: "Pignite",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.FIRE,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.FIGHTING,
            StatsEnum.HP: 90,
            StatsEnum.ATTACK: 93,
            StatsEnum.DEFENSE: 55,
            StatsEnum.SPECIAL_ATTACK: 70,
            StatsEnum.SPECIAL_DEFENSE: 55,
            StatsEnum.SPEED: 55
        }
    },
    "0500": {
        None: {
            PocketMonsterParamEnum.NAME: "Emboar",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.FIRE,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.FIGHTING,
            StatsEnum.HP: 110,
            StatsEnum.ATTACK: 123,
            StatsEnum.DEFENSE: 65,
            StatsEnum.SPECIAL_ATTACK: 100,
            StatsEnum.SPECIAL_DEFENSE: 65,
            StatsEnum.SPEED: 65
        }
    },
    "0501": {
        None: {
            PocketMonsterParamEnum.NAME: "Oshawott",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.WATER,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 55,
            StatsEnum.ATTACK: 55,
            StatsEnum.DEFENSE: 45,
            StatsEnum.SPECIAL_ATTACK: 63,
            StatsEnum.SPECIAL_DEFENSE: 45,
            StatsEnum.SPEED: 45
        }
    },
    "0502": {
        None: {
            PocketMonsterParamEnum.NAME: "Dewott",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.WATER,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 75,
            StatsEnum.ATTACK: 75,
            StatsEnum.DEFENSE: 60,
            StatsEnum.SPECIAL_ATTACK: 83,
            StatsEnum.SPECIAL_DEFENSE: 60,
            StatsEnum.SPEED: 60
        }
    },
    "0503": {
        None: {
            PocketMonsterParamEnum.NAME: "Samurott",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.WATER,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 95,
            StatsEnum.ATTACK: 100,
            StatsEnum.DEFENSE: 85,
            StatsEnum.SPECIAL_ATTACK: 108,
            StatsEnum.SPECIAL_DEFENSE: 70,
            StatsEnum.SPEED: 70
        },
        FormEnum.HISUIAN: {
            PocketMonsterParamEnum.NAME: "Samurott",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.WATER,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.DARK,
            StatsEnum.HP: 90,
            StatsEnum.ATTACK: 108,
            StatsEnum.DEFENSE: 80,
            StatsEnum.SPECIAL_ATTACK: 100,
            StatsEnum.SPECIAL_DEFENSE: 65,
            StatsEnum.SPEED: 85
        }
    },
    "0504": {
        None: {
            PocketMonsterParamEnum.NAME: "Patrat",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.NORMAL,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 45,
            StatsEnum.ATTACK: 55,
            StatsEnum.DEFENSE: 39,
            StatsEnum.SPECIAL_ATTACK: 35,
            StatsEnum.SPECIAL_DEFENSE: 39,
            StatsEnum.SPEED: 42
        }
    },
    "0505": {
        None: {
            PocketMonsterParamEnum.NAME: "Watchog",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.NORMAL,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 60,
            StatsEnum.ATTACK: 85,
            StatsEnum.DEFENSE: 69,
            StatsEnum.SPECIAL_ATTACK: 60,
            StatsEnum.SPECIAL_DEFENSE: 69,
            StatsEnum.SPEED: 77
        }
    },
    "0506": {
        None: {
            PocketMonsterParamEnum.NAME: "Lillipup",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.NORMAL,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 45,
            StatsEnum.ATTACK: 60,
            StatsEnum.DEFENSE: 45,
            StatsEnum.SPECIAL_ATTACK: 25,
            StatsEnum.SPECIAL_DEFENSE: 45,
            StatsEnum.SPEED: 55
        }
    },
    "0507": {
        None: {
            PocketMonsterParamEnum.NAME: "Herdier",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.NORMAL,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 65,
            StatsEnum.ATTACK: 80,
            StatsEnum.DEFENSE: 65,
            StatsEnum.SPECIAL_ATTACK: 35,
            StatsEnum.SPECIAL_DEFENSE: 65,
            StatsEnum.SPEED: 60
        }
    },
    "0508": {
        None: {
            PocketMonsterParamEnum.NAME: "Stoutland",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.NORMAL,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 85,
            StatsEnum.ATTACK: 110,
            StatsEnum.DEFENSE: 90,
            StatsEnum.SPECIAL_ATTACK: 45,
            StatsEnum.SPECIAL_DEFENSE: 90,
            StatsEnum.SPEED: 80
        }
    },
    "0509": {
        None: {
            PocketMonsterParamEnum.NAME: "Purrloin",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.DARK,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 41,
            StatsEnum.ATTACK: 50,
            StatsEnum.DEFENSE: 37,
            StatsEnum.SPECIAL_ATTACK: 50,
            StatsEnum.SPECIAL_DEFENSE: 37,
            StatsEnum.SPEED: 66
        }
    },
    "0510": {
        None: {
            PocketMonsterParamEnum.NAME: "Liepard",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.DARK,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 64,
            StatsEnum.ATTACK: 88,
            StatsEnum.DEFENSE: 50,
            StatsEnum.SPECIAL_ATTACK: 88,
            StatsEnum.SPECIAL_DEFENSE: 50,
            StatsEnum.SPEED: 106
        }
    },
    "0511": {
        None: {
            PocketMonsterParamEnum.NAME: "Pansage",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.GRASS,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 50,
            StatsEnum.ATTACK: 53,
            StatsEnum.DEFENSE: 48,
            StatsEnum.SPECIAL_ATTACK: 53,
            StatsEnum.SPECIAL_DEFENSE: 48,
            StatsEnum.SPEED: 64
        }
    },
    "0512": {
        None: {
            PocketMonsterParamEnum.NAME: "Simisage",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.GRASS,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 75,
            StatsEnum.ATTACK: 98,
            StatsEnum.DEFENSE: 63,
            StatsEnum.SPECIAL_ATTACK: 98,
            StatsEnum.SPECIAL_DEFENSE: 63,
            StatsEnum.SPEED: 101
        }
    },
    "0513": {
        None: {
            PocketMonsterParamEnum.NAME: "Pansear",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.FIRE,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 50,
            StatsEnum.ATTACK: 53,
            StatsEnum.DEFENSE: 48,
            StatsEnum.SPECIAL_ATTACK: 53,
            StatsEnum.SPECIAL_DEFENSE: 48,
            StatsEnum.SPEED: 64
        }
    },
    "0514": {
        None: {
            PocketMonsterParamEnum.NAME: "Simisear",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.FIRE,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 75,
            StatsEnum.ATTACK: 98,
            StatsEnum.DEFENSE: 63,
            StatsEnum.SPECIAL_ATTACK: 98,
            StatsEnum.SPECIAL_DEFENSE: 63,
            StatsEnum.SPEED: 101
        }
    },
    "0515": {
        None: {
            PocketMonsterParamEnum.NAME: "Panpour",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.WATER,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 50,
            StatsEnum.ATTACK: 53,
            StatsEnum.DEFENSE: 48,
            StatsEnum.SPECIAL_ATTACK: 53,
            StatsEnum.SPECIAL_DEFENSE: 48,
            StatsEnum.SPEED: 64
        }
    },
    "0516": {
        None: {
            PocketMonsterParamEnum.NAME: "Simipour",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.WATER,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 75,
            StatsEnum.ATTACK: 98,
            StatsEnum.DEFENSE: 63,
            StatsEnum.SPECIAL_ATTACK: 98,
            StatsEnum.SPECIAL_DEFENSE: 63,
            StatsEnum.SPEED: 101
        }
    },
    "0517": {
        None: {
            PocketMonsterParamEnum.NAME: "Munna",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.PSYCHIC,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 76,
            StatsEnum.ATTACK: 25,
            StatsEnum.DEFENSE: 45,
            StatsEnum.SPECIAL_ATTACK: 67,
            StatsEnum.SPECIAL_DEFENSE: 55,
            StatsEnum.SPEED: 24
        }
    },
    "0518": {
        None: {
            PocketMonsterParamEnum.NAME: "Musharna",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.PSYCHIC,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 116,
            StatsEnum.ATTACK: 55,
            StatsEnum.DEFENSE: 85,
            StatsEnum.SPECIAL_ATTACK: 107,
            StatsEnum.SPECIAL_DEFENSE: 95,
            StatsEnum.SPEED: 29
        }
    },
    "0519": {
        None: {
            PocketMonsterParamEnum.NAME: "Pidove",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.NORMAL,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.FLYING,
            StatsEnum.HP: 50,
            StatsEnum.ATTACK: 55,
            StatsEnum.DEFENSE: 50,
            StatsEnum.SPECIAL_ATTACK: 36,
            StatsEnum.SPECIAL_DEFENSE: 30,
            StatsEnum.SPEED: 43
        }
    },
    "0520": {
        None: {
            PocketMonsterParamEnum.NAME: "Tranquill",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.NORMAL,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.FLYING,
            StatsEnum.HP: 62,
            StatsEnum.ATTACK: 77,
            StatsEnum.DEFENSE: 62,
            StatsEnum.SPECIAL_ATTACK: 50,
            StatsEnum.SPECIAL_DEFENSE: 42,
            StatsEnum.SPEED: 65
        }
    },
    "0521": {
        None: {
            PocketMonsterParamEnum.NAME: "Unfezant",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.NORMAL,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.FLYING,
            StatsEnum.HP: 80,
            StatsEnum.ATTACK: 115,
            StatsEnum.DEFENSE: 80,
            StatsEnum.SPECIAL_ATTACK: 65,
            StatsEnum.SPECIAL_DEFENSE: 55,
            StatsEnum.SPEED: 93
        }
    },
    "0522": {
        None: {
            PocketMonsterParamEnum.NAME: "Blitzle",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.ELECTRIC,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 45,
            StatsEnum.ATTACK: 60,
            StatsEnum.DEFENSE: 32,
            StatsEnum.SPECIAL_ATTACK: 50,
            StatsEnum.SPECIAL_DEFENSE: 32,
            StatsEnum.SPEED: 76
        }
    },
    "0523": {
        None: {
            PocketMonsterParamEnum.NAME: "Zebstrika",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.ELECTRIC,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 75,
            StatsEnum.ATTACK: 100,
            StatsEnum.DEFENSE: 63,
            StatsEnum.SPECIAL_ATTACK: 80,
            StatsEnum.SPECIAL_DEFENSE: 63,
            StatsEnum.SPEED: 116
        }
    },
    "0524": {
        None: {
            PocketMonsterParamEnum.NAME: "Roggenrola",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.ROCK,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 55,
            StatsEnum.ATTACK: 75,
            StatsEnum.DEFENSE: 85,
            StatsEnum.SPECIAL_ATTACK: 25,
            StatsEnum.SPECIAL_DEFENSE: 25,
            StatsEnum.SPEED: 15
        }
    },
    "0525": {
        None: {
            PocketMonsterParamEnum.NAME: "Boldore",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.ROCK,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 70,
            StatsEnum.ATTACK: 105,
            StatsEnum.DEFENSE: 105,
            StatsEnum.SPECIAL_ATTACK: 50,
            StatsEnum.SPECIAL_DEFENSE: 40,
            StatsEnum.SPEED: 20
        }
    },
    "0526": {
        None: {
            PocketMonsterParamEnum.NAME: "Gigalith",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.ROCK,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 85,
            StatsEnum.ATTACK: 135,
            StatsEnum.DEFENSE: 130,
            StatsEnum.SPECIAL_ATTACK: 60,
            StatsEnum.SPECIAL_DEFENSE: 80,
            StatsEnum.SPEED: 25
        }
    },
    "0527": {
        None: {
            PocketMonsterParamEnum.NAME: "Woobat",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.PSYCHIC,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.FLYING,
            StatsEnum.HP: 65,
            StatsEnum.ATTACK: 45,
            StatsEnum.DEFENSE: 43,
            StatsEnum.SPECIAL_ATTACK: 55,
            StatsEnum.SPECIAL_DEFENSE: 43,
            StatsEnum.SPEED: 72
        }
    },
    "0528": {
        None: {
            PocketMonsterParamEnum.NAME: "Swoobat",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.PSYCHIC,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.FLYING,
            StatsEnum.HP: 67,
            StatsEnum.ATTACK: 57,
            StatsEnum.DEFENSE: 55,
            StatsEnum.SPECIAL_ATTACK: 77,
            StatsEnum.SPECIAL_DEFENSE: 55,
            StatsEnum.SPEED: 114
        }
    },
    "0529": {
        None: {
            PocketMonsterParamEnum.NAME: "Drilbur",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.GROUND,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 60,
            StatsEnum.ATTACK: 85,
            StatsEnum.DEFENSE: 40,
            StatsEnum.SPECIAL_ATTACK: 30,
            StatsEnum.SPECIAL_DEFENSE: 45,
            StatsEnum.SPEED: 68
        }
    },
    "0530": {
        None: {
            PocketMonsterParamEnum.NAME: "Excadrill",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.GROUND,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.STEEL,
            StatsEnum.HP: 110,
            StatsEnum.ATTACK: 135,
            StatsEnum.DEFENSE: 60,
            StatsEnum.SPECIAL_ATTACK: 50,
            StatsEnum.SPECIAL_DEFENSE: 65,
            StatsEnum.SPEED: 88
        }
    },
    "0531": {
        None: {
            PocketMonsterParamEnum.NAME: "Audino",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.NORMAL,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 103,
            StatsEnum.ATTACK: 60,
            StatsEnum.DEFENSE: 86,
            StatsEnum.SPECIAL_ATTACK: 60,
            StatsEnum.SPECIAL_DEFENSE: 86,
            StatsEnum.SPEED: 50
        },
        FormEnum.MEGA: {
            PocketMonsterParamEnum.NAME: "Audino",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.NORMAL,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.FAIRY,
            StatsEnum.HP: 103,
            StatsEnum.ATTACK: 60,
            StatsEnum.DEFENSE: 126,
            StatsEnum.SPECIAL_ATTACK: 80,
            StatsEnum.SPECIAL_DEFENSE: 126,
            StatsEnum.SPEED: 50
        }
    },
    "0532": {
        None: {
            PocketMonsterParamEnum.NAME: "Timburr",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.FIGHTING,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 75,
            StatsEnum.ATTACK: 80,
            StatsEnum.DEFENSE: 55,
            StatsEnum.SPECIAL_ATTACK: 25,
            StatsEnum.SPECIAL_DEFENSE: 35,
            StatsEnum.SPEED: 35
        }
    },
    "0533": {
        None: {
            PocketMonsterParamEnum.NAME: "Gurdurr",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.FIGHTING,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 85,
            StatsEnum.ATTACK: 105,
            StatsEnum.DEFENSE: 85,
            StatsEnum.SPECIAL_ATTACK: 40,
            StatsEnum.SPECIAL_DEFENSE: 50,
            StatsEnum.SPEED: 40
        }
    },
    "0534": {
        None: {
            PocketMonsterParamEnum.NAME: "Conkeldurr",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.FIGHTING,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 105,
            StatsEnum.ATTACK: 140,
            StatsEnum.DEFENSE: 95,
            StatsEnum.SPECIAL_ATTACK: 55,
            StatsEnum.SPECIAL_DEFENSE: 65,
            StatsEnum.SPEED: 45
        }
    },
    "0535": {
        None: {
            PocketMonsterParamEnum.NAME: "Tympole",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.WATER,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 50,
            StatsEnum.ATTACK: 50,
            StatsEnum.DEFENSE: 40,
            StatsEnum.SPECIAL_ATTACK: 50,
            StatsEnum.SPECIAL_DEFENSE: 40,
            StatsEnum.SPEED: 64
        }
    },
    "0536": {
        None: {
            PocketMonsterParamEnum.NAME: "Palpitoad",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.WATER,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.GROUND,
            StatsEnum.HP: 75,
            StatsEnum.ATTACK: 65,
            StatsEnum.DEFENSE: 55,
            StatsEnum.SPECIAL_ATTACK: 65,
            StatsEnum.SPECIAL_DEFENSE: 55,
            StatsEnum.SPEED: 69
        }
    },
    "0537": {
        None: {
            PocketMonsterParamEnum.NAME: "Seismitoad",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.WATER,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.GROUND,
            StatsEnum.HP: 105,
            StatsEnum.ATTACK: 95,
            StatsEnum.DEFENSE: 75,
            StatsEnum.SPECIAL_ATTACK: 85,
            StatsEnum.SPECIAL_DEFENSE: 75,
            StatsEnum.SPEED: 74
        }
    },
    "0538": {
        None: {
            PocketMonsterParamEnum.NAME: "Throh",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.FIGHTING,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 120,
            StatsEnum.ATTACK: 100,
            StatsEnum.DEFENSE: 85,
            StatsEnum.SPECIAL_ATTACK: 30,
            StatsEnum.SPECIAL_DEFENSE: 85,
            StatsEnum.SPEED: 45
        }
    },
    "0539": {
        None: {
            PocketMonsterParamEnum.NAME: "Sawk",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.FIGHTING,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 75,
            StatsEnum.ATTACK: 125,
            StatsEnum.DEFENSE: 75,
            StatsEnum.SPECIAL_ATTACK: 30,
            StatsEnum.SPECIAL_DEFENSE: 75,
            StatsEnum.SPEED: 85
        }
    },
    "0540": {
        None: {
            PocketMonsterParamEnum.NAME: "Sewaddle",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.BUG,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.GRASS,
            StatsEnum.HP: 45,
            StatsEnum.ATTACK: 53,
            StatsEnum.DEFENSE: 70,
            StatsEnum.SPECIAL_ATTACK: 40,
            StatsEnum.SPECIAL_DEFENSE: 60,
            StatsEnum.SPEED: 42
        }
    },
    "0541": {
        None: {
            PocketMonsterParamEnum.NAME: "Swadloon",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.BUG,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.GRASS,
            StatsEnum.HP: 55,
            StatsEnum.ATTACK: 63,
            StatsEnum.DEFENSE: 90,
            StatsEnum.SPECIAL_ATTACK: 50,
            StatsEnum.SPECIAL_DEFENSE: 80,
            StatsEnum.SPEED: 42
        }
    },
    "0542": {
        None: {
            PocketMonsterParamEnum.NAME: "Leavanny",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.BUG,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.GRASS,
            StatsEnum.HP: 75,
            StatsEnum.ATTACK: 103,
            StatsEnum.DEFENSE: 80,
            StatsEnum.SPECIAL_ATTACK: 70,
            StatsEnum.SPECIAL_DEFENSE: 80,
            StatsEnum.SPEED: 92
        }
    },
    "0543": {
        None: {
            PocketMonsterParamEnum.NAME: "Venipede",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.BUG,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.POISON,
            StatsEnum.HP: 30,
            StatsEnum.ATTACK: 45,
            StatsEnum.DEFENSE: 59,
            StatsEnum.SPECIAL_ATTACK: 30,
            StatsEnum.SPECIAL_DEFENSE: 39,
            StatsEnum.SPEED: 57
        }
    },
    "0544": {
        None: {
            PocketMonsterParamEnum.NAME: "Whirlipede",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.BUG,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.POISON,
            StatsEnum.HP: 40,
            StatsEnum.ATTACK: 55,
            StatsEnum.DEFENSE: 99,
            StatsEnum.SPECIAL_ATTACK: 40,
            StatsEnum.SPECIAL_DEFENSE: 79,
            StatsEnum.SPEED: 47
        }
    },
    "0545": {
        None: {
            PocketMonsterParamEnum.NAME: "Scolipede",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.BUG,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.POISON,
            StatsEnum.HP: 60,
            StatsEnum.ATTACK: 100,
            StatsEnum.DEFENSE: 89,
            StatsEnum.SPECIAL_ATTACK: 55,
            StatsEnum.SPECIAL_DEFENSE: 69,
            StatsEnum.SPEED: 112
        }
    },
    "0546": {
        None: {
            PocketMonsterParamEnum.NAME: "Cottonee",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.GRASS,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.FAIRY,
            StatsEnum.HP: 40,
            StatsEnum.ATTACK: 27,
            StatsEnum.DEFENSE: 60,
            StatsEnum.SPECIAL_ATTACK: 37,
            StatsEnum.SPECIAL_DEFENSE: 50,
            StatsEnum.SPEED: 66
        }
    },
    "0547": {
        None: {
            PocketMonsterParamEnum.NAME: "Whimsicott",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.GRASS,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.FAIRY,
            StatsEnum.HP: 60,
            StatsEnum.ATTACK: 67,
            StatsEnum.DEFENSE: 85,
            StatsEnum.SPECIAL_ATTACK: 77,
            StatsEnum.SPECIAL_DEFENSE: 75,
            StatsEnum.SPEED: 116
        }
    },
    "0548": {
        None: {
            PocketMonsterParamEnum.NAME: "Petilil",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.GRASS,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 45,
            StatsEnum.ATTACK: 35,
            StatsEnum.DEFENSE: 50,
            StatsEnum.SPECIAL_ATTACK: 70,
            StatsEnum.SPECIAL_DEFENSE: 50,
            StatsEnum.SPEED: 30
        }
    },
    "0549": {
        None: {
            PocketMonsterParamEnum.NAME: "Lilligant",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.GRASS,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 70,
            StatsEnum.ATTACK: 60,
            StatsEnum.DEFENSE: 75,
            StatsEnum.SPECIAL_ATTACK: 110,
            StatsEnum.SPECIAL_DEFENSE: 75,
            StatsEnum.SPEED: 90
        },
        FormEnum.HISUIAN: {
            PocketMonsterParamEnum.NAME: "Lilligant",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.GRASS,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.FIGHTING,
            StatsEnum.HP: 70,
            StatsEnum.ATTACK: 105,
            StatsEnum.DEFENSE: 75,
            StatsEnum.SPECIAL_ATTACK: 50,
            StatsEnum.SPECIAL_DEFENSE: 75,
            StatsEnum.SPEED: 105
        }
    },
    "0550": {
        FormEnum.RED_STRIPED_FORM: {
            PocketMonsterParamEnum.NAME: "Basculin",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.WATER,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 70,
            StatsEnum.ATTACK: 92,
            StatsEnum.DEFENSE: 65,
            StatsEnum.SPECIAL_ATTACK: 80,
            StatsEnum.SPECIAL_DEFENSE: 55,
            StatsEnum.SPEED: 98
        },
        FormEnum.BLUE_STRIPED_FORM: {
            PocketMonsterParamEnum.NAME: "Basculin",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.WATER,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 70,
            StatsEnum.ATTACK: 92,
            StatsEnum.DEFENSE: 65,
            StatsEnum.SPECIAL_ATTACK: 80,
            StatsEnum.SPECIAL_DEFENSE: 55,
            StatsEnum.SPEED: 98
        },
        FormEnum.WHITE_STRIPED_FORM: {
            PocketMonsterParamEnum.NAME: "Basculin",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.WATER,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 70,
            StatsEnum.ATTACK: 92,
            StatsEnum.DEFENSE: 65,
            StatsEnum.SPECIAL_ATTACK: 80,
            StatsEnum.SPECIAL_DEFENSE: 55,
            StatsEnum.SPEED: 98
        }
    },
    "0551": {
        None: {
            PocketMonsterParamEnum.NAME: "Sandile",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.GROUND,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.DARK,
            StatsEnum.HP: 50,
            StatsEnum.ATTACK: 72,
            StatsEnum.DEFENSE: 35,
            StatsEnum.SPECIAL_ATTACK: 35,
            StatsEnum.SPECIAL_DEFENSE: 35,
            StatsEnum.SPEED: 65
        }
    },
    "0552": {
        None: {
            PocketMonsterParamEnum.NAME: "Krokorok",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.GROUND,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.DARK,
            StatsEnum.HP: 60,
            StatsEnum.ATTACK: 82,
            StatsEnum.DEFENSE: 45,
            StatsEnum.SPECIAL_ATTACK: 45,
            StatsEnum.SPECIAL_DEFENSE: 45,
            StatsEnum.SPEED: 74
        }
    },
    "0553": {
        None: {
            PocketMonsterParamEnum.NAME: "Krookodile",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.GROUND,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.DARK,
            StatsEnum.HP: 95,
            StatsEnum.ATTACK: 117,
            StatsEnum.DEFENSE: 80,
            StatsEnum.SPECIAL_ATTACK: 65,
            StatsEnum.SPECIAL_DEFENSE: 70,
            StatsEnum.SPEED: 92
        }
    },
    "0554": {
        None: {
            PocketMonsterParamEnum.NAME: "Darumaka",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.FIRE,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 70,
            StatsEnum.ATTACK: 90,
            StatsEnum.DEFENSE: 45,
            StatsEnum.SPECIAL_ATTACK: 15,
            StatsEnum.SPECIAL_DEFENSE: 45,
            StatsEnum.SPEED: 50
        },
        FormEnum.GALARIAN: {
            PocketMonsterParamEnum.NAME: "Darumaka",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.ICE,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 70,
            StatsEnum.ATTACK: 90,
            StatsEnum.DEFENSE: 45,
            StatsEnum.SPECIAL_ATTACK: 15,
            StatsEnum.SPECIAL_DEFENSE: 45,
            StatsEnum.SPEED: 50
        }
    },
    "0555": {
        FormEnum.STANDARD_MODE: {
            PocketMonsterParamEnum.NAME: "Darmanitan",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.FIRE,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 105,
            StatsEnum.ATTACK: 140,
            StatsEnum.DEFENSE: 55,
            StatsEnum.SPECIAL_ATTACK: 30,
            StatsEnum.SPECIAL_DEFENSE: 55,
            StatsEnum.SPEED: 95
        },
        FormEnum.ZEN_MODE: {
            PocketMonsterParamEnum.NAME: "Darmanitan",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.FIRE,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.PSYCHIC,
            StatsEnum.HP: 105,
            StatsEnum.ATTACK: 30,
            StatsEnum.DEFENSE: 105,
            StatsEnum.SPECIAL_ATTACK: 140,
            StatsEnum.SPECIAL_DEFENSE: 105,
            StatsEnum.SPEED: 55
        },
        FormEnum.GALARIAN_STANDARD_MODE: {
            PocketMonsterParamEnum.NAME: "Darmanitan",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.ICE,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 105,
            StatsEnum.ATTACK: 140,
            StatsEnum.DEFENSE: 55,
            StatsEnum.SPECIAL_ATTACK: 30,
            StatsEnum.SPECIAL_DEFENSE: 55,
            StatsEnum.SPEED: 95
        },
        FormEnum.GALARIAN_ZEN_MODE: {
            PocketMonsterParamEnum.NAME: "Darmanitan",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.ICE,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.FIRE,
            StatsEnum.HP: 105,
            StatsEnum.ATTACK: 160,
            StatsEnum.DEFENSE: 55,
            StatsEnum.SPECIAL_ATTACK: 30,
            StatsEnum.SPECIAL_DEFENSE: 55,
            StatsEnum.SPEED: 135
        }
    },
    "0556": {
        None: {
            PocketMonsterParamEnum.NAME: "Maractus",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.GRASS,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 75,
            StatsEnum.ATTACK: 86,
            StatsEnum.DEFENSE: 67,
            StatsEnum.SPECIAL_ATTACK: 106,
            StatsEnum.SPECIAL_DEFENSE: 67,
            StatsEnum.SPEED: 60
        }
    },
    "0557": {
        None: {
            PocketMonsterParamEnum.NAME: "Dwebble",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.BUG,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.ROCK,
            StatsEnum.HP: 50,
            StatsEnum.ATTACK: 65,
            StatsEnum.DEFENSE: 85,
            StatsEnum.SPECIAL_ATTACK: 35,
            StatsEnum.SPECIAL_DEFENSE: 35,
            StatsEnum.SPEED: 55
        }
    },
    "0558": {
        None: {
            PocketMonsterParamEnum.NAME: "Crustle",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.BUG,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.ROCK,
            StatsEnum.HP: 70,
            StatsEnum.ATTACK: 105,
            StatsEnum.DEFENSE: 125,
            StatsEnum.SPECIAL_ATTACK: 65,
            StatsEnum.SPECIAL_DEFENSE: 75,
            StatsEnum.SPEED: 45
        }
    },
    "0559": {
        None: {
            PocketMonsterParamEnum.NAME: "Scraggy",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.DARK,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.FIGHTING,
            StatsEnum.HP: 50,
            StatsEnum.ATTACK: 75,
            StatsEnum.DEFENSE: 70,
            StatsEnum.SPECIAL_ATTACK: 35,
            StatsEnum.SPECIAL_DEFENSE: 70,
            StatsEnum.SPEED: 48
        }
    },
    "0560": {
        None: {
            PocketMonsterParamEnum.NAME: "Scrafty",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.DARK,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.FIGHTING,
            StatsEnum.HP: 65,
            StatsEnum.ATTACK: 90,
            StatsEnum.DEFENSE: 115,
            StatsEnum.SPECIAL_ATTACK: 45,
            StatsEnum.SPECIAL_DEFENSE: 115,
            StatsEnum.SPEED: 58
        }
    },
    "0561": {
        None: {
            PocketMonsterParamEnum.NAME: "Sigilyph",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.PSYCHIC,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.FLYING,
            StatsEnum.HP: 72,
            StatsEnum.ATTACK: 58,
            StatsEnum.DEFENSE: 80,
            StatsEnum.SPECIAL_ATTACK: 103,
            StatsEnum.SPECIAL_DEFENSE: 80,
            StatsEnum.SPEED: 97
        }
    },
    "0562": {
        None: {
            PocketMonsterParamEnum.NAME: "Yamask",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.GHOST,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 38,
            StatsEnum.ATTACK: 30,
            StatsEnum.DEFENSE: 85,
            StatsEnum.SPECIAL_ATTACK: 55,
            StatsEnum.SPECIAL_DEFENSE: 65,
            StatsEnum.SPEED: 30
        },
        FormEnum.GALARIAN: {
            PocketMonsterParamEnum.NAME: "Yamask",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.GROUND,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.GHOST,
            StatsEnum.HP: 38,
            StatsEnum.ATTACK: 55,
            StatsEnum.DEFENSE: 85,
            StatsEnum.SPECIAL_ATTACK: 30,
            StatsEnum.SPECIAL_DEFENSE: 65,
            StatsEnum.SPEED: 30
        }
    },
    "0563": {
        None: {
            PocketMonsterParamEnum.NAME: "Cofagrigus",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.GHOST,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 58,
            StatsEnum.ATTACK: 50,
            StatsEnum.DEFENSE: 145,
            StatsEnum.SPECIAL_ATTACK: 95,
            StatsEnum.SPECIAL_DEFENSE: 105,
            StatsEnum.SPEED: 30
        }
    },
    "0564": {
        None: {
            PocketMonsterParamEnum.NAME: "Tirtouga",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.WATER,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.ROCK,
            StatsEnum.HP: 54,
            StatsEnum.ATTACK: 78,
            StatsEnum.DEFENSE: 103,
            StatsEnum.SPECIAL_ATTACK: 53,
            StatsEnum.SPECIAL_DEFENSE: 45,
            StatsEnum.SPEED: 22
        }
    },
    "0565": {
        None: {
            PocketMonsterParamEnum.NAME: "Carracosta",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.WATER,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.ROCK,
            StatsEnum.HP: 74,
            StatsEnum.ATTACK: 108,
            StatsEnum.DEFENSE: 133,
            StatsEnum.SPECIAL_ATTACK: 83,
            StatsEnum.SPECIAL_DEFENSE: 65,
            StatsEnum.SPEED: 32
        }
    },
    "0566": {
        None: {
            PocketMonsterParamEnum.NAME: "Archen",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.ROCK,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.FLYING,
            StatsEnum.HP: 55,
            StatsEnum.ATTACK: 112,
            StatsEnum.DEFENSE: 45,
            StatsEnum.SPECIAL_ATTACK: 74,
            StatsEnum.SPECIAL_DEFENSE: 45,
            StatsEnum.SPEED: 70
        }
    },
    "0567": {
        None: {
            PocketMonsterParamEnum.NAME: "Archeops",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.ROCK,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.FLYING,
            StatsEnum.HP: 75,
            StatsEnum.ATTACK: 140,
            StatsEnum.DEFENSE: 65,
            StatsEnum.SPECIAL_ATTACK: 112,
            StatsEnum.SPECIAL_DEFENSE: 65,
            StatsEnum.SPEED: 110
        }
    },
    "0568": {
        None: {
            PocketMonsterParamEnum.NAME: "Trubbish",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.POISON,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 50,
            StatsEnum.ATTACK: 50,
            StatsEnum.DEFENSE: 62,
            StatsEnum.SPECIAL_ATTACK: 40,
            StatsEnum.SPECIAL_DEFENSE: 62,
            StatsEnum.SPEED: 65
        }
    },
    "0569": {
        None: {
            PocketMonsterParamEnum.NAME: "Garbodor",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.POISON,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 80,
            StatsEnum.ATTACK: 95,
            StatsEnum.DEFENSE: 82,
            StatsEnum.SPECIAL_ATTACK: 60,
            StatsEnum.SPECIAL_DEFENSE: 82,
            StatsEnum.SPEED: 75
        }
    },
    "0570": {
        None: {
            PocketMonsterParamEnum.NAME: "Zorua",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.DARK,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 40,
            StatsEnum.ATTACK: 65,
            StatsEnum.DEFENSE: 40,
            StatsEnum.SPECIAL_ATTACK: 80,
            StatsEnum.SPECIAL_DEFENSE: 40,
            StatsEnum.SPEED: 65
        },
        FormEnum.HISUIAN: {
            PocketMonsterParamEnum.NAME: "Zorua",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.NORMAL,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.GHOST,
            StatsEnum.HP: 35,
            StatsEnum.ATTACK: 60,
            StatsEnum.DEFENSE: 40,
            StatsEnum.SPECIAL_ATTACK: 85,
            StatsEnum.SPECIAL_DEFENSE: 40,
            StatsEnum.SPEED: 70
        }
    },
    "0571": {
        None: {
            PocketMonsterParamEnum.NAME: "Zoroark",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.DARK,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 60,
            StatsEnum.ATTACK: 105,
            StatsEnum.DEFENSE: 60,
            StatsEnum.SPECIAL_ATTACK: 120,
            StatsEnum.SPECIAL_DEFENSE: 60,
            StatsEnum.SPEED: 105
        },
        FormEnum.HISUIAN: {
            PocketMonsterParamEnum.NAME: "Zoroark",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.NORMAL,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.GHOST,
            StatsEnum.HP: 55,
            StatsEnum.ATTACK: 100,
            StatsEnum.DEFENSE: 60,
            StatsEnum.SPECIAL_ATTACK: 125,
            StatsEnum.SPECIAL_DEFENSE: 60,
            StatsEnum.SPEED: 110
        }
    },
    "0572": {
        None: {
            PocketMonsterParamEnum.NAME: "Minccino",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.NORMAL,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 55,
            StatsEnum.ATTACK: 50,
            StatsEnum.DEFENSE: 40,
            StatsEnum.SPECIAL_ATTACK: 40,
            StatsEnum.SPECIAL_DEFENSE: 40,
            StatsEnum.SPEED: 75
        }
    },
    "0573": {
        None: {
            PocketMonsterParamEnum.NAME: "Cinccino",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.NORMAL,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 75,
            StatsEnum.ATTACK: 95,
            StatsEnum.DEFENSE: 60,
            StatsEnum.SPECIAL_ATTACK: 65,
            StatsEnum.SPECIAL_DEFENSE: 60,
            StatsEnum.SPEED: 115
        }
    },
    "0574": {
        None: {
            PocketMonsterParamEnum.NAME: "Gothita",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.PSYCHIC,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 45,
            StatsEnum.ATTACK: 30,
            StatsEnum.DEFENSE: 50,
            StatsEnum.SPECIAL_ATTACK: 55,
            StatsEnum.SPECIAL_DEFENSE: 65,
            StatsEnum.SPEED: 45
        }
    },
    "0575": {
        None: {
            PocketMonsterParamEnum.NAME: "Gothorita",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.PSYCHIC,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 60,
            StatsEnum.ATTACK: 45,
            StatsEnum.DEFENSE: 70,
            StatsEnum.SPECIAL_ATTACK: 75,
            StatsEnum.SPECIAL_DEFENSE: 85,
            StatsEnum.SPEED: 55
        }
    },
    "0576": {
        None: {
            PocketMonsterParamEnum.NAME: "Gothitelle",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.PSYCHIC,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 70,
            StatsEnum.ATTACK: 55,
            StatsEnum.DEFENSE: 95,
            StatsEnum.SPECIAL_ATTACK: 95,
            StatsEnum.SPECIAL_DEFENSE: 110,
            StatsEnum.SPEED: 65
        }
    },
    "0577": {
        None: {
            PocketMonsterParamEnum.NAME: "Solosis",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.PSYCHIC,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 45,
            StatsEnum.ATTACK: 30,
            StatsEnum.DEFENSE: 40,
            StatsEnum.SPECIAL_ATTACK: 105,
            StatsEnum.SPECIAL_DEFENSE: 50,
            StatsEnum.SPEED: 20
        }
    },
    "0578": {
        None: {
            PocketMonsterParamEnum.NAME: "Duosion",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.PSYCHIC,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 65,
            StatsEnum.ATTACK: 40,
            StatsEnum.DEFENSE: 50,
            StatsEnum.SPECIAL_ATTACK: 125,
            StatsEnum.SPECIAL_DEFENSE: 60,
            StatsEnum.SPEED: 30
        }
    },
    "0579": {
        None: {
            PocketMonsterParamEnum.NAME: "Reuniclus",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.PSYCHIC,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 110,
            StatsEnum.ATTACK: 65,
            StatsEnum.DEFENSE: 75,
            StatsEnum.SPECIAL_ATTACK: 125,
            StatsEnum.SPECIAL_DEFENSE: 85,
            StatsEnum.SPEED: 30
        }
    },
    "0580": {
        None: {
            PocketMonsterParamEnum.NAME: "Ducklett",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.WATER,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.FLYING,
            StatsEnum.HP: 62,
            StatsEnum.ATTACK: 44,
            StatsEnum.DEFENSE: 50,
            StatsEnum.SPECIAL_ATTACK: 44,
            StatsEnum.SPECIAL_DEFENSE: 50,
            StatsEnum.SPEED: 55
        }
    },
    "0581": {
        None: {
            PocketMonsterParamEnum.NAME: "Swanna",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.WATER,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.FLYING,
            StatsEnum.HP: 75,
            StatsEnum.ATTACK: 87,
            StatsEnum.DEFENSE: 63,
            StatsEnum.SPECIAL_ATTACK: 87,
            StatsEnum.SPECIAL_DEFENSE: 63,
            StatsEnum.SPEED: 98
        }
    },
    "0582": {
        None: {
            PocketMonsterParamEnum.NAME: "Vanillite",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.ICE,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 36,
            StatsEnum.ATTACK: 50,
            StatsEnum.DEFENSE: 50,
            StatsEnum.SPECIAL_ATTACK: 65,
            StatsEnum.SPECIAL_DEFENSE: 60,
            StatsEnum.SPEED: 44
        }
    },
    "0583": {
        None: {
            PocketMonsterParamEnum.NAME: "Vanillish",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.ICE,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 51,
            StatsEnum.ATTACK: 65,
            StatsEnum.DEFENSE: 65,
            StatsEnum.SPECIAL_ATTACK: 80,
            StatsEnum.SPECIAL_DEFENSE: 75,
            StatsEnum.SPEED: 59
        }
    },
    "0584": {
        None: {
            PocketMonsterParamEnum.NAME: "Vanilluxe",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.ICE,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 71,
            StatsEnum.ATTACK: 95,
            StatsEnum.DEFENSE: 85,
            StatsEnum.SPECIAL_ATTACK: 110,
            StatsEnum.SPECIAL_DEFENSE: 95,
            StatsEnum.SPEED: 79
        }
    },
    "0585": {
        None: {
            PocketMonsterParamEnum.NAME: "Deerling",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.NORMAL,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.GRASS,
            StatsEnum.HP: 60,
            StatsEnum.ATTACK: 60,
            StatsEnum.DEFENSE: 50,
            StatsEnum.SPECIAL_ATTACK: 40,
            StatsEnum.SPECIAL_DEFENSE: 50,
            StatsEnum.SPEED: 75
        }
    },
    "0586": {
        None: {
            PocketMonsterParamEnum.NAME: "Sawsbuck",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.NORMAL,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.GRASS,
            StatsEnum.HP: 80,
            StatsEnum.ATTACK: 100,
            StatsEnum.DEFENSE: 70,
            StatsEnum.SPECIAL_ATTACK: 60,
            StatsEnum.SPECIAL_DEFENSE: 70,
            StatsEnum.SPEED: 95
        }
    },
    "0587": {
        None: {
            PocketMonsterParamEnum.NAME: "Emolga",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.ELECTRIC,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.FLYING,
            StatsEnum.HP: 55,
            StatsEnum.ATTACK: 75,
            StatsEnum.DEFENSE: 60,
            StatsEnum.SPECIAL_ATTACK: 75,
            StatsEnum.SPECIAL_DEFENSE: 60,
            StatsEnum.SPEED: 103
        }
    },
    "0588": {
        None: {
            PocketMonsterParamEnum.NAME: "Karrablast",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.BUG,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 50,
            StatsEnum.ATTACK: 75,
            StatsEnum.DEFENSE: 45,
            StatsEnum.SPECIAL_ATTACK: 40,
            StatsEnum.SPECIAL_DEFENSE: 45,
            StatsEnum.SPEED: 60
        }
    },
    "0589": {
        None: {
            PocketMonsterParamEnum.NAME: "Escavalier",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.BUG,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.STEEL,
            StatsEnum.HP: 70,
            StatsEnum.ATTACK: 135,
            StatsEnum.DEFENSE: 105,
            StatsEnum.SPECIAL_ATTACK: 60,
            StatsEnum.SPECIAL_DEFENSE: 105,
            StatsEnum.SPEED: 20
        }
    },
    "0590": {
        None: {
            PocketMonsterParamEnum.NAME: "Foongus",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.GRASS,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.POISON,
            StatsEnum.HP: 69,
            StatsEnum.ATTACK: 55,
            StatsEnum.DEFENSE: 45,
            StatsEnum.SPECIAL_ATTACK: 55,
            StatsEnum.SPECIAL_DEFENSE: 55,
            StatsEnum.SPEED: 15
        }
    },
    "0591": {
        None: {
            PocketMonsterParamEnum.NAME: "Amoonguss",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.GRASS,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.POISON,
            StatsEnum.HP: 114,
            StatsEnum.ATTACK: 85,
            StatsEnum.DEFENSE: 70,
            StatsEnum.SPECIAL_ATTACK: 85,
            StatsEnum.SPECIAL_DEFENSE: 80,
            StatsEnum.SPEED: 30
        }
    },
    "0592": {
        None: {
            PocketMonsterParamEnum.NAME: "Frillish",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.WATER,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.GHOST,
            StatsEnum.HP: 55,
            StatsEnum.ATTACK: 40,
            StatsEnum.DEFENSE: 50,
            StatsEnum.SPECIAL_ATTACK: 65,
            StatsEnum.SPECIAL_DEFENSE: 85,
            StatsEnum.SPEED: 40
        }
    },
    "0593": {
        None: {
            PocketMonsterParamEnum.NAME: "Jellicent",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.WATER,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.GHOST,
            StatsEnum.HP: 100,
            StatsEnum.ATTACK: 60,
            StatsEnum.DEFENSE: 70,
            StatsEnum.SPECIAL_ATTACK: 85,
            StatsEnum.SPECIAL_DEFENSE: 105,
            StatsEnum.SPEED: 60
        }
    },
    "0594": {
        None: {
            PocketMonsterParamEnum.NAME: "Alomomola",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.WATER,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 165,
            StatsEnum.ATTACK: 75,
            StatsEnum.DEFENSE: 80,
            StatsEnum.SPECIAL_ATTACK: 40,
            StatsEnum.SPECIAL_DEFENSE: 45,
            StatsEnum.SPEED: 65
        }
    },
    "0595": {
        None: {
            PocketMonsterParamEnum.NAME: "Joltik",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.BUG,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.ELECTRIC,
            StatsEnum.HP: 50,
            StatsEnum.ATTACK: 47,
            StatsEnum.DEFENSE: 50,
            StatsEnum.SPECIAL_ATTACK: 57,
            StatsEnum.SPECIAL_DEFENSE: 50,
            StatsEnum.SPEED: 65
        }
    },
    "0596": {
        None: {
            PocketMonsterParamEnum.NAME: "Galvantula",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.BUG,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.ELECTRIC,
            StatsEnum.HP: 70,
            StatsEnum.ATTACK: 77,
            StatsEnum.DEFENSE: 60,
            StatsEnum.SPECIAL_ATTACK: 97,
            StatsEnum.SPECIAL_DEFENSE: 60,
            StatsEnum.SPEED: 108
        }
    },
    "0597": {
        None: {
            PocketMonsterParamEnum.NAME: "Ferroseed",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.GRASS,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.STEEL,
            StatsEnum.HP: 44,
            StatsEnum.ATTACK: 50,
            StatsEnum.DEFENSE: 91,
            StatsEnum.SPECIAL_ATTACK: 24,
            StatsEnum.SPECIAL_DEFENSE: 86,
            StatsEnum.SPEED: 10
        }
    },
    "0598": {
        None: {
            PocketMonsterParamEnum.NAME: "Ferrothorn",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.GRASS,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.STEEL,
            StatsEnum.HP: 74,
            StatsEnum.ATTACK: 94,
            StatsEnum.DEFENSE: 131,
            StatsEnum.SPECIAL_ATTACK: 54,
            StatsEnum.SPECIAL_DEFENSE: 116,
            StatsEnum.SPEED: 20
        }
    },
    "0599": {
        None: {
            PocketMonsterParamEnum.NAME: "Klink",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.STEEL,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 40,
            StatsEnum.ATTACK: 55,
            StatsEnum.DEFENSE: 70,
            StatsEnum.SPECIAL_ATTACK: 45,
            StatsEnum.SPECIAL_DEFENSE: 60,
            StatsEnum.SPEED: 30
        }
    },
    "0600": {
        None: {
            PocketMonsterParamEnum.NAME: "Klang",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.STEEL,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 60,
            StatsEnum.ATTACK: 80,
            StatsEnum.DEFENSE: 95,
            StatsEnum.SPECIAL_ATTACK: 70,
            StatsEnum.SPECIAL_DEFENSE: 85,
            StatsEnum.SPEED: 50
        }
    },
    "0601": {
        None: {
            PocketMonsterParamEnum.NAME: "Klinklang",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.STEEL,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 60,
            StatsEnum.ATTACK: 100,
            StatsEnum.DEFENSE: 115,
            StatsEnum.SPECIAL_ATTACK: 70,
            StatsEnum.SPECIAL_DEFENSE: 85,
            StatsEnum.SPEED: 90
        }
    },
    "0602": {
        None: {
            PocketMonsterParamEnum.NAME: "Tynamo",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.ELECTRIC,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 35,
            StatsEnum.ATTACK: 55,
            StatsEnum.DEFENSE: 40,
            StatsEnum.SPECIAL_ATTACK: 45,
            StatsEnum.SPECIAL_DEFENSE: 40,
            StatsEnum.SPEED: 60
        }
    },
    "0603": {
        None: {
            PocketMonsterParamEnum.NAME: "Eelektrik",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.ELECTRIC,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 65,
            StatsEnum.ATTACK: 85,
            StatsEnum.DEFENSE: 70,
            StatsEnum.SPECIAL_ATTACK: 75,
            StatsEnum.SPECIAL_DEFENSE: 70,
            StatsEnum.SPEED: 40
        }
    },
    "0604": {
        None: {
            PocketMonsterParamEnum.NAME: "Eelektross",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.ELECTRIC,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 85,
            StatsEnum.ATTACK: 115,
            StatsEnum.DEFENSE: 80,
            StatsEnum.SPECIAL_ATTACK: 105,
            StatsEnum.SPECIAL_DEFENSE: 80,
            StatsEnum.SPEED: 50
        }
    },
    "0605": {
        None: {
            PocketMonsterParamEnum.NAME: "Elgyem",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.PSYCHIC,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 55,
            StatsEnum.ATTACK: 55,
            StatsEnum.DEFENSE: 55,
            StatsEnum.SPECIAL_ATTACK: 85,
            StatsEnum.SPECIAL_DEFENSE: 55,
            StatsEnum.SPEED: 30
        }
    },
    "0606": {
        None: {
            PocketMonsterParamEnum.NAME: "Beheeyem",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.PSYCHIC,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 75,
            StatsEnum.ATTACK: 75,
            StatsEnum.DEFENSE: 75,
            StatsEnum.SPECIAL_ATTACK: 125,
            StatsEnum.SPECIAL_DEFENSE: 95,
            StatsEnum.SPEED: 40
        }
    },
    "0607": {
        None: {
            PocketMonsterParamEnum.NAME: "Litwick",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.GHOST,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.FIRE,
            StatsEnum.HP: 50,
            StatsEnum.ATTACK: 30,
            StatsEnum.DEFENSE: 55,
            StatsEnum.SPECIAL_ATTACK: 65,
            StatsEnum.SPECIAL_DEFENSE: 55,
            StatsEnum.SPEED: 20
        }
    },
    "0608": {
        None: {
            PocketMonsterParamEnum.NAME: "Lampent",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.GHOST,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.FIRE,
            StatsEnum.HP: 60,
            StatsEnum.ATTACK: 40,
            StatsEnum.DEFENSE: 60,
            StatsEnum.SPECIAL_ATTACK: 95,
            StatsEnum.SPECIAL_DEFENSE: 60,
            StatsEnum.SPEED: 55
        }
    },
    "0609": {
        None: {
            PocketMonsterParamEnum.NAME: "Chandelure",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.GHOST,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.FIRE,
            StatsEnum.HP: 60,
            StatsEnum.ATTACK: 55,
            StatsEnum.DEFENSE: 90,
            StatsEnum.SPECIAL_ATTACK: 145,
            StatsEnum.SPECIAL_DEFENSE: 90,
            StatsEnum.SPEED: 80
        }
    },
    "0610": {
        None: {
            PocketMonsterParamEnum.NAME: "Axew",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.DRAGON,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 46,
            StatsEnum.ATTACK: 87,
            StatsEnum.DEFENSE: 60,
            StatsEnum.SPECIAL_ATTACK: 30,
            StatsEnum.SPECIAL_DEFENSE: 40,
            StatsEnum.SPEED: 57
        }
    },
    "0611": {
        None: {
            PocketMonsterParamEnum.NAME: "Fraxure",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.DRAGON,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 66,
            StatsEnum.ATTACK: 117,
            StatsEnum.DEFENSE: 70,
            StatsEnum.SPECIAL_ATTACK: 40,
            StatsEnum.SPECIAL_DEFENSE: 50,
            StatsEnum.SPEED: 67
        }
    },
    "0612": {
        None: {
            PocketMonsterParamEnum.NAME: "Haxorus",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.DRAGON,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 76,
            StatsEnum.ATTACK: 147,
            StatsEnum.DEFENSE: 90,
            StatsEnum.SPECIAL_ATTACK: 60,
            StatsEnum.SPECIAL_DEFENSE: 70,
            StatsEnum.SPEED: 97
        }
    },
    "0613": {
        None: {
            PocketMonsterParamEnum.NAME: "Cubchoo",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.ICE,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 55,
            StatsEnum.ATTACK: 70,
            StatsEnum.DEFENSE: 40,
            StatsEnum.SPECIAL_ATTACK: 60,
            StatsEnum.SPECIAL_DEFENSE: 40,
            StatsEnum.SPEED: 40
        }
    },
    "0614": {
        None: {
            PocketMonsterParamEnum.NAME: "Beartic",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.ICE,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 95,
            StatsEnum.ATTACK: 130,
            StatsEnum.DEFENSE: 80,
            StatsEnum.SPECIAL_ATTACK: 70,
            StatsEnum.SPECIAL_DEFENSE: 80,
            StatsEnum.SPEED: 50
        }
    },
    "0615": {
        None: {
            PocketMonsterParamEnum.NAME: "Cryogonal",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.ICE,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 80,
            StatsEnum.ATTACK: 50,
            StatsEnum.DEFENSE: 50,
            StatsEnum.SPECIAL_ATTACK: 95,
            StatsEnum.SPECIAL_DEFENSE: 135,
            StatsEnum.SPEED: 105
        }
    },
    "0616": {
        None: {
            PocketMonsterParamEnum.NAME: "Shelmet",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.BUG,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 50,
            StatsEnum.ATTACK: 40,
            StatsEnum.DEFENSE: 85,
            StatsEnum.SPECIAL_ATTACK: 40,
            StatsEnum.SPECIAL_DEFENSE: 65,
            StatsEnum.SPEED: 25
        }
    },
    "0617": {
        None: {
            PocketMonsterParamEnum.NAME: "Accelgor",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.BUG,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 80,
            StatsEnum.ATTACK: 70,
            StatsEnum.DEFENSE: 40,
            StatsEnum.SPECIAL_ATTACK: 100,
            StatsEnum.SPECIAL_DEFENSE: 60,
            StatsEnum.SPEED: 145
        }
    },
    "0618": {
        None: {
            PocketMonsterParamEnum.NAME: "Stunfisk",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.GROUND,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.ELECTRIC,
            StatsEnum.HP: 109,
            StatsEnum.ATTACK: 66,
            StatsEnum.DEFENSE: 84,
            StatsEnum.SPECIAL_ATTACK: 81,
            StatsEnum.SPECIAL_DEFENSE: 99,
            StatsEnum.SPEED: 32
        },
        FormEnum.GALARIAN: {
            PocketMonsterParamEnum.NAME: "Stunfisk",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.GROUND,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.STEEL,
            StatsEnum.HP: 109,
            StatsEnum.ATTACK: 81,
            StatsEnum.DEFENSE: 99,
            StatsEnum.SPECIAL_ATTACK: 66,
            StatsEnum.SPECIAL_DEFENSE: 84,
            StatsEnum.SPEED: 32
        }
    },
    "0619": {
        None: {
            PocketMonsterParamEnum.NAME: "Mienfoo",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.FIGHTING,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 45,
            StatsEnum.ATTACK: 85,
            StatsEnum.DEFENSE: 50,
            StatsEnum.SPECIAL_ATTACK: 55,
            StatsEnum.SPECIAL_DEFENSE: 50,
            StatsEnum.SPEED: 65
        }
    },
    "0620": {
        None: {
            PocketMonsterParamEnum.NAME: "Mienshao",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.FIGHTING,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 65,
            StatsEnum.ATTACK: 125,
            StatsEnum.DEFENSE: 60,
            StatsEnum.SPECIAL_ATTACK: 95,
            StatsEnum.SPECIAL_DEFENSE: 60,
            StatsEnum.SPEED: 105
        }
    },
    "0621": {
        None: {
            PocketMonsterParamEnum.NAME: "Druddigon",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.DRAGON,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 77,
            StatsEnum.ATTACK: 120,
            StatsEnum.DEFENSE: 90,
            StatsEnum.SPECIAL_ATTACK: 60,
            StatsEnum.SPECIAL_DEFENSE: 90,
            StatsEnum.SPEED: 48
        }
    },
    "0622": {
        None: {
            PocketMonsterParamEnum.NAME: "Golett",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.GROUND,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.GHOST,
            StatsEnum.HP: 59,
            StatsEnum.ATTACK: 74,
            StatsEnum.DEFENSE: 50,
            StatsEnum.SPECIAL_ATTACK: 35,
            StatsEnum.SPECIAL_DEFENSE: 50,
            StatsEnum.SPEED: 35
        }
    },
    "0623": {
        None: {
            PocketMonsterParamEnum.NAME: "Golurk",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.GROUND,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.GHOST,
            StatsEnum.HP: 89,
            StatsEnum.ATTACK: 124,
            StatsEnum.DEFENSE: 80,
            StatsEnum.SPECIAL_ATTACK: 55,
            StatsEnum.SPECIAL_DEFENSE: 80,
            StatsEnum.SPEED: 55
        }
    },
    "0624": {
        None: {
            PocketMonsterParamEnum.NAME: "Pawniard",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.DARK,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.STEEL,
            StatsEnum.HP: 45,
            StatsEnum.ATTACK: 85,
            StatsEnum.DEFENSE: 70,
            StatsEnum.SPECIAL_ATTACK: 40,
            StatsEnum.SPECIAL_DEFENSE: 40,
            StatsEnum.SPEED: 60
        }
    },
    "0625": {
        None: {
            PocketMonsterParamEnum.NAME: "Bisharp",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.DARK,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.STEEL,
            StatsEnum.HP: 65,
            StatsEnum.ATTACK: 125,
            StatsEnum.DEFENSE: 100,
            StatsEnum.SPECIAL_ATTACK: 60,
            StatsEnum.SPECIAL_DEFENSE: 70,
            StatsEnum.SPEED: 70
        }
    },
    "0626": {
        None: {
            PocketMonsterParamEnum.NAME: "Bouffalant",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.NORMAL,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 95,
            StatsEnum.ATTACK: 110,
            StatsEnum.DEFENSE: 95,
            StatsEnum.SPECIAL_ATTACK: 40,
            StatsEnum.SPECIAL_DEFENSE: 95,
            StatsEnum.SPEED: 55
        }
    },
    "0627": {
        None: {
            PocketMonsterParamEnum.NAME: "Rufflet",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.NORMAL,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.FLYING,
            StatsEnum.HP: 70,
            StatsEnum.ATTACK: 83,
            StatsEnum.DEFENSE: 50,
            StatsEnum.SPECIAL_ATTACK: 37,
            StatsEnum.SPECIAL_DEFENSE: 50,
            StatsEnum.SPEED: 60
        }
    },
    "0628": {
        None: {
            PocketMonsterParamEnum.NAME: "Braviary",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.NORMAL,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.FLYING,
            StatsEnum.HP: 100,
            StatsEnum.ATTACK: 123,
            StatsEnum.DEFENSE: 75,
            StatsEnum.SPECIAL_ATTACK: 57,
            StatsEnum.SPECIAL_DEFENSE: 75,
            StatsEnum.SPEED: 80
        },
        FormEnum.HISUIAN: {
            PocketMonsterParamEnum.NAME: "Braviary",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.PSYCHIC,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.FLYING,
            StatsEnum.HP: 110,
            StatsEnum.ATTACK: 83,
            StatsEnum.DEFENSE: 70,
            StatsEnum.SPECIAL_ATTACK: 112,
            StatsEnum.SPECIAL_DEFENSE: 70,
            StatsEnum.SPEED: 65
        }
    },
    "0629": {
        None: {
            PocketMonsterParamEnum.NAME: "Vullaby",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.DARK,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.FLYING,
            StatsEnum.HP: 70,
            StatsEnum.ATTACK: 55,
            StatsEnum.DEFENSE: 75,
            StatsEnum.SPECIAL_ATTACK: 45,
            StatsEnum.SPECIAL_DEFENSE: 65,
            StatsEnum.SPEED: 60
        }
    },
    "0630": {
        None: {
            PocketMonsterParamEnum.NAME: "Mandibuzz",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.DARK,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.FLYING,
            StatsEnum.HP: 110,
            StatsEnum.ATTACK: 65,
            StatsEnum.DEFENSE: 105,
            StatsEnum.SPECIAL_ATTACK: 55,
            StatsEnum.SPECIAL_DEFENSE: 95,
            StatsEnum.SPEED: 80
        }
    },
    "0631": {
        None: {
            PocketMonsterParamEnum.NAME: "Heatmor",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.FIRE,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 85,
            StatsEnum.ATTACK: 97,
            StatsEnum.DEFENSE: 66,
            StatsEnum.SPECIAL_ATTACK: 105,
            StatsEnum.SPECIAL_DEFENSE: 66,
            StatsEnum.SPEED: 65
        }
    },
    "0632": {
        None: {
            PocketMonsterParamEnum.NAME: "Durant",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.BUG,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.STEEL,
            StatsEnum.HP: 58,
            StatsEnum.ATTACK: 109,
            StatsEnum.DEFENSE: 112,
            StatsEnum.SPECIAL_ATTACK: 48,
            StatsEnum.SPECIAL_DEFENSE: 48,
            StatsEnum.SPEED: 109
        }
    },
    "0633": {
        None: {
            PocketMonsterParamEnum.NAME: "Deino",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.DARK,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.DRAGON,
            StatsEnum.HP: 52,
            StatsEnum.ATTACK: 65,
            StatsEnum.DEFENSE: 50,
            StatsEnum.SPECIAL_ATTACK: 45,
            StatsEnum.SPECIAL_DEFENSE: 50,
            StatsEnum.SPEED: 38
        }
    },
    "0634": {
        None: {
            PocketMonsterParamEnum.NAME: "Zweilous",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.DARK,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.DRAGON,
            StatsEnum.HP: 72,
            StatsEnum.ATTACK: 85,
            StatsEnum.DEFENSE: 70,
            StatsEnum.SPECIAL_ATTACK: 65,
            StatsEnum.SPECIAL_DEFENSE: 70,
            StatsEnum.SPEED: 58
        }
    },
    "0635": {
        None: {
            PocketMonsterParamEnum.NAME: "Hydreigon",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.DARK,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.DRAGON,
            StatsEnum.HP: 92,
            StatsEnum.ATTACK: 105,
            StatsEnum.DEFENSE: 90,
            StatsEnum.SPECIAL_ATTACK: 125,
            StatsEnum.SPECIAL_DEFENSE: 90,
            StatsEnum.SPEED: 98
        }
    },
    "0636": {
        None: {
            PocketMonsterParamEnum.NAME: "Larvesta",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.BUG,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.FIRE,
            StatsEnum.HP: 55,
            StatsEnum.ATTACK: 85,
            StatsEnum.DEFENSE: 55,
            StatsEnum.SPECIAL_ATTACK: 50,
            StatsEnum.SPECIAL_DEFENSE: 55,
            StatsEnum.SPEED: 60
        }
    },
    "0637": {
        None: {
            PocketMonsterParamEnum.NAME: "Volcarona",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.BUG,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.FIRE,
            StatsEnum.HP: 85,
            StatsEnum.ATTACK: 60,
            StatsEnum.DEFENSE: 65,
            StatsEnum.SPECIAL_ATTACK: 135,
            StatsEnum.SPECIAL_DEFENSE: 105,
            StatsEnum.SPEED: 100
        }
    },
    "0638": {
        None: {
            PocketMonsterParamEnum.NAME: "Cobalion",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.STEEL,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.FIGHTING,
            StatsEnum.HP: 91,
            StatsEnum.ATTACK: 90,
            StatsEnum.DEFENSE: 129,
            StatsEnum.SPECIAL_ATTACK: 90,
            StatsEnum.SPECIAL_DEFENSE: 72,
            StatsEnum.SPEED: 108
        }
    },
    "0639": {
        None: {
            PocketMonsterParamEnum.NAME: "Terrakion",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.ROCK,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.FIGHTING,
            StatsEnum.HP: 91,
            StatsEnum.ATTACK: 129,
            StatsEnum.DEFENSE: 90,
            StatsEnum.SPECIAL_ATTACK: 72,
            StatsEnum.SPECIAL_DEFENSE: 90,
            StatsEnum.SPEED: 108
        }
    },
    "0640": {
        None: {
            PocketMonsterParamEnum.NAME: "Virizion",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.GRASS,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.FIGHTING,
            StatsEnum.HP: 91,
            StatsEnum.ATTACK: 90,
            StatsEnum.DEFENSE: 72,
            StatsEnum.SPECIAL_ATTACK: 90,
            StatsEnum.SPECIAL_DEFENSE: 129,
            StatsEnum.SPEED: 108
        }
    },
    "0641": {
        FormEnum.INCARNATE_FORME: {
            PocketMonsterParamEnum.NAME: "Tornadus",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.FLYING,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 79,
            StatsEnum.ATTACK: 115,
            StatsEnum.DEFENSE: 70,
            StatsEnum.SPECIAL_ATTACK: 125,
            StatsEnum.SPECIAL_DEFENSE: 80,
            StatsEnum.SPEED: 111
        },
        FormEnum.THERIAN_FORME: {
            PocketMonsterParamEnum.NAME: "Tornadus",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.FLYING,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 79,
            StatsEnum.ATTACK: 100,
            StatsEnum.DEFENSE: 80,
            StatsEnum.SPECIAL_ATTACK: 110,
            StatsEnum.SPECIAL_DEFENSE: 90,
            StatsEnum.SPEED: 121
        }
    },
    "0642": {
        FormEnum.INCARNATE_FORME: {
            PocketMonsterParamEnum.NAME: "Thundurus",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.ELECTRIC,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.FLYING,
            StatsEnum.HP: 79,
            StatsEnum.ATTACK: 115,
            StatsEnum.DEFENSE: 70,
            StatsEnum.SPECIAL_ATTACK: 125,
            StatsEnum.SPECIAL_DEFENSE: 80,
            StatsEnum.SPEED: 111
        },
        FormEnum.THERIAN_FORME: {
            PocketMonsterParamEnum.NAME: "Thundurus",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.ELECTRIC,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.FLYING,
            StatsEnum.HP: 79,
            StatsEnum.ATTACK: 105,
            StatsEnum.DEFENSE: 70,
            StatsEnum.SPECIAL_ATTACK: 145,
            StatsEnum.SPECIAL_DEFENSE: 80,
            StatsEnum.SPEED: 101
        }
    },
    "0643": {
        None: {
            PocketMonsterParamEnum.NAME: "Reshiram",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.DRAGON,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.FIRE,
            StatsEnum.HP: 100,
            StatsEnum.ATTACK: 120,
            StatsEnum.DEFENSE: 100,
            StatsEnum.SPECIAL_ATTACK: 150,
            StatsEnum.SPECIAL_DEFENSE: 120,
            StatsEnum.SPEED: 90
        }
    },
    "0644": {
        None: {
            PocketMonsterParamEnum.NAME: "Zekrom",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.DRAGON,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.ELECTRIC,
            StatsEnum.HP: 100,
            StatsEnum.ATTACK: 150,
            StatsEnum.DEFENSE: 120,
            StatsEnum.SPECIAL_ATTACK: 120,
            StatsEnum.SPECIAL_DEFENSE: 100,
            StatsEnum.SPEED: 90
        }
    },
    "0645": {
        FormEnum.INCARNATE_FORME: {
            PocketMonsterParamEnum.NAME: "Landorus",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.GROUND,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.FLYING,
            StatsEnum.HP: 89,
            StatsEnum.ATTACK: 125,
            StatsEnum.DEFENSE: 90,
            StatsEnum.SPECIAL_ATTACK: 115,
            StatsEnum.SPECIAL_DEFENSE: 80,
            StatsEnum.SPEED: 101
        },
        FormEnum.THERIAN_FORME: {
            PocketMonsterParamEnum.NAME: "Landorus",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.GROUND,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.FLYING,
            StatsEnum.HP: 89,
            StatsEnum.ATTACK: 145,
            StatsEnum.DEFENSE: 90,
            StatsEnum.SPECIAL_ATTACK: 105,
            StatsEnum.SPECIAL_DEFENSE: 80,
            StatsEnum.SPEED: 91
        }
    },
    "0646": {
        None: {
            PocketMonsterParamEnum.NAME: "Kyurem",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.DRAGON,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.ICE,
            StatsEnum.HP: 125,
            StatsEnum.ATTACK: 130,
            StatsEnum.DEFENSE: 90,
            StatsEnum.SPECIAL_ATTACK: 130,
            StatsEnum.SPECIAL_DEFENSE: 90,
            StatsEnum.SPEED: 95
        },
        FormEnum.WHITE: {
            PocketMonsterParamEnum.NAME: "Kyurem",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.DRAGON,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.ICE,
            StatsEnum.HP: 125,
            StatsEnum.ATTACK: 120,
            StatsEnum.DEFENSE: 90,
            StatsEnum.SPECIAL_ATTACK: 170,
            StatsEnum.SPECIAL_DEFENSE: 100,
            StatsEnum.SPEED: 95
        },
        FormEnum.BLACK: {
            PocketMonsterParamEnum.NAME: "Kyurem",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.DRAGON,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.ICE,
            StatsEnum.HP: 125,
            StatsEnum.ATTACK: 170,
            StatsEnum.DEFENSE: 100,
            StatsEnum.SPECIAL_ATTACK: 120,
            StatsEnum.SPECIAL_DEFENSE: 90,
            StatsEnum.SPEED: 95
        }
    },
    "0647": {
        FormEnum.ORDINARY_FORM: {
            PocketMonsterParamEnum.NAME: "Keldeo",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.WATER,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.FIGHTING,
            StatsEnum.HP: 91,
            StatsEnum.ATTACK: 72,
            StatsEnum.DEFENSE: 90,
            StatsEnum.SPECIAL_ATTACK: 129,
            StatsEnum.SPECIAL_DEFENSE: 90,
            StatsEnum.SPEED: 108
        },
        FormEnum.RESOLUTE_FORM: {
            PocketMonsterParamEnum.NAME: "Keldeo",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.WATER,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.FIGHTING,
            StatsEnum.HP: 91,
            StatsEnum.ATTACK: 72,
            StatsEnum.DEFENSE: 90,
            StatsEnum.SPECIAL_ATTACK: 129,
            StatsEnum.SPECIAL_DEFENSE: 90,
            StatsEnum.SPEED: 108
        }
    },
    "0648": {
        FormEnum.ARIA_FORME: {
            PocketMonsterParamEnum.NAME: "Meloetta",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.NORMAL,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.PSYCHIC,
            StatsEnum.HP: 100,
            StatsEnum.ATTACK: 77,
            StatsEnum.DEFENSE: 77,
            StatsEnum.SPECIAL_ATTACK: 128,
            StatsEnum.SPECIAL_DEFENSE: 128,
            StatsEnum.SPEED: 90
        },
        FormEnum.PIROUETTE_FORME: {
            PocketMonsterParamEnum.NAME: "Meloetta",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.NORMAL,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.FIGHTING,
            StatsEnum.HP: 100,
            StatsEnum.ATTACK: 128,
            StatsEnum.DEFENSE: 90,
            StatsEnum.SPECIAL_ATTACK: 77,
            StatsEnum.SPECIAL_DEFENSE: 77,
            StatsEnum.SPEED: 128
        }
    },
    "0649": {
        None: {
            PocketMonsterParamEnum.NAME: "Genesect",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.BUG,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.STEEL,
            StatsEnum.HP: 71,
            StatsEnum.ATTACK: 120,
            StatsEnum.DEFENSE: 95,
            StatsEnum.SPECIAL_ATTACK: 120,
            StatsEnum.SPECIAL_DEFENSE: 95,
            StatsEnum.SPEED: 99
        }
    },
    "0650": {
        None: {
            PocketMonsterParamEnum.NAME: "Chespin",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.GRASS,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 56,
            StatsEnum.ATTACK: 61,
            StatsEnum.DEFENSE: 65,
            StatsEnum.SPECIAL_ATTACK: 48,
            StatsEnum.SPECIAL_DEFENSE: 45,
            StatsEnum.SPEED: 38
        }
    },
    "0651": {
        None: {
            PocketMonsterParamEnum.NAME: "Quilladin",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.GRASS,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 61,
            StatsEnum.ATTACK: 78,
            StatsEnum.DEFENSE: 95,
            StatsEnum.SPECIAL_ATTACK: 56,
            StatsEnum.SPECIAL_DEFENSE: 58,
            StatsEnum.SPEED: 57
        }
    },
    "0652": {
        None: {
            PocketMonsterParamEnum.NAME: "Chesnaught",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.GRASS,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.FIGHTING,
            StatsEnum.HP: 88,
            StatsEnum.ATTACK: 107,
            StatsEnum.DEFENSE: 122,
            StatsEnum.SPECIAL_ATTACK: 74,
            StatsEnum.SPECIAL_DEFENSE: 75,
            StatsEnum.SPEED: 64
        }
    },
    "0653": {
        None: {
            PocketMonsterParamEnum.NAME: "Fennekin",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.FIRE,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 40,
            StatsEnum.ATTACK: 45,
            StatsEnum.DEFENSE: 40,
            StatsEnum.SPECIAL_ATTACK: 62,
            StatsEnum.SPECIAL_DEFENSE: 60,
            StatsEnum.SPEED: 60
        }
    },
    "0654": {
        None: {
            PocketMonsterParamEnum.NAME: "Braixen",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.FIRE,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 59,
            StatsEnum.ATTACK: 59,
            StatsEnum.DEFENSE: 58,
            StatsEnum.SPECIAL_ATTACK: 90,
            StatsEnum.SPECIAL_DEFENSE: 70,
            StatsEnum.SPEED: 73
        }
    },
    "0655": {
        None: {
            PocketMonsterParamEnum.NAME: "Delphox",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.FIRE,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.PSYCHIC,
            StatsEnum.HP: 75,
            StatsEnum.ATTACK: 69,
            StatsEnum.DEFENSE: 72,
            StatsEnum.SPECIAL_ATTACK: 114,
            StatsEnum.SPECIAL_DEFENSE: 100,
            StatsEnum.SPEED: 104
        }
    },
    "0656": {
        None: {
            PocketMonsterParamEnum.NAME: "Froakie",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.WATER,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 41,
            StatsEnum.ATTACK: 56,
            StatsEnum.DEFENSE: 40,
            StatsEnum.SPECIAL_ATTACK: 62,
            StatsEnum.SPECIAL_DEFENSE: 44,
            StatsEnum.SPEED: 71
        }
    },
    "0657": {
        None: {
            PocketMonsterParamEnum.NAME: "Frogadier",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.WATER,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 54,
            StatsEnum.ATTACK: 63,
            StatsEnum.DEFENSE: 52,
            StatsEnum.SPECIAL_ATTACK: 83,
            StatsEnum.SPECIAL_DEFENSE: 56,
            StatsEnum.SPEED: 97
        }
    },
    "0658": {
        None: {
            PocketMonsterParamEnum.NAME: "Greninja",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.WATER,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.DARK,
            StatsEnum.HP: 72,
            StatsEnum.ATTACK: 95,
            StatsEnum.DEFENSE: 67,
            StatsEnum.SPECIAL_ATTACK: 103,
            StatsEnum.SPECIAL_DEFENSE: 71,
            StatsEnum.SPEED: 122
        },
        FormEnum.ASH: {
            PocketMonsterParamEnum.NAME: "Greninja",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.WATER,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.DARK,
            StatsEnum.HP: 72,
            StatsEnum.ATTACK: 145,
            StatsEnum.DEFENSE: 67,
            StatsEnum.SPECIAL_ATTACK: 153,
            StatsEnum.SPECIAL_DEFENSE: 71,
            StatsEnum.SPEED: 132
        }
    },
    "0659": {
        None: {
            PocketMonsterParamEnum.NAME: "Bunnelby",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.NORMAL,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 38,
            StatsEnum.ATTACK: 36,
            StatsEnum.DEFENSE: 38,
            StatsEnum.SPECIAL_ATTACK: 32,
            StatsEnum.SPECIAL_DEFENSE: 36,
            StatsEnum.SPEED: 57
        }
    },
    "0660": {
        None: {
            PocketMonsterParamEnum.NAME: "Diggersby",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.NORMAL,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.GROUND,
            StatsEnum.HP: 85,
            StatsEnum.ATTACK: 56,
            StatsEnum.DEFENSE: 77,
            StatsEnum.SPECIAL_ATTACK: 50,
            StatsEnum.SPECIAL_DEFENSE: 77,
            StatsEnum.SPEED: 78
        }
    },
    "0661": {
        None: {
            PocketMonsterParamEnum.NAME: "Fletchling",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.NORMAL,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.FLYING,
            StatsEnum.HP: 45,
            StatsEnum.ATTACK: 50,
            StatsEnum.DEFENSE: 43,
            StatsEnum.SPECIAL_ATTACK: 40,
            StatsEnum.SPECIAL_DEFENSE: 38,
            StatsEnum.SPEED: 62
        }
    },
    "0662": {
        None: {
            PocketMonsterParamEnum.NAME: "Fletchinder",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.FIRE,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.FLYING,
            StatsEnum.HP: 62,
            StatsEnum.ATTACK: 73,
            StatsEnum.DEFENSE: 55,
            StatsEnum.SPECIAL_ATTACK: 56,
            StatsEnum.SPECIAL_DEFENSE: 52,
            StatsEnum.SPEED: 84
        }
    },
    "0663": {
        None: {
            PocketMonsterParamEnum.NAME: "Talonflame",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.FIRE,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.FLYING,
            StatsEnum.HP: 78,
            StatsEnum.ATTACK: 81,
            StatsEnum.DEFENSE: 71,
            StatsEnum.SPECIAL_ATTACK: 74,
            StatsEnum.SPECIAL_DEFENSE: 69,
            StatsEnum.SPEED: 126
        }
    },
    "0664": {
        None: {
            PocketMonsterParamEnum.NAME: "Scatterbug",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.BUG,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 38,
            StatsEnum.ATTACK: 35,
            StatsEnum.DEFENSE: 40,
            StatsEnum.SPECIAL_ATTACK: 27,
            StatsEnum.SPECIAL_DEFENSE: 25,
            StatsEnum.SPEED: 35
        }
    },
    "0665": {
        None: {
            PocketMonsterParamEnum.NAME: "Spewpa",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.BUG,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 45,
            StatsEnum.ATTACK: 22,
            StatsEnum.DEFENSE: 60,
            StatsEnum.SPECIAL_ATTACK: 27,
            StatsEnum.SPECIAL_DEFENSE: 30,
            StatsEnum.SPEED: 29
        }
    },
    "0666": {
        None: {
            PocketMonsterParamEnum.NAME: "Vivillon",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.BUG,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.FLYING,
            StatsEnum.HP: 80,
            StatsEnum.ATTACK: 52,
            StatsEnum.DEFENSE: 50,
            StatsEnum.SPECIAL_ATTACK: 90,
            StatsEnum.SPECIAL_DEFENSE: 50,
            StatsEnum.SPEED: 89
        }
    },
    "0667": {
        None: {
            PocketMonsterParamEnum.NAME: "Litleo",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.FIRE,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.NORMAL,
            StatsEnum.HP: 62,
            StatsEnum.ATTACK: 50,
            StatsEnum.DEFENSE: 58,
            StatsEnum.SPECIAL_ATTACK: 73,
            StatsEnum.SPECIAL_DEFENSE: 54,
            StatsEnum.SPEED: 72
        }
    },
    "0668": {
        None: {
            PocketMonsterParamEnum.NAME: "Pyroar",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.FIRE,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.NORMAL,
            StatsEnum.HP: 86,
            StatsEnum.ATTACK: 68,
            StatsEnum.DEFENSE: 72,
            StatsEnum.SPECIAL_ATTACK: 109,
            StatsEnum.SPECIAL_DEFENSE: 66,
            StatsEnum.SPEED: 106
        }
    },
    "0669": {
        None: {
            PocketMonsterParamEnum.NAME: "Flabébé",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.FAIRY,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 44,
            StatsEnum.ATTACK: 38,
            StatsEnum.DEFENSE: 39,
            StatsEnum.SPECIAL_ATTACK: 61,
            StatsEnum.SPECIAL_DEFENSE: 79,
            StatsEnum.SPEED: 42
        }
    },
    "0670": {
        None: {
            PocketMonsterParamEnum.NAME: "Floette",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.FAIRY,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 54,
            StatsEnum.ATTACK: 45,
            StatsEnum.DEFENSE: 47,
            StatsEnum.SPECIAL_ATTACK: 75,
            StatsEnum.SPECIAL_DEFENSE: 98,
            StatsEnum.SPEED: 52
        }
    },
    "0671": {
        None: {
            PocketMonsterParamEnum.NAME: "Florges",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.FAIRY,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 78,
            StatsEnum.ATTACK: 65,
            StatsEnum.DEFENSE: 68,
            StatsEnum.SPECIAL_ATTACK: 112,
            StatsEnum.SPECIAL_DEFENSE: 154,
            StatsEnum.SPEED: 75
        }
    },
    "0672": {
        None: {
            PocketMonsterParamEnum.NAME: "Skiddo",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.GRASS,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 66,
            StatsEnum.ATTACK: 65,
            StatsEnum.DEFENSE: 48,
            StatsEnum.SPECIAL_ATTACK: 62,
            StatsEnum.SPECIAL_DEFENSE: 57,
            StatsEnum.SPEED: 52
        }
    },
    "0673": {
        None: {
            PocketMonsterParamEnum.NAME: "Gogoat",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.GRASS,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 123,
            StatsEnum.ATTACK: 100,
            StatsEnum.DEFENSE: 62,
            StatsEnum.SPECIAL_ATTACK: 97,
            StatsEnum.SPECIAL_DEFENSE: 81,
            StatsEnum.SPEED: 68
        }
    },
    "0674": {
        None: {
            PocketMonsterParamEnum.NAME: "Pancham",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.FIGHTING,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 67,
            StatsEnum.ATTACK: 82,
            StatsEnum.DEFENSE: 62,
            StatsEnum.SPECIAL_ATTACK: 46,
            StatsEnum.SPECIAL_DEFENSE: 48,
            StatsEnum.SPEED: 43
        }
    },
    "0675": {
        None: {
            PocketMonsterParamEnum.NAME: "Pangoro",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.FIGHTING,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.DARK,
            StatsEnum.HP: 95,
            StatsEnum.ATTACK: 124,
            StatsEnum.DEFENSE: 78,
            StatsEnum.SPECIAL_ATTACK: 69,
            StatsEnum.SPECIAL_DEFENSE: 71,
            StatsEnum.SPEED: 58
        }
    },
    "0676": {
        None: {
            PocketMonsterParamEnum.NAME: "Furfrou",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.NORMAL,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 75,
            StatsEnum.ATTACK: 80,
            StatsEnum.DEFENSE: 60,
            StatsEnum.SPECIAL_ATTACK: 65,
            StatsEnum.SPECIAL_DEFENSE: 90,
            StatsEnum.SPEED: 102
        }
    },
    "0677": {
        None: {
            PocketMonsterParamEnum.NAME: "Espurr",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.PSYCHIC,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 62,
            StatsEnum.ATTACK: 48,
            StatsEnum.DEFENSE: 54,
            StatsEnum.SPECIAL_ATTACK: 63,
            StatsEnum.SPECIAL_DEFENSE: 60,
            StatsEnum.SPEED: 68
        }
    },
    "0678": {
        FormEnum.MALE: {
            PocketMonsterParamEnum.NAME: "Meowstic",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.PSYCHIC,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 74,
            StatsEnum.ATTACK: 48,
            StatsEnum.DEFENSE: 76,
            StatsEnum.SPECIAL_ATTACK: 83,
            StatsEnum.SPECIAL_DEFENSE: 81,
            StatsEnum.SPEED: 104
        },
        FormEnum.FEMALE: {
            PocketMonsterParamEnum.NAME: "Meowstic",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.PSYCHIC,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 74,
            StatsEnum.ATTACK: 48,
            StatsEnum.DEFENSE: 76,
            StatsEnum.SPECIAL_ATTACK: 83,
            StatsEnum.SPECIAL_DEFENSE: 81,
            StatsEnum.SPEED: 104
        }
    },
    "0679": {
        None: {
            PocketMonsterParamEnum.NAME: "Honedge",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.STEEL,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.GHOST,
            StatsEnum.HP: 45,
            StatsEnum.ATTACK: 80,
            StatsEnum.DEFENSE: 100,
            StatsEnum.SPECIAL_ATTACK: 35,
            StatsEnum.SPECIAL_DEFENSE: 37,
            StatsEnum.SPEED: 28
        }
    },
    "0680": {
        None: {
            PocketMonsterParamEnum.NAME: "Doublade",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.STEEL,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.GHOST,
            StatsEnum.HP: 59,
            StatsEnum.ATTACK: 110,
            StatsEnum.DEFENSE: 150,
            StatsEnum.SPECIAL_ATTACK: 45,
            StatsEnum.SPECIAL_DEFENSE: 49,
            StatsEnum.SPEED: 35
        }
    },
    "0681": {
        FormEnum.SHIELD_FORME: {
            PocketMonsterParamEnum.NAME: "Aegislash",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.STEEL,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.GHOST,
            StatsEnum.HP: 60,
            StatsEnum.ATTACK: 50,
            StatsEnum.DEFENSE: 140,
            StatsEnum.SPECIAL_ATTACK: 50,
            StatsEnum.SPECIAL_DEFENSE: 140,
            StatsEnum.SPEED: 60
        },
        FormEnum.BLADE_FORME: {
            PocketMonsterParamEnum.NAME: "Aegislash",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.STEEL,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.GHOST,
            StatsEnum.HP: 60,
            StatsEnum.ATTACK: 140,
            StatsEnum.DEFENSE: 50,
            StatsEnum.SPECIAL_ATTACK: 140,
            StatsEnum.SPECIAL_DEFENSE: 50,
            StatsEnum.SPEED: 60
        }
    },
    "0682": {
        None: {
            PocketMonsterParamEnum.NAME: "Spritzee",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.FAIRY,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 78,
            StatsEnum.ATTACK: 52,
            StatsEnum.DEFENSE: 60,
            StatsEnum.SPECIAL_ATTACK: 63,
            StatsEnum.SPECIAL_DEFENSE: 65,
            StatsEnum.SPEED: 23
        }
    },
    "0683": {
        None: {
            PocketMonsterParamEnum.NAME: "Aromatisse",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.FAIRY,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 101,
            StatsEnum.ATTACK: 72,
            StatsEnum.DEFENSE: 72,
            StatsEnum.SPECIAL_ATTACK: 99,
            StatsEnum.SPECIAL_DEFENSE: 89,
            StatsEnum.SPEED: 29
        }
    },
    "0684": {
        None: {
            PocketMonsterParamEnum.NAME: "Swirlix",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.FAIRY,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 62,
            StatsEnum.ATTACK: 48,
            StatsEnum.DEFENSE: 66,
            StatsEnum.SPECIAL_ATTACK: 59,
            StatsEnum.SPECIAL_DEFENSE: 57,
            StatsEnum.SPEED: 49
        }
    },
    "0685": {
        None: {
            PocketMonsterParamEnum.NAME: "Slurpuff",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.FAIRY,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 82,
            StatsEnum.ATTACK: 80,
            StatsEnum.DEFENSE: 86,
            StatsEnum.SPECIAL_ATTACK: 85,
            StatsEnum.SPECIAL_DEFENSE: 75,
            StatsEnum.SPEED: 72
        }
    },
    "0686": {
        None: {
            PocketMonsterParamEnum.NAME: "Inkay",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.DARK,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.PSYCHIC,
            StatsEnum.HP: 53,
            StatsEnum.ATTACK: 54,
            StatsEnum.DEFENSE: 53,
            StatsEnum.SPECIAL_ATTACK: 37,
            StatsEnum.SPECIAL_DEFENSE: 46,
            StatsEnum.SPEED: 45
        }
    },
    "0687": {
        None: {
            PocketMonsterParamEnum.NAME: "Malamar",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.DARK,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.PSYCHIC,
            StatsEnum.HP: 86,
            StatsEnum.ATTACK: 92,
            StatsEnum.DEFENSE: 88,
            StatsEnum.SPECIAL_ATTACK: 68,
            StatsEnum.SPECIAL_DEFENSE: 75,
            StatsEnum.SPEED: 73
        }
    },
    "0688": {
        None: {
            PocketMonsterParamEnum.NAME: "Binacle",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.ROCK,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.WATER,
            StatsEnum.HP: 42,
            StatsEnum.ATTACK: 52,
            StatsEnum.DEFENSE: 67,
            StatsEnum.SPECIAL_ATTACK: 39,
            StatsEnum.SPECIAL_DEFENSE: 56,
            StatsEnum.SPEED: 50
        }
    },
    "0689": {
        None: {
            PocketMonsterParamEnum.NAME: "Barbaracle",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.ROCK,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.WATER,
            StatsEnum.HP: 72,
            StatsEnum.ATTACK: 105,
            StatsEnum.DEFENSE: 115,
            StatsEnum.SPECIAL_ATTACK: 54,
            StatsEnum.SPECIAL_DEFENSE: 86,
            StatsEnum.SPEED: 68
        }
    },
    "0690": {
        None: {
            PocketMonsterParamEnum.NAME: "Skrelp",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.POISON,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.WATER,
            StatsEnum.HP: 50,
            StatsEnum.ATTACK: 60,
            StatsEnum.DEFENSE: 60,
            StatsEnum.SPECIAL_ATTACK: 60,
            StatsEnum.SPECIAL_DEFENSE: 60,
            StatsEnum.SPEED: 30
        }
    },
    "0691": {
        None: {
            PocketMonsterParamEnum.NAME: "Dragalge",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.POISON,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.DRAGON,
            StatsEnum.HP: 65,
            StatsEnum.ATTACK: 75,
            StatsEnum.DEFENSE: 90,
            StatsEnum.SPECIAL_ATTACK: 97,
            StatsEnum.SPECIAL_DEFENSE: 123,
            StatsEnum.SPEED: 44
        }
    },
    "0692": {
        None: {
            PocketMonsterParamEnum.NAME: "Clauncher",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.WATER,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 50,
            StatsEnum.ATTACK: 53,
            StatsEnum.DEFENSE: 62,
            StatsEnum.SPECIAL_ATTACK: 58,
            StatsEnum.SPECIAL_DEFENSE: 63,
            StatsEnum.SPEED: 44
        }
    },
    "0693": {
        None: {
            PocketMonsterParamEnum.NAME: "Clawitzer",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.WATER,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 71,
            StatsEnum.ATTACK: 73,
            StatsEnum.DEFENSE: 88,
            StatsEnum.SPECIAL_ATTACK: 120,
            StatsEnum.SPECIAL_DEFENSE: 89,
            StatsEnum.SPEED: 59
        }
    },
    "0694": {
        None: {
            PocketMonsterParamEnum.NAME: "Helioptile",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.ELECTRIC,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.NORMAL,
            StatsEnum.HP: 44,
            StatsEnum.ATTACK: 38,
            StatsEnum.DEFENSE: 33,
            StatsEnum.SPECIAL_ATTACK: 61,
            StatsEnum.SPECIAL_DEFENSE: 43,
            StatsEnum.SPEED: 70
        }
    },
    "0695": {
        None: {
            PocketMonsterParamEnum.NAME: "Heliolisk",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.ELECTRIC,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.NORMAL,
            StatsEnum.HP: 62,
            StatsEnum.ATTACK: 55,
            StatsEnum.DEFENSE: 52,
            StatsEnum.SPECIAL_ATTACK: 109,
            StatsEnum.SPECIAL_DEFENSE: 94,
            StatsEnum.SPEED: 109
        }
    },
    "0696": {
        None: {
            PocketMonsterParamEnum.NAME: "Tyrunt",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.ROCK,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.DRAGON,
            StatsEnum.HP: 58,
            StatsEnum.ATTACK: 89,
            StatsEnum.DEFENSE: 77,
            StatsEnum.SPECIAL_ATTACK: 45,
            StatsEnum.SPECIAL_DEFENSE: 45,
            StatsEnum.SPEED: 48
        }
    },
    "0697": {
        None: {
            PocketMonsterParamEnum.NAME: "Tyrantrum",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.ROCK,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.DRAGON,
            StatsEnum.HP: 82,
            StatsEnum.ATTACK: 121,
            StatsEnum.DEFENSE: 119,
            StatsEnum.SPECIAL_ATTACK: 69,
            StatsEnum.SPECIAL_DEFENSE: 59,
            StatsEnum.SPEED: 71
        }
    },
    "0698": {
        None: {
            PocketMonsterParamEnum.NAME: "Amaura",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.ROCK,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.ICE,
            StatsEnum.HP: 77,
            StatsEnum.ATTACK: 59,
            StatsEnum.DEFENSE: 50,
            StatsEnum.SPECIAL_ATTACK: 67,
            StatsEnum.SPECIAL_DEFENSE: 63,
            StatsEnum.SPEED: 46
        }
    },
    "0699": {
        None: {
            PocketMonsterParamEnum.NAME: "Aurorus",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.ROCK,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.ICE,
            StatsEnum.HP: 123,
            StatsEnum.ATTACK: 77,
            StatsEnum.DEFENSE: 72,
            StatsEnum.SPECIAL_ATTACK: 99,
            StatsEnum.SPECIAL_DEFENSE: 92,
            StatsEnum.SPEED: 58
        }
    },
    "0700": {
        None: {
            PocketMonsterParamEnum.NAME: "Sylveon",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.FAIRY,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 95,
            StatsEnum.ATTACK: 65,
            StatsEnum.DEFENSE: 65,
            StatsEnum.SPECIAL_ATTACK: 110,
            StatsEnum.SPECIAL_DEFENSE: 130,
            StatsEnum.SPEED: 60
        }
    },
    "0701": {
        None: {
            PocketMonsterParamEnum.NAME: "Hawlucha",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.FIGHTING,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.FLYING,
            StatsEnum.HP: 78,
            StatsEnum.ATTACK: 92,
            StatsEnum.DEFENSE: 75,
            StatsEnum.SPECIAL_ATTACK: 74,
            StatsEnum.SPECIAL_DEFENSE: 63,
            StatsEnum.SPEED: 118
        }
    },
    "0702": {
        None: {
            PocketMonsterParamEnum.NAME: "Dedenne",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.ELECTRIC,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.FAIRY,
            StatsEnum.HP: 67,
            StatsEnum.ATTACK: 58,
            StatsEnum.DEFENSE: 57,
            StatsEnum.SPECIAL_ATTACK: 81,
            StatsEnum.SPECIAL_DEFENSE: 67,
            StatsEnum.SPEED: 101
        }
    },
    "0703": {
        None: {
            PocketMonsterParamEnum.NAME: "Carbink",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.ROCK,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.FAIRY,
            StatsEnum.HP: 50,
            StatsEnum.ATTACK: 50,
            StatsEnum.DEFENSE: 150,
            StatsEnum.SPECIAL_ATTACK: 50,
            StatsEnum.SPECIAL_DEFENSE: 150,
            StatsEnum.SPEED: 50
        }
    },
    "0704": {
        None: {
            PocketMonsterParamEnum.NAME: "Goomy",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.DRAGON,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 45,
            StatsEnum.ATTACK: 50,
            StatsEnum.DEFENSE: 35,
            StatsEnum.SPECIAL_ATTACK: 55,
            StatsEnum.SPECIAL_DEFENSE: 75,
            StatsEnum.SPEED: 40
        }
    },
    "0705": {
        None: {
            PocketMonsterParamEnum.NAME: "Sliggoo",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.DRAGON,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 68,
            StatsEnum.ATTACK: 75,
            StatsEnum.DEFENSE: 53,
            StatsEnum.SPECIAL_ATTACK: 83,
            StatsEnum.SPECIAL_DEFENSE: 113,
            StatsEnum.SPEED: 60
        },
        FormEnum.HISUIAN: {
            PocketMonsterParamEnum.NAME: "Sliggoo",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.STEEL,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.DRAGON,
            StatsEnum.HP: 58,
            StatsEnum.ATTACK: 75,
            StatsEnum.DEFENSE: 83,
            StatsEnum.SPECIAL_ATTACK: 83,
            StatsEnum.SPECIAL_DEFENSE: 113,
            StatsEnum.SPEED: 40
        }
    },
    "0706": {
        None: {
            PocketMonsterParamEnum.NAME: "Goodra",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.DRAGON,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 90,
            StatsEnum.ATTACK: 100,
            StatsEnum.DEFENSE: 70,
            StatsEnum.SPECIAL_ATTACK: 110,
            StatsEnum.SPECIAL_DEFENSE: 150,
            StatsEnum.SPEED: 80
        },
        FormEnum.HISUIAN: {
            PocketMonsterParamEnum.NAME: "Goodra",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.STEEL,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.DRAGON,
            StatsEnum.HP: 80,
            StatsEnum.ATTACK: 100,
            StatsEnum.DEFENSE: 100,
            StatsEnum.SPECIAL_ATTACK: 110,
            StatsEnum.SPECIAL_DEFENSE: 150,
            StatsEnum.SPEED: 60
        }
    },
    "0707": {
        None: {
            PocketMonsterParamEnum.NAME: "Klefki",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.STEEL,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.FAIRY,
            StatsEnum.HP: 57,
            StatsEnum.ATTACK: 80,
            StatsEnum.DEFENSE: 91,
            StatsEnum.SPECIAL_ATTACK: 80,
            StatsEnum.SPECIAL_DEFENSE: 87,
            StatsEnum.SPEED: 75
        }
    },
    "0708": {
        None: {
            PocketMonsterParamEnum.NAME: "Phantump",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.GHOST,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.GRASS,
            StatsEnum.HP: 43,
            StatsEnum.ATTACK: 70,
            StatsEnum.DEFENSE: 48,
            StatsEnum.SPECIAL_ATTACK: 50,
            StatsEnum.SPECIAL_DEFENSE: 60,
            StatsEnum.SPEED: 38
        }
    },
    "0709": {
        None: {
            PocketMonsterParamEnum.NAME: "TreveNonet",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.GHOST,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.GRASS,
            StatsEnum.HP: 85,
            StatsEnum.ATTACK: 110,
            StatsEnum.DEFENSE: 76,
            StatsEnum.SPECIAL_ATTACK: 65,
            StatsEnum.SPECIAL_DEFENSE: 82,
            StatsEnum.SPEED: 56
        }
    },
    "0710": {
        FormEnum.AVERAGE_SIZE: {
            PocketMonsterParamEnum.NAME: "Pumpkaboo",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.GHOST,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.GRASS,
            StatsEnum.HP: 49,
            StatsEnum.ATTACK: 66,
            StatsEnum.DEFENSE: 70,
            StatsEnum.SPECIAL_ATTACK: 44,
            StatsEnum.SPECIAL_DEFENSE: 55,
            StatsEnum.SPEED: 51
        },
        FormEnum.SMALL_SIZE: {
            PocketMonsterParamEnum.NAME: "Pumpkaboo",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.GHOST,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.GRASS,
            StatsEnum.HP: 44,
            StatsEnum.ATTACK: 66,
            StatsEnum.DEFENSE: 70,
            StatsEnum.SPECIAL_ATTACK: 44,
            StatsEnum.SPECIAL_DEFENSE: 55,
            StatsEnum.SPEED: 56
        },
        FormEnum.LARGE_SIZE: {
            PocketMonsterParamEnum.NAME: "Pumpkaboo",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.GHOST,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.GRASS,
            StatsEnum.HP: 54,
            StatsEnum.ATTACK: 66,
            StatsEnum.DEFENSE: 70,
            StatsEnum.SPECIAL_ATTACK: 44,
            StatsEnum.SPECIAL_DEFENSE: 55,
            StatsEnum.SPEED: 46
        },
        FormEnum.SUPER_SIZE: {
            PocketMonsterParamEnum.NAME: "Pumpkaboo",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.GHOST,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.GRASS,
            StatsEnum.HP: 59,
            StatsEnum.ATTACK: 66,
            StatsEnum.DEFENSE: 70,
            StatsEnum.SPECIAL_ATTACK: 44,
            StatsEnum.SPECIAL_DEFENSE: 55,
            StatsEnum.SPEED: 41
        }
    },
    "0711": {
        FormEnum.AVERAGE_SIZE: {
            PocketMonsterParamEnum.NAME: "Gourgeist",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.GHOST,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.GRASS,
            StatsEnum.HP: 65,
            StatsEnum.ATTACK: 90,
            StatsEnum.DEFENSE: 122,
            StatsEnum.SPECIAL_ATTACK: 58,
            StatsEnum.SPECIAL_DEFENSE: 75,
            StatsEnum.SPEED: 84
        },
        FormEnum.SMALL_SIZE: {
            PocketMonsterParamEnum.NAME: "Gourgeist",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.GHOST,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.GRASS,
            StatsEnum.HP: 55,
            StatsEnum.ATTACK: 85,
            StatsEnum.DEFENSE: 122,
            StatsEnum.SPECIAL_ATTACK: 58,
            StatsEnum.SPECIAL_DEFENSE: 75,
            StatsEnum.SPEED: 99
        },
        FormEnum.LARGE_SIZE: {
            PocketMonsterParamEnum.NAME: "Gourgeist",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.GHOST,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.GRASS,
            StatsEnum.HP: 75,
            StatsEnum.ATTACK: 95,
            StatsEnum.DEFENSE: 122,
            StatsEnum.SPECIAL_ATTACK: 58,
            StatsEnum.SPECIAL_DEFENSE: 75,
            StatsEnum.SPEED: 69
        },
        FormEnum.SUPER_SIZE: {
            PocketMonsterParamEnum.NAME: "Gourgeist",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.GHOST,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.GRASS,
            StatsEnum.HP: 85,
            StatsEnum.ATTACK: 100,
            StatsEnum.DEFENSE: 122,
            StatsEnum.SPECIAL_ATTACK: 58,
            StatsEnum.SPECIAL_DEFENSE: 75,
            StatsEnum.SPEED: 54
        }
    },
    "0712": {
        None: {
            PocketMonsterParamEnum.NAME: "Bergmite",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.ICE,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 55,
            StatsEnum.ATTACK: 69,
            StatsEnum.DEFENSE: 85,
            StatsEnum.SPECIAL_ATTACK: 32,
            StatsEnum.SPECIAL_DEFENSE: 35,
            StatsEnum.SPEED: 28
        }
    },
    "0713": {
        None: {
            PocketMonsterParamEnum.NAME: "Avalugg",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.ICE,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 95,
            StatsEnum.ATTACK: 117,
            StatsEnum.DEFENSE: 184,
            StatsEnum.SPECIAL_ATTACK: 44,
            StatsEnum.SPECIAL_DEFENSE: 46,
            StatsEnum.SPEED: 28
        },
        FormEnum.HISUIAN: {
            PocketMonsterParamEnum.NAME: "Avalugg",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.ICE,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.ROCK,
            StatsEnum.HP: 95,
            StatsEnum.ATTACK: 127,
            StatsEnum.DEFENSE: 184,
            StatsEnum.SPECIAL_ATTACK: 34,
            StatsEnum.SPECIAL_DEFENSE: 36,
            StatsEnum.SPEED: 38
        }
    },
    "0714": {
        None: {
            PocketMonsterParamEnum.NAME: "Noibat",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.FLYING,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.DRAGON,
            StatsEnum.HP: 40,
            StatsEnum.ATTACK: 30,
            StatsEnum.DEFENSE: 35,
            StatsEnum.SPECIAL_ATTACK: 45,
            StatsEnum.SPECIAL_DEFENSE: 40,
            StatsEnum.SPEED: 55
        }
    },
    "0715": {
        None: {
            PocketMonsterParamEnum.NAME: "Noivern",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.FLYING,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.DRAGON,
            StatsEnum.HP: 85,
            StatsEnum.ATTACK: 70,
            StatsEnum.DEFENSE: 80,
            StatsEnum.SPECIAL_ATTACK: 97,
            StatsEnum.SPECIAL_DEFENSE: 80,
            StatsEnum.SPEED: 123
        }
    },
    "0716": {
        None: {
            PocketMonsterParamEnum.NAME: "Xerneas",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.FAIRY,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 126,
            StatsEnum.ATTACK: 131,
            StatsEnum.DEFENSE: 95,
            StatsEnum.SPECIAL_ATTACK: 131,
            StatsEnum.SPECIAL_DEFENSE: 98,
            StatsEnum.SPEED: 99
        }
    },
    "0717": {
        None: {
            PocketMonsterParamEnum.NAME: "Yveltal",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.DARK,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.FLYING,
            StatsEnum.HP: 126,
            StatsEnum.ATTACK: 131,
            StatsEnum.DEFENSE: 95,
            StatsEnum.SPECIAL_ATTACK: 131,
            StatsEnum.SPECIAL_DEFENSE: 98,
            StatsEnum.SPEED: 99
        }
    },
    "0718": {
        FormEnum._50_FORME: {
            PocketMonsterParamEnum.NAME: "Zygarde",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.DRAGON,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.GROUND,
            StatsEnum.HP: 108,
            StatsEnum.ATTACK: 100,
            StatsEnum.DEFENSE: 121,
            StatsEnum.SPECIAL_ATTACK: 81,
            StatsEnum.SPECIAL_DEFENSE: 95,
            StatsEnum.SPEED: 95
        },
        FormEnum._10_FORME: {
            PocketMonsterParamEnum.NAME: "Zygarde",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.DRAGON,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.GROUND,
            StatsEnum.HP: 54,
            StatsEnum.ATTACK: 100,
            StatsEnum.DEFENSE: 71,
            StatsEnum.SPECIAL_ATTACK: 61,
            StatsEnum.SPECIAL_DEFENSE: 85,
            StatsEnum.SPEED: 115
        },
        FormEnum.COMPLETE_FORME: {
            PocketMonsterParamEnum.NAME: "Zygarde",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.DRAGON,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.GROUND,
            StatsEnum.HP: 216,
            StatsEnum.ATTACK: 100,
            StatsEnum.DEFENSE: 121,
            StatsEnum.SPECIAL_ATTACK: 91,
            StatsEnum.SPECIAL_DEFENSE: 95,
            StatsEnum.SPEED: 85
        }
    },
    "0719": {
        None: {
            PocketMonsterParamEnum.NAME: "Diancie",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.ROCK,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.FAIRY,
            StatsEnum.HP: 50,
            StatsEnum.ATTACK: 100,
            StatsEnum.DEFENSE: 150,
            StatsEnum.SPECIAL_ATTACK: 100,
            StatsEnum.SPECIAL_DEFENSE: 150,
            StatsEnum.SPEED: 50
        },
        FormEnum.MEGA: {
            PocketMonsterParamEnum.NAME: "Diancie",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.ROCK,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.FAIRY,
            StatsEnum.HP: 50,
            StatsEnum.ATTACK: 160,
            StatsEnum.DEFENSE: 110,
            StatsEnum.SPECIAL_ATTACK: 160,
            StatsEnum.SPECIAL_DEFENSE: 110,
            StatsEnum.SPEED: 110
        }
    },
    "0720": {
        FormEnum.CONFINED: {
            PocketMonsterParamEnum.NAME: "Hoopa",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.PSYCHIC,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.GHOST,
            StatsEnum.HP: 80,
            StatsEnum.ATTACK: 110,
            StatsEnum.DEFENSE: 60,
            StatsEnum.SPECIAL_ATTACK: 150,
            StatsEnum.SPECIAL_DEFENSE: 130,
            StatsEnum.SPEED: 70
        },
        FormEnum.UNBOUND: {
            PocketMonsterParamEnum.NAME: "Hoopa",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.PSYCHIC,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.DARK,
            StatsEnum.HP: 80,
            StatsEnum.ATTACK: 160,
            StatsEnum.DEFENSE: 60,
            StatsEnum.SPECIAL_ATTACK: 170,
            StatsEnum.SPECIAL_DEFENSE: 130,
            StatsEnum.SPEED: 80
        }
    },
    "0721": {
        None: {
            PocketMonsterParamEnum.NAME: "Volcanion",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.FIRE,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.WATER,
            StatsEnum.HP: 80,
            StatsEnum.ATTACK: 110,
            StatsEnum.DEFENSE: 120,
            StatsEnum.SPECIAL_ATTACK: 130,
            StatsEnum.SPECIAL_DEFENSE: 90,
            StatsEnum.SPEED: 70
        }
    },
    "0722": {
        None: {
            PocketMonsterParamEnum.NAME: "Rowlet",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.GRASS,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.FLYING,
            StatsEnum.HP: 68,
            StatsEnum.ATTACK: 55,
            StatsEnum.DEFENSE: 55,
            StatsEnum.SPECIAL_ATTACK: 50,
            StatsEnum.SPECIAL_DEFENSE: 50,
            StatsEnum.SPEED: 42
        }
    },
    "0723": {
        None: {
            PocketMonsterParamEnum.NAME: "Dartrix",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.GRASS,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.FLYING,
            StatsEnum.HP: 78,
            StatsEnum.ATTACK: 75,
            StatsEnum.DEFENSE: 75,
            StatsEnum.SPECIAL_ATTACK: 70,
            StatsEnum.SPECIAL_DEFENSE: 70,
            StatsEnum.SPEED: 52
        }
    },
    "0724": {
        None: {
            PocketMonsterParamEnum.NAME: "Decidueye",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.GRASS,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.GHOST,
            StatsEnum.HP: 78,
            StatsEnum.ATTACK: 107,
            StatsEnum.DEFENSE: 75,
            StatsEnum.SPECIAL_ATTACK: 100,
            StatsEnum.SPECIAL_DEFENSE: 100,
            StatsEnum.SPEED: 70
        },
        FormEnum.HISUIAN: {
            PocketMonsterParamEnum.NAME: "Decidueye",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.GRASS,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.FIGHTING,
            StatsEnum.HP: 88,
            StatsEnum.ATTACK: 112,
            StatsEnum.DEFENSE: 80,
            StatsEnum.SPECIAL_ATTACK: 95,
            StatsEnum.SPECIAL_DEFENSE: 95,
            StatsEnum.SPEED: 60
        }
    },
    "0725": {
        None: {
            PocketMonsterParamEnum.NAME: "Litten",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.FIRE,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 45,
            StatsEnum.ATTACK: 65,
            StatsEnum.DEFENSE: 40,
            StatsEnum.SPECIAL_ATTACK: 60,
            StatsEnum.SPECIAL_DEFENSE: 40,
            StatsEnum.SPEED: 70
        }
    },
    "0726": {
        None: {
            PocketMonsterParamEnum.NAME: "Torracat",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.FIRE,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 65,
            StatsEnum.ATTACK: 85,
            StatsEnum.DEFENSE: 50,
            StatsEnum.SPECIAL_ATTACK: 80,
            StatsEnum.SPECIAL_DEFENSE: 50,
            StatsEnum.SPEED: 90
        }
    },
    "0727": {
        None: {
            PocketMonsterParamEnum.NAME: "Incineroar",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.FIRE,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.DARK,
            StatsEnum.HP: 95,
            StatsEnum.ATTACK: 115,
            StatsEnum.DEFENSE: 90,
            StatsEnum.SPECIAL_ATTACK: 80,
            StatsEnum.SPECIAL_DEFENSE: 90,
            StatsEnum.SPEED: 60
        }
    },
    "0728": {
        None: {
            PocketMonsterParamEnum.NAME: "Popplio",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.WATER,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 50,
            StatsEnum.ATTACK: 54,
            StatsEnum.DEFENSE: 54,
            StatsEnum.SPECIAL_ATTACK: 66,
            StatsEnum.SPECIAL_DEFENSE: 56,
            StatsEnum.SPEED: 40
        }
    },
    "0729": {
        None: {
            PocketMonsterParamEnum.NAME: "Brionne",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.WATER,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 60,
            StatsEnum.ATTACK: 69,
            StatsEnum.DEFENSE: 69,
            StatsEnum.SPECIAL_ATTACK: 91,
            StatsEnum.SPECIAL_DEFENSE: 81,
            StatsEnum.SPEED: 50
        }
    },
    "0730": {
        None: {
            PocketMonsterParamEnum.NAME: "Primarina",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.WATER,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.FAIRY,
            StatsEnum.HP: 80,
            StatsEnum.ATTACK: 74,
            StatsEnum.DEFENSE: 74,
            StatsEnum.SPECIAL_ATTACK: 126,
            StatsEnum.SPECIAL_DEFENSE: 116,
            StatsEnum.SPEED: 60
        }
    },
    "0731": {
        None: {
            PocketMonsterParamEnum.NAME: "Pikipek",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.NORMAL,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.FLYING,
            StatsEnum.HP: 35,
            StatsEnum.ATTACK: 75,
            StatsEnum.DEFENSE: 30,
            StatsEnum.SPECIAL_ATTACK: 30,
            StatsEnum.SPECIAL_DEFENSE: 30,
            StatsEnum.SPEED: 65
        }
    },
    "0732": {
        None: {
            PocketMonsterParamEnum.NAME: "Trumbeak",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.NORMAL,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.FLYING,
            StatsEnum.HP: 55,
            StatsEnum.ATTACK: 85,
            StatsEnum.DEFENSE: 50,
            StatsEnum.SPECIAL_ATTACK: 40,
            StatsEnum.SPECIAL_DEFENSE: 50,
            StatsEnum.SPEED: 75
        }
    },
    "0733": {
        None: {
            PocketMonsterParamEnum.NAME: "Toucannon",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.NORMAL,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.FLYING,
            StatsEnum.HP: 80,
            StatsEnum.ATTACK: 120,
            StatsEnum.DEFENSE: 75,
            StatsEnum.SPECIAL_ATTACK: 75,
            StatsEnum.SPECIAL_DEFENSE: 75,
            StatsEnum.SPEED: 60
        }
    },
    "0734": {
        None: {
            PocketMonsterParamEnum.NAME: "Yungoos",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.NORMAL,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 48,
            StatsEnum.ATTACK: 70,
            StatsEnum.DEFENSE: 30,
            StatsEnum.SPECIAL_ATTACK: 30,
            StatsEnum.SPECIAL_DEFENSE: 30,
            StatsEnum.SPEED: 45
        }
    },
    "0735": {
        None: {
            PocketMonsterParamEnum.NAME: "Gumshoos",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.NORMAL,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 88,
            StatsEnum.ATTACK: 110,
            StatsEnum.DEFENSE: 60,
            StatsEnum.SPECIAL_ATTACK: 55,
            StatsEnum.SPECIAL_DEFENSE: 60,
            StatsEnum.SPEED: 45
        }
    },
    "0736": {
        None: {
            PocketMonsterParamEnum.NAME: "Grubbin",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.BUG,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 47,
            StatsEnum.ATTACK: 62,
            StatsEnum.DEFENSE: 45,
            StatsEnum.SPECIAL_ATTACK: 55,
            StatsEnum.SPECIAL_DEFENSE: 45,
            StatsEnum.SPEED: 46
        }
    },
    "0737": {
        None: {
            PocketMonsterParamEnum.NAME: "Charjabug",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.BUG,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.ELECTRIC,
            StatsEnum.HP: 57,
            StatsEnum.ATTACK: 82,
            StatsEnum.DEFENSE: 95,
            StatsEnum.SPECIAL_ATTACK: 55,
            StatsEnum.SPECIAL_DEFENSE: 75,
            StatsEnum.SPEED: 36
        }
    },
    "0738": {
        None: {
            PocketMonsterParamEnum.NAME: "Vikavolt",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.BUG,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.ELECTRIC,
            StatsEnum.HP: 77,
            StatsEnum.ATTACK: 70,
            StatsEnum.DEFENSE: 90,
            StatsEnum.SPECIAL_ATTACK: 145,
            StatsEnum.SPECIAL_DEFENSE: 75,
            StatsEnum.SPEED: 43
        }
    },
    "0739": {
        None: {
            PocketMonsterParamEnum.NAME: "Crabrawler",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.FIGHTING,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 47,
            StatsEnum.ATTACK: 82,
            StatsEnum.DEFENSE: 57,
            StatsEnum.SPECIAL_ATTACK: 42,
            StatsEnum.SPECIAL_DEFENSE: 47,
            StatsEnum.SPEED: 63
        }
    },
    "0740": {
        None: {
            PocketMonsterParamEnum.NAME: "Crabominable",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.FIGHTING,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.ICE,
            StatsEnum.HP: 97,
            StatsEnum.ATTACK: 132,
            StatsEnum.DEFENSE: 77,
            StatsEnum.SPECIAL_ATTACK: 62,
            StatsEnum.SPECIAL_DEFENSE: 67,
            StatsEnum.SPEED: 43
        }
    },
    "0741": {
        FormEnum.BAILE_STYLE: {
            PocketMonsterParamEnum.NAME: "Oricorio",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.FIRE,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.FLYING,
            StatsEnum.HP: 75,
            StatsEnum.ATTACK: 70,
            StatsEnum.DEFENSE: 70,
            StatsEnum.SPECIAL_ATTACK: 98,
            StatsEnum.SPECIAL_DEFENSE: 70,
            StatsEnum.SPEED: 93
        },
        FormEnum.POM_POM_STYLE: {
            PocketMonsterParamEnum.NAME: "Oricorio",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.ELECTRIC,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.FLYING,
            StatsEnum.HP: 75,
            StatsEnum.ATTACK: 70,
            StatsEnum.DEFENSE: 70,
            StatsEnum.SPECIAL_ATTACK: 98,
            StatsEnum.SPECIAL_DEFENSE: 70,
            StatsEnum.SPEED: 93
        },
        FormEnum.PAU_STYLE: {
            PocketMonsterParamEnum.NAME: "Oricorio",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.PSYCHIC,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.FLYING,
            StatsEnum.HP: 75,
            StatsEnum.ATTACK: 70,
            StatsEnum.DEFENSE: 70,
            StatsEnum.SPECIAL_ATTACK: 98,
            StatsEnum.SPECIAL_DEFENSE: 70,
            StatsEnum.SPEED: 93
        },
        FormEnum.SENSU_STYLE: {
            PocketMonsterParamEnum.NAME: "Oricorio",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.GHOST,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.FLYING,
            StatsEnum.HP: 75,
            StatsEnum.ATTACK: 70,
            StatsEnum.DEFENSE: 70,
            StatsEnum.SPECIAL_ATTACK: 98,
            StatsEnum.SPECIAL_DEFENSE: 70,
            StatsEnum.SPEED: 93
        }
    },
    "0742": {
        None: {
            PocketMonsterParamEnum.NAME: "Cutiefly",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.BUG,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.FAIRY,
            StatsEnum.HP: 40,
            StatsEnum.ATTACK: 45,
            StatsEnum.DEFENSE: 40,
            StatsEnum.SPECIAL_ATTACK: 55,
            StatsEnum.SPECIAL_DEFENSE: 40,
            StatsEnum.SPEED: 84
        }
    },
    "0743": {
        None: {
            PocketMonsterParamEnum.NAME: "Ribombee",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.BUG,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.FAIRY,
            StatsEnum.HP: 60,
            StatsEnum.ATTACK: 55,
            StatsEnum.DEFENSE: 60,
            StatsEnum.SPECIAL_ATTACK: 95,
            StatsEnum.SPECIAL_DEFENSE: 70,
            StatsEnum.SPEED: 124
        }
    },
    "0744": {
        None: {
            PocketMonsterParamEnum.NAME: "Rockruff",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.ROCK,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 45,
            StatsEnum.ATTACK: 65,
            StatsEnum.DEFENSE: 40,
            StatsEnum.SPECIAL_ATTACK: 30,
            StatsEnum.SPECIAL_DEFENSE: 40,
            StatsEnum.SPEED: 60
        },
        FormEnum.OWN_TEMPO: {
            PocketMonsterParamEnum.NAME: "Rockruff",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.ROCK,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 45,
            StatsEnum.ATTACK: 65,
            StatsEnum.DEFENSE: 40,
            StatsEnum.SPECIAL_ATTACK: 30,
            StatsEnum.SPECIAL_DEFENSE: 40,
            StatsEnum.SPEED: 60
        }
    },
    "0745": {
        FormEnum.MIDDAY_FORM: {
            PocketMonsterParamEnum.NAME: "Lycanroc",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.ROCK,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 75,
            StatsEnum.ATTACK: 115,
            StatsEnum.DEFENSE: 65,
            StatsEnum.SPECIAL_ATTACK: 55,
            StatsEnum.SPECIAL_DEFENSE: 65,
            StatsEnum.SPEED: 112
        },
        FormEnum.MIDNIGHT_FORM: {
            PocketMonsterParamEnum.NAME: "Lycanroc",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.ROCK,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 85,
            StatsEnum.ATTACK: 115,
            StatsEnum.DEFENSE: 75,
            StatsEnum.SPECIAL_ATTACK: 55,
            StatsEnum.SPECIAL_DEFENSE: 75,
            StatsEnum.SPEED: 82
        },
        FormEnum.DUSK_FORM: {
            PocketMonsterParamEnum.NAME: "Lycanroc",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.ROCK,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 75,
            StatsEnum.ATTACK: 117,
            StatsEnum.DEFENSE: 65,
            StatsEnum.SPECIAL_ATTACK: 55,
            StatsEnum.SPECIAL_DEFENSE: 65,
            StatsEnum.SPEED: 110
        }
    },
    "0746": {
        FormEnum.SOLO_FORM: {
            PocketMonsterParamEnum.NAME: "Wishiwashi",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.WATER,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 45,
            StatsEnum.ATTACK: 20,
            StatsEnum.DEFENSE: 20,
            StatsEnum.SPECIAL_ATTACK: 25,
            StatsEnum.SPECIAL_DEFENSE: 25,
            StatsEnum.SPEED: 40
        },
        FormEnum.SCHOOL_FORM: {
            PocketMonsterParamEnum.NAME: "Wishiwashi",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.WATER,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 45,
            StatsEnum.ATTACK: 140,
            StatsEnum.DEFENSE: 130,
            StatsEnum.SPECIAL_ATTACK: 140,
            StatsEnum.SPECIAL_DEFENSE: 135,
            StatsEnum.SPEED: 30
        }
    },
    "0747": {
        None: {
            PocketMonsterParamEnum.NAME: "Mareanie",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.POISON,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.WATER,
            StatsEnum.HP: 50,
            StatsEnum.ATTACK: 53,
            StatsEnum.DEFENSE: 62,
            StatsEnum.SPECIAL_ATTACK: 43,
            StatsEnum.SPECIAL_DEFENSE: 52,
            StatsEnum.SPEED: 45
        }
    },
    "0748": {
        None: {
            PocketMonsterParamEnum.NAME: "Toxapex",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.POISON,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.WATER,
            StatsEnum.HP: 50,
            StatsEnum.ATTACK: 63,
            StatsEnum.DEFENSE: 152,
            StatsEnum.SPECIAL_ATTACK: 53,
            StatsEnum.SPECIAL_DEFENSE: 142,
            StatsEnum.SPEED: 35
        }
    },
    "0749": {
        None: {
            PocketMonsterParamEnum.NAME: "Mudbray",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.GROUND,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 70,
            StatsEnum.ATTACK: 100,
            StatsEnum.DEFENSE: 70,
            StatsEnum.SPECIAL_ATTACK: 45,
            StatsEnum.SPECIAL_DEFENSE: 55,
            StatsEnum.SPEED: 45
        }
    },
    "0750": {
        None: {
            PocketMonsterParamEnum.NAME: "Mudsdale",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.GROUND,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 100,
            StatsEnum.ATTACK: 125,
            StatsEnum.DEFENSE: 100,
            StatsEnum.SPECIAL_ATTACK: 55,
            StatsEnum.SPECIAL_DEFENSE: 85,
            StatsEnum.SPEED: 35
        }
    },
    "0751": {
        None: {
            PocketMonsterParamEnum.NAME: "Dewpider",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.WATER,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.BUG,
            StatsEnum.HP: 38,
            StatsEnum.ATTACK: 40,
            StatsEnum.DEFENSE: 52,
            StatsEnum.SPECIAL_ATTACK: 40,
            StatsEnum.SPECIAL_DEFENSE: 72,
            StatsEnum.SPEED: 27
        }
    },
    "0752": {
        None: {
            PocketMonsterParamEnum.NAME: "Araquanid",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.WATER,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.BUG,
            StatsEnum.HP: 68,
            StatsEnum.ATTACK: 70,
            StatsEnum.DEFENSE: 92,
            StatsEnum.SPECIAL_ATTACK: 50,
            StatsEnum.SPECIAL_DEFENSE: 132,
            StatsEnum.SPEED: 42
        }
    },
    "0753": {
        None: {
            PocketMonsterParamEnum.NAME: "Fomantis",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.GRASS,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 40,
            StatsEnum.ATTACK: 55,
            StatsEnum.DEFENSE: 35,
            StatsEnum.SPECIAL_ATTACK: 50,
            StatsEnum.SPECIAL_DEFENSE: 35,
            StatsEnum.SPEED: 35
        }
    },
    "0754": {
        None: {
            PocketMonsterParamEnum.NAME: "Lurantis",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.GRASS,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 70,
            StatsEnum.ATTACK: 105,
            StatsEnum.DEFENSE: 90,
            StatsEnum.SPECIAL_ATTACK: 80,
            StatsEnum.SPECIAL_DEFENSE: 90,
            StatsEnum.SPEED: 45
        }
    },
    "0755": {
        None: {
            PocketMonsterParamEnum.NAME: "Morelull",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.GRASS,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.FAIRY,
            StatsEnum.HP: 40,
            StatsEnum.ATTACK: 35,
            StatsEnum.DEFENSE: 55,
            StatsEnum.SPECIAL_ATTACK: 65,
            StatsEnum.SPECIAL_DEFENSE: 75,
            StatsEnum.SPEED: 15
        }
    },
    "0756": {
        None: {
            PocketMonsterParamEnum.NAME: "Shiinotic",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.GRASS,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.FAIRY,
            StatsEnum.HP: 60,
            StatsEnum.ATTACK: 45,
            StatsEnum.DEFENSE: 80,
            StatsEnum.SPECIAL_ATTACK: 90,
            StatsEnum.SPECIAL_DEFENSE: 100,
            StatsEnum.SPEED: 30
        }
    },
    "0757": {
        None: {
            PocketMonsterParamEnum.NAME: "Salandit",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.POISON,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.FIRE,
            StatsEnum.HP: 48,
            StatsEnum.ATTACK: 44,
            StatsEnum.DEFENSE: 40,
            StatsEnum.SPECIAL_ATTACK: 71,
            StatsEnum.SPECIAL_DEFENSE: 40,
            StatsEnum.SPEED: 77
        }
    },
    "0758": {
        None: {
            PocketMonsterParamEnum.NAME: "Salazzle",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.POISON,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.FIRE,
            StatsEnum.HP: 68,
            StatsEnum.ATTACK: 64,
            StatsEnum.DEFENSE: 60,
            StatsEnum.SPECIAL_ATTACK: 111,
            StatsEnum.SPECIAL_DEFENSE: 60,
            StatsEnum.SPEED: 117
        }
    },
    "0759": {
        None: {
            PocketMonsterParamEnum.NAME: "Stufful",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.NORMAL,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.FIGHTING,
            StatsEnum.HP: 70,
            StatsEnum.ATTACK: 75,
            StatsEnum.DEFENSE: 50,
            StatsEnum.SPECIAL_ATTACK: 45,
            StatsEnum.SPECIAL_DEFENSE: 50,
            StatsEnum.SPEED: 50
        }
    },
    "0760": {
        None: {
            PocketMonsterParamEnum.NAME: "Bewear",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.NORMAL,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.FIGHTING,
            StatsEnum.HP: 120,
            StatsEnum.ATTACK: 125,
            StatsEnum.DEFENSE: 80,
            StatsEnum.SPECIAL_ATTACK: 55,
            StatsEnum.SPECIAL_DEFENSE: 60,
            StatsEnum.SPEED: 60
        }
    },
    "0761": {
        None: {
            PocketMonsterParamEnum.NAME: "Bounsweet",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.GRASS,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 42,
            StatsEnum.ATTACK: 30,
            StatsEnum.DEFENSE: 38,
            StatsEnum.SPECIAL_ATTACK: 30,
            StatsEnum.SPECIAL_DEFENSE: 38,
            StatsEnum.SPEED: 32
        }
    },
    "0762": {
        None: {
            PocketMonsterParamEnum.NAME: "Steenee",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.GRASS,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 52,
            StatsEnum.ATTACK: 40,
            StatsEnum.DEFENSE: 48,
            StatsEnum.SPECIAL_ATTACK: 40,
            StatsEnum.SPECIAL_DEFENSE: 48,
            StatsEnum.SPEED: 62
        }
    },
    "0763": {
        None: {
            PocketMonsterParamEnum.NAME: "Tsareena",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.GRASS,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 72,
            StatsEnum.ATTACK: 120,
            StatsEnum.DEFENSE: 98,
            StatsEnum.SPECIAL_ATTACK: 50,
            StatsEnum.SPECIAL_DEFENSE: 98,
            StatsEnum.SPEED: 72
        }
    },
    "0764": {
        None: {
            PocketMonsterParamEnum.NAME: "Comfey",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.FAIRY,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 51,
            StatsEnum.ATTACK: 52,
            StatsEnum.DEFENSE: 90,
            StatsEnum.SPECIAL_ATTACK: 82,
            StatsEnum.SPECIAL_DEFENSE: 110,
            StatsEnum.SPEED: 100
        }
    },
    "0765": {
        None: {
            PocketMonsterParamEnum.NAME: "Oranguru",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.NORMAL,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.PSYCHIC,
            StatsEnum.HP: 90,
            StatsEnum.ATTACK: 60,
            StatsEnum.DEFENSE: 80,
            StatsEnum.SPECIAL_ATTACK: 90,
            StatsEnum.SPECIAL_DEFENSE: 110,
            StatsEnum.SPEED: 60
        }
    },
    "0766": {
        None: {
            PocketMonsterParamEnum.NAME: "Passimian",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.FIGHTING,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 100,
            StatsEnum.ATTACK: 120,
            StatsEnum.DEFENSE: 90,
            StatsEnum.SPECIAL_ATTACK: 40,
            StatsEnum.SPECIAL_DEFENSE: 60,
            StatsEnum.SPEED: 80
        }
    },
    "0767": {
        None: {
            PocketMonsterParamEnum.NAME: "Wimpod",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.BUG,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.WATER,
            StatsEnum.HP: 25,
            StatsEnum.ATTACK: 35,
            StatsEnum.DEFENSE: 40,
            StatsEnum.SPECIAL_ATTACK: 20,
            StatsEnum.SPECIAL_DEFENSE: 30,
            StatsEnum.SPEED: 80
        }
    },
    "0768": {
        None: {
            PocketMonsterParamEnum.NAME: "Golisopod",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.BUG,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.WATER,
            StatsEnum.HP: 75,
            StatsEnum.ATTACK: 125,
            StatsEnum.DEFENSE: 140,
            StatsEnum.SPECIAL_ATTACK: 60,
            StatsEnum.SPECIAL_DEFENSE: 90,
            StatsEnum.SPEED: 40
        }
    },
    "0769": {
        None: {
            PocketMonsterParamEnum.NAME: "Sandygast",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.GHOST,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.GROUND,
            StatsEnum.HP: 55,
            StatsEnum.ATTACK: 55,
            StatsEnum.DEFENSE: 80,
            StatsEnum.SPECIAL_ATTACK: 70,
            StatsEnum.SPECIAL_DEFENSE: 45,
            StatsEnum.SPEED: 15
        }
    },
    "0770": {
        None: {
            PocketMonsterParamEnum.NAME: "Palossand",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.GHOST,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.GROUND,
            StatsEnum.HP: 85,
            StatsEnum.ATTACK: 75,
            StatsEnum.DEFENSE: 110,
            StatsEnum.SPECIAL_ATTACK: 100,
            StatsEnum.SPECIAL_DEFENSE: 75,
            StatsEnum.SPEED: 35
        }
    },
    "0771": {
        None: {
            PocketMonsterParamEnum.NAME: "Pyukumuku",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.WATER,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 55,
            StatsEnum.ATTACK: 60,
            StatsEnum.DEFENSE: 130,
            StatsEnum.SPECIAL_ATTACK: 30,
            StatsEnum.SPECIAL_DEFENSE: 130,
            StatsEnum.SPEED: 5
        }
    },
    "0772": {
        None: {
            PocketMonsterParamEnum.NAME: "Type: Null",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.NORMAL,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 95,
            StatsEnum.ATTACK: 95,
            StatsEnum.DEFENSE: 95,
            StatsEnum.SPECIAL_ATTACK: 95,
            StatsEnum.SPECIAL_DEFENSE: 95,
            StatsEnum.SPEED: 59
        }
    },
    "0773": {
        None: {
            PocketMonsterParamEnum.NAME: "Silvally",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.NORMAL,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 95,
            StatsEnum.ATTACK: 95,
            StatsEnum.DEFENSE: 95,
            StatsEnum.SPECIAL_ATTACK: 95,
            StatsEnum.SPECIAL_DEFENSE: 95,
            StatsEnum.SPEED: 95
        }
    },
    "0774": {
        FormEnum.METEOR_FORM: {
            PocketMonsterParamEnum.NAME: "Minior",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.ROCK,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.FLYING,
            StatsEnum.HP: 60,
            StatsEnum.ATTACK: 60,
            StatsEnum.DEFENSE: 100,
            StatsEnum.SPECIAL_ATTACK: 60,
            StatsEnum.SPECIAL_DEFENSE: 100,
            StatsEnum.SPEED: 60
        },
        FormEnum.CORE_FORM: {
            PocketMonsterParamEnum.NAME: "Minior",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.ROCK,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.FLYING,
            StatsEnum.HP: 60,
            StatsEnum.ATTACK: 100,
            StatsEnum.DEFENSE: 60,
            StatsEnum.SPECIAL_ATTACK: 100,
            StatsEnum.SPECIAL_DEFENSE: 60,
            StatsEnum.SPEED: 120
        }
    },
    "0775": {
        None: {
            PocketMonsterParamEnum.NAME: "Komala",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.NORMAL,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 65,
            StatsEnum.ATTACK: 115,
            StatsEnum.DEFENSE: 65,
            StatsEnum.SPECIAL_ATTACK: 75,
            StatsEnum.SPECIAL_DEFENSE: 95,
            StatsEnum.SPEED: 65
        }
    },
    "0776": {
        None: {
            PocketMonsterParamEnum.NAME: "Turtonator",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.FIRE,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.DRAGON,
            StatsEnum.HP: 60,
            StatsEnum.ATTACK: 78,
            StatsEnum.DEFENSE: 135,
            StatsEnum.SPECIAL_ATTACK: 91,
            StatsEnum.SPECIAL_DEFENSE: 85,
            StatsEnum.SPEED: 36
        }
    },
    "0777": {
        None: {
            PocketMonsterParamEnum.NAME: "Togedemaru",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.ELECTRIC,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.STEEL,
            StatsEnum.HP: 65,
            StatsEnum.ATTACK: 98,
            StatsEnum.DEFENSE: 63,
            StatsEnum.SPECIAL_ATTACK: 40,
            StatsEnum.SPECIAL_DEFENSE: 73,
            StatsEnum.SPEED: 96
        }
    },
    "0778": {
        None: {
            PocketMonsterParamEnum.NAME: "Mimikyu",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.GHOST,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.FAIRY,
            StatsEnum.HP: 55,
            StatsEnum.ATTACK: 90,
            StatsEnum.DEFENSE: 80,
            StatsEnum.SPECIAL_ATTACK: 50,
            StatsEnum.SPECIAL_DEFENSE: 105,
            StatsEnum.SPEED: 96
        }
    },
    "0779": {
        None: {
            PocketMonsterParamEnum.NAME: "Bruxish",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.WATER,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.PSYCHIC,
            StatsEnum.HP: 68,
            StatsEnum.ATTACK: 105,
            StatsEnum.DEFENSE: 70,
            StatsEnum.SPECIAL_ATTACK: 70,
            StatsEnum.SPECIAL_DEFENSE: 70,
            StatsEnum.SPEED: 92
        }
    },
    "0780": {
        None: {
            PocketMonsterParamEnum.NAME: "Drampa",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.NORMAL,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.DRAGON,
            StatsEnum.HP: 78,
            StatsEnum.ATTACK: 60,
            StatsEnum.DEFENSE: 85,
            StatsEnum.SPECIAL_ATTACK: 135,
            StatsEnum.SPECIAL_DEFENSE: 91,
            StatsEnum.SPEED: 36
        }
    },
    "0781": {
        None: {
            PocketMonsterParamEnum.NAME: "Dhelmise",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.GHOST,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.GRASS,
            StatsEnum.HP: 70,
            StatsEnum.ATTACK: 131,
            StatsEnum.DEFENSE: 100,
            StatsEnum.SPECIAL_ATTACK: 86,
            StatsEnum.SPECIAL_DEFENSE: 90,
            StatsEnum.SPEED: 40
        }
    },
    "0782": {
        None: {
            PocketMonsterParamEnum.NAME: "Jangmo-o",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.DRAGON,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 45,
            StatsEnum.ATTACK: 55,
            StatsEnum.DEFENSE: 65,
            StatsEnum.SPECIAL_ATTACK: 45,
            StatsEnum.SPECIAL_DEFENSE: 45,
            StatsEnum.SPEED: 45
        }
    },
    "0783": {
        None: {
            PocketMonsterParamEnum.NAME: "Hakamo-o",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.DRAGON,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.FIGHTING,
            StatsEnum.HP: 55,
            StatsEnum.ATTACK: 75,
            StatsEnum.DEFENSE: 90,
            StatsEnum.SPECIAL_ATTACK: 65,
            StatsEnum.SPECIAL_DEFENSE: 70,
            StatsEnum.SPEED: 65
        }
    },
    "0784": {
        None: {
            PocketMonsterParamEnum.NAME: "Kommo-o",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.DRAGON,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.FIGHTING,
            StatsEnum.HP: 75,
            StatsEnum.ATTACK: 110,
            StatsEnum.DEFENSE: 125,
            StatsEnum.SPECIAL_ATTACK: 100,
            StatsEnum.SPECIAL_DEFENSE: 105,
            StatsEnum.SPEED: 85
        }
    },
    "0785": {
        None: {
            PocketMonsterParamEnum.NAME: "Tapu Koko",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.ELECTRIC,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.FAIRY,
            StatsEnum.HP: 70,
            StatsEnum.ATTACK: 115,
            StatsEnum.DEFENSE: 85,
            StatsEnum.SPECIAL_ATTACK: 95,
            StatsEnum.SPECIAL_DEFENSE: 75,
            StatsEnum.SPEED: 130
        }
    },
    "0786": {
        None: {
            PocketMonsterParamEnum.NAME: "Tapu Lele",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.PSYCHIC,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.FAIRY,
            StatsEnum.HP: 70,
            StatsEnum.ATTACK: 85,
            StatsEnum.DEFENSE: 75,
            StatsEnum.SPECIAL_ATTACK: 130,
            StatsEnum.SPECIAL_DEFENSE: 115,
            StatsEnum.SPEED: 95
        }
    },
    "0787": {
        None: {
            PocketMonsterParamEnum.NAME: "Tapu Bulu",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.GRASS,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.FAIRY,
            StatsEnum.HP: 70,
            StatsEnum.ATTACK: 130,
            StatsEnum.DEFENSE: 115,
            StatsEnum.SPECIAL_ATTACK: 85,
            StatsEnum.SPECIAL_DEFENSE: 95,
            StatsEnum.SPEED: 75
        }
    },
    "0788": {
        None: {
            PocketMonsterParamEnum.NAME: "Tapu Fini",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.WATER,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.FAIRY,
            StatsEnum.HP: 70,
            StatsEnum.ATTACK: 75,
            StatsEnum.DEFENSE: 115,
            StatsEnum.SPECIAL_ATTACK: 95,
            StatsEnum.SPECIAL_DEFENSE: 130,
            StatsEnum.SPEED: 85
        }
    },
    "0789": {
        None: {
            PocketMonsterParamEnum.NAME: "Cosmog",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.PSYCHIC,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 43,
            StatsEnum.ATTACK: 29,
            StatsEnum.DEFENSE: 31,
            StatsEnum.SPECIAL_ATTACK: 29,
            StatsEnum.SPECIAL_DEFENSE: 31,
            StatsEnum.SPEED: 37
        }
    },
    "0790": {
        None: {
            PocketMonsterParamEnum.NAME: "Cosmoem",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.PSYCHIC,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 43,
            StatsEnum.ATTACK: 29,
            StatsEnum.DEFENSE: 131,
            StatsEnum.SPECIAL_ATTACK: 29,
            StatsEnum.SPECIAL_DEFENSE: 131,
            StatsEnum.SPEED: 37
        }
    },
    "0791": {
        None: {
            PocketMonsterParamEnum.NAME: "Solgaleo",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.PSYCHIC,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.STEEL,
            StatsEnum.HP: 137,
            StatsEnum.ATTACK: 137,
            StatsEnum.DEFENSE: 107,
            StatsEnum.SPECIAL_ATTACK: 113,
            StatsEnum.SPECIAL_DEFENSE: 89,
            StatsEnum.SPEED: 97
        }
    },
    "0792": {
        None: {
            PocketMonsterParamEnum.NAME: "Lunala",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.PSYCHIC,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.GHOST,
            StatsEnum.HP: 137,
            StatsEnum.ATTACK: 113,
            StatsEnum.DEFENSE: 89,
            StatsEnum.SPECIAL_ATTACK: 137,
            StatsEnum.SPECIAL_DEFENSE: 107,
            StatsEnum.SPEED: 97
        }
    },
    "0793": {
        None: {
            PocketMonsterParamEnum.NAME: "Nihilego",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.ROCK,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.POISON,
            StatsEnum.HP: 109,
            StatsEnum.ATTACK: 53,
            StatsEnum.DEFENSE: 47,
            StatsEnum.SPECIAL_ATTACK: 127,
            StatsEnum.SPECIAL_DEFENSE: 131,
            StatsEnum.SPEED: 103
        }
    },
    "0794": {
        None: {
            PocketMonsterParamEnum.NAME: "Buzzwole",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.BUG,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.FIGHTING,
            StatsEnum.HP: 107,
            StatsEnum.ATTACK: 139,
            StatsEnum.DEFENSE: 139,
            StatsEnum.SPECIAL_ATTACK: 53,
            StatsEnum.SPECIAL_DEFENSE: 53,
            StatsEnum.SPEED: 79
        }
    },
    "0795": {
        None: {
            PocketMonsterParamEnum.NAME: "Pheromosa",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.BUG,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.FIGHTING,
            StatsEnum.HP: 71,
            StatsEnum.ATTACK: 137,
            StatsEnum.DEFENSE: 37,
            StatsEnum.SPECIAL_ATTACK: 137,
            StatsEnum.SPECIAL_DEFENSE: 37,
            StatsEnum.SPEED: 151
        }
    },
    "0796": {
        None: {
            PocketMonsterParamEnum.NAME: "Xurkitree",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.ELECTRIC,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 83,
            StatsEnum.ATTACK: 89,
            StatsEnum.DEFENSE: 71,
            StatsEnum.SPECIAL_ATTACK: 173,
            StatsEnum.SPECIAL_DEFENSE: 71,
            StatsEnum.SPEED: 83
        }
    },
    "0797": {
        None: {
            PocketMonsterParamEnum.NAME: "Celesteela",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.STEEL,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.FLYING,
            StatsEnum.HP: 97,
            StatsEnum.ATTACK: 101,
            StatsEnum.DEFENSE: 103,
            StatsEnum.SPECIAL_ATTACK: 107,
            StatsEnum.SPECIAL_DEFENSE: 101,
            StatsEnum.SPEED: 61
        }
    },
    "0798": {
        None: {
            PocketMonsterParamEnum.NAME: "Kartana",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.GRASS,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.STEEL,
            StatsEnum.HP: 59,
            StatsEnum.ATTACK: 181,
            StatsEnum.DEFENSE: 131,
            StatsEnum.SPECIAL_ATTACK: 59,
            StatsEnum.SPECIAL_DEFENSE: 31,
            StatsEnum.SPEED: 109
        }
    },
    "0799": {
        None: {
            PocketMonsterParamEnum.NAME: "Guzzlord",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.DARK,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.DRAGON,
            StatsEnum.HP: 223,
            StatsEnum.ATTACK: 101,
            StatsEnum.DEFENSE: 53,
            StatsEnum.SPECIAL_ATTACK: 97,
            StatsEnum.SPECIAL_DEFENSE: 53,
            StatsEnum.SPEED: 43
        }
    },
    "0800": {
        None: {
            PocketMonsterParamEnum.NAME: "Necrozma",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.PSYCHIC,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 97,
            StatsEnum.ATTACK: 107,
            StatsEnum.DEFENSE: 101,
            StatsEnum.SPECIAL_ATTACK: 127,
            StatsEnum.SPECIAL_DEFENSE: 89,
            StatsEnum.SPEED: 79
        },
        FormEnum.DUSK_MANE: {
            PocketMonsterParamEnum.NAME: "Necrozma",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.PSYCHIC,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.STEEL,
            StatsEnum.HP: 97,
            StatsEnum.ATTACK: 157,
            StatsEnum.DEFENSE: 127,
            StatsEnum.SPECIAL_ATTACK: 113,
            StatsEnum.SPECIAL_DEFENSE: 109,
            StatsEnum.SPEED: 77
        },
        FormEnum.DAWN_WINGS: {
            PocketMonsterParamEnum.NAME: "Necrozma",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.PSYCHIC,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.GHOST,
            StatsEnum.HP: 97,
            StatsEnum.ATTACK: 113,
            StatsEnum.DEFENSE: 109,
            StatsEnum.SPECIAL_ATTACK: 157,
            StatsEnum.SPECIAL_DEFENSE: 127,
            StatsEnum.SPEED: 77
        },
        FormEnum.ULTRA: {
            PocketMonsterParamEnum.NAME: "Necrozma",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.PSYCHIC,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.DRAGON,
            StatsEnum.HP: 97,
            StatsEnum.ATTACK: 167,
            StatsEnum.DEFENSE: 97,
            StatsEnum.SPECIAL_ATTACK: 167,
            StatsEnum.SPECIAL_DEFENSE: 97,
            StatsEnum.SPEED: 129
        }
    },
    "0801": {
        None: {
            PocketMonsterParamEnum.NAME: "Magearna",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.STEEL,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.FAIRY,
            StatsEnum.HP: 80,
            StatsEnum.ATTACK: 95,
            StatsEnum.DEFENSE: 115,
            StatsEnum.SPECIAL_ATTACK: 130,
            StatsEnum.SPECIAL_DEFENSE: 115,
            StatsEnum.SPEED: 65
        }
    },
    "0802": {
        None: {
            PocketMonsterParamEnum.NAME: "Marshadow",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.FIGHTING,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.GHOST,
            StatsEnum.HP: 90,
            StatsEnum.ATTACK: 125,
            StatsEnum.DEFENSE: 80,
            StatsEnum.SPECIAL_ATTACK: 90,
            StatsEnum.SPECIAL_DEFENSE: 90,
            StatsEnum.SPEED: 125
        }
    },
    "0803": {
        None: {
            PocketMonsterParamEnum.NAME: "Poipole",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.POISON,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 67,
            StatsEnum.ATTACK: 73,
            StatsEnum.DEFENSE: 67,
            StatsEnum.SPECIAL_ATTACK: 73,
            StatsEnum.SPECIAL_DEFENSE: 67,
            StatsEnum.SPEED: 73
        }
    },
    "0804": {
        None: {
            PocketMonsterParamEnum.NAME: "Naganadel",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.POISON,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.DRAGON,
            StatsEnum.HP: 73,
            StatsEnum.ATTACK: 73,
            StatsEnum.DEFENSE: 73,
            StatsEnum.SPECIAL_ATTACK: 127,
            StatsEnum.SPECIAL_DEFENSE: 73,
            StatsEnum.SPEED: 121
        }
    },
    "0805": {
        None: {
            PocketMonsterParamEnum.NAME: "Stakataka",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.ROCK,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.STEEL,
            StatsEnum.HP: 61,
            StatsEnum.ATTACK: 131,
            StatsEnum.DEFENSE: 211,
            StatsEnum.SPECIAL_ATTACK: 53,
            StatsEnum.SPECIAL_DEFENSE: 101,
            StatsEnum.SPEED: 13
        }
    },
    "0806": {
        None: {
            PocketMonsterParamEnum.NAME: "Blacephalon",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.FIRE,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.GHOST,
            StatsEnum.HP: 53,
            StatsEnum.ATTACK: 127,
            StatsEnum.DEFENSE: 53,
            StatsEnum.SPECIAL_ATTACK: 151,
            StatsEnum.SPECIAL_DEFENSE: 79,
            StatsEnum.SPEED: 107
        }
    },
    "0807": {
        None: {
            PocketMonsterParamEnum.NAME: "Zeraora",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.ELECTRIC,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 88,
            StatsEnum.ATTACK: 112,
            StatsEnum.DEFENSE: 75,
            StatsEnum.SPECIAL_ATTACK: 102,
            StatsEnum.SPECIAL_DEFENSE: 80,
            StatsEnum.SPEED: 143
        }
    },
    "0808": {
        None: {
            PocketMonsterParamEnum.NAME: "Meltan",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.STEEL,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 46,
            StatsEnum.ATTACK: 65,
            StatsEnum.DEFENSE: 65,
            StatsEnum.SPECIAL_ATTACK: 55,
            StatsEnum.SPECIAL_DEFENSE: 35,
            StatsEnum.SPEED: 34
        }
    },
    "0809": {
        None: {
            PocketMonsterParamEnum.NAME: "Melmetal",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.STEEL,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 135,
            StatsEnum.ATTACK: 143,
            StatsEnum.DEFENSE: 143,
            StatsEnum.SPECIAL_ATTACK: 80,
            StatsEnum.SPECIAL_DEFENSE: 65,
            StatsEnum.SPEED: 34
        }
    },
    "0810": {
        None: {
            PocketMonsterParamEnum.NAME: "Grookey",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.GRASS,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 50,
            StatsEnum.ATTACK: 65,
            StatsEnum.DEFENSE: 50,
            StatsEnum.SPECIAL_ATTACK: 40,
            StatsEnum.SPECIAL_DEFENSE: 40,
            StatsEnum.SPEED: 65
        }
    },
    "0811": {
        None: {
            PocketMonsterParamEnum.NAME: "Thwackey",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.GRASS,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 70,
            StatsEnum.ATTACK: 85,
            StatsEnum.DEFENSE: 70,
            StatsEnum.SPECIAL_ATTACK: 55,
            StatsEnum.SPECIAL_DEFENSE: 60,
            StatsEnum.SPEED: 80
        }
    },
    "0812": {
        None: {
            PocketMonsterParamEnum.NAME: "Rillaboom",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.GRASS,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 100,
            StatsEnum.ATTACK: 125,
            StatsEnum.DEFENSE: 90,
            StatsEnum.SPECIAL_ATTACK: 60,
            StatsEnum.SPECIAL_DEFENSE: 70,
            StatsEnum.SPEED: 85
        }
    },
    "0813": {
        None: {
            PocketMonsterParamEnum.NAME: "Scorbunny",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.FIRE,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 50,
            StatsEnum.ATTACK: 71,
            StatsEnum.DEFENSE: 40,
            StatsEnum.SPECIAL_ATTACK: 40,
            StatsEnum.SPECIAL_DEFENSE: 40,
            StatsEnum.SPEED: 69
        }
    },
    "0814": {
        None: {
            PocketMonsterParamEnum.NAME: "Raboot",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.FIRE,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 65,
            StatsEnum.ATTACK: 86,
            StatsEnum.DEFENSE: 60,
            StatsEnum.SPECIAL_ATTACK: 55,
            StatsEnum.SPECIAL_DEFENSE: 60,
            StatsEnum.SPEED: 94
        }
    },
    "0815": {
        None: {
            PocketMonsterParamEnum.NAME: "Cinderace",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.FIRE,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 80,
            StatsEnum.ATTACK: 116,
            StatsEnum.DEFENSE: 75,
            StatsEnum.SPECIAL_ATTACK: 65,
            StatsEnum.SPECIAL_DEFENSE: 75,
            StatsEnum.SPEED: 119
        }
    },
    "0816": {
        None: {
            PocketMonsterParamEnum.NAME: "Sobble",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.WATER,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 50,
            StatsEnum.ATTACK: 40,
            StatsEnum.DEFENSE: 40,
            StatsEnum.SPECIAL_ATTACK: 70,
            StatsEnum.SPECIAL_DEFENSE: 40,
            StatsEnum.SPEED: 70
        }
    },
    "0817": {
        None: {
            PocketMonsterParamEnum.NAME: "Drizzile",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.WATER,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 65,
            StatsEnum.ATTACK: 60,
            StatsEnum.DEFENSE: 55,
            StatsEnum.SPECIAL_ATTACK: 95,
            StatsEnum.SPECIAL_DEFENSE: 55,
            StatsEnum.SPEED: 90
        }
    },
    "0818": {
        None: {
            PocketMonsterParamEnum.NAME: "Inteleon",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.WATER,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 70,
            StatsEnum.ATTACK: 85,
            StatsEnum.DEFENSE: 65,
            StatsEnum.SPECIAL_ATTACK: 125,
            StatsEnum.SPECIAL_DEFENSE: 65,
            StatsEnum.SPEED: 120
        }
    },
    "0819": {
        None: {
            PocketMonsterParamEnum.NAME: "Skwovet",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.NORMAL,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 70,
            StatsEnum.ATTACK: 55,
            StatsEnum.DEFENSE: 55,
            StatsEnum.SPECIAL_ATTACK: 35,
            StatsEnum.SPECIAL_DEFENSE: 35,
            StatsEnum.SPEED: 25
        }
    },
    "0820": {
        None: {
            PocketMonsterParamEnum.NAME: "Greedent",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.NORMAL,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 120,
            StatsEnum.ATTACK: 95,
            StatsEnum.DEFENSE: 95,
            StatsEnum.SPECIAL_ATTACK: 55,
            StatsEnum.SPECIAL_DEFENSE: 75,
            StatsEnum.SPEED: 20
        }
    },
    "0821": {
        None: {
            PocketMonsterParamEnum.NAME: "Rookidee",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.FLYING,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 38,
            StatsEnum.ATTACK: 47,
            StatsEnum.DEFENSE: 35,
            StatsEnum.SPECIAL_ATTACK: 33,
            StatsEnum.SPECIAL_DEFENSE: 35,
            StatsEnum.SPEED: 57
        }
    },
    "0822": {
        None: {
            PocketMonsterParamEnum.NAME: "Corvisquire",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.FLYING,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 68,
            StatsEnum.ATTACK: 67,
            StatsEnum.DEFENSE: 55,
            StatsEnum.SPECIAL_ATTACK: 43,
            StatsEnum.SPECIAL_DEFENSE: 55,
            StatsEnum.SPEED: 77
        }
    },
    "0823": {
        None: {
            PocketMonsterParamEnum.NAME: "Corviknight",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.FLYING,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.STEEL,
            StatsEnum.HP: 98,
            StatsEnum.ATTACK: 87,
            StatsEnum.DEFENSE: 105,
            StatsEnum.SPECIAL_ATTACK: 53,
            StatsEnum.SPECIAL_DEFENSE: 85,
            StatsEnum.SPEED: 67
        }
    },
    "0824": {
        None: {
            PocketMonsterParamEnum.NAME: "Blipbug",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.BUG,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 25,
            StatsEnum.ATTACK: 20,
            StatsEnum.DEFENSE: 20,
            StatsEnum.SPECIAL_ATTACK: 25,
            StatsEnum.SPECIAL_DEFENSE: 45,
            StatsEnum.SPEED: 45
        }
    },
    "0825": {
        None: {
            PocketMonsterParamEnum.NAME: "Dottler",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.BUG,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.PSYCHIC,
            StatsEnum.HP: 50,
            StatsEnum.ATTACK: 35,
            StatsEnum.DEFENSE: 80,
            StatsEnum.SPECIAL_ATTACK: 50,
            StatsEnum.SPECIAL_DEFENSE: 90,
            StatsEnum.SPEED: 30
        }
    },
    "0826": {
        None: {
            PocketMonsterParamEnum.NAME: "Orbeetle",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.BUG,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.PSYCHIC,
            StatsEnum.HP: 60,
            StatsEnum.ATTACK: 45,
            StatsEnum.DEFENSE: 110,
            StatsEnum.SPECIAL_ATTACK: 80,
            StatsEnum.SPECIAL_DEFENSE: 120,
            StatsEnum.SPEED: 90
        }
    },
    "0827": {
        None: {
            PocketMonsterParamEnum.NAME: "Nickit",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.DARK,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 40,
            StatsEnum.ATTACK: 28,
            StatsEnum.DEFENSE: 28,
            StatsEnum.SPECIAL_ATTACK: 47,
            StatsEnum.SPECIAL_DEFENSE: 52,
            StatsEnum.SPEED: 50
        }
    },
    "0828": {
        None: {
            PocketMonsterParamEnum.NAME: "Thievul",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.DARK,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 70,
            StatsEnum.ATTACK: 58,
            StatsEnum.DEFENSE: 58,
            StatsEnum.SPECIAL_ATTACK: 87,
            StatsEnum.SPECIAL_DEFENSE: 92,
            StatsEnum.SPEED: 90
        }
    },
    "0829": {
        None: {
            PocketMonsterParamEnum.NAME: "Gossifleur",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.GRASS,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 40,
            StatsEnum.ATTACK: 40,
            StatsEnum.DEFENSE: 60,
            StatsEnum.SPECIAL_ATTACK: 40,
            StatsEnum.SPECIAL_DEFENSE: 60,
            StatsEnum.SPEED: 10
        }
    },
    "0830": {
        None: {
            PocketMonsterParamEnum.NAME: "Eldegoss",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.GRASS,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 60,
            StatsEnum.ATTACK: 50,
            StatsEnum.DEFENSE: 90,
            StatsEnum.SPECIAL_ATTACK: 80,
            StatsEnum.SPECIAL_DEFENSE: 120,
            StatsEnum.SPEED: 60
        }
    },
    "0831": {
        None: {
            PocketMonsterParamEnum.NAME: "Wooloo",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.NORMAL,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 42,
            StatsEnum.ATTACK: 40,
            StatsEnum.DEFENSE: 55,
            StatsEnum.SPECIAL_ATTACK: 40,
            StatsEnum.SPECIAL_DEFENSE: 45,
            StatsEnum.SPEED: 48
        }
    },
    "0832": {
        None: {
            PocketMonsterParamEnum.NAME: "Dubwool",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.NORMAL,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 72,
            StatsEnum.ATTACK: 80,
            StatsEnum.DEFENSE: 100,
            StatsEnum.SPECIAL_ATTACK: 60,
            StatsEnum.SPECIAL_DEFENSE: 90,
            StatsEnum.SPEED: 88
        }
    },
    "0833": {
        None: {
            PocketMonsterParamEnum.NAME: "Chewtle",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.WATER,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 50,
            StatsEnum.ATTACK: 64,
            StatsEnum.DEFENSE: 50,
            StatsEnum.SPECIAL_ATTACK: 38,
            StatsEnum.SPECIAL_DEFENSE: 38,
            StatsEnum.SPEED: 44
        }
    },
    "0834": {
        None: {
            PocketMonsterParamEnum.NAME: "Drednaw",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.WATER,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.ROCK,
            StatsEnum.HP: 90,
            StatsEnum.ATTACK: 115,
            StatsEnum.DEFENSE: 90,
            StatsEnum.SPECIAL_ATTACK: 48,
            StatsEnum.SPECIAL_DEFENSE: 68,
            StatsEnum.SPEED: 74
        }
    },
    "0835": {
        None: {
            PocketMonsterParamEnum.NAME: "Yamper",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.ELECTRIC,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 59,
            StatsEnum.ATTACK: 45,
            StatsEnum.DEFENSE: 50,
            StatsEnum.SPECIAL_ATTACK: 40,
            StatsEnum.SPECIAL_DEFENSE: 50,
            StatsEnum.SPEED: 26
        }
    },
    "0836": {
        None: {
            PocketMonsterParamEnum.NAME: "Boltund",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.ELECTRIC,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 69,
            StatsEnum.ATTACK: 90,
            StatsEnum.DEFENSE: 60,
            StatsEnum.SPECIAL_ATTACK: 90,
            StatsEnum.SPECIAL_DEFENSE: 60,
            StatsEnum.SPEED: 121
        }
    },
    "0837": {
        None: {
            PocketMonsterParamEnum.NAME: "Rolycoly",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.ROCK,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 30,
            StatsEnum.ATTACK: 40,
            StatsEnum.DEFENSE: 50,
            StatsEnum.SPECIAL_ATTACK: 40,
            StatsEnum.SPECIAL_DEFENSE: 50,
            StatsEnum.SPEED: 30
        }
    },
    "0838": {
        None: {
            PocketMonsterParamEnum.NAME: "Carkol",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.ROCK,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.FIRE,
            StatsEnum.HP: 80,
            StatsEnum.ATTACK: 60,
            StatsEnum.DEFENSE: 90,
            StatsEnum.SPECIAL_ATTACK: 60,
            StatsEnum.SPECIAL_DEFENSE: 70,
            StatsEnum.SPEED: 50
        }
    },
    "0839": {
        None: {
            PocketMonsterParamEnum.NAME: "Coalossal",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.ROCK,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.FIRE,
            StatsEnum.HP: 110,
            StatsEnum.ATTACK: 80,
            StatsEnum.DEFENSE: 120,
            StatsEnum.SPECIAL_ATTACK: 80,
            StatsEnum.SPECIAL_DEFENSE: 90,
            StatsEnum.SPEED: 30
        }
    },
    "0840": {
        None: {
            PocketMonsterParamEnum.NAME: "Applin",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.GRASS,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.DRAGON,
            StatsEnum.HP: 40,
            StatsEnum.ATTACK: 40,
            StatsEnum.DEFENSE: 80,
            StatsEnum.SPECIAL_ATTACK: 40,
            StatsEnum.SPECIAL_DEFENSE: 40,
            StatsEnum.SPEED: 20
        }
    },
    "0841": {
        None: {
            PocketMonsterParamEnum.NAME: "Flapple",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.GRASS,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.DRAGON,
            StatsEnum.HP: 70,
            StatsEnum.ATTACK: 110,
            StatsEnum.DEFENSE: 80,
            StatsEnum.SPECIAL_ATTACK: 95,
            StatsEnum.SPECIAL_DEFENSE: 60,
            StatsEnum.SPEED: 70
        }
    },
    "0842": {
        None: {
            PocketMonsterParamEnum.NAME: "Appletun",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.GRASS,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.DRAGON,
            StatsEnum.HP: 110,
            StatsEnum.ATTACK: 85,
            StatsEnum.DEFENSE: 80,
            StatsEnum.SPECIAL_ATTACK: 100,
            StatsEnum.SPECIAL_DEFENSE: 80,
            StatsEnum.SPEED: 30
        }
    },
    "0843": {
        None: {
            PocketMonsterParamEnum.NAME: "Silicobra",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.GROUND,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 52,
            StatsEnum.ATTACK: 57,
            StatsEnum.DEFENSE: 75,
            StatsEnum.SPECIAL_ATTACK: 35,
            StatsEnum.SPECIAL_DEFENSE: 50,
            StatsEnum.SPEED: 46
        }
    },
    "0844": {
        None: {
            PocketMonsterParamEnum.NAME: "Sandaconda",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.GROUND,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 72,
            StatsEnum.ATTACK: 107,
            StatsEnum.DEFENSE: 125,
            StatsEnum.SPECIAL_ATTACK: 65,
            StatsEnum.SPECIAL_DEFENSE: 70,
            StatsEnum.SPEED: 71
        }
    },
    "0845": {
        None: {
            PocketMonsterParamEnum.NAME: "Cramorant",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.FLYING,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.WATER,
            StatsEnum.HP: 70,
            StatsEnum.ATTACK: 85,
            StatsEnum.DEFENSE: 55,
            StatsEnum.SPECIAL_ATTACK: 85,
            StatsEnum.SPECIAL_DEFENSE: 95,
            StatsEnum.SPEED: 85
        }
    },
    "0846": {
        None: {
            PocketMonsterParamEnum.NAME: "Arrokuda",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.WATER,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 41,
            StatsEnum.ATTACK: 63,
            StatsEnum.DEFENSE: 40,
            StatsEnum.SPECIAL_ATTACK: 40,
            StatsEnum.SPECIAL_DEFENSE: 30,
            StatsEnum.SPEED: 66
        }
    },
    "0847": {
        None: {
            PocketMonsterParamEnum.NAME: "Barraskewda",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.WATER,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 61,
            StatsEnum.ATTACK: 123,
            StatsEnum.DEFENSE: 60,
            StatsEnum.SPECIAL_ATTACK: 60,
            StatsEnum.SPECIAL_DEFENSE: 50,
            StatsEnum.SPEED: 136
        }
    },
    "0848": {
        None: {
            PocketMonsterParamEnum.NAME: "Toxel",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.ELECTRIC,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.POISON,
            StatsEnum.HP: 40,
            StatsEnum.ATTACK: 38,
            StatsEnum.DEFENSE: 35,
            StatsEnum.SPECIAL_ATTACK: 54,
            StatsEnum.SPECIAL_DEFENSE: 35,
            StatsEnum.SPEED: 40
        }
    },
    "0849": {
        FormEnum.AMPED_FORM: {
            PocketMonsterParamEnum.NAME: "Toxtricity",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.ELECTRIC,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.POISON,
            StatsEnum.HP: 75,
            StatsEnum.ATTACK: 98,
            StatsEnum.DEFENSE: 70,
            StatsEnum.SPECIAL_ATTACK: 114,
            StatsEnum.SPECIAL_DEFENSE: 70,
            StatsEnum.SPEED: 75
        },
        FormEnum.LOW_KEY_FORM: {
            PocketMonsterParamEnum.NAME: "Toxtricity",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.ELECTRIC,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.POISON,
            StatsEnum.HP: 75,
            StatsEnum.ATTACK: 98,
            StatsEnum.DEFENSE: 70,
            StatsEnum.SPECIAL_ATTACK: 114,
            StatsEnum.SPECIAL_DEFENSE: 70,
            StatsEnum.SPEED: 75
        }
    },
    "0850": {
        None: {
            PocketMonsterParamEnum.NAME: "Sizzlipede",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.FIRE,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.BUG,
            StatsEnum.HP: 50,
            StatsEnum.ATTACK: 65,
            StatsEnum.DEFENSE: 45,
            StatsEnum.SPECIAL_ATTACK: 50,
            StatsEnum.SPECIAL_DEFENSE: 50,
            StatsEnum.SPEED: 45
        }
    },
    "0851": {
        None: {
            PocketMonsterParamEnum.NAME: "Centiskorch",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.FIRE,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.BUG,
            StatsEnum.HP: 100,
            StatsEnum.ATTACK: 115,
            StatsEnum.DEFENSE: 65,
            StatsEnum.SPECIAL_ATTACK: 90,
            StatsEnum.SPECIAL_DEFENSE: 90,
            StatsEnum.SPEED: 65
        }
    },
    "0852": {
        None: {
            PocketMonsterParamEnum.NAME: "Clobbopus",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.FIGHTING,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 50,
            StatsEnum.ATTACK: 68,
            StatsEnum.DEFENSE: 60,
            StatsEnum.SPECIAL_ATTACK: 50,
            StatsEnum.SPECIAL_DEFENSE: 50,
            StatsEnum.SPEED: 32
        }
    },
    "0853": {
        None: {
            PocketMonsterParamEnum.NAME: "Grapploct",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.FIGHTING,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 80,
            StatsEnum.ATTACK: 118,
            StatsEnum.DEFENSE: 90,
            StatsEnum.SPECIAL_ATTACK: 70,
            StatsEnum.SPECIAL_DEFENSE: 80,
            StatsEnum.SPEED: 42
        }
    },
    "0854": {
        None: {
            PocketMonsterParamEnum.NAME: "Sinistea",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.GHOST,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 40,
            StatsEnum.ATTACK: 45,
            StatsEnum.DEFENSE: 45,
            StatsEnum.SPECIAL_ATTACK: 74,
            StatsEnum.SPECIAL_DEFENSE: 54,
            StatsEnum.SPEED: 50
        }
    },
    "0855": {
        None: {
            PocketMonsterParamEnum.NAME: "Polteageist",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.GHOST,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 60,
            StatsEnum.ATTACK: 65,
            StatsEnum.DEFENSE: 65,
            StatsEnum.SPECIAL_ATTACK: 134,
            StatsEnum.SPECIAL_DEFENSE: 114,
            StatsEnum.SPEED: 70
        }
    },
    "0856": {
        None: {
            PocketMonsterParamEnum.NAME: "Hatenna",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.PSYCHIC,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 42,
            StatsEnum.ATTACK: 30,
            StatsEnum.DEFENSE: 45,
            StatsEnum.SPECIAL_ATTACK: 56,
            StatsEnum.SPECIAL_DEFENSE: 53,
            StatsEnum.SPEED: 39
        }
    },
    "0857": {
        None: {
            PocketMonsterParamEnum.NAME: "Hattrem",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.PSYCHIC,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 57,
            StatsEnum.ATTACK: 40,
            StatsEnum.DEFENSE: 65,
            StatsEnum.SPECIAL_ATTACK: 86,
            StatsEnum.SPECIAL_DEFENSE: 73,
            StatsEnum.SPEED: 49
        }
    },
    "0858": {
        None: {
            PocketMonsterParamEnum.NAME: "Hatterene",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.PSYCHIC,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.FAIRY,
            StatsEnum.HP: 57,
            StatsEnum.ATTACK: 90,
            StatsEnum.DEFENSE: 95,
            StatsEnum.SPECIAL_ATTACK: 136,
            StatsEnum.SPECIAL_DEFENSE: 103,
            StatsEnum.SPEED: 29
        }
    },
    "0859": {
        None: {
            PocketMonsterParamEnum.NAME: "Impidimp",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.DARK,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.FAIRY,
            StatsEnum.HP: 45,
            StatsEnum.ATTACK: 45,
            StatsEnum.DEFENSE: 30,
            StatsEnum.SPECIAL_ATTACK: 55,
            StatsEnum.SPECIAL_DEFENSE: 40,
            StatsEnum.SPEED: 50
        }
    },
    "0860": {
        None: {
            PocketMonsterParamEnum.NAME: "Morgrem",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.DARK,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.FAIRY,
            StatsEnum.HP: 65,
            StatsEnum.ATTACK: 60,
            StatsEnum.DEFENSE: 45,
            StatsEnum.SPECIAL_ATTACK: 75,
            StatsEnum.SPECIAL_DEFENSE: 55,
            StatsEnum.SPEED: 70
        }
    },
    "0861": {
        None: {
            PocketMonsterParamEnum.NAME: "Grimmsnarl",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.DARK,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.FAIRY,
            StatsEnum.HP: 95,
            StatsEnum.ATTACK: 120,
            StatsEnum.DEFENSE: 65,
            StatsEnum.SPECIAL_ATTACK: 95,
            StatsEnum.SPECIAL_DEFENSE: 75,
            StatsEnum.SPEED: 60
        }
    },
    "0862": {
        None: {
            PocketMonsterParamEnum.NAME: "Obstagoon",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.DARK,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.NORMAL,
            StatsEnum.HP: 93,
            StatsEnum.ATTACK: 90,
            StatsEnum.DEFENSE: 101,
            StatsEnum.SPECIAL_ATTACK: 60,
            StatsEnum.SPECIAL_DEFENSE: 81,
            StatsEnum.SPEED: 95
        }
    },
    "0863": {
        None: {
            PocketMonsterParamEnum.NAME: "Perrserker",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.STEEL,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 70,
            StatsEnum.ATTACK: 110,
            StatsEnum.DEFENSE: 100,
            StatsEnum.SPECIAL_ATTACK: 50,
            StatsEnum.SPECIAL_DEFENSE: 60,
            StatsEnum.SPEED: 50
        }
    },
    "0864": {
        None: {
            PocketMonsterParamEnum.NAME: "Cursola",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.GHOST,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 60,
            StatsEnum.ATTACK: 95,
            StatsEnum.DEFENSE: 50,
            StatsEnum.SPECIAL_ATTACK: 145,
            StatsEnum.SPECIAL_DEFENSE: 130,
            StatsEnum.SPEED: 30
        }
    },
    "0865": {
        None: {
            PocketMonsterParamEnum.NAME: "Sirfetch'd",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.FIGHTING,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 62,
            StatsEnum.ATTACK: 135,
            StatsEnum.DEFENSE: 95,
            StatsEnum.SPECIAL_ATTACK: 68,
            StatsEnum.SPECIAL_DEFENSE: 82,
            StatsEnum.SPEED: 65
        }
    },
    "0866": {
        None: {
            PocketMonsterParamEnum.NAME: "Mr. Rime",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.ICE,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.PSYCHIC,
            StatsEnum.HP: 80,
            StatsEnum.ATTACK: 85,
            StatsEnum.DEFENSE: 75,
            StatsEnum.SPECIAL_ATTACK: 110,
            StatsEnum.SPECIAL_DEFENSE: 100,
            StatsEnum.SPEED: 70
        }
    },
    "0867": {
        None: {
            PocketMonsterParamEnum.NAME: "Runerigus",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.GROUND,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.GHOST,
            StatsEnum.HP: 58,
            StatsEnum.ATTACK: 95,
            StatsEnum.DEFENSE: 145,
            StatsEnum.SPECIAL_ATTACK: 50,
            StatsEnum.SPECIAL_DEFENSE: 105,
            StatsEnum.SPEED: 30
        }
    },
    "0868": {
        None: {
            PocketMonsterParamEnum.NAME: "Milcery",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.FAIRY,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 45,
            StatsEnum.ATTACK: 40,
            StatsEnum.DEFENSE: 40,
            StatsEnum.SPECIAL_ATTACK: 50,
            StatsEnum.SPECIAL_DEFENSE: 61,
            StatsEnum.SPEED: 34
        }
    },
    "0869": {
        None: {
            PocketMonsterParamEnum.NAME: "Alcremie",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.FAIRY,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 65,
            StatsEnum.ATTACK: 60,
            StatsEnum.DEFENSE: 75,
            StatsEnum.SPECIAL_ATTACK: 110,
            StatsEnum.SPECIAL_DEFENSE: 121,
            StatsEnum.SPEED: 64
        }
    },
    "0870": {
        None: {
            PocketMonsterParamEnum.NAME: "Falinks",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.FIGHTING,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 65,
            StatsEnum.ATTACK: 100,
            StatsEnum.DEFENSE: 100,
            StatsEnum.SPECIAL_ATTACK: 70,
            StatsEnum.SPECIAL_DEFENSE: 60,
            StatsEnum.SPEED: 75
        }
    },
    "0871": {
        None: {
            PocketMonsterParamEnum.NAME: "Pincurchin",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.ELECTRIC,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 48,
            StatsEnum.ATTACK: 101,
            StatsEnum.DEFENSE: 95,
            StatsEnum.SPECIAL_ATTACK: 91,
            StatsEnum.SPECIAL_DEFENSE: 85,
            StatsEnum.SPEED: 15
        }
    },
    "0872": {
        None: {
            PocketMonsterParamEnum.NAME: "Snom",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.ICE,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.BUG,
            StatsEnum.HP: 30,
            StatsEnum.ATTACK: 25,
            StatsEnum.DEFENSE: 35,
            StatsEnum.SPECIAL_ATTACK: 45,
            StatsEnum.SPECIAL_DEFENSE: 30,
            StatsEnum.SPEED: 20
        }
    },
    "0873": {
        None: {
            PocketMonsterParamEnum.NAME: "Frosmoth",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.ICE,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.BUG,
            StatsEnum.HP: 70,
            StatsEnum.ATTACK: 65,
            StatsEnum.DEFENSE: 60,
            StatsEnum.SPECIAL_ATTACK: 125,
            StatsEnum.SPECIAL_DEFENSE: 90,
            StatsEnum.SPEED: 65
        }
    },
    "0874": {
        None: {
            PocketMonsterParamEnum.NAME: "Stonjourner",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.ROCK,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 100,
            StatsEnum.ATTACK: 125,
            StatsEnum.DEFENSE: 135,
            StatsEnum.SPECIAL_ATTACK: 20,
            StatsEnum.SPECIAL_DEFENSE: 20,
            StatsEnum.SPEED: 70
        }
    },
    "0875": {
        FormEnum.ICE_FACE: {
            PocketMonsterParamEnum.NAME: "Eiscue",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.ICE,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 75,
            StatsEnum.ATTACK: 80,
            StatsEnum.DEFENSE: 110,
            StatsEnum.SPECIAL_ATTACK: 65,
            StatsEnum.SPECIAL_DEFENSE: 90,
            StatsEnum.SPEED: 50
        },
        FormEnum.NOICE_FACE: {
            PocketMonsterParamEnum.NAME: "Eiscue",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.ICE,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 75,
            StatsEnum.ATTACK: 80,
            StatsEnum.DEFENSE: 70,
            StatsEnum.SPECIAL_ATTACK: 65,
            StatsEnum.SPECIAL_DEFENSE: 50,
            StatsEnum.SPEED: 130
        }
    },
    "0876": {
        FormEnum.MALE: {
            PocketMonsterParamEnum.NAME: "Indeedee",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.PSYCHIC,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.NORMAL,
            StatsEnum.HP: 60,
            StatsEnum.ATTACK: 65,
            StatsEnum.DEFENSE: 55,
            StatsEnum.SPECIAL_ATTACK: 105,
            StatsEnum.SPECIAL_DEFENSE: 95,
            StatsEnum.SPEED: 95
        },
        FormEnum.FEMALE: {
            PocketMonsterParamEnum.NAME: "Indeedee",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.PSYCHIC,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.NORMAL,
            StatsEnum.HP: 70,
            StatsEnum.ATTACK: 55,
            StatsEnum.DEFENSE: 65,
            StatsEnum.SPECIAL_ATTACK: 95,
            StatsEnum.SPECIAL_DEFENSE: 105,
            StatsEnum.SPEED: 85
        }
    },
    "0877": {
        FormEnum.FULL_BELLY_MODE: {
            PocketMonsterParamEnum.NAME: "Morpeko",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.ELECTRIC,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.DARK,
            StatsEnum.HP: 58,
            StatsEnum.ATTACK: 95,
            StatsEnum.DEFENSE: 58,
            StatsEnum.SPECIAL_ATTACK: 70,
            StatsEnum.SPECIAL_DEFENSE: 58,
            StatsEnum.SPEED: 97
        },
        FormEnum.HANGRY_MODE: {
            PocketMonsterParamEnum.NAME: "Morpeko",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.ELECTRIC,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.DARK,
            StatsEnum.HP: 58,
            StatsEnum.ATTACK: 95,
            StatsEnum.DEFENSE: 58,
            StatsEnum.SPECIAL_ATTACK: 70,
            StatsEnum.SPECIAL_DEFENSE: 58,
            StatsEnum.SPEED: 97
        }
    },
    "0878": {
        None: {
            PocketMonsterParamEnum.NAME: "Cufant",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.STEEL,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 72,
            StatsEnum.ATTACK: 80,
            StatsEnum.DEFENSE: 49,
            StatsEnum.SPECIAL_ATTACK: 40,
            StatsEnum.SPECIAL_DEFENSE: 49,
            StatsEnum.SPEED: 40
        }
    },
    "0879": {
        None: {
            PocketMonsterParamEnum.NAME: "Copperajah",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.STEEL,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 122,
            StatsEnum.ATTACK: 130,
            StatsEnum.DEFENSE: 69,
            StatsEnum.SPECIAL_ATTACK: 80,
            StatsEnum.SPECIAL_DEFENSE: 69,
            StatsEnum.SPEED: 30
        }
    },
    "0880": {
        None: {
            PocketMonsterParamEnum.NAME: "Dracozolt",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.ELECTRIC,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.DRAGON,
            StatsEnum.HP: 90,
            StatsEnum.ATTACK: 100,
            StatsEnum.DEFENSE: 90,
            StatsEnum.SPECIAL_ATTACK: 80,
            StatsEnum.SPECIAL_DEFENSE: 70,
            StatsEnum.SPEED: 75
        }
    },
    "0881": {
        None: {
            PocketMonsterParamEnum.NAME: "Arctozolt",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.ELECTRIC,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.ICE,
            StatsEnum.HP: 90,
            StatsEnum.ATTACK: 100,
            StatsEnum.DEFENSE: 90,
            StatsEnum.SPECIAL_ATTACK: 90,
            StatsEnum.SPECIAL_DEFENSE: 80,
            StatsEnum.SPEED: 55
        }
    },
    "0882": {
        None: {
            PocketMonsterParamEnum.NAME: "Dracovish",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.WATER,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.DRAGON,
            StatsEnum.HP: 90,
            StatsEnum.ATTACK: 90,
            StatsEnum.DEFENSE: 100,
            StatsEnum.SPECIAL_ATTACK: 70,
            StatsEnum.SPECIAL_DEFENSE: 80,
            StatsEnum.SPEED: 75
        }
    },
    "0883": {
        None: {
            PocketMonsterParamEnum.NAME: "Arctovish",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.WATER,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.ICE,
            StatsEnum.HP: 90,
            StatsEnum.ATTACK: 90,
            StatsEnum.DEFENSE: 100,
            StatsEnum.SPECIAL_ATTACK: 80,
            StatsEnum.SPECIAL_DEFENSE: 90,
            StatsEnum.SPEED: 55
        }
    },
    "0884": {
        None: {
            PocketMonsterParamEnum.NAME: "Duraludon",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.STEEL,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.DRAGON,
            StatsEnum.HP: 70,
            StatsEnum.ATTACK: 95,
            StatsEnum.DEFENSE: 115,
            StatsEnum.SPECIAL_ATTACK: 120,
            StatsEnum.SPECIAL_DEFENSE: 50,
            StatsEnum.SPEED: 85
        }
    },
    "0885": {
        None: {
            PocketMonsterParamEnum.NAME: "Dreepy",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.DRAGON,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.GHOST,
            StatsEnum.HP: 28,
            StatsEnum.ATTACK: 60,
            StatsEnum.DEFENSE: 30,
            StatsEnum.SPECIAL_ATTACK: 40,
            StatsEnum.SPECIAL_DEFENSE: 30,
            StatsEnum.SPEED: 82
        }
    },
    "0886": {
        None: {
            PocketMonsterParamEnum.NAME: "Drakloak",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.DRAGON,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.GHOST,
            StatsEnum.HP: 68,
            StatsEnum.ATTACK: 80,
            StatsEnum.DEFENSE: 50,
            StatsEnum.SPECIAL_ATTACK: 60,
            StatsEnum.SPECIAL_DEFENSE: 50,
            StatsEnum.SPEED: 102
        }
    },
    "0887": {
        None: {
            PocketMonsterParamEnum.NAME: "Dragapult",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.DRAGON,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.GHOST,
            StatsEnum.HP: 88,
            StatsEnum.ATTACK: 120,
            StatsEnum.DEFENSE: 75,
            StatsEnum.SPECIAL_ATTACK: 100,
            StatsEnum.SPECIAL_DEFENSE: 75,
            StatsEnum.SPEED: 142
        }
    },
    "0888": {
        FormEnum.HERO_OF_MANY_BATTLES: {
            PocketMonsterParamEnum.NAME: "Zacian",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.FAIRY,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 92,
            StatsEnum.ATTACK: 120,
            StatsEnum.DEFENSE: 115,
            StatsEnum.SPECIAL_ATTACK: 80,
            StatsEnum.SPECIAL_DEFENSE: 115,
            StatsEnum.SPEED: 138
        },
        FormEnum.CROWNED_SWORD: {
            PocketMonsterParamEnum.NAME: "Zacian",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.FAIRY,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.STEEL,
            StatsEnum.HP: 92,
            StatsEnum.ATTACK: 150,
            StatsEnum.DEFENSE: 115,
            StatsEnum.SPECIAL_ATTACK: 80,
            StatsEnum.SPECIAL_DEFENSE: 115,
            StatsEnum.SPEED: 148
        }
    },
    "0889": {
        FormEnum.HERO_OF_MANY_BATTLES: {
            PocketMonsterParamEnum.NAME: "Zamazenta",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.FIGHTING,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 92,
            StatsEnum.ATTACK: 120,
            StatsEnum.DEFENSE: 115,
            StatsEnum.SPECIAL_ATTACK: 80,
            StatsEnum.SPECIAL_DEFENSE: 115,
            StatsEnum.SPEED: 138
        },
        FormEnum.CROWNED_SHIELD: {
            PocketMonsterParamEnum.NAME: "Zamazenta",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.FIGHTING,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.STEEL,
            StatsEnum.HP: 92,
            StatsEnum.ATTACK: 120,
            StatsEnum.DEFENSE: 140,
            StatsEnum.SPECIAL_ATTACK: 80,
            StatsEnum.SPECIAL_DEFENSE: 140,
            StatsEnum.SPEED: 128
        }
    },
    "0890": {
        None: {
            PocketMonsterParamEnum.NAME: "Eternatus",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.POISON,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.DRAGON,
            StatsEnum.HP: 140,
            StatsEnum.ATTACK: 85,
            StatsEnum.DEFENSE: 95,
            StatsEnum.SPECIAL_ATTACK: 145,
            StatsEnum.SPECIAL_DEFENSE: 95,
            StatsEnum.SPEED: 130
        },
        FormEnum.ETERNAMAX: {
            PocketMonsterParamEnum.NAME: "Eternatus",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.POISON,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.DRAGON,
            StatsEnum.HP: 255,
            StatsEnum.ATTACK: 115,
            StatsEnum.DEFENSE: 250,
            StatsEnum.SPECIAL_ATTACK: 125,
            StatsEnum.SPECIAL_DEFENSE: 250,
            StatsEnum.SPEED: 130
        }
    },
    "0891": {
        None: {
            PocketMonsterParamEnum.NAME: "Kubfu",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.FIGHTING,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 60,
            StatsEnum.ATTACK: 90,
            StatsEnum.DEFENSE: 60,
            StatsEnum.SPECIAL_ATTACK: 53,
            StatsEnum.SPECIAL_DEFENSE: 50,
            StatsEnum.SPEED: 72
        }
    },
    "0892": {
        FormEnum.SINGLE_STRIKE_STYLE: {
            PocketMonsterParamEnum.NAME: "Urshifu",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.FIGHTING,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.DARK,
            StatsEnum.HP: 100,
            StatsEnum.ATTACK: 130,
            StatsEnum.DEFENSE: 100,
            StatsEnum.SPECIAL_ATTACK: 63,
            StatsEnum.SPECIAL_DEFENSE: 60,
            StatsEnum.SPEED: 97
        },
        FormEnum.RAPID_STRIKE_STYLE: {
            PocketMonsterParamEnum.NAME: "Urshifu",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.FIGHTING,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.WATER,
            StatsEnum.HP: 100,
            StatsEnum.ATTACK: 130,
            StatsEnum.DEFENSE: 100,
            StatsEnum.SPECIAL_ATTACK: 63,
            StatsEnum.SPECIAL_DEFENSE: 60,
            StatsEnum.SPEED: 97
        }
    },
    "0893": {
        None: {
            PocketMonsterParamEnum.NAME: "Zarude",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.DARK,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.GRASS,
            StatsEnum.HP: 105,
            StatsEnum.ATTACK: 120,
            StatsEnum.DEFENSE: 105,
            StatsEnum.SPECIAL_ATTACK: 70,
            StatsEnum.SPECIAL_DEFENSE: 95,
            StatsEnum.SPEED: 105
        }
    },
    "0894": {
        None: {
            PocketMonsterParamEnum.NAME: "Regieleki",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.ELECTRIC,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 80,
            StatsEnum.ATTACK: 100,
            StatsEnum.DEFENSE: 50,
            StatsEnum.SPECIAL_ATTACK: 100,
            StatsEnum.SPECIAL_DEFENSE: 50,
            StatsEnum.SPEED: 200
        }
    },
    "0895": {
        None: {
            PocketMonsterParamEnum.NAME: "Regidrago",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.DRAGON,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 200,
            StatsEnum.ATTACK: 100,
            StatsEnum.DEFENSE: 50,
            StatsEnum.SPECIAL_ATTACK: 100,
            StatsEnum.SPECIAL_DEFENSE: 50,
            StatsEnum.SPEED: 80
        }
    },
    "0896": {
        None: {
            PocketMonsterParamEnum.NAME: "Glastrier",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.ICE,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 100,
            StatsEnum.ATTACK: 145,
            StatsEnum.DEFENSE: 130,
            StatsEnum.SPECIAL_ATTACK: 65,
            StatsEnum.SPECIAL_DEFENSE: 110,
            StatsEnum.SPEED: 30
        }
    },
    "0897": {
        None: {
            PocketMonsterParamEnum.NAME: "Spectrier",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.GHOST,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 100,
            StatsEnum.ATTACK: 65,
            StatsEnum.DEFENSE: 60,
            StatsEnum.SPECIAL_ATTACK: 145,
            StatsEnum.SPECIAL_DEFENSE: 80,
            StatsEnum.SPEED: 130
        }
    },
    "0898": {
        None: {
            PocketMonsterParamEnum.NAME: "Calyrex",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.PSYCHIC,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.GRASS,
            StatsEnum.HP: 100,
            StatsEnum.ATTACK: 80,
            StatsEnum.DEFENSE: 80,
            StatsEnum.SPECIAL_ATTACK: 80,
            StatsEnum.SPECIAL_DEFENSE: 80,
            StatsEnum.SPEED: 80
        },
        FormEnum.ICE_RIDER: {
            PocketMonsterParamEnum.NAME: "Calyrex",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.PSYCHIC,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.ICE,
            StatsEnum.HP: 100,
            StatsEnum.ATTACK: 165,
            StatsEnum.DEFENSE: 150,
            StatsEnum.SPECIAL_ATTACK: 85,
            StatsEnum.SPECIAL_DEFENSE: 130,
            StatsEnum.SPEED: 50
        },
        FormEnum.SHADOW_RIDER: {
            PocketMonsterParamEnum.NAME: "Calyrex",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.PSYCHIC,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.GHOST,
            StatsEnum.HP: 100,
            StatsEnum.ATTACK: 85,
            StatsEnum.DEFENSE: 80,
            StatsEnum.SPECIAL_ATTACK: 165,
            StatsEnum.SPECIAL_DEFENSE: 100,
            StatsEnum.SPEED: 150
        }
    },
    "0899": {
        None: {
            PocketMonsterParamEnum.NAME: "Wyrdeer",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.NORMAL,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.PSYCHIC,
            StatsEnum.HP: 103,
            StatsEnum.ATTACK: 105,
            StatsEnum.DEFENSE: 72,
            StatsEnum.SPECIAL_ATTACK: 105,
            StatsEnum.SPECIAL_DEFENSE: 75,
            StatsEnum.SPEED: 65
        }
    },
    "0900": {
        None: {
            PocketMonsterParamEnum.NAME: "Kleavor",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.BUG,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.ROCK,
            StatsEnum.HP: 70,
            StatsEnum.ATTACK: 135,
            StatsEnum.DEFENSE: 95,
            StatsEnum.SPECIAL_ATTACK: 45,
            StatsEnum.SPECIAL_DEFENSE: 70,
            StatsEnum.SPEED: 85
        }
    },
    "0901": {
        None: {
            PocketMonsterParamEnum.NAME: "Ursaluna",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.GROUND,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.NORMAL,
            StatsEnum.HP: 130,
            StatsEnum.ATTACK: 140,
            StatsEnum.DEFENSE: 105,
            StatsEnum.SPECIAL_ATTACK: 45,
            StatsEnum.SPECIAL_DEFENSE: 80,
            StatsEnum.SPEED: 50
        },
        FormEnum.BLOODMOON: {
            PocketMonsterParamEnum.NAME: "Ursaluna",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.GROUND,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.NORMAL,
            StatsEnum.HP: 113,
            StatsEnum.ATTACK: 70,
            StatsEnum.DEFENSE: 120,
            StatsEnum.SPECIAL_ATTACK: 135,
            StatsEnum.SPECIAL_DEFENSE: 65,
            StatsEnum.SPEED: 52
        }
    },
    "0902": {
        FormEnum.MALE: {
            PocketMonsterParamEnum.NAME: "Basculegion",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.WATER,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.GHOST,
            StatsEnum.HP: 120,
            StatsEnum.ATTACK: 112,
            StatsEnum.DEFENSE: 65,
            StatsEnum.SPECIAL_ATTACK: 80,
            StatsEnum.SPECIAL_DEFENSE: 75,
            StatsEnum.SPEED: 78
        },
        FormEnum.FEMALE: {
            PocketMonsterParamEnum.NAME: "Basculegion",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.WATER,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.GHOST,
            StatsEnum.HP: 120,
            StatsEnum.ATTACK: 92,
            StatsEnum.DEFENSE: 65,
            StatsEnum.SPECIAL_ATTACK: 100,
            StatsEnum.SPECIAL_DEFENSE: 75,
            StatsEnum.SPEED: 78
        }
    },
    "0903": {
        None: {
            PocketMonsterParamEnum.NAME: "Sneasler",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.FIGHTING,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.POISON,
            StatsEnum.HP: 80,
            StatsEnum.ATTACK: 130,
            StatsEnum.DEFENSE: 60,
            StatsEnum.SPECIAL_ATTACK: 40,
            StatsEnum.SPECIAL_DEFENSE: 80,
            StatsEnum.SPEED: 120
        }
    },
    "0904": {
        None: {
            PocketMonsterParamEnum.NAME: "Overqwil",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.DARK,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.POISON,
            StatsEnum.HP: 85,
            StatsEnum.ATTACK: 115,
            StatsEnum.DEFENSE: 95,
            StatsEnum.SPECIAL_ATTACK: 65,
            StatsEnum.SPECIAL_DEFENSE: 65,
            StatsEnum.SPEED: 85
        }
    },
    "0905": {
        FormEnum.INCARNATE_FORME: {
            PocketMonsterParamEnum.NAME: "Enamorus",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.FAIRY,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.FLYING,
            StatsEnum.HP: 74,
            StatsEnum.ATTACK: 115,
            StatsEnum.DEFENSE: 70,
            StatsEnum.SPECIAL_ATTACK: 135,
            StatsEnum.SPECIAL_DEFENSE: 80,
            StatsEnum.SPEED: 106
        },
        FormEnum.THERIAN_FORME: {
            PocketMonsterParamEnum.NAME: "Enamorus",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.FAIRY,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.FLYING,
            StatsEnum.HP: 74,
            StatsEnum.ATTACK: 115,
            StatsEnum.DEFENSE: 110,
            StatsEnum.SPECIAL_ATTACK: 135,
            StatsEnum.SPECIAL_DEFENSE: 100,
            StatsEnum.SPEED: 46
        }
    },
    "0906": {
        None: {
            PocketMonsterParamEnum.NAME: "Sprigatito",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.GRASS,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 40,
            StatsEnum.ATTACK: 61,
            StatsEnum.DEFENSE: 54,
            StatsEnum.SPECIAL_ATTACK: 45,
            StatsEnum.SPECIAL_DEFENSE: 45,
            StatsEnum.SPEED: 65
        }
    },
    "0907": {
        None: {
            PocketMonsterParamEnum.NAME: "Floragato",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.GRASS,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 61,
            StatsEnum.ATTACK: 80,
            StatsEnum.DEFENSE: 63,
            StatsEnum.SPECIAL_ATTACK: 60,
            StatsEnum.SPECIAL_DEFENSE: 63,
            StatsEnum.SPEED: 83
        }
    },
    "0908": {
        None: {
            PocketMonsterParamEnum.NAME: "Meowscarada",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.GRASS,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.DARK,
            StatsEnum.HP: 76,
            StatsEnum.ATTACK: 110,
            StatsEnum.DEFENSE: 70,
            StatsEnum.SPECIAL_ATTACK: 81,
            StatsEnum.SPECIAL_DEFENSE: 70,
            StatsEnum.SPEED: 123
        }
    },
    "0909": {
        None: {
            PocketMonsterParamEnum.NAME: "Fuecoco",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.FIRE,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 67,
            StatsEnum.ATTACK: 45,
            StatsEnum.DEFENSE: 59,
            StatsEnum.SPECIAL_ATTACK: 63,
            StatsEnum.SPECIAL_DEFENSE: 40,
            StatsEnum.SPEED: 36
        }
    },
    "0910": {
        None: {
            PocketMonsterParamEnum.NAME: "Crocalor",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.FIRE,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 81,
            StatsEnum.ATTACK: 55,
            StatsEnum.DEFENSE: 78,
            StatsEnum.SPECIAL_ATTACK: 90,
            StatsEnum.SPECIAL_DEFENSE: 58,
            StatsEnum.SPEED: 49
        }
    },
    "0911": {
        None: {
            PocketMonsterParamEnum.NAME: "Skeledirge",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.FIRE,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.GHOST,
            StatsEnum.HP: 104,
            StatsEnum.ATTACK: 75,
            StatsEnum.DEFENSE: 100,
            StatsEnum.SPECIAL_ATTACK: 110,
            StatsEnum.SPECIAL_DEFENSE: 75,
            StatsEnum.SPEED: 66
        }
    },
    "0912": {
        None: {
            PocketMonsterParamEnum.NAME: "Quaxly",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.WATER,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 55,
            StatsEnum.ATTACK: 65,
            StatsEnum.DEFENSE: 45,
            StatsEnum.SPECIAL_ATTACK: 50,
            StatsEnum.SPECIAL_DEFENSE: 45,
            StatsEnum.SPEED: 50
        }
    },
    "0913": {
        None: {
            PocketMonsterParamEnum.NAME: "Quaxwell",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.WATER,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 70,
            StatsEnum.ATTACK: 85,
            StatsEnum.DEFENSE: 65,
            StatsEnum.SPECIAL_ATTACK: 65,
            StatsEnum.SPECIAL_DEFENSE: 60,
            StatsEnum.SPEED: 65
        }
    },
    "0914": {
        None: {
            PocketMonsterParamEnum.NAME: "Quaquaval",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.WATER,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.FIGHTING,
            StatsEnum.HP: 85,
            StatsEnum.ATTACK: 120,
            StatsEnum.DEFENSE: 80,
            StatsEnum.SPECIAL_ATTACK: 85,
            StatsEnum.SPECIAL_DEFENSE: 75,
            StatsEnum.SPEED: 85
        }
    },
    "0915": {
        None: {
            PocketMonsterParamEnum.NAME: "Lechonk",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.NORMAL,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 54,
            StatsEnum.ATTACK: 45,
            StatsEnum.DEFENSE: 40,
            StatsEnum.SPECIAL_ATTACK: 35,
            StatsEnum.SPECIAL_DEFENSE: 45,
            StatsEnum.SPEED: 35
        }
    },
    "0916": {
        "Male": {
            PocketMonsterParamEnum.NAME: "Oinkologne",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.NORMAL,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 110,
            StatsEnum.ATTACK: 100,
            StatsEnum.DEFENSE: 75,
            StatsEnum.SPECIAL_ATTACK: 59,
            StatsEnum.SPECIAL_DEFENSE: 80,
            StatsEnum.SPEED: 65
        },
        "Female": {
            PocketMonsterParamEnum.NAME: "Oinkologne",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.NORMAL,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 115,
            StatsEnum.ATTACK: 90,
            StatsEnum.DEFENSE: 70,
            StatsEnum.SPECIAL_ATTACK: 59,
            StatsEnum.SPECIAL_DEFENSE: 90,
            StatsEnum.SPEED: 65
        }
    },
    "0917": {
        None: {
            PocketMonsterParamEnum.NAME: "Tarountula",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.BUG,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 35,
            StatsEnum.ATTACK: 41,
            StatsEnum.DEFENSE: 45,
            StatsEnum.SPECIAL_ATTACK: 29,
            StatsEnum.SPECIAL_DEFENSE: 40,
            StatsEnum.SPEED: 20
        }
    },
    "0918": {
        None: {
            PocketMonsterParamEnum.NAME: "Spidops",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.BUG,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 60,
            StatsEnum.ATTACK: 79,
            StatsEnum.DEFENSE: 92,
            StatsEnum.SPECIAL_ATTACK: 52,
            StatsEnum.SPECIAL_DEFENSE: 86,
            StatsEnum.SPEED: 35
        }
    },
    "0919": {
        None: {
            PocketMonsterParamEnum.NAME: "Nymble",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.BUG,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 33,
            StatsEnum.ATTACK: 46,
            StatsEnum.DEFENSE: 40,
            StatsEnum.SPECIAL_ATTACK: 21,
            StatsEnum.SPECIAL_DEFENSE: 25,
            StatsEnum.SPEED: 45
        }
    },
    "0920": {
        None: {
            PocketMonsterParamEnum.NAME: "Lokix",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.BUG,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.DARK,
            StatsEnum.HP: 71,
            StatsEnum.ATTACK: 102,
            StatsEnum.DEFENSE: 78,
            StatsEnum.SPECIAL_ATTACK: 52,
            StatsEnum.SPECIAL_DEFENSE: 55,
            StatsEnum.SPEED: 92
        }
    },
    "0921": {
        None: {
            PocketMonsterParamEnum.NAME: "Pawmi",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.ELECTRIC,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 45,
            StatsEnum.ATTACK: 50,
            StatsEnum.DEFENSE: 20,
            StatsEnum.SPECIAL_ATTACK: 40,
            StatsEnum.SPECIAL_DEFENSE: 25,
            StatsEnum.SPEED: 60
        }
    },
    "0922": {
        None: {
            PocketMonsterParamEnum.NAME: "Pawmo",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.ELECTRIC,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.FIGHTING,
            StatsEnum.HP: 60,
            StatsEnum.ATTACK: 75,
            StatsEnum.DEFENSE: 40,
            StatsEnum.SPECIAL_ATTACK: 50,
            StatsEnum.SPECIAL_DEFENSE: 40,
            StatsEnum.SPEED: 85
        }
    },
    "0923": {
        None: {
            PocketMonsterParamEnum.NAME: "Pawmot",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.ELECTRIC,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.FIGHTING,
            StatsEnum.HP: 70,
            StatsEnum.ATTACK: 115,
            StatsEnum.DEFENSE: 70,
            StatsEnum.SPECIAL_ATTACK: 70,
            StatsEnum.SPECIAL_DEFENSE: 60,
            StatsEnum.SPEED: 105
        }
    },
    "0924": {
        None: {
            PocketMonsterParamEnum.NAME: "Tandemaus",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.NORMAL,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 50,
            StatsEnum.ATTACK: 50,
            StatsEnum.DEFENSE: 45,
            StatsEnum.SPECIAL_ATTACK: 40,
            StatsEnum.SPECIAL_DEFENSE: 45,
            StatsEnum.SPEED: 75
        }
    },
    "0925": {
        "Family of Four": {
            PocketMonsterParamEnum.NAME: "Maushold",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.NORMAL,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 74,
            StatsEnum.ATTACK: 75,
            StatsEnum.DEFENSE: 70,
            StatsEnum.SPECIAL_ATTACK: 65,
            StatsEnum.SPECIAL_DEFENSE: 75,
            StatsEnum.SPEED: 111
        },
        "Family of Three": {
            PocketMonsterParamEnum.NAME: "Maushold",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.NORMAL,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 74,
            StatsEnum.ATTACK: 75,
            StatsEnum.DEFENSE: 70,
            StatsEnum.SPECIAL_ATTACK: 65,
            StatsEnum.SPECIAL_DEFENSE: 75,
            StatsEnum.SPEED: 111
        }
    },
    "0926": {
        None: {
            PocketMonsterParamEnum.NAME: "Fidough",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.FAIRY,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 37,
            StatsEnum.ATTACK: 55,
            StatsEnum.DEFENSE: 70,
            StatsEnum.SPECIAL_ATTACK: 30,
            StatsEnum.SPECIAL_DEFENSE: 55,
            StatsEnum.SPEED: 65
        }
    },
    "0927": {
        None: {
            PocketMonsterParamEnum.NAME: "Dachsbun",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.FAIRY,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 57,
            StatsEnum.ATTACK: 80,
            StatsEnum.DEFENSE: 115,
            StatsEnum.SPECIAL_ATTACK: 50,
            StatsEnum.SPECIAL_DEFENSE: 80,
            StatsEnum.SPEED: 95
        }
    },
    "0928": {
        None: {
            PocketMonsterParamEnum.NAME: "Smoliv",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.GRASS,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.NORMAL,
            StatsEnum.HP: 41,
            StatsEnum.ATTACK: 35,
            StatsEnum.DEFENSE: 45,
            StatsEnum.SPECIAL_ATTACK: 58,
            StatsEnum.SPECIAL_DEFENSE: 51,
            StatsEnum.SPEED: 30
        }
    },
    "0929": {
        None: {
            PocketMonsterParamEnum.NAME: "Dolliv",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.GRASS,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.NORMAL,
            StatsEnum.HP: 52,
            StatsEnum.ATTACK: 53,
            StatsEnum.DEFENSE: 60,
            StatsEnum.SPECIAL_ATTACK: 78,
            StatsEnum.SPECIAL_DEFENSE: 78,
            StatsEnum.SPEED: 33
        }
    },
    "0930": {
        None: {
            PocketMonsterParamEnum.NAME: "Arboliva",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.GRASS,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.NORMAL,
            StatsEnum.HP: 78,
            StatsEnum.ATTACK: 69,
            StatsEnum.DEFENSE: 90,
            StatsEnum.SPECIAL_ATTACK: 125,
            StatsEnum.SPECIAL_DEFENSE: 109,
            StatsEnum.SPEED: 39
        }
    },
    "0931": {
        "Green Plumage": {
            PocketMonsterParamEnum.NAME: "Squawkabilly",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.NORMAL,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.FLYING,
            StatsEnum.HP: 82,
            StatsEnum.ATTACK: 96,
            StatsEnum.DEFENSE: 51,
            StatsEnum.SPECIAL_ATTACK: 45,
            StatsEnum.SPECIAL_DEFENSE: 51,
            StatsEnum.SPEED: 92
        },
        "Blue Plumage": {
            PocketMonsterParamEnum.NAME: "Squawkabilly",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.NORMAL,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.FLYING,
            StatsEnum.HP: 82,
            StatsEnum.ATTACK: 96,
            StatsEnum.DEFENSE: 51,
            StatsEnum.SPECIAL_ATTACK: 45,
            StatsEnum.SPECIAL_DEFENSE: 51,
            StatsEnum.SPEED: 92
        },
        "Yellow Plumage": {
            PocketMonsterParamEnum.NAME: "Squawkabilly",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.NORMAL,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.FLYING,
            StatsEnum.HP: 82,
            StatsEnum.ATTACK: 96,
            StatsEnum.DEFENSE: 51,
            StatsEnum.SPECIAL_ATTACK: 45,
            StatsEnum.SPECIAL_DEFENSE: 51,
            StatsEnum.SPEED: 92
        },
        "White Plumage": {
            PocketMonsterParamEnum.NAME: "Squawkabilly",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.NORMAL,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.FLYING,
            StatsEnum.HP: 82,
            StatsEnum.ATTACK: 96,
            StatsEnum.DEFENSE: 51,
            StatsEnum.SPECIAL_ATTACK: 45,
            StatsEnum.SPECIAL_DEFENSE: 51,
            StatsEnum.SPEED: 92
        }
    },
    "0932": {
        None: {
            PocketMonsterParamEnum.NAME: "Nacli",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.ROCK,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 55,
            StatsEnum.ATTACK: 55,
            StatsEnum.DEFENSE: 75,
            StatsEnum.SPECIAL_ATTACK: 35,
            StatsEnum.SPECIAL_DEFENSE: 35,
            StatsEnum.SPEED: 25
        }
    },
    "0933": {
        None: {
            PocketMonsterParamEnum.NAME: "Naclstack",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.ROCK,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 60,
            StatsEnum.ATTACK: 60,
            StatsEnum.DEFENSE: 100,
            StatsEnum.SPECIAL_ATTACK: 35,
            StatsEnum.SPECIAL_DEFENSE: 65,
            StatsEnum.SPEED: 35
        }
    },
    "0934": {
        None: {
            PocketMonsterParamEnum.NAME: "Garganacl",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.ROCK,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 100,
            StatsEnum.ATTACK: 100,
            StatsEnum.DEFENSE: 130,
            StatsEnum.SPECIAL_ATTACK: 45,
            StatsEnum.SPECIAL_DEFENSE: 90,
            StatsEnum.SPEED: 35
        }
    },
    "0935": {
        None: {
            PocketMonsterParamEnum.NAME: "Charcadet",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.FIRE,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 40,
            StatsEnum.ATTACK: 50,
            StatsEnum.DEFENSE: 40,
            StatsEnum.SPECIAL_ATTACK: 50,
            StatsEnum.SPECIAL_DEFENSE: 40,
            StatsEnum.SPEED: 35
        }
    },
    "0936": {
        None: {
            PocketMonsterParamEnum.NAME: "Armarouge",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.FIRE,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.PSYCHIC,
            StatsEnum.HP: 85,
            StatsEnum.ATTACK: 60,
            StatsEnum.DEFENSE: 100,
            StatsEnum.SPECIAL_ATTACK: 125,
            StatsEnum.SPECIAL_DEFENSE: 80,
            StatsEnum.SPEED: 75
        }
    },
    "0937": {
        None: {
            PocketMonsterParamEnum.NAME: "Ceruledge",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.FIRE,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.GHOST,
            StatsEnum.HP: 75,
            StatsEnum.ATTACK: 125,
            StatsEnum.DEFENSE: 80,
            StatsEnum.SPECIAL_ATTACK: 60,
            StatsEnum.SPECIAL_DEFENSE: 100,
            StatsEnum.SPEED: 85
        }
    },
    "0938": {
        None: {
            PocketMonsterParamEnum.NAME: "Tadbulb",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.ELECTRIC,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 61,
            StatsEnum.ATTACK: 31,
            StatsEnum.DEFENSE: 41,
            StatsEnum.SPECIAL_ATTACK: 59,
            StatsEnum.SPECIAL_DEFENSE: 35,
            StatsEnum.SPEED: 45
        }
    },
    "0939": {
        None: {
            PocketMonsterParamEnum.NAME: "Bellibolt",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.ELECTRIC,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 109,
            StatsEnum.ATTACK: 64,
            StatsEnum.DEFENSE: 91,
            StatsEnum.SPECIAL_ATTACK: 103,
            StatsEnum.SPECIAL_DEFENSE: 83,
            StatsEnum.SPEED: 45
        }
    },
    "0940": {
        None: {
            PocketMonsterParamEnum.NAME: "Wattrel",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.ELECTRIC,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.FLYING,
            StatsEnum.HP: 40,
            StatsEnum.ATTACK: 40,
            StatsEnum.DEFENSE: 35,
            StatsEnum.SPECIAL_ATTACK: 55,
            StatsEnum.SPECIAL_DEFENSE: 40,
            StatsEnum.SPEED: 70
        }
    },
    "0941": {
        None: {
            PocketMonsterParamEnum.NAME: "Kilowattrel",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.ELECTRIC,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.FLYING,
            StatsEnum.HP: 70,
            StatsEnum.ATTACK: 70,
            StatsEnum.DEFENSE: 60,
            StatsEnum.SPECIAL_ATTACK: 105,
            StatsEnum.SPECIAL_DEFENSE: 60,
            StatsEnum.SPEED: 125
        }
    },
    "0942": {
        None: {
            PocketMonsterParamEnum.NAME: "Maschiff",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.DARK,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 60,
            StatsEnum.ATTACK: 78,
            StatsEnum.DEFENSE: 60,
            StatsEnum.SPECIAL_ATTACK: 40,
            StatsEnum.SPECIAL_DEFENSE: 51,
            StatsEnum.SPEED: 51
        }
    },
    "0943": {
        None: {
            PocketMonsterParamEnum.NAME: "Mabosstiff",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.DARK,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 80,
            StatsEnum.ATTACK: 120,
            StatsEnum.DEFENSE: 90,
            StatsEnum.SPECIAL_ATTACK: 60,
            StatsEnum.SPECIAL_DEFENSE: 70,
            StatsEnum.SPEED: 85
        }
    },
    "0944": {
        None: {
            PocketMonsterParamEnum.NAME: "Shroodle",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.POISON,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.NORMAL,
            StatsEnum.HP: 40,
            StatsEnum.ATTACK: 65,
            StatsEnum.DEFENSE: 35,
            StatsEnum.SPECIAL_ATTACK: 40,
            StatsEnum.SPECIAL_DEFENSE: 35,
            StatsEnum.SPEED: 75
        }
    },
    "0945": {
        None: {
            PocketMonsterParamEnum.NAME: "Grafaiai",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.POISON,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.NORMAL,
            StatsEnum.HP: 63,
            StatsEnum.ATTACK: 95,
            StatsEnum.DEFENSE: 65,
            StatsEnum.SPECIAL_ATTACK: 80,
            StatsEnum.SPECIAL_DEFENSE: 72,
            StatsEnum.SPEED: 110
        }
    },
    "0946": {
        None: {
            PocketMonsterParamEnum.NAME: "Bramblin",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.GRASS,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.GHOST,
            StatsEnum.HP: 40,
            StatsEnum.ATTACK: 65,
            StatsEnum.DEFENSE: 30,
            StatsEnum.SPECIAL_ATTACK: 45,
            StatsEnum.SPECIAL_DEFENSE: 35,
            StatsEnum.SPEED: 60
        }
    },
    "0947": {
        None: {
            PocketMonsterParamEnum.NAME: "Brambleghast",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.GRASS,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.GHOST,
            StatsEnum.HP: 55,
            StatsEnum.ATTACK: 115,
            StatsEnum.DEFENSE: 70,
            StatsEnum.SPECIAL_ATTACK: 80,
            StatsEnum.SPECIAL_DEFENSE: 70,
            StatsEnum.SPEED: 90
        }
    },
    "0948": {
        None: {
            PocketMonsterParamEnum.NAME: "Toedscool",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.GROUND,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.GRASS,
            StatsEnum.HP: 40,
            StatsEnum.ATTACK: 40,
            StatsEnum.DEFENSE: 35,
            StatsEnum.SPECIAL_ATTACK: 50,
            StatsEnum.SPECIAL_DEFENSE: 100,
            StatsEnum.SPEED: 70
        }
    },
    "0949": {
        None: {
            PocketMonsterParamEnum.NAME: "Toedscruel",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.GROUND,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.GRASS,
            StatsEnum.HP: 80,
            StatsEnum.ATTACK: 70,
            StatsEnum.DEFENSE: 65,
            StatsEnum.SPECIAL_ATTACK: 80,
            StatsEnum.SPECIAL_DEFENSE: 120,
            StatsEnum.SPEED: 100
        }
    },
    "0950": {
        None: {
            PocketMonsterParamEnum.NAME: "Klawf",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.ROCK,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 70,
            StatsEnum.ATTACK: 100,
            StatsEnum.DEFENSE: 115,
            StatsEnum.SPECIAL_ATTACK: 35,
            StatsEnum.SPECIAL_DEFENSE: 55,
            StatsEnum.SPEED: 75
        }
    },
    "0951": {
        None: {
            PocketMonsterParamEnum.NAME: "Capsakid",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.GRASS,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 50,
            StatsEnum.ATTACK: 62,
            StatsEnum.DEFENSE: 40,
            StatsEnum.SPECIAL_ATTACK: 62,
            StatsEnum.SPECIAL_DEFENSE: 40,
            StatsEnum.SPEED: 50
        }
    },
    "0952": {
        None: {
            PocketMonsterParamEnum.NAME: "Scovillain",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.GRASS,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.FIRE,
            StatsEnum.HP: 65,
            StatsEnum.ATTACK: 108,
            StatsEnum.DEFENSE: 65,
            StatsEnum.SPECIAL_ATTACK: 108,
            StatsEnum.SPECIAL_DEFENSE: 65,
            StatsEnum.SPEED: 75
        }
    },
    "0953": {
        None: {
            PocketMonsterParamEnum.NAME: "Rellor",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.BUG,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 41,
            StatsEnum.ATTACK: 50,
            StatsEnum.DEFENSE: 60,
            StatsEnum.SPECIAL_ATTACK: 31,
            StatsEnum.SPECIAL_DEFENSE: 58,
            StatsEnum.SPEED: 30
        }
    },
    "0954": {
        None: {
            PocketMonsterParamEnum.NAME: "Rabsca",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.BUG,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.PSYCHIC,
            StatsEnum.HP: 75,
            StatsEnum.ATTACK: 50,
            StatsEnum.DEFENSE: 85,
            StatsEnum.SPECIAL_ATTACK: 115,
            StatsEnum.SPECIAL_DEFENSE: 100,
            StatsEnum.SPEED: 45
        }
    },
    "0955": {
        None: {
            PocketMonsterParamEnum.NAME: "Flittle",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.PSYCHIC,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 30,
            StatsEnum.ATTACK: 35,
            StatsEnum.DEFENSE: 30,
            StatsEnum.SPECIAL_ATTACK: 55,
            StatsEnum.SPECIAL_DEFENSE: 30,
            StatsEnum.SPEED: 75
        }
    },
    "0956": {
        None: {
            PocketMonsterParamEnum.NAME: "Espathra",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.PSYCHIC,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 95,
            StatsEnum.ATTACK: 60,
            StatsEnum.DEFENSE: 60,
            StatsEnum.SPECIAL_ATTACK: 101,
            StatsEnum.SPECIAL_DEFENSE: 60,
            StatsEnum.SPEED: 105
        }
    },
    "0957": {
        None: {
            PocketMonsterParamEnum.NAME: "Tinkatink",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.FAIRY,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.STEEL,
            StatsEnum.HP: 50,
            StatsEnum.ATTACK: 45,
            StatsEnum.DEFENSE: 45,
            StatsEnum.SPECIAL_ATTACK: 35,
            StatsEnum.SPECIAL_DEFENSE: 64,
            StatsEnum.SPEED: 58
        }
    },
    "0958": {
        None: {
            PocketMonsterParamEnum.NAME: "Tinkatuff",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.FAIRY,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.STEEL,
            StatsEnum.HP: 65,
            StatsEnum.ATTACK: 55,
            StatsEnum.DEFENSE: 55,
            StatsEnum.SPECIAL_ATTACK: 45,
            StatsEnum.SPECIAL_DEFENSE: 82,
            StatsEnum.SPEED: 78
        }
    },
    "0959": {
        None: {
            PocketMonsterParamEnum.NAME: "Tinkaton",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.FAIRY,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.STEEL,
            StatsEnum.HP: 85,
            StatsEnum.ATTACK: 75,
            StatsEnum.DEFENSE: 77,
            StatsEnum.SPECIAL_ATTACK: 70,
            StatsEnum.SPECIAL_DEFENSE: 105,
            StatsEnum.SPEED: 94
        }
    },
    "0960": {
        None: {
            PocketMonsterParamEnum.NAME: "Wiglett",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.WATER,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 10,
            StatsEnum.ATTACK: 55,
            StatsEnum.DEFENSE: 25,
            StatsEnum.SPECIAL_ATTACK: 35,
            StatsEnum.SPECIAL_DEFENSE: 25,
            StatsEnum.SPEED: 95
        }
    },
    "0961": {
        None: {
            PocketMonsterParamEnum.NAME: "Wugtrio",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.WATER,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 35,
            StatsEnum.ATTACK: 100,
            StatsEnum.DEFENSE: 50,
            StatsEnum.SPECIAL_ATTACK: 50,
            StatsEnum.SPECIAL_DEFENSE: 70,
            StatsEnum.SPEED: 120
        }
    },
    "0962": {
        None: {
            PocketMonsterParamEnum.NAME: "Bombirdier",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.FLYING,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.DARK,
            StatsEnum.HP: 70,
            StatsEnum.ATTACK: 103,
            StatsEnum.DEFENSE: 85,
            StatsEnum.SPECIAL_ATTACK: 60,
            StatsEnum.SPECIAL_DEFENSE: 85,
            StatsEnum.SPEED: 82
        }
    },
    "0963": {
        None: {
            PocketMonsterParamEnum.NAME: "Finizen",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.WATER,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 70,
            StatsEnum.ATTACK: 45,
            StatsEnum.DEFENSE: 40,
            StatsEnum.SPECIAL_ATTACK: 45,
            StatsEnum.SPECIAL_DEFENSE: 40,
            StatsEnum.SPEED: 75
        }
    },
    "0964": {
        "Zero Form": {
            PocketMonsterParamEnum.NAME: "Palafin",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.WATER,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 100,
            StatsEnum.ATTACK: 70,
            StatsEnum.DEFENSE: 72,
            StatsEnum.SPECIAL_ATTACK: 53,
            StatsEnum.SPECIAL_DEFENSE: 62,
            StatsEnum.SPEED: 100
        },
        "Hero Form": {
            PocketMonsterParamEnum.NAME: "Palafin",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.WATER,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 100,
            StatsEnum.ATTACK: 160,
            StatsEnum.DEFENSE: 97,
            StatsEnum.SPECIAL_ATTACK: 106,
            StatsEnum.SPECIAL_DEFENSE: 87,
            StatsEnum.SPEED: 100
        }
    },
    "0965": {
        None: {
            PocketMonsterParamEnum.NAME: "Varoom",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.STEEL,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.POISON,
            StatsEnum.HP: 45,
            StatsEnum.ATTACK: 70,
            StatsEnum.DEFENSE: 63,
            StatsEnum.SPECIAL_ATTACK: 30,
            StatsEnum.SPECIAL_DEFENSE: 45,
            StatsEnum.SPEED: 47
        }
    },
    "0966": {
        None: {
            PocketMonsterParamEnum.NAME: "Revavroom",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.STEEL,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.POISON,
            StatsEnum.HP: 80,
            StatsEnum.ATTACK: 119,
            StatsEnum.DEFENSE: 90,
            StatsEnum.SPECIAL_ATTACK: 54,
            StatsEnum.SPECIAL_DEFENSE: 67,
            StatsEnum.SPEED: 90
        }
    },
    "0967": {
        None: {
            PocketMonsterParamEnum.NAME: "Cyclizar",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.DRAGON,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.NORMAL,
            StatsEnum.HP: 70,
            StatsEnum.ATTACK: 95,
            StatsEnum.DEFENSE: 65,
            StatsEnum.SPECIAL_ATTACK: 85,
            StatsEnum.SPECIAL_DEFENSE: 65,
            StatsEnum.SPEED: 121
        }
    },
    "0968": {
        None: {
            PocketMonsterParamEnum.NAME: "Orthworm",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.STEEL,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 70,
            StatsEnum.ATTACK: 85,
            StatsEnum.DEFENSE: 145,
            StatsEnum.SPECIAL_ATTACK: 60,
            StatsEnum.SPECIAL_DEFENSE: 55,
            StatsEnum.SPEED: 65
        }
    },
    "0969": {
        None: {
            PocketMonsterParamEnum.NAME: "Glimmet",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.ROCK,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.POISON,
            StatsEnum.HP: 48,
            StatsEnum.ATTACK: 35,
            StatsEnum.DEFENSE: 42,
            StatsEnum.SPECIAL_ATTACK: 105,
            StatsEnum.SPECIAL_DEFENSE: 60,
            StatsEnum.SPEED: 60
        }
    },
    "0970": {
        None: {
            PocketMonsterParamEnum.NAME: "Glimmora",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.ROCK,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.POISON,
            StatsEnum.HP: 83,
            StatsEnum.ATTACK: 55,
            StatsEnum.DEFENSE: 90,
            StatsEnum.SPECIAL_ATTACK: 130,
            StatsEnum.SPECIAL_DEFENSE: 81,
            StatsEnum.SPEED: 86
        }
    },
    "0971": {
        None: {
            PocketMonsterParamEnum.NAME: "Greavard",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.GHOST,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 50,
            StatsEnum.ATTACK: 61,
            StatsEnum.DEFENSE: 60,
            StatsEnum.SPECIAL_ATTACK: 30,
            StatsEnum.SPECIAL_DEFENSE: 55,
            StatsEnum.SPEED: 34
        }
    },
    "0972": {
        None: {
            PocketMonsterParamEnum.NAME: "Houndstone",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.GHOST,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 72,
            StatsEnum.ATTACK: 101,
            StatsEnum.DEFENSE: 100,
            StatsEnum.SPECIAL_ATTACK: 50,
            StatsEnum.SPECIAL_DEFENSE: 97,
            StatsEnum.SPEED: 68
        }
    },
    "0973": {
        None: {
            PocketMonsterParamEnum.NAME: "Flamigo",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.FLYING,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.FIGHTING,
            StatsEnum.HP: 82,
            StatsEnum.ATTACK: 115,
            StatsEnum.DEFENSE: 74,
            StatsEnum.SPECIAL_ATTACK: 75,
            StatsEnum.SPECIAL_DEFENSE: 64,
            StatsEnum.SPEED: 90
        }
    },
    "0974": {
        None: {
            PocketMonsterParamEnum.NAME: "Cetoddle",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.ICE,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 108,
            StatsEnum.ATTACK: 68,
            StatsEnum.DEFENSE: 45,
            StatsEnum.SPECIAL_ATTACK: 30,
            StatsEnum.SPECIAL_DEFENSE: 40,
            StatsEnum.SPEED: 43
        }
    },
    "0975": {
        None: {
            PocketMonsterParamEnum.NAME: "Cetitan",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.ICE,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 170,
            StatsEnum.ATTACK: 113,
            StatsEnum.DEFENSE: 65,
            StatsEnum.SPECIAL_ATTACK: 45,
            StatsEnum.SPECIAL_DEFENSE: 55,
            StatsEnum.SPEED: 73
        }
    },
    "0976": {
        None: {
            PocketMonsterParamEnum.NAME: "Veluza",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.WATER,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.PSYCHIC,
            StatsEnum.HP: 90,
            StatsEnum.ATTACK: 102,
            StatsEnum.DEFENSE: 73,
            StatsEnum.SPECIAL_ATTACK: 78,
            StatsEnum.SPECIAL_DEFENSE: 65,
            StatsEnum.SPEED: 70
        }
    },
    "0977": {
        None: {
            PocketMonsterParamEnum.NAME: "Dondozo",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.WATER,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 150,
            StatsEnum.ATTACK: 100,
            StatsEnum.DEFENSE: 115,
            StatsEnum.SPECIAL_ATTACK: 65,
            StatsEnum.SPECIAL_DEFENSE: 65,
            StatsEnum.SPEED: 35
        }
    },
    "0978": {
        "Curly Form": {
            PocketMonsterParamEnum.NAME: "Tatsugiri",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.DRAGON,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.WATER,
            StatsEnum.HP: 68,
            StatsEnum.ATTACK: 50,
            StatsEnum.DEFENSE: 60,
            StatsEnum.SPECIAL_ATTACK: 120,
            StatsEnum.SPECIAL_DEFENSE: 95,
            StatsEnum.SPEED: 82
        },
        "Droopy Form": {
            PocketMonsterParamEnum.NAME: "Tatsugiri",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.DRAGON,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.WATER,
            StatsEnum.HP: 68,
            StatsEnum.ATTACK: 50,
            StatsEnum.DEFENSE: 60,
            StatsEnum.SPECIAL_ATTACK: 120,
            StatsEnum.SPECIAL_DEFENSE: 95,
            StatsEnum.SPEED: 82
        },
        "Stretchy Form": {
            PocketMonsterParamEnum.NAME: "Tatsugiri",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.DRAGON,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.WATER,
            StatsEnum.HP: 68,
            StatsEnum.ATTACK: 50,
            StatsEnum.DEFENSE: 60,
            StatsEnum.SPECIAL_ATTACK: 120,
            StatsEnum.SPECIAL_DEFENSE: 95,
            StatsEnum.SPEED: 82
        }
    },
    "0979": {
        None: {
            PocketMonsterParamEnum.NAME: "Annihilape",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.FIGHTING,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.GHOST,
            StatsEnum.HP: 110,
            StatsEnum.ATTACK: 115,
            StatsEnum.DEFENSE: 80,
            StatsEnum.SPECIAL_ATTACK: 50,
            StatsEnum.SPECIAL_DEFENSE: 90,
            StatsEnum.SPEED: 90
        }
    },
    "0980": {
        None: {
            PocketMonsterParamEnum.NAME: "Clodsire",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.POISON,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.GROUND,
            StatsEnum.HP: 130,
            StatsEnum.ATTACK: 75,
            StatsEnum.DEFENSE: 60,
            StatsEnum.SPECIAL_ATTACK: 45,
            StatsEnum.SPECIAL_DEFENSE: 100,
            StatsEnum.SPEED: 20
        }
    },
    "0981": {
        None: {
            PocketMonsterParamEnum.NAME: "Farigiraf",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.NORMAL,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.PSYCHIC,
            StatsEnum.HP: 120,
            StatsEnum.ATTACK: 90,
            StatsEnum.DEFENSE: 70,
            StatsEnum.SPECIAL_ATTACK: 110,
            StatsEnum.SPECIAL_DEFENSE: 70,
            StatsEnum.SPEED: 60
        }
    },
    "0982": {
        "Two-Segment Form": {
            PocketMonsterParamEnum.NAME: "Dudunsparce",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.NORMAL,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 125,
            StatsEnum.ATTACK: 100,
            StatsEnum.DEFENSE: 80,
            StatsEnum.SPECIAL_ATTACK: 85,
            StatsEnum.SPECIAL_DEFENSE: 75,
            StatsEnum.SPEED: 55
        },
        "Three-Segment Form": {
            PocketMonsterParamEnum.NAME: "Dudunsparce",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.NORMAL,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 125,
            StatsEnum.ATTACK: 100,
            StatsEnum.DEFENSE: 80,
            StatsEnum.SPECIAL_ATTACK: 85,
            StatsEnum.SPECIAL_DEFENSE: 75,
            StatsEnum.SPEED: 55
        }
    },
    "0983": {
        None: {
            PocketMonsterParamEnum.NAME: "Kingambit",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.DARK,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.STEEL,
            StatsEnum.HP: 100,
            StatsEnum.ATTACK: 135,
            StatsEnum.DEFENSE: 120,
            StatsEnum.SPECIAL_ATTACK: 60,
            StatsEnum.SPECIAL_DEFENSE: 85,
            StatsEnum.SPEED: 50
        }
    },
    "0984": {
        None: {
            PocketMonsterParamEnum.NAME: "Great Tusk",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.GROUND,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.FIGHTING,
            StatsEnum.HP: 115,
            StatsEnum.ATTACK: 131,
            StatsEnum.DEFENSE: 131,
            StatsEnum.SPECIAL_ATTACK: 53,
            StatsEnum.SPECIAL_DEFENSE: 53,
            StatsEnum.SPEED: 87
        }
    },
    "0985": {
        None: {
            PocketMonsterParamEnum.NAME: "Scream Tail",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.FAIRY,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.PSYCHIC,
            StatsEnum.HP: 115,
            StatsEnum.ATTACK: 65,
            StatsEnum.DEFENSE: 99,
            StatsEnum.SPECIAL_ATTACK: 65,
            StatsEnum.SPECIAL_DEFENSE: 115,
            StatsEnum.SPEED: 111
        }
    },
    "0986": {
        None: {
            PocketMonsterParamEnum.NAME: "Brute Bonnet",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.GRASS,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.DARK,
            StatsEnum.HP: 111,
            StatsEnum.ATTACK: 127,
            StatsEnum.DEFENSE: 99,
            StatsEnum.SPECIAL_ATTACK: 79,
            StatsEnum.SPECIAL_DEFENSE: 99,
            StatsEnum.SPEED: 55
        }
    },
    "0987": {
        None: {
            PocketMonsterParamEnum.NAME: "Flutter Mane",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.GHOST,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.FAIRY,
            StatsEnum.HP: 55,
            StatsEnum.ATTACK: 55,
            StatsEnum.DEFENSE: 55,
            StatsEnum.SPECIAL_ATTACK: 135,
            StatsEnum.SPECIAL_DEFENSE: 135,
            StatsEnum.SPEED: 135
        }
    },
    "0988": {
        None: {
            PocketMonsterParamEnum.NAME: "Slither Wing",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.BUG,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.FIGHTING,
            StatsEnum.HP: 85,
            StatsEnum.ATTACK: 135,
            StatsEnum.DEFENSE: 79,
            StatsEnum.SPECIAL_ATTACK: 85,
            StatsEnum.SPECIAL_DEFENSE: 105,
            StatsEnum.SPEED: 81
        }
    },
    "0989": {
        None: {
            PocketMonsterParamEnum.NAME: "Sandy Shocks",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.ELECTRIC,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.GROUND,
            StatsEnum.HP: 85,
            StatsEnum.ATTACK: 81,
            StatsEnum.DEFENSE: 97,
            StatsEnum.SPECIAL_ATTACK: 121,
            StatsEnum.SPECIAL_DEFENSE: 85,
            StatsEnum.SPEED: 101
        }
    },
    "0990": {
        None: {
            PocketMonsterParamEnum.NAME: "Iron Treads",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.GROUND,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.STEEL,
            StatsEnum.HP: 90,
            StatsEnum.ATTACK: 112,
            StatsEnum.DEFENSE: 120,
            StatsEnum.SPECIAL_ATTACK: 72,
            StatsEnum.SPECIAL_DEFENSE: 70,
            StatsEnum.SPEED: 106
        }
    },
    "0991": {
        None: {
            PocketMonsterParamEnum.NAME: "Iron Bundle",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.ICE,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.WATER,
            StatsEnum.HP: 56,
            StatsEnum.ATTACK: 80,
            StatsEnum.DEFENSE: 114,
            StatsEnum.SPECIAL_ATTACK: 124,
            StatsEnum.SPECIAL_DEFENSE: 60,
            StatsEnum.SPEED: 136
        }
    },
    "0992": {
        None: {
            PocketMonsterParamEnum.NAME: "Iron Hands",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.FIGHTING,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.ELECTRIC,
            StatsEnum.HP: 154,
            StatsEnum.ATTACK: 140,
            StatsEnum.DEFENSE: 108,
            StatsEnum.SPECIAL_ATTACK: 50,
            StatsEnum.SPECIAL_DEFENSE: 68,
            StatsEnum.SPEED: 50
        }
    },
    "0993": {
        None: {
            PocketMonsterParamEnum.NAME: "Iron Jugulis",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.DARK,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.FLYING,
            StatsEnum.HP: 94,
            StatsEnum.ATTACK: 80,
            StatsEnum.DEFENSE: 86,
            StatsEnum.SPECIAL_ATTACK: 122,
            StatsEnum.SPECIAL_DEFENSE: 80,
            StatsEnum.SPEED: 108
        }
    },
    "0994": {
        None: {
            PocketMonsterParamEnum.NAME: "Iron Moth",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.FIRE,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.POISON,
            StatsEnum.HP: 80,
            StatsEnum.ATTACK: 70,
            StatsEnum.DEFENSE: 60,
            StatsEnum.SPECIAL_ATTACK: 140,
            StatsEnum.SPECIAL_DEFENSE: 110,
            StatsEnum.SPEED: 110
        }
    },
    "0995": {
        None: {
            PocketMonsterParamEnum.NAME: "Iron Thorns",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.ROCK,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.ELECTRIC,
            StatsEnum.HP: 100,
            StatsEnum.ATTACK: 134,
            StatsEnum.DEFENSE: 110,
            StatsEnum.SPECIAL_ATTACK: 70,
            StatsEnum.SPECIAL_DEFENSE: 84,
            StatsEnum.SPEED: 72
        }
    },
    "0996": {
        None: {
            PocketMonsterParamEnum.NAME: "Frigibax",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.DRAGON,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.ICE,
            StatsEnum.HP: 65,
            StatsEnum.ATTACK: 75,
            StatsEnum.DEFENSE: 45,
            StatsEnum.SPECIAL_ATTACK: 35,
            StatsEnum.SPECIAL_DEFENSE: 45,
            StatsEnum.SPEED: 55
        }
    },
    "0997": {
        None: {
            PocketMonsterParamEnum.NAME: "Arctibax",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.DRAGON,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.ICE,
            StatsEnum.HP: 90,
            StatsEnum.ATTACK: 95,
            StatsEnum.DEFENSE: 66,
            StatsEnum.SPECIAL_ATTACK: 45,
            StatsEnum.SPECIAL_DEFENSE: 65,
            StatsEnum.SPEED: 62
        }
    },
    "0998": {
        None: {
            PocketMonsterParamEnum.NAME: "Baxcalibur",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.DRAGON,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.ICE,
            StatsEnum.HP: 115,
            StatsEnum.ATTACK: 145,
            StatsEnum.DEFENSE: 92,
            StatsEnum.SPECIAL_ATTACK: 75,
            StatsEnum.SPECIAL_DEFENSE: 86,
            StatsEnum.SPEED: 87
        }
    },
    "0999": {
        "Chest Form": {
            PocketMonsterParamEnum.NAME: "Gimmighoul",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.GHOST,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 45,
            StatsEnum.ATTACK: 30,
            StatsEnum.DEFENSE: 70,
            StatsEnum.SPECIAL_ATTACK: 75,
            StatsEnum.SPECIAL_DEFENSE: 70,
            StatsEnum.SPEED: 10
        },
        "Roaming Form": {
            PocketMonsterParamEnum.NAME: "Gimmighoul",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.GHOST,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 45,
            StatsEnum.ATTACK: 30,
            StatsEnum.DEFENSE: 25,
            StatsEnum.SPECIAL_ATTACK: 75,
            StatsEnum.SPECIAL_DEFENSE: 45,
            StatsEnum.SPEED: 80
        }
    },
    "1000": {
        None: {
            PocketMonsterParamEnum.NAME: "Gholdengo",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.STEEL,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.GHOST,
            StatsEnum.HP: 87,
            StatsEnum.ATTACK: 60,
            StatsEnum.DEFENSE: 95,
            StatsEnum.SPECIAL_ATTACK: 133,
            StatsEnum.SPECIAL_DEFENSE: 91,
            StatsEnum.SPEED: 84
        }
    },
    "1001": {
        None: {
            PocketMonsterParamEnum.NAME: "Wo-Chien",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.DARK,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.GRASS,
            StatsEnum.HP: 85,
            StatsEnum.ATTACK: 85,
            StatsEnum.DEFENSE: 100,
            StatsEnum.SPECIAL_ATTACK: 95,
            StatsEnum.SPECIAL_DEFENSE: 135,
            StatsEnum.SPEED: 70
        }
    },
    "1002": {
        None: {
            PocketMonsterParamEnum.NAME: "Chien-Pao",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.DARK,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.ICE,
            StatsEnum.HP: 80,
            StatsEnum.ATTACK: 120,
            StatsEnum.DEFENSE: 80,
            StatsEnum.SPECIAL_ATTACK: 90,
            StatsEnum.SPECIAL_DEFENSE: 65,
            StatsEnum.SPEED: 135
        }
    },
    "1003": {
        None: {
            PocketMonsterParamEnum.NAME: "Ting-Lu",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.DARK,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.GROUND,
            StatsEnum.HP: 155,
            StatsEnum.ATTACK: 110,
            StatsEnum.DEFENSE: 125,
            StatsEnum.SPECIAL_ATTACK: 55,
            StatsEnum.SPECIAL_DEFENSE: 80,
            StatsEnum.SPEED: 45
        }
    },
    "1004": {
        None: {
            PocketMonsterParamEnum.NAME: "Chi-Yu",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.DARK,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.FIRE,
            StatsEnum.HP: 55,
            StatsEnum.ATTACK: 80,
            StatsEnum.DEFENSE: 80,
            StatsEnum.SPECIAL_ATTACK: 135,
            StatsEnum.SPECIAL_DEFENSE: 120,
            StatsEnum.SPEED: 100
        }
    },
    "1005": {
        None: {
            PocketMonsterParamEnum.NAME: "Roaring Moon",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.DRAGON,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.DARK,
            StatsEnum.HP: 105,
            StatsEnum.ATTACK: 139,
            StatsEnum.DEFENSE: 71,
            StatsEnum.SPECIAL_ATTACK: 55,
            StatsEnum.SPECIAL_DEFENSE: 101,
            StatsEnum.SPEED: 119
        }
    },
    "1006": {
        None: {
            PocketMonsterParamEnum.NAME: "Iron Valiant",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.FAIRY,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.FIGHTING,
            StatsEnum.HP: 74,
            StatsEnum.ATTACK: 130,
            StatsEnum.DEFENSE: 90,
            StatsEnum.SPECIAL_ATTACK: 120,
            StatsEnum.SPECIAL_DEFENSE: 60,
            StatsEnum.SPEED: 116
        }
    },
    "1007": {
        None: {
            PocketMonsterParamEnum.NAME: "Koraidon",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.FIGHTING,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.DRAGON,
            StatsEnum.HP: 100,
            StatsEnum.ATTACK: 135,
            StatsEnum.DEFENSE: 115,
            StatsEnum.SPECIAL_ATTACK: 85,
            StatsEnum.SPECIAL_DEFENSE: 100,
            StatsEnum.SPEED: 135
        }
    },
    "1008": {
        None: {
            PocketMonsterParamEnum.NAME: "Miraidon",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.ELECTRIC,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.DRAGON,
            StatsEnum.HP: 100,
            StatsEnum.ATTACK: 85,
            StatsEnum.DEFENSE: 100,
            StatsEnum.SPECIAL_ATTACK: 135,
            StatsEnum.SPECIAL_DEFENSE: 115,
            StatsEnum.SPEED: 135
        }
    },
    "1009": {
        None: {
            PocketMonsterParamEnum.NAME: "Walking Wake",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.WATER,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.DRAGON,
            StatsEnum.HP: 99,
            StatsEnum.ATTACK: 83,
            StatsEnum.DEFENSE: 91,
            StatsEnum.SPECIAL_ATTACK: 125,
            StatsEnum.SPECIAL_DEFENSE: 83,
            StatsEnum.SPEED: 109
        }
    },
    "1010": {
        None: {
            PocketMonsterParamEnum.NAME: "Iron Leaves",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.GRASS,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.PSYCHIC,
            StatsEnum.HP: 90,
            StatsEnum.ATTACK: 130,
            StatsEnum.DEFENSE: 88,
            StatsEnum.SPECIAL_ATTACK: 70,
            StatsEnum.SPECIAL_DEFENSE: 108,
            StatsEnum.SPEED: 104
        }
    },
    "1011": {
        None: {
            PocketMonsterParamEnum.NAME: "Dipplin",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.GRASS,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.DRAGON,
            StatsEnum.HP: 80,
            StatsEnum.ATTACK: 80,
            StatsEnum.DEFENSE: 110,
            StatsEnum.SPECIAL_ATTACK: 95,
            StatsEnum.SPECIAL_DEFENSE: 80,
            StatsEnum.SPEED: 40
        }
    },
    "1012": {
        None: {
            PocketMonsterParamEnum.NAME: "Poltchageist",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.GRASS,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.GHOST,
            StatsEnum.HP: 40,
            StatsEnum.ATTACK: 45,
            StatsEnum.DEFENSE: 45,
            StatsEnum.SPECIAL_ATTACK: 74,
            StatsEnum.SPECIAL_DEFENSE: 54,
            StatsEnum.SPEED: 50
        }
    },
    "1013": {
        None: {
            PocketMonsterParamEnum.NAME: "Sinistcha",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.GRASS,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.GHOST,
            StatsEnum.HP: 71,
            StatsEnum.ATTACK: 60,
            StatsEnum.DEFENSE: 106,
            StatsEnum.SPECIAL_ATTACK: 121,
            StatsEnum.SPECIAL_DEFENSE: 80,
            StatsEnum.SPEED: 70
        }
    },
    "1014": {
        None: {
            PocketMonsterParamEnum.NAME: "Okidogi",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.POISON,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.FIGHTING,
            StatsEnum.HP: 88,
            StatsEnum.ATTACK: 128,
            StatsEnum.DEFENSE: 115,
            StatsEnum.SPECIAL_ATTACK: 58,
            StatsEnum.SPECIAL_DEFENSE: 86,
            StatsEnum.SPEED: 80
        }
    },
    "1015": {
        None: {
            PocketMonsterParamEnum.NAME: "Munkidori",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.POISON,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.PSYCHIC,
            StatsEnum.HP: 88,
            StatsEnum.ATTACK: 75,
            StatsEnum.DEFENSE: 66,
            StatsEnum.SPECIAL_ATTACK: 130,
            StatsEnum.SPECIAL_DEFENSE: 90,
            StatsEnum.SPEED: 106
        }
    },
    "1016": {
        None: {
            PocketMonsterParamEnum.NAME: "Fezandipiti",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.POISON,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.FAIRY,
            StatsEnum.HP: 88,
            StatsEnum.ATTACK: 91,
            StatsEnum.DEFENSE: 82,
            StatsEnum.SPECIAL_ATTACK: 70,
            StatsEnum.SPECIAL_DEFENSE: 125,
            StatsEnum.SPEED: 99
        }
    },
    "1017": {
        "Teal Mask": {
            PocketMonsterParamEnum.NAME: "Ogerpon",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.GRASS,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 80,
            StatsEnum.ATTACK: 120,
            StatsEnum.DEFENSE: 84,
            StatsEnum.SPECIAL_ATTACK: 60,
            StatsEnum.SPECIAL_DEFENSE: 96,
            StatsEnum.SPEED: 110
        },
        "Wellspring Mask": {
            PocketMonsterParamEnum.NAME: "Ogerpon",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.GRASS,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.WATER,
            StatsEnum.HP: 80,
            StatsEnum.ATTACK: 120,
            StatsEnum.DEFENSE: 84,
            StatsEnum.SPECIAL_ATTACK: 60,
            StatsEnum.SPECIAL_DEFENSE: 96,
            StatsEnum.SPEED: 110
        },
        "Hearthflame Mask": {
            PocketMonsterParamEnum.NAME: "Ogerpon",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.GRASS,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.FIRE,
            StatsEnum.HP: 80,
            StatsEnum.ATTACK: 120,
            StatsEnum.DEFENSE: 84,
            StatsEnum.SPECIAL_ATTACK: 60,
            StatsEnum.SPECIAL_DEFENSE: 96,
            StatsEnum.SPEED: 110
        },
        "Cornerstone Mask": {
            PocketMonsterParamEnum.NAME: "Ogerpon",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.GRASS,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.ROCK,
            StatsEnum.HP: 80,
            StatsEnum.ATTACK: 120,
            StatsEnum.DEFENSE: 84,
            StatsEnum.SPECIAL_ATTACK: 60,
            StatsEnum.SPECIAL_DEFENSE: 96,
            StatsEnum.SPEED: 110
        }
    },
    "1018": {
        None: {
            PocketMonsterParamEnum.NAME: "Archaludon",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.STEEL,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.DRAGON,
            StatsEnum.HP: 90,
            StatsEnum.ATTACK: 105,
            StatsEnum.DEFENSE: 130,
            StatsEnum.SPECIAL_ATTACK: 125,
            StatsEnum.SPECIAL_DEFENSE: 65,
            StatsEnum.SPEED: 85
        }
    },
    "1019": {
        None: {
            PocketMonsterParamEnum.NAME: "Hydrapple",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.GRASS,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.DRAGON,
            StatsEnum.HP: 106,
            StatsEnum.ATTACK: 80,
            StatsEnum.DEFENSE: 110,
            StatsEnum.SPECIAL_ATTACK: 120,
            StatsEnum.SPECIAL_DEFENSE: 80,
            StatsEnum.SPEED: 44
        }
    },
    "1020": {
        None: {
            PocketMonsterParamEnum.NAME: "Gouging Fire",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.FIRE,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.DRAGON,
            StatsEnum.HP: 105,
            StatsEnum.ATTACK: 115,
            StatsEnum.DEFENSE: 121,
            StatsEnum.SPECIAL_ATTACK: 65,
            StatsEnum.SPECIAL_DEFENSE: 93,
            StatsEnum.SPEED: 91
        }
    },
    "1021": {
        None: {
            PocketMonsterParamEnum.NAME: "Raging Bolt",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.ELECTRIC,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.DRAGON,
            StatsEnum.HP: 125,
            StatsEnum.ATTACK: 73,
            StatsEnum.DEFENSE: 91,
            StatsEnum.SPECIAL_ATTACK: 137,
            StatsEnum.SPECIAL_DEFENSE: 89,
            StatsEnum.SPEED: 75
        }
    },
    "1022": {
        None: {
            PocketMonsterParamEnum.NAME: "Iron Boulder",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.ROCK,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.PSYCHIC,
            StatsEnum.HP: 90,
            StatsEnum.ATTACK: 120,
            StatsEnum.DEFENSE: 80,
            StatsEnum.SPECIAL_ATTACK: 68,
            StatsEnum.SPECIAL_DEFENSE: 108,
            StatsEnum.SPEED: 124
        }
    },
    "1023": {
        None: {
            PocketMonsterParamEnum.NAME: "Iron Crown",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.STEEL,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.PSYCHIC,
            StatsEnum.HP: 90,
            StatsEnum.ATTACK: 72,
            StatsEnum.DEFENSE: 100,
            StatsEnum.SPECIAL_ATTACK: 122,
            StatsEnum.SPECIAL_DEFENSE: 108,
            StatsEnum.SPEED: 98
        }
    },
    "1024": {
        "Normal Form": {
            PocketMonsterParamEnum.NAME: "Terapagos",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.NORMAL,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 90,
            StatsEnum.ATTACK: 65,
            StatsEnum.DEFENSE: 85,
            StatsEnum.SPECIAL_ATTACK: 65,
            StatsEnum.SPECIAL_DEFENSE: 85,
            StatsEnum.SPEED: 60
        },
        "Terastal Form": {
            PocketMonsterParamEnum.NAME: "Terapagos",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.NORMAL,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 95,
            StatsEnum.ATTACK: 95,
            StatsEnum.DEFENSE: 110,
            StatsEnum.SPECIAL_ATTACK: 105,
            StatsEnum.SPECIAL_DEFENSE: 110,
            StatsEnum.SPEED: 85
        },
        "Stellar Form": {
            PocketMonsterParamEnum.NAME: "Terapagos",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.NORMAL,
            PocketMonsterParamEnum.TYPE_2: None,
            StatsEnum.HP: 160,
            StatsEnum.ATTACK: 105,
            StatsEnum.DEFENSE: 110,
            StatsEnum.SPECIAL_ATTACK: 130,
            StatsEnum.SPECIAL_DEFENSE: 110,
            StatsEnum.SPEED: 85
        }
    },
    "1025": {
        None: {
            PocketMonsterParamEnum.NAME: "Pecharunt",
            PocketMonsterParamEnum.TYPE_1: TypesEnum.POISON,
            PocketMonsterParamEnum.TYPE_2: TypesEnum.GHOST,
            StatsEnum.HP: 88,
            StatsEnum.ATTACK: 88,
            StatsEnum.DEFENSE: 160,
            StatsEnum.SPECIAL_ATTACK: 88,
            StatsEnum.SPECIAL_DEFENSE: 88,
            StatsEnum.SPEED: 88
        }
    }
}
