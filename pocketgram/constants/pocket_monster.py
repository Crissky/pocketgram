from pocketgram.enums.stats import StatsEnum


POCKET_MONSTERS_DICT = {
    "0001": {
        None: {
            "Name": "Bulbasaur",
            "Type 1": "Grass",
            "Type 2": "Poison",
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
            "Name": "Ivysaur",
            "Type 1": "Grass",
            "Type 2": "Poison",
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
            "Name": "Venusaur",
            "Type 1": "Grass",
            "Type 2": "Poison",
            StatsEnum.HP: 80,
            StatsEnum.ATTACK: 82,
            StatsEnum.DEFENSE: 83,
            StatsEnum.SPECIAL_ATTACK: 100,
            StatsEnum.SPECIAL_DEFENSE: 100,
            StatsEnum.SPEED: 80
        },
        "Mega Venusaur": {
            "Name": "Venusaur",
            "Type 1": "Grass",
            "Type 2": "Poison",
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
            "Name": "Charmander",
            "Type 1": "Fire",
            "Type 2": None,
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
            "Name": "Charmeleon",
            "Type 1": "Fire",
            "Type 2": None,
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
            "Name": "Charizard",
            "Type 1": "Fire",
            "Type 2": "Flying",
            StatsEnum.HP: 78,
            StatsEnum.ATTACK: 84,
            StatsEnum.DEFENSE: 78,
            StatsEnum.SPECIAL_ATTACK: 109,
            StatsEnum.SPECIAL_DEFENSE: 85,
            StatsEnum.SPEED: 100
        },
        "Mega Charizard X": {
            "Name": "Charizard",
            "Type 1": "Fire",
            "Type 2": "Dragon",
            StatsEnum.HP: 78,
            StatsEnum.ATTACK: 130,
            StatsEnum.DEFENSE: 111,
            StatsEnum.SPECIAL_ATTACK: 130,
            StatsEnum.SPECIAL_DEFENSE: 85,
            StatsEnum.SPEED: 100
        },
        "Mega Charizard Y": {
            "Name": "Charizard",
            "Type 1": "Fire",
            "Type 2": "Flying",
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
            "Name": "Squirtle",
            "Type 1": "Water",
            "Type 2": None,
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
            "Name": "Wartortle",
            "Type 1": "Water",
            "Type 2": None,
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
            "Name": "Blastoise",
            "Type 1": "Water",
            "Type 2": None,
            StatsEnum.HP: 79,
            StatsEnum.ATTACK: 83,
            StatsEnum.DEFENSE: 100,
            StatsEnum.SPECIAL_ATTACK: 85,
            StatsEnum.SPECIAL_DEFENSE: 105,
            StatsEnum.SPEED: 78
        },
        "Mega Blastoise": {
            "Name": "Blastoise",
            "Type 1": "Water",
            "Type 2": None,
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
            "Name": "Caterpie",
            "Type 1": "Bug",
            "Type 2": None,
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
            "Name": "Metapod",
            "Type 1": "Bug",
            "Type 2": None,
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
            "Name": "Butterfree",
            "Type 1": "Bug",
            "Type 2": "Flying",
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
            "Name": "Weedle",
            "Type 1": "Bug",
            "Type 2": "Poison",
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
            "Name": "Kakuna",
            "Type 1": "Bug",
            "Type 2": "Poison",
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
            "Name": "Beedrill",
            "Type 1": "Bug",
            "Type 2": "Poison",
            StatsEnum.HP: 65,
            StatsEnum.ATTACK: 90,
            StatsEnum.DEFENSE: 40,
            StatsEnum.SPECIAL_ATTACK: 45,
            StatsEnum.SPECIAL_DEFENSE: 80,
            StatsEnum.SPEED: 75
        },
        "Mega Beedrill": {
            "Name": "Beedrill",
            "Type 1": "Bug",
            "Type 2": "Poison",
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
            "Name": "Pidgey",
            "Type 1": "Normal",
            "Type 2": "Flying",
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
            "Name": "Pidgeotto",
            "Type 1": "Normal",
            "Type 2": "Flying",
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
            "Name": "Pidgeot",
            "Type 1": "Normal",
            "Type 2": "Flying",
            StatsEnum.HP: 83,
            StatsEnum.ATTACK: 80,
            StatsEnum.DEFENSE: 75,
            StatsEnum.SPECIAL_ATTACK: 70,
            StatsEnum.SPECIAL_DEFENSE: 70,
            StatsEnum.SPEED: 101
        },
        "Mega Pidgeot": {
            "Name": "Pidgeot",
            "Type 1": "Normal",
            "Type 2": "Flying",
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
            "Name": "Rattata",
            "Type 1": "Normal",
            "Type 2": None,
            StatsEnum.HP: 30,
            StatsEnum.ATTACK: 56,
            StatsEnum.DEFENSE: 35,
            StatsEnum.SPECIAL_ATTACK: 25,
            StatsEnum.SPECIAL_DEFENSE: 35,
            StatsEnum.SPEED: 72
        },
        "Alolan Rattata": {
            "Name": "Rattata",
            "Type 1": "Dark",
            "Type 2": "Normal",
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
            "Name": "Raticate",
            "Type 1": "Normal",
            "Type 2": None,
            StatsEnum.HP: 55,
            StatsEnum.ATTACK: 81,
            StatsEnum.DEFENSE: 60,
            StatsEnum.SPECIAL_ATTACK: 50,
            StatsEnum.SPECIAL_DEFENSE: 70,
            StatsEnum.SPEED: 97
        },
        "Alolan Raticate": {
            "Name": "Raticate",
            "Type 1": "Dark",
            "Type 2": "Normal",
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
            "Name": "Spearow",
            "Type 1": "Normal",
            "Type 2": "Flying",
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
            "Name": "Fearow",
            "Type 1": "Normal",
            "Type 2": "Flying",
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
            "Name": "Ekans",
            "Type 1": "Poison",
            "Type 2": None,
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
            "Name": "Arbok",
            "Type 1": "Poison",
            "Type 2": None,
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
            "Name": "Pikachu",
            "Type 1": "Electric",
            "Type 2": None,
            StatsEnum.HP: 35,
            StatsEnum.ATTACK: 55,
            StatsEnum.DEFENSE: 40,
            StatsEnum.SPECIAL_ATTACK: 50,
            StatsEnum.SPECIAL_DEFENSE: 50,
            StatsEnum.SPEED: 90
        },
        "Partner Pikachu": {
            "Name": "Pikachu",
            "Type 1": "Electric",
            "Type 2": None,
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
            "Name": "Raichu",
            "Type 1": "Electric",
            "Type 2": None,
            StatsEnum.HP: 60,
            StatsEnum.ATTACK: 90,
            StatsEnum.DEFENSE: 55,
            StatsEnum.SPECIAL_ATTACK: 90,
            StatsEnum.SPECIAL_DEFENSE: 80,
            StatsEnum.SPEED: 110
        },
        "Alolan Raichu": {
            "Name": "Raichu",
            "Type 1": "Electric",
            "Type 2": "Psychic",
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
            "Name": "Sandshrew",
            "Type 1": "Ground",
            "Type 2": None,
            StatsEnum.HP: 50,
            StatsEnum.ATTACK: 75,
            StatsEnum.DEFENSE: 85,
            StatsEnum.SPECIAL_ATTACK: 20,
            StatsEnum.SPECIAL_DEFENSE: 30,
            StatsEnum.SPEED: 40
        },
        "Alolan Sandshrew": {
            "Name": "Sandshrew",
            "Type 1": "Ice",
            "Type 2": "Steel",
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
            "Name": "Sandslash",
            "Type 1": "Ground",
            "Type 2": None,
            StatsEnum.HP: 75,
            StatsEnum.ATTACK: 100,
            StatsEnum.DEFENSE: 110,
            StatsEnum.SPECIAL_ATTACK: 45,
            StatsEnum.SPECIAL_DEFENSE: 55,
            StatsEnum.SPEED: 65
        },
        "Alolan Sandslash": {
            "Name": "Sandslash",
            "Type 1": "Ice",
            "Type 2": "Steel",
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
            "Name": "Nidoran♀",
            "Type 1": "Poison",
            "Type 2": None,
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
            "Name": "Nidorina",
            "Type 1": "Poison",
            "Type 2": None,
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
            "Name": "Nidoqueen",
            "Type 1": "Poison",
            "Type 2": "Ground",
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
            "Name": "Nidoran♂",
            "Type 1": "Poison",
            "Type 2": None,
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
            "Name": "Nidorino",
            "Type 1": "Poison",
            "Type 2": None,
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
            "Name": "Nidoking",
            "Type 1": "Poison",
            "Type 2": "Ground",
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
            "Name": "Clefairy",
            "Type 1": "Fairy",
            "Type 2": None,
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
            "Name": "Clefable",
            "Type 1": "Fairy",
            "Type 2": None,
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
            "Name": "Vulpix",
            "Type 1": "Fire",
            "Type 2": None,
            StatsEnum.HP: 38,
            StatsEnum.ATTACK: 41,
            StatsEnum.DEFENSE: 40,
            StatsEnum.SPECIAL_ATTACK: 50,
            StatsEnum.SPECIAL_DEFENSE: 65,
            StatsEnum.SPEED: 65
        },
        "Alolan Vulpix": {
            "Name": "Vulpix",
            "Type 1": "Ice",
            "Type 2": None,
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
            "Name": "Ninetales",
            "Type 1": "Fire",
            "Type 2": None,
            StatsEnum.HP: 73,
            StatsEnum.ATTACK: 76,
            StatsEnum.DEFENSE: 75,
            StatsEnum.SPECIAL_ATTACK: 81,
            StatsEnum.SPECIAL_DEFENSE: 100,
            StatsEnum.SPEED: 100
        },
        "Alolan Ninetales": {
            "Name": "Ninetales",
            "Type 1": "Ice",
            "Type 2": "Fairy",
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
            "Name": "Jigglypuff",
            "Type 1": "Normal",
            "Type 2": "Fairy",
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
            "Name": "Wigglytuff",
            "Type 1": "Normal",
            "Type 2": "Fairy",
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
            "Name": "Zubat",
            "Type 1": "Poison",
            "Type 2": "Flying",
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
            "Name": "Golbat",
            "Type 1": "Poison",
            "Type 2": "Flying",
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
            "Name": "Oddish",
            "Type 1": "Grass",
            "Type 2": "Poison",
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
            "Name": "Gloom",
            "Type 1": "Grass",
            "Type 2": "Poison",
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
            "Name": "Vileplume",
            "Type 1": "Grass",
            "Type 2": "Poison",
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
            "Name": "Paras",
            "Type 1": "Bug",
            "Type 2": "Grass",
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
            "Name": "Parasect",
            "Type 1": "Bug",
            "Type 2": "Grass",
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
            "Name": "Venonat",
            "Type 1": "Bug",
            "Type 2": "Poison",
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
            "Name": "Venomoth",
            "Type 1": "Bug",
            "Type 2": "Poison",
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
            "Name": "Diglett",
            "Type 1": "Ground",
            "Type 2": None,
            StatsEnum.HP: 10,
            StatsEnum.ATTACK: 55,
            StatsEnum.DEFENSE: 25,
            StatsEnum.SPECIAL_ATTACK: 35,
            StatsEnum.SPECIAL_DEFENSE: 45,
            StatsEnum.SPEED: 95
        },
        "Alolan Diglett": {
            "Name": "Diglett",
            "Type 1": "Ground",
            "Type 2": "Steel",
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
            "Name": "Dugtrio",
            "Type 1": "Ground",
            "Type 2": None,
            StatsEnum.HP: 35,
            StatsEnum.ATTACK: 100,
            StatsEnum.DEFENSE: 50,
            StatsEnum.SPECIAL_ATTACK: 50,
            StatsEnum.SPECIAL_DEFENSE: 70,
            StatsEnum.SPEED: 120
        },
        "Alolan Dugtrio": {
            "Name": "Dugtrio",
            "Type 1": "Ground",
            "Type 2": "Steel",
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
            "Name": "Meowth",
            "Type 1": "Normal",
            "Type 2": None,
            StatsEnum.HP: 40,
            StatsEnum.ATTACK: 45,
            StatsEnum.DEFENSE: 35,
            StatsEnum.SPECIAL_ATTACK: 40,
            StatsEnum.SPECIAL_DEFENSE: 40,
            StatsEnum.SPEED: 90
        },
        "Alolan Meowth": {
            "Name": "Meowth",
            "Type 1": "Dark",
            "Type 2": None,
            StatsEnum.HP: 40,
            StatsEnum.ATTACK: 35,
            StatsEnum.DEFENSE: 35,
            StatsEnum.SPECIAL_ATTACK: 50,
            StatsEnum.SPECIAL_DEFENSE: 40,
            StatsEnum.SPEED: 90
        },
        "Galarian Meowth": {
            "Name": "Meowth",
            "Type 1": "Steel",
            "Type 2": None,
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
            "Name": "Persian",
            "Type 1": "Normal",
            "Type 2": None,
            StatsEnum.HP: 65,
            StatsEnum.ATTACK: 70,
            StatsEnum.DEFENSE: 60,
            StatsEnum.SPECIAL_ATTACK: 65,
            StatsEnum.SPECIAL_DEFENSE: 65,
            StatsEnum.SPEED: 115
        },
        "Alolan Persian": {
            "Name": "Persian",
            "Type 1": "Dark",
            "Type 2": None,
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
            "Name": "Psyduck",
            "Type 1": "Water",
            "Type 2": None,
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
            "Name": "Golduck",
            "Type 1": "Water",
            "Type 2": None,
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
            "Name": "Mankey",
            "Type 1": "Fighting",
            "Type 2": None,
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
            "Name": "Primeape",
            "Type 1": "Fighting",
            "Type 2": None,
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
            "Name": "Growlithe",
            "Type 1": "Fire",
            "Type 2": None,
            StatsEnum.HP: 55,
            StatsEnum.ATTACK: 70,
            StatsEnum.DEFENSE: 45,
            StatsEnum.SPECIAL_ATTACK: 70,
            StatsEnum.SPECIAL_DEFENSE: 50,
            StatsEnum.SPEED: 60
        },
        "Hisuian Growlithe": {
            "Name": "Growlithe",
            "Type 1": "Fire",
            "Type 2": "Rock",
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
            "Name": "Arcanine",
            "Type 1": "Fire",
            "Type 2": None,
            StatsEnum.HP: 90,
            StatsEnum.ATTACK: 110,
            StatsEnum.DEFENSE: 80,
            StatsEnum.SPECIAL_ATTACK: 100,
            StatsEnum.SPECIAL_DEFENSE: 80,
            StatsEnum.SPEED: 95
        },
        "Hisuian Arcanine": {
            "Name": "Arcanine",
            "Type 1": "Fire",
            "Type 2": "Rock",
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
            "Name": "Poliwag",
            "Type 1": "Water",
            "Type 2": None,
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
            "Name": "Poliwhirl",
            "Type 1": "Water",
            "Type 2": None,
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
            "Name": "Poliwrath",
            "Type 1": "Water",
            "Type 2": "Fighting",
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
            "Name": "Abra",
            "Type 1": "Psychic",
            "Type 2": None,
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
            "Name": "Kadabra",
            "Type 1": "Psychic",
            "Type 2": None,
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
            "Name": "Alakazam",
            "Type 1": "Psychic",
            "Type 2": None,
            StatsEnum.HP: 55,
            StatsEnum.ATTACK: 50,
            StatsEnum.DEFENSE: 45,
            StatsEnum.SPECIAL_ATTACK: 135,
            StatsEnum.SPECIAL_DEFENSE: 95,
            StatsEnum.SPEED: 120
        },
        "Mega Alakazam": {
            "Name": "Alakazam",
            "Type 1": "Psychic",
            "Type 2": None,
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
            "Name": "Machop",
            "Type 1": "Fighting",
            "Type 2": None,
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
            "Name": "Machoke",
            "Type 1": "Fighting",
            "Type 2": None,
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
            "Name": "Machamp",
            "Type 1": "Fighting",
            "Type 2": None,
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
            "Name": "Bellsprout",
            "Type 1": "Grass",
            "Type 2": "Poison",
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
            "Name": "Weepinbell",
            "Type 1": "Grass",
            "Type 2": "Poison",
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
            "Name": "Victreebel",
            "Type 1": "Grass",
            "Type 2": "Poison",
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
            "Name": "Tentacool",
            "Type 1": "Water",
            "Type 2": "Poison",
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
            "Name": "Tentacruel",
            "Type 1": "Water",
            "Type 2": "Poison",
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
            "Name": "Geodude",
            "Type 1": "Rock",
            "Type 2": "Ground",
            StatsEnum.HP: 40,
            StatsEnum.ATTACK: 80,
            StatsEnum.DEFENSE: 100,
            StatsEnum.SPECIAL_ATTACK: 30,
            StatsEnum.SPECIAL_DEFENSE: 30,
            StatsEnum.SPEED: 20
        },
        "Alolan Geodude": {
            "Name": "Geodude",
            "Type 1": "Rock",
            "Type 2": "Electric",
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
            "Name": "Graveler",
            "Type 1": "Rock",
            "Type 2": "Ground",
            StatsEnum.HP: 55,
            StatsEnum.ATTACK: 95,
            StatsEnum.DEFENSE: 115,
            StatsEnum.SPECIAL_ATTACK: 45,
            StatsEnum.SPECIAL_DEFENSE: 45,
            StatsEnum.SPEED: 35
        },
        "Alolan Graveler": {
            "Name": "Graveler",
            "Type 1": "Rock",
            "Type 2": "Electric",
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
            "Name": "Golem",
            "Type 1": "Rock",
            "Type 2": "Ground",
            StatsEnum.HP: 80,
            StatsEnum.ATTACK: 120,
            StatsEnum.DEFENSE: 130,
            StatsEnum.SPECIAL_ATTACK: 55,
            StatsEnum.SPECIAL_DEFENSE: 65,
            StatsEnum.SPEED: 45
        },
        "Alolan Golem": {
            "Name": "Golem",
            "Type 1": "Rock",
            "Type 2": "Electric",
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
            "Name": "Ponyta",
            "Type 1": "Fire",
            "Type 2": None,
            StatsEnum.HP: 50,
            StatsEnum.ATTACK: 85,
            StatsEnum.DEFENSE: 55,
            StatsEnum.SPECIAL_ATTACK: 65,
            StatsEnum.SPECIAL_DEFENSE: 65,
            StatsEnum.SPEED: 90
        },
        "Galarian Ponyta": {
            "Name": "Ponyta",
            "Type 1": "Psychic",
            "Type 2": None,
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
            "Name": "Rapidash",
            "Type 1": "Fire",
            "Type 2": None,
            StatsEnum.HP: 65,
            StatsEnum.ATTACK: 100,
            StatsEnum.DEFENSE: 70,
            StatsEnum.SPECIAL_ATTACK: 80,
            StatsEnum.SPECIAL_DEFENSE: 80,
            StatsEnum.SPEED: 105
        },
        "Galarian Rapidash": {
            "Name": "Rapidash",
            "Type 1": "Psychic",
            "Type 2": "Fairy",
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
            "Name": "Slowpoke",
            "Type 1": "Water",
            "Type 2": "Psychic",
            StatsEnum.HP: 90,
            StatsEnum.ATTACK: 65,
            StatsEnum.DEFENSE: 65,
            StatsEnum.SPECIAL_ATTACK: 40,
            StatsEnum.SPECIAL_DEFENSE: 40,
            StatsEnum.SPEED: 15
        },
        "Galarian Slowpoke": {
            "Name": "Slowpoke",
            "Type 1": "Psychic",
            "Type 2": None,
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
            "Name": "Slowbro",
            "Type 1": "Water",
            "Type 2": "Psychic",
            StatsEnum.HP: 95,
            StatsEnum.ATTACK: 75,
            StatsEnum.DEFENSE: 110,
            StatsEnum.SPECIAL_ATTACK: 100,
            StatsEnum.SPECIAL_DEFENSE: 80,
            StatsEnum.SPEED: 30
        },
        "Mega Slowbro": {
            "Name": "Slowbro",
            "Type 1": "Water",
            "Type 2": "Psychic",
            StatsEnum.HP: 95,
            StatsEnum.ATTACK: 75,
            StatsEnum.DEFENSE: 180,
            StatsEnum.SPECIAL_ATTACK: 130,
            StatsEnum.SPECIAL_DEFENSE: 80,
            StatsEnum.SPEED: 30
        },
        "Galarian Slowbro": {
            "Name": "Slowbro",
            "Type 1": "Poison",
            "Type 2": "Psychic",
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
            "Name": "Magnemite",
            "Type 1": "Electric",
            "Type 2": "Steel",
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
            "Name": "Magneton",
            "Type 1": "Electric",
            "Type 2": "Steel",
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
            "Name": "Farfetch'd",
            "Type 1": "Normal",
            "Type 2": "Flying",
            StatsEnum.HP: 52,
            StatsEnum.ATTACK: 90,
            StatsEnum.DEFENSE: 55,
            StatsEnum.SPECIAL_ATTACK: 58,
            StatsEnum.SPECIAL_DEFENSE: 62,
            StatsEnum.SPEED: 60
        },
        "Galarian Farfetch'd": {
            "Name": "Farfetch'd",
            "Type 1": "Fighting",
            "Type 2": None,
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
            "Name": "Doduo",
            "Type 1": "Normal",
            "Type 2": "Flying",
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
            "Name": "Dodrio",
            "Type 1": "Normal",
            "Type 2": "Flying",
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
            "Name": "Seel",
            "Type 1": "Water",
            "Type 2": None,
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
            "Name": "Dewgong",
            "Type 1": "Water",
            "Type 2": "Ice",
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
            "Name": "Grimer",
            "Type 1": "Poison",
            "Type 2": None,
            StatsEnum.HP: 80,
            StatsEnum.ATTACK: 80,
            StatsEnum.DEFENSE: 50,
            StatsEnum.SPECIAL_ATTACK: 40,
            StatsEnum.SPECIAL_DEFENSE: 50,
            StatsEnum.SPEED: 25
        },
        "Alolan Grimer": {
            "Name": "Grimer",
            "Type 1": "Poison",
            "Type 2": "Dark",
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
            "Name": "Muk",
            "Type 1": "Poison",
            "Type 2": None,
            StatsEnum.HP: 105,
            StatsEnum.ATTACK: 105,
            StatsEnum.DEFENSE: 75,
            StatsEnum.SPECIAL_ATTACK: 65,
            StatsEnum.SPECIAL_DEFENSE: 100,
            StatsEnum.SPEED: 50
        },
        "Alolan Muk": {
            "Name": "Muk",
            "Type 1": "Poison",
            "Type 2": "Dark",
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
            "Name": "Shellder",
            "Type 1": "Water",
            "Type 2": None,
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
            "Name": "Cloyster",
            "Type 1": "Water",
            "Type 2": "Ice",
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
            "Name": "Gastly",
            "Type 1": "Ghost",
            "Type 2": "Poison",
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
            "Name": "Haunter",
            "Type 1": "Ghost",
            "Type 2": "Poison",
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
            "Name": "Gengar",
            "Type 1": "Ghost",
            "Type 2": "Poison",
            StatsEnum.HP: 60,
            StatsEnum.ATTACK: 65,
            StatsEnum.DEFENSE: 60,
            StatsEnum.SPECIAL_ATTACK: 130,
            StatsEnum.SPECIAL_DEFENSE: 75,
            StatsEnum.SPEED: 110
        },
        "Mega Gengar": {
            "Name": "Gengar",
            "Type 1": "Ghost",
            "Type 2": "Poison",
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
            "Name": "Onix",
            "Type 1": "Rock",
            "Type 2": "Ground",
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
            "Name": "Drowzee",
            "Type 1": "Psychic",
            "Type 2": None,
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
            "Name": "Hypno",
            "Type 1": "Psychic",
            "Type 2": None,
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
            "Name": "Krabby",
            "Type 1": "Water",
            "Type 2": None,
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
            "Name": "Kingler",
            "Type 1": "Water",
            "Type 2": None,
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
            "Name": "Voltorb",
            "Type 1": "Electric",
            "Type 2": None,
            StatsEnum.HP: 40,
            StatsEnum.ATTACK: 30,
            StatsEnum.DEFENSE: 50,
            StatsEnum.SPECIAL_ATTACK: 55,
            StatsEnum.SPECIAL_DEFENSE: 55,
            StatsEnum.SPEED: 100
        },
        "Hisuian Voltorb": {
            "Name": "Voltorb",
            "Type 1": "Electric",
            "Type 2": "Grass",
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
            "Name": "Electrode",
            "Type 1": "Electric",
            "Type 2": None,
            StatsEnum.HP: 60,
            StatsEnum.ATTACK: 50,
            StatsEnum.DEFENSE: 70,
            StatsEnum.SPECIAL_ATTACK: 80,
            StatsEnum.SPECIAL_DEFENSE: 80,
            StatsEnum.SPEED: 150
        },
        "Hisuian Electrode": {
            "Name": "Electrode",
            "Type 1": "Electric",
            "Type 2": "Grass",
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
            "Name": "Exeggcute",
            "Type 1": "Grass",
            "Type 2": "Psychic",
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
            "Name": "Exeggutor",
            "Type 1": "Grass",
            "Type 2": "Psychic",
            StatsEnum.HP: 95,
            StatsEnum.ATTACK: 95,
            StatsEnum.DEFENSE: 85,
            StatsEnum.SPECIAL_ATTACK: 125,
            StatsEnum.SPECIAL_DEFENSE: 75,
            StatsEnum.SPEED: 55
        },
        "Alolan Exeggutor": {
            "Name": "Exeggutor",
            "Type 1": "Grass",
            "Type 2": "Dragon",
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
            "Name": "Cubone",
            "Type 1": "Ground",
            "Type 2": None,
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
            "Name": "Marowak",
            "Type 1": "Ground",
            "Type 2": None,
            StatsEnum.HP: 60,
            StatsEnum.ATTACK: 80,
            StatsEnum.DEFENSE: 110,
            StatsEnum.SPECIAL_ATTACK: 50,
            StatsEnum.SPECIAL_DEFENSE: 80,
            StatsEnum.SPEED: 45
        },
        "Alolan Marowak": {
            "Name": "Marowak",
            "Type 1": "Fire",
            "Type 2": "Ghost",
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
            "Name": "Hitmonlee",
            "Type 1": "Fighting",
            "Type 2": None,
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
            "Name": "Hitmonchan",
            "Type 1": "Fighting",
            "Type 2": None,
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
            "Name": "Lickitung",
            "Type 1": "Normal",
            "Type 2": None,
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
            "Name": "Koffing",
            "Type 1": "Poison",
            "Type 2": None,
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
            "Name": "Weezing",
            "Type 1": "Poison",
            "Type 2": None,
            StatsEnum.HP: 65,
            StatsEnum.ATTACK: 90,
            StatsEnum.DEFENSE: 120,
            StatsEnum.SPECIAL_ATTACK: 85,
            StatsEnum.SPECIAL_DEFENSE: 70,
            StatsEnum.SPEED: 60
        },
        "Galarian Weezing": {
            "Name": "Weezing",
            "Type 1": "Poison",
            "Type 2": "Fairy",
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
            "Name": "Rhyhorn",
            "Type 1": "Ground",
            "Type 2": "Rock",
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
            "Name": "Rhydon",
            "Type 1": "Ground",
            "Type 2": "Rock",
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
            "Name": "Chansey",
            "Type 1": "Normal",
            "Type 2": None,
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
            "Name": "Tangela",
            "Type 1": "Grass",
            "Type 2": None,
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
            "Name": "Kangaskhan",
            "Type 1": "Normal",
            "Type 2": None,
            StatsEnum.HP: 105,
            StatsEnum.ATTACK: 95,
            StatsEnum.DEFENSE: 80,
            StatsEnum.SPECIAL_ATTACK: 40,
            StatsEnum.SPECIAL_DEFENSE: 80,
            StatsEnum.SPEED: 90
        },
        "Mega Kangaskhan": {
            "Name": "Kangaskhan",
            "Type 1": "Normal",
            "Type 2": None,
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
            "Name": "Horsea",
            "Type 1": "Water",
            "Type 2": None,
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
            "Name": "Seadra",
            "Type 1": "Water",
            "Type 2": None,
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
            "Name": "Goldeen",
            "Type 1": "Water",
            "Type 2": None,
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
            "Name": "Seaking",
            "Type 1": "Water",
            "Type 2": None,
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
            "Name": "Staryu",
            "Type 1": "Water",
            "Type 2": None,
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
            "Name": "Starmie",
            "Type 1": "Water",
            "Type 2": "Psychic",
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
            "Name": "Mr. Mime",
            "Type 1": "Psychic",
            "Type 2": "Fairy",
            StatsEnum.HP: 40,
            StatsEnum.ATTACK: 45,
            StatsEnum.DEFENSE: 65,
            StatsEnum.SPECIAL_ATTACK: 100,
            StatsEnum.SPECIAL_DEFENSE: 120,
            StatsEnum.SPEED: 90
        },
        "Galarian Mr. Mime": {
            "Name": "Mr. Mime",
            "Type 1": "Ice",
            "Type 2": "Psychic",
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
            "Name": "Scyther",
            "Type 1": "Bug",
            "Type 2": "Flying",
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
            "Name": "Jynx",
            "Type 1": "Ice",
            "Type 2": "Psychic",
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
            "Name": "Electabuzz",
            "Type 1": "Electric",
            "Type 2": None,
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
            "Name": "Magmar",
            "Type 1": "Fire",
            "Type 2": None,
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
            "Name": "Pinsir",
            "Type 1": "Bug",
            "Type 2": None,
            StatsEnum.HP: 65,
            StatsEnum.ATTACK: 125,
            StatsEnum.DEFENSE: 100,
            StatsEnum.SPECIAL_ATTACK: 55,
            StatsEnum.SPECIAL_DEFENSE: 70,
            StatsEnum.SPEED: 85
        },
        "Mega Pinsir": {
            "Name": "Pinsir",
            "Type 1": "Bug",
            "Type 2": "Flying",
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
            "Name": "Tauros",
            "Type 1": "Normal",
            "Type 2": None,
            StatsEnum.HP: 75,
            StatsEnum.ATTACK: 100,
            StatsEnum.DEFENSE: 95,
            StatsEnum.SPECIAL_ATTACK: 40,
            StatsEnum.SPECIAL_DEFENSE: 70,
            StatsEnum.SPEED: 110
        },
        "Combat Breed": {
            "Name": "Tauros",
            "Type 1": "Fighting",
            "Type 2": None,
            StatsEnum.HP: 75,
            StatsEnum.ATTACK: 110,
            StatsEnum.DEFENSE: 105,
            StatsEnum.SPECIAL_ATTACK: 30,
            StatsEnum.SPECIAL_DEFENSE: 70,
            StatsEnum.SPEED: 100
        },
        "Blaze Breed": {
            "Name": "Tauros",
            "Type 1": "Fighting",
            "Type 2": "Fire",
            StatsEnum.HP: 75,
            StatsEnum.ATTACK: 110,
            StatsEnum.DEFENSE: 105,
            StatsEnum.SPECIAL_ATTACK: 30,
            StatsEnum.SPECIAL_DEFENSE: 70,
            StatsEnum.SPEED: 100
        },
        "Aqua Breed": {
            "Name": "Tauros",
            "Type 1": "Fighting",
            "Type 2": "Water",
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
            "Name": "Magikarp",
            "Type 1": "Water",
            "Type 2": None,
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
            "Name": "Gyarados",
            "Type 1": "Water",
            "Type 2": "Flying",
            StatsEnum.HP: 95,
            StatsEnum.ATTACK: 125,
            StatsEnum.DEFENSE: 79,
            StatsEnum.SPECIAL_ATTACK: 60,
            StatsEnum.SPECIAL_DEFENSE: 100,
            StatsEnum.SPEED: 81
        },
        "Mega Gyarados": {
            "Name": "Gyarados",
            "Type 1": "Water",
            "Type 2": "Dark",
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
            "Name": "Lapras",
            "Type 1": "Water",
            "Type 2": "Ice",
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
            "Name": "Ditto",
            "Type 1": "Normal",
            "Type 2": None,
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
            "Name": "Eevee",
            "Type 1": "Normal",
            "Type 2": None,
            StatsEnum.HP: 55,
            StatsEnum.ATTACK: 55,
            StatsEnum.DEFENSE: 50,
            StatsEnum.SPECIAL_ATTACK: 45,
            StatsEnum.SPECIAL_DEFENSE: 65,
            StatsEnum.SPEED: 55
        },
        "Partner Eevee": {
            "Name": "Eevee",
            "Type 1": "Normal",
            "Type 2": None,
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
            "Name": "Vaporeon",
            "Type 1": "Water",
            "Type 2": None,
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
            "Name": "Jolteon",
            "Type 1": "Electric",
            "Type 2": None,
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
            "Name": "Flareon",
            "Type 1": "Fire",
            "Type 2": None,
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
            "Name": "Porygon",
            "Type 1": "Normal",
            "Type 2": None,
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
            "Name": "Omanyte",
            "Type 1": "Rock",
            "Type 2": "Water",
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
            "Name": "Omastar",
            "Type 1": "Rock",
            "Type 2": "Water",
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
            "Name": "Kabuto",
            "Type 1": "Rock",
            "Type 2": "Water",
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
            "Name": "Kabutops",
            "Type 1": "Rock",
            "Type 2": "Water",
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
            "Name": "Aerodactyl",
            "Type 1": "Rock",
            "Type 2": "Flying",
            StatsEnum.HP: 80,
            StatsEnum.ATTACK: 105,
            StatsEnum.DEFENSE: 65,
            StatsEnum.SPECIAL_ATTACK: 60,
            StatsEnum.SPECIAL_DEFENSE: 75,
            StatsEnum.SPEED: 130
        },
        "Mega Aerodactyl": {
            "Name": "Aerodactyl",
            "Type 1": "Rock",
            "Type 2": "Flying",
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
            "Name": "Snorlax",
            "Type 1": "Normal",
            "Type 2": None,
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
            "Name": "Articuno",
            "Type 1": "Ice",
            "Type 2": "Flying",
            StatsEnum.HP: 90,
            StatsEnum.ATTACK: 85,
            StatsEnum.DEFENSE: 100,
            StatsEnum.SPECIAL_ATTACK: 95,
            StatsEnum.SPECIAL_DEFENSE: 125,
            StatsEnum.SPEED: 85
        },
        "Galarian Articuno": {
            "Name": "Articuno",
            "Type 1": "Psychic",
            "Type 2": "Flying",
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
            "Name": "Zapdos",
            "Type 1": "Electric",
            "Type 2": "Flying",
            StatsEnum.HP: 90,
            StatsEnum.ATTACK: 90,
            StatsEnum.DEFENSE: 85,
            StatsEnum.SPECIAL_ATTACK: 125,
            StatsEnum.SPECIAL_DEFENSE: 90,
            StatsEnum.SPEED: 100
        },
        "Galarian Zapdos": {
            "Name": "Zapdos",
            "Type 1": "Fighting",
            "Type 2": "Flying",
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
            "Name": "Moltres",
            "Type 1": "Fire",
            "Type 2": "Flying",
            StatsEnum.HP: 90,
            StatsEnum.ATTACK: 100,
            StatsEnum.DEFENSE: 90,
            StatsEnum.SPECIAL_ATTACK: 125,
            StatsEnum.SPECIAL_DEFENSE: 85,
            StatsEnum.SPEED: 90
        },
        "Galarian Moltres": {
            "Name": "Moltres",
            "Type 1": "Dark",
            "Type 2": "Flying",
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
            "Name": "Dratini",
            "Type 1": "Dragon",
            "Type 2": None,
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
            "Name": "Dragonair",
            "Type 1": "Dragon",
            "Type 2": None,
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
            "Name": "Dragonite",
            "Type 1": "Dragon",
            "Type 2": "Flying",
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
            "Name": "Mewtwo",
            "Type 1": "Psychic",
            "Type 2": None,
            StatsEnum.HP: 106,
            StatsEnum.ATTACK: 110,
            StatsEnum.DEFENSE: 90,
            StatsEnum.SPECIAL_ATTACK: 154,
            StatsEnum.SPECIAL_DEFENSE: 90,
            StatsEnum.SPEED: 130
        },
        "Mega Mewtwo X": {
            "Name": "Mewtwo",
            "Type 1": "Psychic",
            "Type 2": "Fighting",
            StatsEnum.HP: 106,
            StatsEnum.ATTACK: 190,
            StatsEnum.DEFENSE: 100,
            StatsEnum.SPECIAL_ATTACK: 154,
            StatsEnum.SPECIAL_DEFENSE: 100,
            StatsEnum.SPEED: 130
        },
        "Mega Mewtwo Y": {
            "Name": "Mewtwo",
            "Type 1": "Psychic",
            "Type 2": None,
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
            "Name": "Mew",
            "Type 1": "Psychic",
            "Type 2": None,
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
            "Name": "Chikorita",
            "Type 1": "Grass",
            "Type 2": None,
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
            "Name": "Bayleef",
            "Type 1": "Grass",
            "Type 2": None,
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
            "Name": "Meganium",
            "Type 1": "Grass",
            "Type 2": None,
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
            "Name": "Cyndaquil",
            "Type 1": "Fire",
            "Type 2": None,
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
            "Name": "Quilava",
            "Type 1": "Fire",
            "Type 2": None,
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
            "Name": "Typhlosion",
            "Type 1": "Fire",
            "Type 2": None,
            StatsEnum.HP: 78,
            StatsEnum.ATTACK: 84,
            StatsEnum.DEFENSE: 78,
            StatsEnum.SPECIAL_ATTACK: 109,
            StatsEnum.SPECIAL_DEFENSE: 85,
            StatsEnum.SPEED: 100
        },
        "Hisuian Typhlosion": {
            "Name": "Typhlosion",
            "Type 1": "Fire",
            "Type 2": "Ghost",
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
            "Name": "Totodile",
            "Type 1": "Water",
            "Type 2": None,
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
            "Name": "Croconaw",
            "Type 1": "Water",
            "Type 2": None,
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
            "Name": "Feraligatr",
            "Type 1": "Water",
            "Type 2": None,
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
            "Name": "Sentret",
            "Type 1": "Normal",
            "Type 2": None,
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
            "Name": "Furret",
            "Type 1": "Normal",
            "Type 2": None,
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
            "Name": "Hoothoot",
            "Type 1": "Normal",
            "Type 2": "Flying",
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
            "Name": "Noctowl",
            "Type 1": "Normal",
            "Type 2": "Flying",
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
            "Name": "Ledyba",
            "Type 1": "Bug",
            "Type 2": "Flying",
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
            "Name": "Ledian",
            "Type 1": "Bug",
            "Type 2": "Flying",
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
            "Name": "Spinarak",
            "Type 1": "Bug",
            "Type 2": "Poison",
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
            "Name": "Ariados",
            "Type 1": "Bug",
            "Type 2": "Poison",
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
            "Name": "Crobat",
            "Type 1": "Poison",
            "Type 2": "Flying",
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
            "Name": "Chinchou",
            "Type 1": "Water",
            "Type 2": "Electric",
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
            "Name": "Lanturn",
            "Type 1": "Water",
            "Type 2": "Electric",
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
            "Name": "Pichu",
            "Type 1": "Electric",
            "Type 2": None,
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
            "Name": "Cleffa",
            "Type 1": "Fairy",
            "Type 2": None,
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
            "Name": "Igglybuff",
            "Type 1": "Normal",
            "Type 2": "Fairy",
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
            "Name": "Togepi",
            "Type 1": "Fairy",
            "Type 2": None,
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
            "Name": "Togetic",
            "Type 1": "Fairy",
            "Type 2": "Flying",
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
            "Name": "Natu",
            "Type 1": "Psychic",
            "Type 2": "Flying",
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
            "Name": "Xatu",
            "Type 1": "Psychic",
            "Type 2": "Flying",
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
            "Name": "Mareep",
            "Type 1": "Electric",
            "Type 2": None,
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
            "Name": "Flaaffy",
            "Type 1": "Electric",
            "Type 2": None,
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
            "Name": "Ampharos",
            "Type 1": "Electric",
            "Type 2": None,
            StatsEnum.HP: 90,
            StatsEnum.ATTACK: 75,
            StatsEnum.DEFENSE: 85,
            StatsEnum.SPECIAL_ATTACK: 115,
            StatsEnum.SPECIAL_DEFENSE: 90,
            StatsEnum.SPEED: 55
        },
        "Mega Ampharos": {
            "Name": "Ampharos",
            "Type 1": "Electric",
            "Type 2": "Dragon",
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
            "Name": "Bellossom",
            "Type 1": "Grass",
            "Type 2": None,
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
            "Name": "Marill",
            "Type 1": "Water",
            "Type 2": "Fairy",
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
            "Name": "Azumarill",
            "Type 1": "Water",
            "Type 2": "Fairy",
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
            "Name": "Sudowoodo",
            "Type 1": "Rock",
            "Type 2": None,
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
            "Name": "Politoed",
            "Type 1": "Water",
            "Type 2": None,
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
            "Name": "Hoppip",
            "Type 1": "Grass",
            "Type 2": "Flying",
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
            "Name": "Skiploom",
            "Type 1": "Grass",
            "Type 2": "Flying",
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
            "Name": "Jumpluff",
            "Type 1": "Grass",
            "Type 2": "Flying",
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
            "Name": "Aipom",
            "Type 1": "Normal",
            "Type 2": None,
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
            "Name": "Sunkern",
            "Type 1": "Grass",
            "Type 2": None,
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
            "Name": "Sunflora",
            "Type 1": "Grass",
            "Type 2": None,
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
            "Name": "Yanma",
            "Type 1": "Bug",
            "Type 2": "Flying",
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
            "Name": "Wooper",
            "Type 1": "Water",
            "Type 2": "Ground",
            StatsEnum.HP: 55,
            StatsEnum.ATTACK: 45,
            StatsEnum.DEFENSE: 45,
            StatsEnum.SPECIAL_ATTACK: 25,
            StatsEnum.SPECIAL_DEFENSE: 25,
            StatsEnum.SPEED: 15
        },
        "Paldean Wooper": {
            "Name": "Wooper",
            "Type 1": "Poison",
            "Type 2": "Ground",
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
            "Name": "Quagsire",
            "Type 1": "Water",
            "Type 2": "Ground",
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
            "Name": "Espeon",
            "Type 1": "Psychic",
            "Type 2": None,
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
            "Name": "Umbreon",
            "Type 1": "Dark",
            "Type 2": None,
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
            "Name": "Murkrow",
            "Type 1": "Dark",
            "Type 2": "Flying",
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
            "Name": "Slowking",
            "Type 1": "Water",
            "Type 2": "Psychic",
            StatsEnum.HP: 95,
            StatsEnum.ATTACK: 75,
            StatsEnum.DEFENSE: 80,
            StatsEnum.SPECIAL_ATTACK: 100,
            StatsEnum.SPECIAL_DEFENSE: 110,
            StatsEnum.SPEED: 30
        },
        "Galarian Slowking": {
            "Name": "Slowking",
            "Type 1": "Poison",
            "Type 2": "Psychic",
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
            "Name": "Misdreavus",
            "Type 1": "Ghost",
            "Type 2": None,
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
            "Name": "Unown",
            "Type 1": "Psychic",
            "Type 2": None,
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
            "Name": "Wobbuffet",
            "Type 1": "Psychic",
            "Type 2": None,
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
            "Name": "Girafarig",
            "Type 1": "Normal",
            "Type 2": "Psychic",
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
            "Name": "Pineco",
            "Type 1": "Bug",
            "Type 2": None,
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
            "Name": "Forretress",
            "Type 1": "Bug",
            "Type 2": "Steel",
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
            "Name": "Dunsparce",
            "Type 1": "Normal",
            "Type 2": None,
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
            "Name": "Gligar",
            "Type 1": "Ground",
            "Type 2": "Flying",
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
            "Name": "Steelix",
            "Type 1": "Steel",
            "Type 2": "Ground",
            StatsEnum.HP: 75,
            StatsEnum.ATTACK: 85,
            StatsEnum.DEFENSE: 200,
            StatsEnum.SPECIAL_ATTACK: 55,
            StatsEnum.SPECIAL_DEFENSE: 65,
            StatsEnum.SPEED: 30
        },
        "Mega Steelix": {
            "Name": "Steelix",
            "Type 1": "Steel",
            "Type 2": "Ground",
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
            "Name": "Snubbull",
            "Type 1": "Fairy",
            "Type 2": None,
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
            "Name": "Granbull",
            "Type 1": "Fairy",
            "Type 2": None,
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
            "Name": "Qwilfish",
            "Type 1": "Water",
            "Type 2": "Poison",
            StatsEnum.HP: 65,
            StatsEnum.ATTACK: 95,
            StatsEnum.DEFENSE: 85,
            StatsEnum.SPECIAL_ATTACK: 55,
            StatsEnum.SPECIAL_DEFENSE: 55,
            StatsEnum.SPEED: 85
        },
        "Hisuian Qwilfish": {
            "Name": "Qwilfish",
            "Type 1": "Dark",
            "Type 2": "Poison",
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
            "Name": "Scizor",
            "Type 1": "Bug",
            "Type 2": "Steel",
            StatsEnum.HP: 70,
            StatsEnum.ATTACK: 130,
            StatsEnum.DEFENSE: 100,
            StatsEnum.SPECIAL_ATTACK: 55,
            StatsEnum.SPECIAL_DEFENSE: 80,
            StatsEnum.SPEED: 65
        },
        "Mega Scizor": {
            "Name": "Scizor",
            "Type 1": "Bug",
            "Type 2": "Steel",
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
            "Name": "Shuckle",
            "Type 1": "Bug",
            "Type 2": "Rock",
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
            "Name": "Heracross",
            "Type 1": "Bug",
            "Type 2": "Fighting",
            StatsEnum.HP: 80,
            StatsEnum.ATTACK: 125,
            StatsEnum.DEFENSE: 75,
            StatsEnum.SPECIAL_ATTACK: 40,
            StatsEnum.SPECIAL_DEFENSE: 95,
            StatsEnum.SPEED: 85
        },
        "Mega Heracross": {
            "Name": "Heracross",
            "Type 1": "Bug",
            "Type 2": "Fighting",
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
            "Name": "Sneasel",
            "Type 1": "Dark",
            "Type 2": "Ice",
            StatsEnum.HP: 55,
            StatsEnum.ATTACK: 95,
            StatsEnum.DEFENSE: 55,
            StatsEnum.SPECIAL_ATTACK: 35,
            StatsEnum.SPECIAL_DEFENSE: 75,
            StatsEnum.SPEED: 115
        },
        "Hisuian Sneasel": {
            "Name": "Sneasel",
            "Type 1": "Fighting",
            "Type 2": "Poison",
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
            "Name": "Teddiursa",
            "Type 1": "Normal",
            "Type 2": None,
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
            "Name": "Ursaring",
            "Type 1": "Normal",
            "Type 2": None,
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
            "Name": "Slugma",
            "Type 1": "Fire",
            "Type 2": None,
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
            "Name": "Magcargo",
            "Type 1": "Fire",
            "Type 2": "Rock",
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
            "Name": "Swinub",
            "Type 1": "Ice",
            "Type 2": "Ground",
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
            "Name": "Piloswine",
            "Type 1": "Ice",
            "Type 2": "Ground",
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
            "Name": "Corsola",
            "Type 1": "Water",
            "Type 2": "Rock",
            StatsEnum.HP: 65,
            StatsEnum.ATTACK: 55,
            StatsEnum.DEFENSE: 95,
            StatsEnum.SPECIAL_ATTACK: 65,
            StatsEnum.SPECIAL_DEFENSE: 95,
            StatsEnum.SPEED: 35
        },
        "Galarian Corsola": {
            "Name": "Corsola",
            "Type 1": "Ghost",
            "Type 2": None,
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
            "Name": "Remoraid",
            "Type 1": "Water",
            "Type 2": None,
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
            "Name": "Octillery",
            "Type 1": "Water",
            "Type 2": None,
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
            "Name": "Delibird",
            "Type 1": "Ice",
            "Type 2": "Flying",
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
            "Name": "Mantine",
            "Type 1": "Water",
            "Type 2": "Flying",
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
            "Name": "Skarmory",
            "Type 1": "Steel",
            "Type 2": "Flying",
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
            "Name": "Houndour",
            "Type 1": "Dark",
            "Type 2": "Fire",
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
            "Name": "Houndoom",
            "Type 1": "Dark",
            "Type 2": "Fire",
            StatsEnum.HP: 75,
            StatsEnum.ATTACK: 90,
            StatsEnum.DEFENSE: 50,
            StatsEnum.SPECIAL_ATTACK: 110,
            StatsEnum.SPECIAL_DEFENSE: 80,
            StatsEnum.SPEED: 95
        },
        "Mega Houndoom": {
            "Name": "Houndoom",
            "Type 1": "Dark",
            "Type 2": "Fire",
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
            "Name": "Kingdra",
            "Type 1": "Water",
            "Type 2": "Dragon",
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
            "Name": "Phanpy",
            "Type 1": "Ground",
            "Type 2": None,
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
            "Name": "Donphan",
            "Type 1": "Ground",
            "Type 2": None,
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
            "Name": "Porygon2",
            "Type 1": "Normal",
            "Type 2": None,
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
            "Name": "Stantler",
            "Type 1": "Normal",
            "Type 2": None,
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
            "Name": "Smeargle",
            "Type 1": "Normal",
            "Type 2": None,
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
            "Name": "Tyrogue",
            "Type 1": "Fighting",
            "Type 2": None,
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
            "Name": "Hitmontop",
            "Type 1": "Fighting",
            "Type 2": None,
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
            "Name": "Smoochum",
            "Type 1": "Ice",
            "Type 2": "Psychic",
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
            "Name": "Elekid",
            "Type 1": "Electric",
            "Type 2": None,
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
            "Name": "Magby",
            "Type 1": "Fire",
            "Type 2": None,
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
            "Name": "Miltank",
            "Type 1": "Normal",
            "Type 2": None,
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
            "Name": "Blissey",
            "Type 1": "Normal",
            "Type 2": None,
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
            "Name": "Raikou",
            "Type 1": "Electric",
            "Type 2": None,
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
            "Name": "Entei",
            "Type 1": "Fire",
            "Type 2": None,
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
            "Name": "Suicune",
            "Type 1": "Water",
            "Type 2": None,
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
            "Name": "Larvitar",
            "Type 1": "Rock",
            "Type 2": "Ground",
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
            "Name": "Pupitar",
            "Type 1": "Rock",
            "Type 2": "Ground",
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
            "Name": "Tyranitar",
            "Type 1": "Rock",
            "Type 2": "Dark",
            StatsEnum.HP: 100,
            StatsEnum.ATTACK: 134,
            StatsEnum.DEFENSE: 110,
            StatsEnum.SPECIAL_ATTACK: 95,
            StatsEnum.SPECIAL_DEFENSE: 100,
            StatsEnum.SPEED: 61
        },
        "Mega Tyranitar": {
            "Name": "Tyranitar",
            "Type 1": "Rock",
            "Type 2": "Dark",
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
            "Name": "Lugia",
            "Type 1": "Psychic",
            "Type 2": "Flying",
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
            "Name": "Ho-oh",
            "Type 1": "Fire",
            "Type 2": "Flying",
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
            "Name": "Celebi",
            "Type 1": "Psychic",
            "Type 2": "Grass",
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
            "Name": "Treecko",
            "Type 1": "Grass",
            "Type 2": None,
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
            "Name": "Grovyle",
            "Type 1": "Grass",
            "Type 2": None,
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
            "Name": "Sceptile",
            "Type 1": "Grass",
            "Type 2": None,
            StatsEnum.HP: 70,
            StatsEnum.ATTACK: 85,
            StatsEnum.DEFENSE: 65,
            StatsEnum.SPECIAL_ATTACK: 105,
            StatsEnum.SPECIAL_DEFENSE: 85,
            StatsEnum.SPEED: 120
        },
        "Mega Sceptile": {
            "Name": "Sceptile",
            "Type 1": "Grass",
            "Type 2": "Dragon",
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
            "Name": "Torchic",
            "Type 1": "Fire",
            "Type 2": None,
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
            "Name": "Combusken",
            "Type 1": "Fire",
            "Type 2": "Fighting",
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
            "Name": "Blaziken",
            "Type 1": "Fire",
            "Type 2": "Fighting",
            StatsEnum.HP: 80,
            StatsEnum.ATTACK: 120,
            StatsEnum.DEFENSE: 70,
            StatsEnum.SPECIAL_ATTACK: 110,
            StatsEnum.SPECIAL_DEFENSE: 70,
            StatsEnum.SPEED: 80
        },
        "Mega Blaziken": {
            "Name": "Blaziken",
            "Type 1": "Fire",
            "Type 2": "Fighting",
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
            "Name": "Mudkip",
            "Type 1": "Water",
            "Type 2": None,
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
            "Name": "Marshtomp",
            "Type 1": "Water",
            "Type 2": "Ground",
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
            "Name": "Swampert",
            "Type 1": "Water",
            "Type 2": "Ground",
            StatsEnum.HP: 100,
            StatsEnum.ATTACK: 110,
            StatsEnum.DEFENSE: 90,
            StatsEnum.SPECIAL_ATTACK: 85,
            StatsEnum.SPECIAL_DEFENSE: 90,
            StatsEnum.SPEED: 60
        },
        "Mega Swampert": {
            "Name": "Swampert",
            "Type 1": "Water",
            "Type 2": "Ground",
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
            "Name": "Poochyena",
            "Type 1": "Dark",
            "Type 2": None,
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
            "Name": "Mightyena",
            "Type 1": "Dark",
            "Type 2": None,
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
            "Name": "Zigzagoon",
            "Type 1": "Normal",
            "Type 2": None,
            StatsEnum.HP: 38,
            StatsEnum.ATTACK: 30,
            StatsEnum.DEFENSE: 41,
            StatsEnum.SPECIAL_ATTACK: 30,
            StatsEnum.SPECIAL_DEFENSE: 41,
            StatsEnum.SPEED: 60
        },
        "Galarian Zigzagoon": {
            "Name": "Zigzagoon",
            "Type 1": "Dark",
            "Type 2": "Normal",
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
            "Name": "Linoone",
            "Type 1": "Normal",
            "Type 2": None,
            StatsEnum.HP: 78,
            StatsEnum.ATTACK: 70,
            StatsEnum.DEFENSE: 61,
            StatsEnum.SPECIAL_ATTACK: 50,
            StatsEnum.SPECIAL_DEFENSE: 61,
            StatsEnum.SPEED: 100
        },
        "Galarian Linoone": {
            "Name": "Linoone",
            "Type 1": "Dark",
            "Type 2": "Normal",
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
            "Name": "Wurmple",
            "Type 1": "Bug",
            "Type 2": None,
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
            "Name": "Silcoon",
            "Type 1": "Bug",
            "Type 2": None,
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
            "Name": "Beautifly",
            "Type 1": "Bug",
            "Type 2": "Flying",
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
            "Name": "Cascoon",
            "Type 1": "Bug",
            "Type 2": None,
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
            "Name": "Dustox",
            "Type 1": "Bug",
            "Type 2": "Poison",
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
            "Name": "Lotad",
            "Type 1": "Water",
            "Type 2": "Grass",
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
            "Name": "Lombre",
            "Type 1": "Water",
            "Type 2": "Grass",
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
            "Name": "Ludicolo",
            "Type 1": "Water",
            "Type 2": "Grass",
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
            "Name": "Seedot",
            "Type 1": "Grass",
            "Type 2": None,
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
            "Name": "Nuzleaf",
            "Type 1": "Grass",
            "Type 2": "Dark",
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
            "Name": "Shiftry",
            "Type 1": "Grass",
            "Type 2": "Dark",
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
            "Name": "Taillow",
            "Type 1": "Normal",
            "Type 2": "Flying",
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
            "Name": "Swellow",
            "Type 1": "Normal",
            "Type 2": "Flying",
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
            "Name": "Wingull",
            "Type 1": "Water",
            "Type 2": "Flying",
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
            "Name": "Pelipper",
            "Type 1": "Water",
            "Type 2": "Flying",
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
            "Name": "Ralts",
            "Type 1": "Psychic",
            "Type 2": "Fairy",
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
            "Name": "Kirlia",
            "Type 1": "Psychic",
            "Type 2": "Fairy",
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
            "Name": "Gardevoir",
            "Type 1": "Psychic",
            "Type 2": "Fairy",
            StatsEnum.HP: 68,
            StatsEnum.ATTACK: 65,
            StatsEnum.DEFENSE: 65,
            StatsEnum.SPECIAL_ATTACK: 125,
            StatsEnum.SPECIAL_DEFENSE: 115,
            StatsEnum.SPEED: 80
        },
        "Mega Gardevoir": {
            "Name": "Gardevoir",
            "Type 1": "Psychic",
            "Type 2": "Fairy",
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
            "Name": "Surskit",
            "Type 1": "Bug",
            "Type 2": "Water",
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
            "Name": "Masquerain",
            "Type 1": "Bug",
            "Type 2": "Flying",
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
            "Name": "Shroomish",
            "Type 1": "Grass",
            "Type 2": None,
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
            "Name": "Breloom",
            "Type 1": "Grass",
            "Type 2": "Fighting",
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
            "Name": "Slakoth",
            "Type 1": "Normal",
            "Type 2": None,
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
            "Name": "Vigoroth",
            "Type 1": "Normal",
            "Type 2": None,
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
            "Name": "Slaking",
            "Type 1": "Normal",
            "Type 2": None,
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
            "Name": "Nincada",
            "Type 1": "Bug",
            "Type 2": "Ground",
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
            "Name": "Ninjask",
            "Type 1": "Bug",
            "Type 2": "Flying",
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
            "Name": "Shedinja",
            "Type 1": "Bug",
            "Type 2": "Ghost",
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
            "Name": "Whismur",
            "Type 1": "Normal",
            "Type 2": None,
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
            "Name": "Loudred",
            "Type 1": "Normal",
            "Type 2": None,
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
            "Name": "Exploud",
            "Type 1": "Normal",
            "Type 2": None,
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
            "Name": "Makuhita",
            "Type 1": "Fighting",
            "Type 2": None,
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
            "Name": "Hariyama",
            "Type 1": "Fighting",
            "Type 2": None,
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
            "Name": "Azurill",
            "Type 1": "Normal",
            "Type 2": "Fairy",
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
            "Name": "Nosepass",
            "Type 1": "Rock",
            "Type 2": None,
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
            "Name": "Skitty",
            "Type 1": "Normal",
            "Type 2": None,
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
            "Name": "Delcatty",
            "Type 1": "Normal",
            "Type 2": None,
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
            "Name": "Sableye",
            "Type 1": "Dark",
            "Type 2": "Ghost",
            StatsEnum.HP: 50,
            StatsEnum.ATTACK: 75,
            StatsEnum.DEFENSE: 75,
            StatsEnum.SPECIAL_ATTACK: 65,
            StatsEnum.SPECIAL_DEFENSE: 65,
            StatsEnum.SPEED: 50
        },
        "Mega Sableye": {
            "Name": "Sableye",
            "Type 1": "Dark",
            "Type 2": "Ghost",
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
            "Name": "Mawile",
            "Type 1": "Steel",
            "Type 2": "Fairy",
            StatsEnum.HP: 50,
            StatsEnum.ATTACK: 85,
            StatsEnum.DEFENSE: 85,
            StatsEnum.SPECIAL_ATTACK: 55,
            StatsEnum.SPECIAL_DEFENSE: 55,
            StatsEnum.SPEED: 50
        },
        "Mega Mawile": {
            "Name": "Mawile",
            "Type 1": "Steel",
            "Type 2": "Fairy",
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
            "Name": "Aron",
            "Type 1": "Steel",
            "Type 2": "Rock",
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
            "Name": "Lairon",
            "Type 1": "Steel",
            "Type 2": "Rock",
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
            "Name": "Aggron",
            "Type 1": "Steel",
            "Type 2": "Rock",
            StatsEnum.HP: 70,
            StatsEnum.ATTACK: 110,
            StatsEnum.DEFENSE: 180,
            StatsEnum.SPECIAL_ATTACK: 60,
            StatsEnum.SPECIAL_DEFENSE: 60,
            StatsEnum.SPEED: 50
        },
        "Mega Aggron": {
            "Name": "Aggron",
            "Type 1": "Steel",
            "Type 2": None,
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
            "Name": "Meditite",
            "Type 1": "Fighting",
            "Type 2": "Psychic",
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
            "Name": "Medicham",
            "Type 1": "Fighting",
            "Type 2": "Psychic",
            StatsEnum.HP: 60,
            StatsEnum.ATTACK: 60,
            StatsEnum.DEFENSE: 75,
            StatsEnum.SPECIAL_ATTACK: 60,
            StatsEnum.SPECIAL_DEFENSE: 75,
            StatsEnum.SPEED: 80
        },
        "Mega Medicham": {
            "Name": "Medicham",
            "Type 1": "Fighting",
            "Type 2": "Psychic",
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
            "Name": "Electrike",
            "Type 1": "Electric",
            "Type 2": None,
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
            "Name": "Manectric",
            "Type 1": "Electric",
            "Type 2": None,
            StatsEnum.HP: 70,
            StatsEnum.ATTACK: 75,
            StatsEnum.DEFENSE: 60,
            StatsEnum.SPECIAL_ATTACK: 105,
            StatsEnum.SPECIAL_DEFENSE: 60,
            StatsEnum.SPEED: 105
        },
        "Mega Manectric": {
            "Name": "Manectric",
            "Type 1": "Electric",
            "Type 2": None,
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
            "Name": "Plusle",
            "Type 1": "Electric",
            "Type 2": None,
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
            "Name": "Minun",
            "Type 1": "Electric",
            "Type 2": None,
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
            "Name": "Volbeat",
            "Type 1": "Bug",
            "Type 2": None,
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
            "Name": "Illumise",
            "Type 1": "Bug",
            "Type 2": None,
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
            "Name": "Roselia",
            "Type 1": "Grass",
            "Type 2": "Poison",
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
            "Name": "Gulpin",
            "Type 1": "Poison",
            "Type 2": None,
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
            "Name": "Swalot",
            "Type 1": "Poison",
            "Type 2": None,
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
            "Name": "Carvanha",
            "Type 1": "Water",
            "Type 2": "Dark",
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
            "Name": "Sharpedo",
            "Type 1": "Water",
            "Type 2": "Dark",
            StatsEnum.HP: 70,
            StatsEnum.ATTACK: 120,
            StatsEnum.DEFENSE: 40,
            StatsEnum.SPECIAL_ATTACK: 95,
            StatsEnum.SPECIAL_DEFENSE: 40,
            StatsEnum.SPEED: 95
        },
        "Mega Sharpedo": {
            "Name": "Sharpedo",
            "Type 1": "Water",
            "Type 2": "Dark",
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
            "Name": "Wailmer",
            "Type 1": "Water",
            "Type 2": None,
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
            "Name": "Wailord",
            "Type 1": "Water",
            "Type 2": None,
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
            "Name": "Numel",
            "Type 1": "Fire",
            "Type 2": "Ground",
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
            "Name": "Camerupt",
            "Type 1": "Fire",
            "Type 2": "Ground",
            StatsEnum.HP: 70,
            StatsEnum.ATTACK: 100,
            StatsEnum.DEFENSE: 70,
            StatsEnum.SPECIAL_ATTACK: 105,
            StatsEnum.SPECIAL_DEFENSE: 75,
            StatsEnum.SPEED: 40
        },
        "Mega Camerupt": {
            "Name": "Camerupt",
            "Type 1": "Fire",
            "Type 2": "Ground",
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
            "Name": "Torkoal",
            "Type 1": "Fire",
            "Type 2": None,
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
            "Name": "Spoink",
            "Type 1": "Psychic",
            "Type 2": None,
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
            "Name": "Grumpig",
            "Type 1": "Psychic",
            "Type 2": None,
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
            "Name": "Spinda",
            "Type 1": "Normal",
            "Type 2": None,
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
            "Name": "Trapinch",
            "Type 1": "Ground",
            "Type 2": None,
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
            "Name": "Vibrava",
            "Type 1": "Ground",
            "Type 2": "Dragon",
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
            "Name": "Flygon",
            "Type 1": "Ground",
            "Type 2": "Dragon",
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
            "Name": "Cacnea",
            "Type 1": "Grass",
            "Type 2": None,
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
            "Name": "Cacturne",
            "Type 1": "Grass",
            "Type 2": "Dark",
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
            "Name": "Swablu",
            "Type 1": "Normal",
            "Type 2": "Flying",
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
            "Name": "Altaria",
            "Type 1": "Dragon",
            "Type 2": "Flying",
            StatsEnum.HP: 75,
            StatsEnum.ATTACK: 70,
            StatsEnum.DEFENSE: 90,
            StatsEnum.SPECIAL_ATTACK: 70,
            StatsEnum.SPECIAL_DEFENSE: 105,
            StatsEnum.SPEED: 80
        },
        "Mega Altaria": {
            "Name": "Altaria",
            "Type 1": "Dragon",
            "Type 2": "Fairy",
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
            "Name": "Zangoose",
            "Type 1": "Normal",
            "Type 2": None,
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
            "Name": "Seviper",
            "Type 1": "Poison",
            "Type 2": None,
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
            "Name": "Lunatone",
            "Type 1": "Rock",
            "Type 2": "Psychic",
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
            "Name": "Solrock",
            "Type 1": "Rock",
            "Type 2": "Psychic",
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
            "Name": "Barboach",
            "Type 1": "Water",
            "Type 2": "Ground",
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
            "Name": "Whiscash",
            "Type 1": "Water",
            "Type 2": "Ground",
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
            "Name": "Corphish",
            "Type 1": "Water",
            "Type 2": None,
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
            "Name": "Crawdaunt",
            "Type 1": "Water",
            "Type 2": "Dark",
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
            "Name": "Baltoy",
            "Type 1": "Ground",
            "Type 2": "Psychic",
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
            "Name": "Claydol",
            "Type 1": "Ground",
            "Type 2": "Psychic",
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
            "Name": "Lileep",
            "Type 1": "Rock",
            "Type 2": "Grass",
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
            "Name": "Cradily",
            "Type 1": "Rock",
            "Type 2": "Grass",
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
            "Name": "Anorith",
            "Type 1": "Rock",
            "Type 2": "Bug",
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
            "Name": "Armaldo",
            "Type 1": "Rock",
            "Type 2": "Bug",
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
            "Name": "Feebas",
            "Type 1": "Water",
            "Type 2": None,
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
            "Name": "Milotic",
            "Type 1": "Water",
            "Type 2": None,
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
            "Name": "Castform",
            "Type 1": "Normal",
            "Type 2": None,
            StatsEnum.HP: 70,
            StatsEnum.ATTACK: 70,
            StatsEnum.DEFENSE: 70,
            StatsEnum.SPECIAL_ATTACK: 70,
            StatsEnum.SPECIAL_DEFENSE: 70,
            StatsEnum.SPEED: 70
        },
        "Sunny Form": {
            "Name": "Castform",
            "Type 1": "Fire",
            "Type 2": None,
            StatsEnum.HP: 70,
            StatsEnum.ATTACK: 70,
            StatsEnum.DEFENSE: 70,
            StatsEnum.SPECIAL_ATTACK: 70,
            StatsEnum.SPECIAL_DEFENSE: 70,
            StatsEnum.SPEED: 70
        },
        "Rainy Form": {
            "Name": "Castform",
            "Type 1": "Water",
            "Type 2": None,
            StatsEnum.HP: 70,
            StatsEnum.ATTACK: 70,
            StatsEnum.DEFENSE: 70,
            StatsEnum.SPECIAL_ATTACK: 70,
            StatsEnum.SPECIAL_DEFENSE: 70,
            StatsEnum.SPEED: 70
        },
        "Snowy Form": {
            "Name": "Castform",
            "Type 1": "Ice",
            "Type 2": None,
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
            "Name": "Kecleon",
            "Type 1": "Normal",
            "Type 2": None,
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
            "Name": "Shuppet",
            "Type 1": "Ghost",
            "Type 2": None,
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
            "Name": "Banette",
            "Type 1": "Ghost",
            "Type 2": None,
            StatsEnum.HP: 64,
            StatsEnum.ATTACK: 115,
            StatsEnum.DEFENSE: 65,
            StatsEnum.SPECIAL_ATTACK: 83,
            StatsEnum.SPECIAL_DEFENSE: 63,
            StatsEnum.SPEED: 65
        },
        "Mega Banette": {
            "Name": "Banette",
            "Type 1": "Ghost",
            "Type 2": None,
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
            "Name": "Duskull",
            "Type 1": "Ghost",
            "Type 2": None,
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
            "Name": "Dusclops",
            "Type 1": "Ghost",
            "Type 2": None,
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
            "Name": "Tropius",
            "Type 1": "Grass",
            "Type 2": "Flying",
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
            "Name": "Chimecho",
            "Type 1": "Psychic",
            "Type 2": None,
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
            "Name": "Absol",
            "Type 1": "Dark",
            "Type 2": None,
            StatsEnum.HP: 65,
            StatsEnum.ATTACK: 130,
            StatsEnum.DEFENSE: 60,
            StatsEnum.SPECIAL_ATTACK: 75,
            StatsEnum.SPECIAL_DEFENSE: 60,
            StatsEnum.SPEED: 75
        },
        "Mega Absol": {
            "Name": "Absol",
            "Type 1": "Dark",
            "Type 2": None,
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
            "Name": "Wynaut",
            "Type 1": "Psychic",
            "Type 2": None,
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
            "Name": "Snorunt",
            "Type 1": "Ice",
            "Type 2": None,
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
            "Name": "Glalie",
            "Type 1": "Ice",
            "Type 2": None,
            StatsEnum.HP: 80,
            StatsEnum.ATTACK: 80,
            StatsEnum.DEFENSE: 80,
            StatsEnum.SPECIAL_ATTACK: 80,
            StatsEnum.SPECIAL_DEFENSE: 80,
            StatsEnum.SPEED: 80
        },
        "Mega Glalie": {
            "Name": "Glalie",
            "Type 1": "Ice",
            "Type 2": None,
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
            "Name": "Spheal",
            "Type 1": "Ice",
            "Type 2": "Water",
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
            "Name": "Sealeo",
            "Type 1": "Ice",
            "Type 2": "Water",
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
            "Name": "Walrein",
            "Type 1": "Ice",
            "Type 2": "Water",
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
            "Name": "Clamperl",
            "Type 1": "Water",
            "Type 2": None,
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
            "Name": "Huntail",
            "Type 1": "Water",
            "Type 2": None,
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
            "Name": "Gorebyss",
            "Type 1": "Water",
            "Type 2": None,
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
            "Name": "Relicanth",
            "Type 1": "Water",
            "Type 2": "Rock",
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
            "Name": "Luvdisc",
            "Type 1": "Water",
            "Type 2": None,
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
            "Name": "Bagon",
            "Type 1": "Dragon",
            "Type 2": None,
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
            "Name": "Shelgon",
            "Type 1": "Dragon",
            "Type 2": None,
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
            "Name": "Salamence",
            "Type 1": "Dragon",
            "Type 2": "Flying",
            StatsEnum.HP: 95,
            StatsEnum.ATTACK: 135,
            StatsEnum.DEFENSE: 80,
            StatsEnum.SPECIAL_ATTACK: 110,
            StatsEnum.SPECIAL_DEFENSE: 80,
            StatsEnum.SPEED: 100
        },
        "Mega Salamence": {
            "Name": "Salamence",
            "Type 1": "Dragon",
            "Type 2": "Flying",
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
            "Name": "Beldum",
            "Type 1": "Steel",
            "Type 2": "Psychic",
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
            "Name": "Metang",
            "Type 1": "Steel",
            "Type 2": "Psychic",
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
            "Name": "Metagross",
            "Type 1": "Steel",
            "Type 2": "Psychic",
            StatsEnum.HP: 80,
            StatsEnum.ATTACK: 135,
            StatsEnum.DEFENSE: 130,
            StatsEnum.SPECIAL_ATTACK: 95,
            StatsEnum.SPECIAL_DEFENSE: 90,
            StatsEnum.SPEED: 70
        },
        "Mega Metagross": {
            "Name": "Metagross",
            "Type 1": "Steel",
            "Type 2": "Psychic",
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
            "Name": "Regirock",
            "Type 1": "Rock",
            "Type 2": None,
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
            "Name": "Regice",
            "Type 1": "Ice",
            "Type 2": None,
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
            "Name": "Registeel",
            "Type 1": "Steel",
            "Type 2": None,
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
            "Name": "Latias",
            "Type 1": "Dragon",
            "Type 2": "Psychic",
            StatsEnum.HP: 80,
            StatsEnum.ATTACK: 80,
            StatsEnum.DEFENSE: 90,
            StatsEnum.SPECIAL_ATTACK: 110,
            StatsEnum.SPECIAL_DEFENSE: 130,
            StatsEnum.SPEED: 110
        },
        "Mega Latias": {
            "Name": "Latias",
            "Type 1": "Dragon",
            "Type 2": "Psychic",
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
            "Name": "Latios",
            "Type 1": "Dragon",
            "Type 2": "Psychic",
            StatsEnum.HP: 80,
            StatsEnum.ATTACK: 90,
            StatsEnum.DEFENSE: 80,
            StatsEnum.SPECIAL_ATTACK: 130,
            StatsEnum.SPECIAL_DEFENSE: 110,
            StatsEnum.SPEED: 110
        },
        "Mega Latios": {
            "Name": "Latios",
            "Type 1": "Dragon",
            "Type 2": "Psychic",
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
            "Name": "Kyogre",
            "Type 1": "Water",
            "Type 2": None,
            StatsEnum.HP: 100,
            StatsEnum.ATTACK: 100,
            StatsEnum.DEFENSE: 90,
            StatsEnum.SPECIAL_ATTACK: 150,
            StatsEnum.SPECIAL_DEFENSE: 140,
            StatsEnum.SPEED: 90
        },
        "Primal Kyogre": {
            "Name": "Kyogre",
            "Type 1": "Water",
            "Type 2": None,
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
            "Name": "Groudon",
            "Type 1": "Ground",
            "Type 2": None,
            StatsEnum.HP: 100,
            StatsEnum.ATTACK: 150,
            StatsEnum.DEFENSE: 140,
            StatsEnum.SPECIAL_ATTACK: 100,
            StatsEnum.SPECIAL_DEFENSE: 90,
            StatsEnum.SPEED: 90
        },
        "Primal Groudon": {
            "Name": "Groudon",
            "Type 1": "Ground",
            "Type 2": "Fire",
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
            "Name": "Rayquaza",
            "Type 1": "Dragon",
            "Type 2": "Flying",
            StatsEnum.HP: 105,
            StatsEnum.ATTACK: 150,
            StatsEnum.DEFENSE: 90,
            StatsEnum.SPECIAL_ATTACK: 150,
            StatsEnum.SPECIAL_DEFENSE: 90,
            StatsEnum.SPEED: 95
        },
        "Mega Rayquaza": {
            "Name": "Rayquaza",
            "Type 1": "Dragon",
            "Type 2": "Flying",
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
            "Name": "Jirachi",
            "Type 1": "Steel",
            "Type 2": "Psychic",
            StatsEnum.HP: 100,
            StatsEnum.ATTACK: 100,
            StatsEnum.DEFENSE: 100,
            StatsEnum.SPECIAL_ATTACK: 100,
            StatsEnum.SPECIAL_DEFENSE: 100,
            StatsEnum.SPEED: 100
        }
    },
    "0386": {
        "Normal Forme": {
            "Name": "Deoxys",
            "Type 1": "Psychic",
            "Type 2": None,
            StatsEnum.HP: 50,
            StatsEnum.ATTACK: 150,
            StatsEnum.DEFENSE: 50,
            StatsEnum.SPECIAL_ATTACK: 150,
            StatsEnum.SPECIAL_DEFENSE: 50,
            StatsEnum.SPEED: 150
        },
        "Attack Forme": {
            "Name": "Deoxys",
            "Type 1": "Psychic",
            "Type 2": None,
            StatsEnum.HP: 50,
            StatsEnum.ATTACK: 180,
            StatsEnum.DEFENSE: 20,
            StatsEnum.SPECIAL_ATTACK: 180,
            StatsEnum.SPECIAL_DEFENSE: 20,
            StatsEnum.SPEED: 150
        },
        "Defense Forme": {
            "Name": "Deoxys",
            "Type 1": "Psychic",
            "Type 2": None,
            StatsEnum.HP: 50,
            StatsEnum.ATTACK: 70,
            StatsEnum.DEFENSE: 160,
            StatsEnum.SPECIAL_ATTACK: 70,
            StatsEnum.SPECIAL_DEFENSE: 160,
            StatsEnum.SPEED: 90
        },
        "Speed Forme": {
            "Name": "Deoxys",
            "Type 1": "Psychic",
            "Type 2": None,
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
            "Name": "Turtwig",
            "Type 1": "Grass",
            "Type 2": None,
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
            "Name": "Grotle",
            "Type 1": "Grass",
            "Type 2": None,
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
            "Name": "Torterra",
            "Type 1": "Grass",
            "Type 2": "Ground",
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
            "Name": "Chimchar",
            "Type 1": "Fire",
            "Type 2": None,
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
            "Name": "Monferno",
            "Type 1": "Fire",
            "Type 2": "Fighting",
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
            "Name": "Infernape",
            "Type 1": "Fire",
            "Type 2": "Fighting",
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
            "Name": "Piplup",
            "Type 1": "Water",
            "Type 2": None,
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
            "Name": "Prinplup",
            "Type 1": "Water",
            "Type 2": None,
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
            "Name": "Empoleon",
            "Type 1": "Water",
            "Type 2": "Steel",
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
            "Name": "Starly",
            "Type 1": "Normal",
            "Type 2": "Flying",
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
            "Name": "Staravia",
            "Type 1": "Normal",
            "Type 2": "Flying",
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
            "Name": "Staraptor",
            "Type 1": "Normal",
            "Type 2": "Flying",
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
            "Name": "Bidoof",
            "Type 1": "Normal",
            "Type 2": None,
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
            "Name": "Bibarel",
            "Type 1": "Normal",
            "Type 2": "Water",
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
            "Name": "Kricketot",
            "Type 1": "Bug",
            "Type 2": None,
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
            "Name": "Kricketune",
            "Type 1": "Bug",
            "Type 2": None,
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
            "Name": "Shinx",
            "Type 1": "Electric",
            "Type 2": None,
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
            "Name": "Luxio",
            "Type 1": "Electric",
            "Type 2": None,
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
            "Name": "Luxray",
            "Type 1": "Electric",
            "Type 2": None,
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
            "Name": "Budew",
            "Type 1": "Grass",
            "Type 2": "Poison",
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
            "Name": "Roserade",
            "Type 1": "Grass",
            "Type 2": "Poison",
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
            "Name": "Cranidos",
            "Type 1": "Rock",
            "Type 2": None,
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
            "Name": "Rampardos",
            "Type 1": "Rock",
            "Type 2": None,
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
            "Name": "Shieldon",
            "Type 1": "Rock",
            "Type 2": "Steel",
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
            "Name": "Bastiodon",
            "Type 1": "Rock",
            "Type 2": "Steel",
            StatsEnum.HP: 60,
            StatsEnum.ATTACK: 52,
            StatsEnum.DEFENSE: 168,
            StatsEnum.SPECIAL_ATTACK: 47,
            StatsEnum.SPECIAL_DEFENSE: 138,
            StatsEnum.SPEED: 30
        }
    },
    "0412": {
        "Plant Cloak": {
            "Name": "Burmy",
            "Type 1": "Bug",
            "Type 2": None,
            StatsEnum.HP: 40,
            StatsEnum.ATTACK: 29,
            StatsEnum.DEFENSE: 45,
            StatsEnum.SPECIAL_ATTACK: 29,
            StatsEnum.SPECIAL_DEFENSE: 45,
            StatsEnum.SPEED: 36
        },
        "Sandy Cloak": {
            "Name": "Burmy",
            "Type 1": "Bug",
            "Type 2": None,
            StatsEnum.HP: 40,
            StatsEnum.ATTACK: 29,
            StatsEnum.DEFENSE: 45,
            StatsEnum.SPECIAL_ATTACK: 29,
            StatsEnum.SPECIAL_DEFENSE: 45,
            StatsEnum.SPEED: 36
        },
        "Trash Cloak": {
            "Name": "Burmy",
            "Type 1": "Bug",
            "Type 2": None,
            StatsEnum.HP: 40,
            StatsEnum.ATTACK: 29,
            StatsEnum.DEFENSE: 45,
            StatsEnum.SPECIAL_ATTACK: 29,
            StatsEnum.SPECIAL_DEFENSE: 45,
            StatsEnum.SPEED: 36
        }
    },
    "0413": {
        "Plant Cloak": {
            "Name": "Wormadam",
            "Type 1": "Bug",
            "Type 2": "Grass",
            StatsEnum.HP: 60,
            StatsEnum.ATTACK: 59,
            StatsEnum.DEFENSE: 85,
            StatsEnum.SPECIAL_ATTACK: 79,
            StatsEnum.SPECIAL_DEFENSE: 105,
            StatsEnum.SPEED: 36
        },
        "Sandy Cloak": {
            "Name": "Wormadam",
            "Type 1": "Bug",
            "Type 2": "Ground",
            StatsEnum.HP: 60,
            StatsEnum.ATTACK: 79,
            StatsEnum.DEFENSE: 105,
            StatsEnum.SPECIAL_ATTACK: 59,
            StatsEnum.SPECIAL_DEFENSE: 85,
            StatsEnum.SPEED: 36
        },
        "Trash Cloak": {
            "Name": "Wormadam",
            "Type 1": "Bug",
            "Type 2": "Steel",
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
            "Name": "Mothim",
            "Type 1": "Bug",
            "Type 2": "Flying",
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
            "Name": "Combee",
            "Type 1": "Bug",
            "Type 2": "Flying",
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
            "Name": "Vespiquen",
            "Type 1": "Bug",
            "Type 2": "Flying",
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
            "Name": "Pachirisu",
            "Type 1": "Electric",
            "Type 2": None,
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
            "Name": "Buizel",
            "Type 1": "Water",
            "Type 2": None,
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
            "Name": "Floatzel",
            "Type 1": "Water",
            "Type 2": None,
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
            "Name": "Cherubi",
            "Type 1": "Grass",
            "Type 2": None,
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
            "Name": "Cherrim",
            "Type 1": "Grass",
            "Type 2": None,
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
            "Name": "Shellos",
            "Type 1": "Water",
            "Type 2": None,
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
            "Name": "Gastrodon",
            "Type 1": "Water",
            "Type 2": "Ground",
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
            "Name": "Ambipom",
            "Type 1": "Normal",
            "Type 2": None,
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
            "Name": "Drifloon",
            "Type 1": "Ghost",
            "Type 2": "Flying",
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
            "Name": "Drifblim",
            "Type 1": "Ghost",
            "Type 2": "Flying",
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
            "Name": "Buneary",
            "Type 1": "Normal",
            "Type 2": None,
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
            "Name": "Lopunny",
            "Type 1": "Normal",
            "Type 2": None,
            StatsEnum.HP: 65,
            StatsEnum.ATTACK: 76,
            StatsEnum.DEFENSE: 84,
            StatsEnum.SPECIAL_ATTACK: 54,
            StatsEnum.SPECIAL_DEFENSE: 96,
            StatsEnum.SPEED: 105
        },
        "Mega Lopunny": {
            "Name": "Lopunny",
            "Type 1": "Normal",
            "Type 2": "Fighting",
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
            "Name": "Mismagius",
            "Type 1": "Ghost",
            "Type 2": None,
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
            "Name": "Honchkrow",
            "Type 1": "Dark",
            "Type 2": "Flying",
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
            "Name": "Glameow",
            "Type 1": "Normal",
            "Type 2": None,
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
            "Name": "Purugly",
            "Type 1": "Normal",
            "Type 2": None,
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
            "Name": "Chingling",
            "Type 1": "Psychic",
            "Type 2": None,
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
            "Name": "Stunky",
            "Type 1": "Poison",
            "Type 2": "Dark",
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
            "Name": "Skuntank",
            "Type 1": "Poison",
            "Type 2": "Dark",
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
            "Name": "Bronzor",
            "Type 1": "Steel",
            "Type 2": "Psychic",
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
            "Name": "Bronzong",
            "Type 1": "Steel",
            "Type 2": "Psychic",
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
            "Name": "Bonsly",
            "Type 1": "Rock",
            "Type 2": None,
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
            "Name": "Mime Jr.",
            "Type 1": "Psychic",
            "Type 2": "Fairy",
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
            "Name": "Happiny",
            "Type 1": "Normal",
            "Type 2": None,
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
            "Name": "Chatot",
            "Type 1": "Normal",
            "Type 2": "Flying",
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
            "Name": "Spiritomb",
            "Type 1": "Ghost",
            "Type 2": "Dark",
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
            "Name": "Gible",
            "Type 1": "Dragon",
            "Type 2": "Ground",
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
            "Name": "Gabite",
            "Type 1": "Dragon",
            "Type 2": "Ground",
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
            "Name": "Garchomp",
            "Type 1": "Dragon",
            "Type 2": "Ground",
            StatsEnum.HP: 108,
            StatsEnum.ATTACK: 130,
            StatsEnum.DEFENSE: 95,
            StatsEnum.SPECIAL_ATTACK: 80,
            StatsEnum.SPECIAL_DEFENSE: 85,
            StatsEnum.SPEED: 102
        },
        "Mega Garchomp": {
            "Name": "Garchomp",
            "Type 1": "Dragon",
            "Type 2": "Ground",
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
            "Name": "Munchlax",
            "Type 1": "Normal",
            "Type 2": None,
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
            "Name": "Riolu",
            "Type 1": "Fighting",
            "Type 2": None,
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
            "Name": "Lucario",
            "Type 1": "Fighting",
            "Type 2": "Steel",
            StatsEnum.HP: 70,
            StatsEnum.ATTACK: 110,
            StatsEnum.DEFENSE: 70,
            StatsEnum.SPECIAL_ATTACK: 115,
            StatsEnum.SPECIAL_DEFENSE: 70,
            StatsEnum.SPEED: 90
        },
        "Mega Lucario": {
            "Name": "Lucario",
            "Type 1": "Fighting",
            "Type 2": "Steel",
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
            "Name": "Hippopotas",
            "Type 1": "Ground",
            "Type 2": None,
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
            "Name": "Hippowdon",
            "Type 1": "Ground",
            "Type 2": None,
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
            "Name": "Skorupi",
            "Type 1": "Poison",
            "Type 2": "Bug",
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
            "Name": "Drapion",
            "Type 1": "Poison",
            "Type 2": "Dark",
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
            "Name": "Croagunk",
            "Type 1": "Poison",
            "Type 2": "Fighting",
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
            "Name": "Toxicroak",
            "Type 1": "Poison",
            "Type 2": "Fighting",
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
            "Name": "Carnivine",
            "Type 1": "Grass",
            "Type 2": None,
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
            "Name": "Finneon",
            "Type 1": "Water",
            "Type 2": None,
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
            "Name": "Lumineon",
            "Type 1": "Water",
            "Type 2": None,
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
            "Name": "Mantyke",
            "Type 1": "Water",
            "Type 2": "Flying",
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
            "Name": "Snover",
            "Type 1": "Grass",
            "Type 2": "Ice",
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
            "Name": "Abomasnow",
            "Type 1": "Grass",
            "Type 2": "Ice",
            StatsEnum.HP: 90,
            StatsEnum.ATTACK: 92,
            StatsEnum.DEFENSE: 75,
            StatsEnum.SPECIAL_ATTACK: 92,
            StatsEnum.SPECIAL_DEFENSE: 85,
            StatsEnum.SPEED: 60
        },
        "Mega Abomasnow": {
            "Name": "Abomasnow",
            "Type 1": "Grass",
            "Type 2": "Ice",
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
            "Name": "Weavile",
            "Type 1": "Dark",
            "Type 2": "Ice",
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
            "Name": "Magnezone",
            "Type 1": "Electric",
            "Type 2": "Steel",
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
            "Name": "Lickilicky",
            "Type 1": "Normal",
            "Type 2": None,
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
            "Name": "Rhyperior",
            "Type 1": "Ground",
            "Type 2": "Rock",
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
            "Name": "Tangrowth",
            "Type 1": "Grass",
            "Type 2": None,
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
            "Name": "Electivire",
            "Type 1": "Electric",
            "Type 2": None,
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
            "Name": "Magmortar",
            "Type 1": "Fire",
            "Type 2": None,
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
            "Name": "Togekiss",
            "Type 1": "Fairy",
            "Type 2": "Flying",
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
            "Name": "Yanmega",
            "Type 1": "Bug",
            "Type 2": "Flying",
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
            "Name": "Leafeon",
            "Type 1": "Grass",
            "Type 2": None,
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
            "Name": "Glaceon",
            "Type 1": "Ice",
            "Type 2": None,
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
            "Name": "Gliscor",
            "Type 1": "Ground",
            "Type 2": "Flying",
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
            "Name": "Mamoswine",
            "Type 1": "Ice",
            "Type 2": "Ground",
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
            "Name": "Porygon-Z",
            "Type 1": "Normal",
            "Type 2": None,
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
            "Name": "Gallade",
            "Type 1": "Psychic",
            "Type 2": "Fighting",
            StatsEnum.HP: 68,
            StatsEnum.ATTACK: 125,
            StatsEnum.DEFENSE: 65,
            StatsEnum.SPECIAL_ATTACK: 65,
            StatsEnum.SPECIAL_DEFENSE: 115,
            StatsEnum.SPEED: 80
        },
        "Mega Gallade": {
            "Name": "Gallade",
            "Type 1": "Psychic",
            "Type 2": "Fighting",
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
            "Name": "Probopass",
            "Type 1": "Rock",
            "Type 2": "Steel",
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
            "Name": "Dusknoir",
            "Type 1": "Ghost",
            "Type 2": None,
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
            "Name": "Froslass",
            "Type 1": "Ice",
            "Type 2": "Ghost",
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
            "Name": "Rotom",
            "Type 1": "Electric",
            "Type 2": "Ghost",
            StatsEnum.HP: 50,
            StatsEnum.ATTACK: 50,
            StatsEnum.DEFENSE: 77,
            StatsEnum.SPECIAL_ATTACK: 95,
            StatsEnum.SPECIAL_DEFENSE: 77,
            StatsEnum.SPEED: 91
        },
        "Heat Rotom": {
            "Name": "Rotom",
            "Type 1": "Electric",
            "Type 2": "Fire",
            StatsEnum.HP: 50,
            StatsEnum.ATTACK: 65,
            StatsEnum.DEFENSE: 107,
            StatsEnum.SPECIAL_ATTACK: 105,
            StatsEnum.SPECIAL_DEFENSE: 107,
            StatsEnum.SPEED: 86
        },
        "Wash Rotom": {
            "Name": "Rotom",
            "Type 1": "Electric",
            "Type 2": "Water",
            StatsEnum.HP: 50,
            StatsEnum.ATTACK: 65,
            StatsEnum.DEFENSE: 107,
            StatsEnum.SPECIAL_ATTACK: 105,
            StatsEnum.SPECIAL_DEFENSE: 107,
            StatsEnum.SPEED: 86
        },
        "Frost Rotom": {
            "Name": "Rotom",
            "Type 1": "Electric",
            "Type 2": "Ice",
            StatsEnum.HP: 50,
            StatsEnum.ATTACK: 65,
            StatsEnum.DEFENSE: 107,
            StatsEnum.SPECIAL_ATTACK: 105,
            StatsEnum.SPECIAL_DEFENSE: 107,
            StatsEnum.SPEED: 86
        },
        "Fan Rotom": {
            "Name": "Rotom",
            "Type 1": "Electric",
            "Type 2": "Flying",
            StatsEnum.HP: 50,
            StatsEnum.ATTACK: 65,
            StatsEnum.DEFENSE: 107,
            StatsEnum.SPECIAL_ATTACK: 105,
            StatsEnum.SPECIAL_DEFENSE: 107,
            StatsEnum.SPEED: 86
        },
        "Mow Rotom": {
            "Name": "Rotom",
            "Type 1": "Electric",
            "Type 2": "Grass",
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
            "Name": "Uxie",
            "Type 1": "Psychic",
            "Type 2": None,
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
            "Name": "Mesprit",
            "Type 1": "Psychic",
            "Type 2": None,
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
            "Name": "Azelf",
            "Type 1": "Psychic",
            "Type 2": None,
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
            "Name": "Dialga",
            "Type 1": "Steel",
            "Type 2": "Dragon",
            StatsEnum.HP: 100,
            StatsEnum.ATTACK: 120,
            StatsEnum.DEFENSE: 120,
            StatsEnum.SPECIAL_ATTACK: 150,
            StatsEnum.SPECIAL_DEFENSE: 100,
            StatsEnum.SPEED: 90
        },
        "Origin Forme": {
            "Name": "Dialga",
            "Type 1": "Steel",
            "Type 2": "Dragon",
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
            "Name": "Palkia",
            "Type 1": "Water",
            "Type 2": "Dragon",
            StatsEnum.HP: 90,
            StatsEnum.ATTACK: 120,
            StatsEnum.DEFENSE: 100,
            StatsEnum.SPECIAL_ATTACK: 150,
            StatsEnum.SPECIAL_DEFENSE: 120,
            StatsEnum.SPEED: 100
        },
        "Origin Forme": {
            "Name": "Palkia",
            "Type 1": "Water",
            "Type 2": "Dragon",
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
            "Name": "Heatran",
            "Type 1": "Fire",
            "Type 2": "Steel",
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
            "Name": "Regigigas",
            "Type 1": "Normal",
            "Type 2": None,
            StatsEnum.HP: 110,
            StatsEnum.ATTACK: 160,
            StatsEnum.DEFENSE: 110,
            StatsEnum.SPECIAL_ATTACK: 80,
            StatsEnum.SPECIAL_DEFENSE: 110,
            StatsEnum.SPEED: 100
        }
    },
    "0487": {
        "Altered Forme": {
            "Name": "Giratina",
            "Type 1": "Ghost",
            "Type 2": "Dragon",
            StatsEnum.HP: 150,
            StatsEnum.ATTACK: 100,
            StatsEnum.DEFENSE: 120,
            StatsEnum.SPECIAL_ATTACK: 100,
            StatsEnum.SPECIAL_DEFENSE: 120,
            StatsEnum.SPEED: 90
        },
        "Origin Forme": {
            "Name": "Giratina",
            "Type 1": "Ghost",
            "Type 2": "Dragon",
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
            "Name": "Cresselia",
            "Type 1": "Psychic",
            "Type 2": None,
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
            "Name": "Phione",
            "Type 1": "Water",
            "Type 2": None,
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
            "Name": "Manaphy",
            "Type 1": "Water",
            "Type 2": None,
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
            "Name": "Darkrai",
            "Type 1": "Dark",
            "Type 2": None,
            StatsEnum.HP: 70,
            StatsEnum.ATTACK: 90,
            StatsEnum.DEFENSE: 90,
            StatsEnum.SPECIAL_ATTACK: 135,
            StatsEnum.SPECIAL_DEFENSE: 90,
            StatsEnum.SPEED: 125
        }
    },
    "0492": {
        "Land Forme": {
            "Name": "Shaymin",
            "Type 1": "Grass",
            "Type 2": None,
            StatsEnum.HP: 100,
            StatsEnum.ATTACK: 100,
            StatsEnum.DEFENSE: 100,
            StatsEnum.SPECIAL_ATTACK: 100,
            StatsEnum.SPECIAL_DEFENSE: 100,
            StatsEnum.SPEED: 100
        },
        "Sky Forme": {
            "Name": "Shaymin",
            "Type 1": "Grass",
            "Type 2": "Flying",
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
            "Name": "Arceus",
            "Type 1": "Normal",
            "Type 2": None,
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
            "Name": "Victini",
            "Type 1": "Psychic",
            "Type 2": "Fire",
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
            "Name": "Snivy",
            "Type 1": "Grass",
            "Type 2": None,
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
            "Name": "Servine",
            "Type 1": "Grass",
            "Type 2": None,
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
            "Name": "Serperior",
            "Type 1": "Grass",
            "Type 2": None,
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
            "Name": "Tepig",
            "Type 1": "Fire",
            "Type 2": None,
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
            "Name": "Pignite",
            "Type 1": "Fire",
            "Type 2": "Fighting",
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
            "Name": "Emboar",
            "Type 1": "Fire",
            "Type 2": "Fighting",
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
            "Name": "Oshawott",
            "Type 1": "Water",
            "Type 2": None,
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
            "Name": "Dewott",
            "Type 1": "Water",
            "Type 2": None,
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
            "Name": "Samurott",
            "Type 1": "Water",
            "Type 2": None,
            StatsEnum.HP: 95,
            StatsEnum.ATTACK: 100,
            StatsEnum.DEFENSE: 85,
            StatsEnum.SPECIAL_ATTACK: 108,
            StatsEnum.SPECIAL_DEFENSE: 70,
            StatsEnum.SPEED: 70
        },
        "Hisuian Samurott": {
            "Name": "Samurott",
            "Type 1": "Water",
            "Type 2": "Dark",
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
            "Name": "Patrat",
            "Type 1": "Normal",
            "Type 2": None,
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
            "Name": "Watchog",
            "Type 1": "Normal",
            "Type 2": None,
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
            "Name": "Lillipup",
            "Type 1": "Normal",
            "Type 2": None,
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
            "Name": "Herdier",
            "Type 1": "Normal",
            "Type 2": None,
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
            "Name": "Stoutland",
            "Type 1": "Normal",
            "Type 2": None,
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
            "Name": "Purrloin",
            "Type 1": "Dark",
            "Type 2": None,
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
            "Name": "Liepard",
            "Type 1": "Dark",
            "Type 2": None,
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
            "Name": "Pansage",
            "Type 1": "Grass",
            "Type 2": None,
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
            "Name": "Simisage",
            "Type 1": "Grass",
            "Type 2": None,
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
            "Name": "Pansear",
            "Type 1": "Fire",
            "Type 2": None,
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
            "Name": "Simisear",
            "Type 1": "Fire",
            "Type 2": None,
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
            "Name": "Panpour",
            "Type 1": "Water",
            "Type 2": None,
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
            "Name": "Simipour",
            "Type 1": "Water",
            "Type 2": None,
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
            "Name": "Munna",
            "Type 1": "Psychic",
            "Type 2": None,
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
            "Name": "Musharna",
            "Type 1": "Psychic",
            "Type 2": None,
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
            "Name": "Pidove",
            "Type 1": "Normal",
            "Type 2": "Flying",
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
            "Name": "Tranquill",
            "Type 1": "Normal",
            "Type 2": "Flying",
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
            "Name": "Unfezant",
            "Type 1": "Normal",
            "Type 2": "Flying",
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
            "Name": "Blitzle",
            "Type 1": "Electric",
            "Type 2": None,
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
            "Name": "Zebstrika",
            "Type 1": "Electric",
            "Type 2": None,
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
            "Name": "Roggenrola",
            "Type 1": "Rock",
            "Type 2": None,
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
            "Name": "Boldore",
            "Type 1": "Rock",
            "Type 2": None,
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
            "Name": "Gigalith",
            "Type 1": "Rock",
            "Type 2": None,
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
            "Name": "Woobat",
            "Type 1": "Psychic",
            "Type 2": "Flying",
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
            "Name": "Swoobat",
            "Type 1": "Psychic",
            "Type 2": "Flying",
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
            "Name": "Drilbur",
            "Type 1": "Ground",
            "Type 2": None,
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
            "Name": "Excadrill",
            "Type 1": "Ground",
            "Type 2": "Steel",
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
            "Name": "Audino",
            "Type 1": "Normal",
            "Type 2": None,
            StatsEnum.HP: 103,
            StatsEnum.ATTACK: 60,
            StatsEnum.DEFENSE: 86,
            StatsEnum.SPECIAL_ATTACK: 60,
            StatsEnum.SPECIAL_DEFENSE: 86,
            StatsEnum.SPEED: 50
        },
        "Mega Audino": {
            "Name": "Audino",
            "Type 1": "Normal",
            "Type 2": "Fairy",
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
            "Name": "Timburr",
            "Type 1": "Fighting",
            "Type 2": None,
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
            "Name": "Gurdurr",
            "Type 1": "Fighting",
            "Type 2": None,
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
            "Name": "Conkeldurr",
            "Type 1": "Fighting",
            "Type 2": None,
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
            "Name": "Tympole",
            "Type 1": "Water",
            "Type 2": None,
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
            "Name": "Palpitoad",
            "Type 1": "Water",
            "Type 2": "Ground",
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
            "Name": "Seismitoad",
            "Type 1": "Water",
            "Type 2": "Ground",
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
            "Name": "Throh",
            "Type 1": "Fighting",
            "Type 2": None,
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
            "Name": "Sawk",
            "Type 1": "Fighting",
            "Type 2": None,
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
            "Name": "Sewaddle",
            "Type 1": "Bug",
            "Type 2": "Grass",
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
            "Name": "Swadloon",
            "Type 1": "Bug",
            "Type 2": "Grass",
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
            "Name": "Leavanny",
            "Type 1": "Bug",
            "Type 2": "Grass",
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
            "Name": "Venipede",
            "Type 1": "Bug",
            "Type 2": "Poison",
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
            "Name": "Whirlipede",
            "Type 1": "Bug",
            "Type 2": "Poison",
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
            "Name": "Scolipede",
            "Type 1": "Bug",
            "Type 2": "Poison",
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
            "Name": "Cottonee",
            "Type 1": "Grass",
            "Type 2": "Fairy",
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
            "Name": "Whimsicott",
            "Type 1": "Grass",
            "Type 2": "Fairy",
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
            "Name": "Petilil",
            "Type 1": "Grass",
            "Type 2": None,
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
            "Name": "Lilligant",
            "Type 1": "Grass",
            "Type 2": None,
            StatsEnum.HP: 70,
            StatsEnum.ATTACK: 60,
            StatsEnum.DEFENSE: 75,
            StatsEnum.SPECIAL_ATTACK: 110,
            StatsEnum.SPECIAL_DEFENSE: 75,
            StatsEnum.SPEED: 90
        },
        "Hisuian Lilligant": {
            "Name": "Lilligant",
            "Type 1": "Grass",
            "Type 2": "Fighting",
            StatsEnum.HP: 70,
            StatsEnum.ATTACK: 105,
            StatsEnum.DEFENSE: 75,
            StatsEnum.SPECIAL_ATTACK: 50,
            StatsEnum.SPECIAL_DEFENSE: 75,
            StatsEnum.SPEED: 105
        }
    },
    "0550": {
        "Red-Striped Form": {
            "Name": "Basculin",
            "Type 1": "Water",
            "Type 2": None,
            StatsEnum.HP: 70,
            StatsEnum.ATTACK: 92,
            StatsEnum.DEFENSE: 65,
            StatsEnum.SPECIAL_ATTACK: 80,
            StatsEnum.SPECIAL_DEFENSE: 55,
            StatsEnum.SPEED: 98
        },
        "Blue-Striped Form": {
            "Name": "Basculin",
            "Type 1": "Water",
            "Type 2": None,
            StatsEnum.HP: 70,
            StatsEnum.ATTACK: 92,
            StatsEnum.DEFENSE: 65,
            StatsEnum.SPECIAL_ATTACK: 80,
            StatsEnum.SPECIAL_DEFENSE: 55,
            StatsEnum.SPEED: 98
        },
        "White-Striped Form": {
            "Name": "Basculin",
            "Type 1": "Water",
            "Type 2": None,
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
            "Name": "Sandile",
            "Type 1": "Ground",
            "Type 2": "Dark",
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
            "Name": "Krokorok",
            "Type 1": "Ground",
            "Type 2": "Dark",
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
            "Name": "Krookodile",
            "Type 1": "Ground",
            "Type 2": "Dark",
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
            "Name": "Darumaka",
            "Type 1": "Fire",
            "Type 2": None,
            StatsEnum.HP: 70,
            StatsEnum.ATTACK: 90,
            StatsEnum.DEFENSE: 45,
            StatsEnum.SPECIAL_ATTACK: 15,
            StatsEnum.SPECIAL_DEFENSE: 45,
            StatsEnum.SPEED: 50
        },
        "Galarian Darumaka": {
            "Name": "Darumaka",
            "Type 1": "Ice",
            "Type 2": None,
            StatsEnum.HP: 70,
            StatsEnum.ATTACK: 90,
            StatsEnum.DEFENSE: 45,
            StatsEnum.SPECIAL_ATTACK: 15,
            StatsEnum.SPECIAL_DEFENSE: 45,
            StatsEnum.SPEED: 50
        }
    },
    "0555": {
        "Standard Mode": {
            "Name": "Darmanitan",
            "Type 1": "Fire",
            "Type 2": None,
            StatsEnum.HP: 105,
            StatsEnum.ATTACK: 140,
            StatsEnum.DEFENSE: 55,
            StatsEnum.SPECIAL_ATTACK: 30,
            StatsEnum.SPECIAL_DEFENSE: 55,
            StatsEnum.SPEED: 95
        },
        "Zen Mode": {
            "Name": "Darmanitan",
            "Type 1": "Fire",
            "Type 2": "Psychic",
            StatsEnum.HP: 105,
            StatsEnum.ATTACK: 30,
            StatsEnum.DEFENSE: 105,
            StatsEnum.SPECIAL_ATTACK: 140,
            StatsEnum.SPECIAL_DEFENSE: 105,
            StatsEnum.SPEED: 55
        },
        "Galarian Standard Mode": {
            "Name": "Darmanitan",
            "Type 1": "Ice",
            "Type 2": None,
            StatsEnum.HP: 105,
            StatsEnum.ATTACK: 140,
            StatsEnum.DEFENSE: 55,
            StatsEnum.SPECIAL_ATTACK: 30,
            StatsEnum.SPECIAL_DEFENSE: 55,
            StatsEnum.SPEED: 95
        },
        "Galarian Zen Mode": {
            "Name": "Darmanitan",
            "Type 1": "Ice",
            "Type 2": "Fire",
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
            "Name": "Maractus",
            "Type 1": "Grass",
            "Type 2": None,
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
            "Name": "Dwebble",
            "Type 1": "Bug",
            "Type 2": "Rock",
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
            "Name": "Crustle",
            "Type 1": "Bug",
            "Type 2": "Rock",
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
            "Name": "Scraggy",
            "Type 1": "Dark",
            "Type 2": "Fighting",
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
            "Name": "Scrafty",
            "Type 1": "Dark",
            "Type 2": "Fighting",
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
            "Name": "Sigilyph",
            "Type 1": "Psychic",
            "Type 2": "Flying",
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
            "Name": "Yamask",
            "Type 1": "Ghost",
            "Type 2": None,
            StatsEnum.HP: 38,
            StatsEnum.ATTACK: 30,
            StatsEnum.DEFENSE: 85,
            StatsEnum.SPECIAL_ATTACK: 55,
            StatsEnum.SPECIAL_DEFENSE: 65,
            StatsEnum.SPEED: 30
        },
        "Galarian Yamask": {
            "Name": "Yamask",
            "Type 1": "Ground",
            "Type 2": "Ghost",
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
            "Name": "Cofagrigus",
            "Type 1": "Ghost",
            "Type 2": None,
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
            "Name": "Tirtouga",
            "Type 1": "Water",
            "Type 2": "Rock",
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
            "Name": "Carracosta",
            "Type 1": "Water",
            "Type 2": "Rock",
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
            "Name": "Archen",
            "Type 1": "Rock",
            "Type 2": "Flying",
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
            "Name": "Archeops",
            "Type 1": "Rock",
            "Type 2": "Flying",
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
            "Name": "Trubbish",
            "Type 1": "Poison",
            "Type 2": None,
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
            "Name": "Garbodor",
            "Type 1": "Poison",
            "Type 2": None,
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
            "Name": "Zorua",
            "Type 1": "Dark",
            "Type 2": None,
            StatsEnum.HP: 40,
            StatsEnum.ATTACK: 65,
            StatsEnum.DEFENSE: 40,
            StatsEnum.SPECIAL_ATTACK: 80,
            StatsEnum.SPECIAL_DEFENSE: 40,
            StatsEnum.SPEED: 65
        },
        "Hisuian Zorua": {
            "Name": "Zorua",
            "Type 1": "Normal",
            "Type 2": "Ghost",
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
            "Name": "Zoroark",
            "Type 1": "Dark",
            "Type 2": None,
            StatsEnum.HP: 60,
            StatsEnum.ATTACK: 105,
            StatsEnum.DEFENSE: 60,
            StatsEnum.SPECIAL_ATTACK: 120,
            StatsEnum.SPECIAL_DEFENSE: 60,
            StatsEnum.SPEED: 105
        },
        "Hisuian Zoroark": {
            "Name": "Zoroark",
            "Type 1": "Normal",
            "Type 2": "Ghost",
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
            "Name": "Minccino",
            "Type 1": "Normal",
            "Type 2": None,
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
            "Name": "Cinccino",
            "Type 1": "Normal",
            "Type 2": None,
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
            "Name": "Gothita",
            "Type 1": "Psychic",
            "Type 2": None,
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
            "Name": "Gothorita",
            "Type 1": "Psychic",
            "Type 2": None,
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
            "Name": "Gothitelle",
            "Type 1": "Psychic",
            "Type 2": None,
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
            "Name": "Solosis",
            "Type 1": "Psychic",
            "Type 2": None,
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
            "Name": "Duosion",
            "Type 1": "Psychic",
            "Type 2": None,
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
            "Name": "Reuniclus",
            "Type 1": "Psychic",
            "Type 2": None,
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
            "Name": "Ducklett",
            "Type 1": "Water",
            "Type 2": "Flying",
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
            "Name": "Swanna",
            "Type 1": "Water",
            "Type 2": "Flying",
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
            "Name": "Vanillite",
            "Type 1": "Ice",
            "Type 2": None,
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
            "Name": "Vanillish",
            "Type 1": "Ice",
            "Type 2": None,
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
            "Name": "Vanilluxe",
            "Type 1": "Ice",
            "Type 2": None,
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
            "Name": "Deerling",
            "Type 1": "Normal",
            "Type 2": "Grass",
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
            "Name": "Sawsbuck",
            "Type 1": "Normal",
            "Type 2": "Grass",
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
            "Name": "Emolga",
            "Type 1": "Electric",
            "Type 2": "Flying",
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
            "Name": "Karrablast",
            "Type 1": "Bug",
            "Type 2": None,
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
            "Name": "Escavalier",
            "Type 1": "Bug",
            "Type 2": "Steel",
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
            "Name": "Foongus",
            "Type 1": "Grass",
            "Type 2": "Poison",
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
            "Name": "Amoonguss",
            "Type 1": "Grass",
            "Type 2": "Poison",
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
            "Name": "Frillish",
            "Type 1": "Water",
            "Type 2": "Ghost",
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
            "Name": "Jellicent",
            "Type 1": "Water",
            "Type 2": "Ghost",
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
            "Name": "Alomomola",
            "Type 1": "Water",
            "Type 2": None,
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
            "Name": "Joltik",
            "Type 1": "Bug",
            "Type 2": "Electric",
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
            "Name": "Galvantula",
            "Type 1": "Bug",
            "Type 2": "Electric",
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
            "Name": "Ferroseed",
            "Type 1": "Grass",
            "Type 2": "Steel",
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
            "Name": "Ferrothorn",
            "Type 1": "Grass",
            "Type 2": "Steel",
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
            "Name": "Klink",
            "Type 1": "Steel",
            "Type 2": None,
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
            "Name": "Klang",
            "Type 1": "Steel",
            "Type 2": None,
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
            "Name": "Klinklang",
            "Type 1": "Steel",
            "Type 2": None,
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
            "Name": "Tynamo",
            "Type 1": "Electric",
            "Type 2": None,
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
            "Name": "Eelektrik",
            "Type 1": "Electric",
            "Type 2": None,
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
            "Name": "Eelektross",
            "Type 1": "Electric",
            "Type 2": None,
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
            "Name": "Elgyem",
            "Type 1": "Psychic",
            "Type 2": None,
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
            "Name": "Beheeyem",
            "Type 1": "Psychic",
            "Type 2": None,
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
            "Name": "Litwick",
            "Type 1": "Ghost",
            "Type 2": "Fire",
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
            "Name": "Lampent",
            "Type 1": "Ghost",
            "Type 2": "Fire",
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
            "Name": "Chandelure",
            "Type 1": "Ghost",
            "Type 2": "Fire",
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
            "Name": "Axew",
            "Type 1": "Dragon",
            "Type 2": None,
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
            "Name": "Fraxure",
            "Type 1": "Dragon",
            "Type 2": None,
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
            "Name": "Haxorus",
            "Type 1": "Dragon",
            "Type 2": None,
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
            "Name": "Cubchoo",
            "Type 1": "Ice",
            "Type 2": None,
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
            "Name": "Beartic",
            "Type 1": "Ice",
            "Type 2": None,
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
            "Name": "Cryogonal",
            "Type 1": "Ice",
            "Type 2": None,
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
            "Name": "Shelmet",
            "Type 1": "Bug",
            "Type 2": None,
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
            "Name": "Accelgor",
            "Type 1": "Bug",
            "Type 2": None,
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
            "Name": "Stunfisk",
            "Type 1": "Ground",
            "Type 2": "Electric",
            StatsEnum.HP: 109,
            StatsEnum.ATTACK: 66,
            StatsEnum.DEFENSE: 84,
            StatsEnum.SPECIAL_ATTACK: 81,
            StatsEnum.SPECIAL_DEFENSE: 99,
            StatsEnum.SPEED: 32
        },
        "Galarian Stunfisk": {
            "Name": "Stunfisk",
            "Type 1": "Ground",
            "Type 2": "Steel",
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
            "Name": "Mienfoo",
            "Type 1": "Fighting",
            "Type 2": None,
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
            "Name": "Mienshao",
            "Type 1": "Fighting",
            "Type 2": None,
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
            "Name": "Druddigon",
            "Type 1": "Dragon",
            "Type 2": None,
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
            "Name": "Golett",
            "Type 1": "Ground",
            "Type 2": "Ghost",
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
            "Name": "Golurk",
            "Type 1": "Ground",
            "Type 2": "Ghost",
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
            "Name": "Pawniard",
            "Type 1": "Dark",
            "Type 2": "Steel",
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
            "Name": "Bisharp",
            "Type 1": "Dark",
            "Type 2": "Steel",
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
            "Name": "Bouffalant",
            "Type 1": "Normal",
            "Type 2": None,
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
            "Name": "Rufflet",
            "Type 1": "Normal",
            "Type 2": "Flying",
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
            "Name": "Braviary",
            "Type 1": "Normal",
            "Type 2": "Flying",
            StatsEnum.HP: 100,
            StatsEnum.ATTACK: 123,
            StatsEnum.DEFENSE: 75,
            StatsEnum.SPECIAL_ATTACK: 57,
            StatsEnum.SPECIAL_DEFENSE: 75,
            StatsEnum.SPEED: 80
        },
        "Hisuian Braviary": {
            "Name": "Braviary",
            "Type 1": "Psychic",
            "Type 2": "Flying",
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
            "Name": "Vullaby",
            "Type 1": "Dark",
            "Type 2": "Flying",
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
            "Name": "Mandibuzz",
            "Type 1": "Dark",
            "Type 2": "Flying",
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
            "Name": "Heatmor",
            "Type 1": "Fire",
            "Type 2": None,
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
            "Name": "Durant",
            "Type 1": "Bug",
            "Type 2": "Steel",
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
            "Name": "Deino",
            "Type 1": "Dark",
            "Type 2": "Dragon",
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
            "Name": "Zweilous",
            "Type 1": "Dark",
            "Type 2": "Dragon",
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
            "Name": "Hydreigon",
            "Type 1": "Dark",
            "Type 2": "Dragon",
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
            "Name": "Larvesta",
            "Type 1": "Bug",
            "Type 2": "Fire",
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
            "Name": "Volcarona",
            "Type 1": "Bug",
            "Type 2": "Fire",
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
            "Name": "Cobalion",
            "Type 1": "Steel",
            "Type 2": "Fighting",
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
            "Name": "Terrakion",
            "Type 1": "Rock",
            "Type 2": "Fighting",
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
            "Name": "Virizion",
            "Type 1": "Grass",
            "Type 2": "Fighting",
            StatsEnum.HP: 91,
            StatsEnum.ATTACK: 90,
            StatsEnum.DEFENSE: 72,
            StatsEnum.SPECIAL_ATTACK: 90,
            StatsEnum.SPECIAL_DEFENSE: 129,
            StatsEnum.SPEED: 108
        }
    },
    "0641": {
        "Incarnate Forme": {
            "Name": "Tornadus",
            "Type 1": "Flying",
            "Type 2": None,
            StatsEnum.HP: 79,
            StatsEnum.ATTACK: 115,
            StatsEnum.DEFENSE: 70,
            StatsEnum.SPECIAL_ATTACK: 125,
            StatsEnum.SPECIAL_DEFENSE: 80,
            StatsEnum.SPEED: 111
        },
        "Therian Forme": {
            "Name": "Tornadus",
            "Type 1": "Flying",
            "Type 2": None,
            StatsEnum.HP: 79,
            StatsEnum.ATTACK: 100,
            StatsEnum.DEFENSE: 80,
            StatsEnum.SPECIAL_ATTACK: 110,
            StatsEnum.SPECIAL_DEFENSE: 90,
            StatsEnum.SPEED: 121
        }
    },
    "0642": {
        "Incarnate Forme": {
            "Name": "Thundurus",
            "Type 1": "Electric",
            "Type 2": "Flying",
            StatsEnum.HP: 79,
            StatsEnum.ATTACK: 115,
            StatsEnum.DEFENSE: 70,
            StatsEnum.SPECIAL_ATTACK: 125,
            StatsEnum.SPECIAL_DEFENSE: 80,
            StatsEnum.SPEED: 111
        },
        "Therian Forme": {
            "Name": "Thundurus",
            "Type 1": "Electric",
            "Type 2": "Flying",
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
            "Name": "Reshiram",
            "Type 1": "Dragon",
            "Type 2": "Fire",
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
            "Name": "Zekrom",
            "Type 1": "Dragon",
            "Type 2": "Electric",
            StatsEnum.HP: 100,
            StatsEnum.ATTACK: 150,
            StatsEnum.DEFENSE: 120,
            StatsEnum.SPECIAL_ATTACK: 120,
            StatsEnum.SPECIAL_DEFENSE: 100,
            StatsEnum.SPEED: 90
        }
    },
    "0645": {
        "Incarnate Forme": {
            "Name": "Landorus",
            "Type 1": "Ground",
            "Type 2": "Flying",
            StatsEnum.HP: 89,
            StatsEnum.ATTACK: 125,
            StatsEnum.DEFENSE: 90,
            StatsEnum.SPECIAL_ATTACK: 115,
            StatsEnum.SPECIAL_DEFENSE: 80,
            StatsEnum.SPEED: 101
        },
        "Therian Forme": {
            "Name": "Landorus",
            "Type 1": "Ground",
            "Type 2": "Flying",
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
            "Name": "Kyurem",
            "Type 1": "Dragon",
            "Type 2": "Ice",
            StatsEnum.HP: 125,
            StatsEnum.ATTACK: 130,
            StatsEnum.DEFENSE: 90,
            StatsEnum.SPECIAL_ATTACK: 130,
            StatsEnum.SPECIAL_DEFENSE: 90,
            StatsEnum.SPEED: 95
        },
        "White Kyurem": {
            "Name": "Kyurem",
            "Type 1": "Dragon",
            "Type 2": "Ice",
            StatsEnum.HP: 125,
            StatsEnum.ATTACK: 120,
            StatsEnum.DEFENSE: 90,
            StatsEnum.SPECIAL_ATTACK: 170,
            StatsEnum.SPECIAL_DEFENSE: 100,
            StatsEnum.SPEED: 95
        },
        "Black Kyurem": {
            "Name": "Kyurem",
            "Type 1": "Dragon",
            "Type 2": "Ice",
            StatsEnum.HP: 125,
            StatsEnum.ATTACK: 170,
            StatsEnum.DEFENSE: 100,
            StatsEnum.SPECIAL_ATTACK: 120,
            StatsEnum.SPECIAL_DEFENSE: 90,
            StatsEnum.SPEED: 95
        }
    },
    "0647": {
        "Ordinary Form": {
            "Name": "Keldeo",
            "Type 1": "Water",
            "Type 2": "Fighting",
            StatsEnum.HP: 91,
            StatsEnum.ATTACK: 72,
            StatsEnum.DEFENSE: 90,
            StatsEnum.SPECIAL_ATTACK: 129,
            StatsEnum.SPECIAL_DEFENSE: 90,
            StatsEnum.SPEED: 108
        },
        "Resolute Form": {
            "Name": "Keldeo",
            "Type 1": "Water",
            "Type 2": "Fighting",
            StatsEnum.HP: 91,
            StatsEnum.ATTACK: 72,
            StatsEnum.DEFENSE: 90,
            StatsEnum.SPECIAL_ATTACK: 129,
            StatsEnum.SPECIAL_DEFENSE: 90,
            StatsEnum.SPEED: 108
        }
    },
    "0648": {
        "Aria Forme": {
            "Name": "Meloetta",
            "Type 1": "Normal",
            "Type 2": "Psychic",
            StatsEnum.HP: 100,
            StatsEnum.ATTACK: 77,
            StatsEnum.DEFENSE: 77,
            StatsEnum.SPECIAL_ATTACK: 128,
            StatsEnum.SPECIAL_DEFENSE: 128,
            StatsEnum.SPEED: 90
        },
        "Pirouette Forme": {
            "Name": "Meloetta",
            "Type 1": "Normal",
            "Type 2": "Fighting",
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
            "Name": "Genesect",
            "Type 1": "Bug",
            "Type 2": "Steel",
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
            "Name": "Chespin",
            "Type 1": "Grass",
            "Type 2": None,
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
            "Name": "Quilladin",
            "Type 1": "Grass",
            "Type 2": None,
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
            "Name": "Chesnaught",
            "Type 1": "Grass",
            "Type 2": "Fighting",
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
            "Name": "Fennekin",
            "Type 1": "Fire",
            "Type 2": None,
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
            "Name": "Braixen",
            "Type 1": "Fire",
            "Type 2": None,
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
            "Name": "Delphox",
            "Type 1": "Fire",
            "Type 2": "Psychic",
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
            "Name": "Froakie",
            "Type 1": "Water",
            "Type 2": None,
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
            "Name": "Frogadier",
            "Type 1": "Water",
            "Type 2": None,
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
            "Name": "Greninja",
            "Type 1": "Water",
            "Type 2": "Dark",
            StatsEnum.HP: 72,
            StatsEnum.ATTACK: 95,
            StatsEnum.DEFENSE: 67,
            StatsEnum.SPECIAL_ATTACK: 103,
            StatsEnum.SPECIAL_DEFENSE: 71,
            StatsEnum.SPEED: 122
        },
        "Ash-Greninja": {
            "Name": "Greninja",
            "Type 1": "Water",
            "Type 2": "Dark",
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
            "Name": "Bunnelby",
            "Type 1": "Normal",
            "Type 2": None,
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
            "Name": "Diggersby",
            "Type 1": "Normal",
            "Type 2": "Ground",
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
            "Name": "Fletchling",
            "Type 1": "Normal",
            "Type 2": "Flying",
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
            "Name": "Fletchinder",
            "Type 1": "Fire",
            "Type 2": "Flying",
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
            "Name": "Talonflame",
            "Type 1": "Fire",
            "Type 2": "Flying",
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
            "Name": "Scatterbug",
            "Type 1": "Bug",
            "Type 2": None,
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
            "Name": "Spewpa",
            "Type 1": "Bug",
            "Type 2": None,
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
            "Name": "Vivillon",
            "Type 1": "Bug",
            "Type 2": "Flying",
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
            "Name": "Litleo",
            "Type 1": "Fire",
            "Type 2": "Normal",
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
            "Name": "Pyroar",
            "Type 1": "Fire",
            "Type 2": "Normal",
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
            "Name": "Flabébé",
            "Type 1": "Fairy",
            "Type 2": None,
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
            "Name": "Floette",
            "Type 1": "Fairy",
            "Type 2": None,
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
            "Name": "Florges",
            "Type 1": "Fairy",
            "Type 2": None,
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
            "Name": "Skiddo",
            "Type 1": "Grass",
            "Type 2": None,
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
            "Name": "Gogoat",
            "Type 1": "Grass",
            "Type 2": None,
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
            "Name": "Pancham",
            "Type 1": "Fighting",
            "Type 2": None,
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
            "Name": "Pangoro",
            "Type 1": "Fighting",
            "Type 2": "Dark",
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
            "Name": "Furfrou",
            "Type 1": "Normal",
            "Type 2": None,
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
            "Name": "Espurr",
            "Type 1": "Psychic",
            "Type 2": None,
            StatsEnum.HP: 62,
            StatsEnum.ATTACK: 48,
            StatsEnum.DEFENSE: 54,
            StatsEnum.SPECIAL_ATTACK: 63,
            StatsEnum.SPECIAL_DEFENSE: 60,
            StatsEnum.SPEED: 68
        }
    },
    "0678": {
        "Male": {
            "Name": "Meowstic",
            "Type 1": "Psychic",
            "Type 2": None,
            StatsEnum.HP: 74,
            StatsEnum.ATTACK: 48,
            StatsEnum.DEFENSE: 76,
            StatsEnum.SPECIAL_ATTACK: 83,
            StatsEnum.SPECIAL_DEFENSE: 81,
            StatsEnum.SPEED: 104
        },
        "Female": {
            "Name": "Meowstic",
            "Type 1": "Psychic",
            "Type 2": None,
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
            "Name": "Honedge",
            "Type 1": "Steel",
            "Type 2": "Ghost",
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
            "Name": "Doublade",
            "Type 1": "Steel",
            "Type 2": "Ghost",
            StatsEnum.HP: 59,
            StatsEnum.ATTACK: 110,
            StatsEnum.DEFENSE: 150,
            StatsEnum.SPECIAL_ATTACK: 45,
            StatsEnum.SPECIAL_DEFENSE: 49,
            StatsEnum.SPEED: 35
        }
    },
    "0681": {
        "Shield Forme": {
            "Name": "Aegislash",
            "Type 1": "Steel",
            "Type 2": "Ghost",
            StatsEnum.HP: 60,
            StatsEnum.ATTACK: 50,
            StatsEnum.DEFENSE: 140,
            StatsEnum.SPECIAL_ATTACK: 50,
            StatsEnum.SPECIAL_DEFENSE: 140,
            StatsEnum.SPEED: 60
        },
        "Blade Forme": {
            "Name": "Aegislash",
            "Type 1": "Steel",
            "Type 2": "Ghost",
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
            "Name": "Spritzee",
            "Type 1": "Fairy",
            "Type 2": None,
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
            "Name": "Aromatisse",
            "Type 1": "Fairy",
            "Type 2": None,
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
            "Name": "Swirlix",
            "Type 1": "Fairy",
            "Type 2": None,
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
            "Name": "Slurpuff",
            "Type 1": "Fairy",
            "Type 2": None,
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
            "Name": "Inkay",
            "Type 1": "Dark",
            "Type 2": "Psychic",
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
            "Name": "Malamar",
            "Type 1": "Dark",
            "Type 2": "Psychic",
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
            "Name": "Binacle",
            "Type 1": "Rock",
            "Type 2": "Water",
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
            "Name": "Barbaracle",
            "Type 1": "Rock",
            "Type 2": "Water",
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
            "Name": "Skrelp",
            "Type 1": "Poison",
            "Type 2": "Water",
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
            "Name": "Dragalge",
            "Type 1": "Poison",
            "Type 2": "Dragon",
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
            "Name": "Clauncher",
            "Type 1": "Water",
            "Type 2": None,
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
            "Name": "Clawitzer",
            "Type 1": "Water",
            "Type 2": None,
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
            "Name": "Helioptile",
            "Type 1": "Electric",
            "Type 2": "Normal",
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
            "Name": "Heliolisk",
            "Type 1": "Electric",
            "Type 2": "Normal",
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
            "Name": "Tyrunt",
            "Type 1": "Rock",
            "Type 2": "Dragon",
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
            "Name": "Tyrantrum",
            "Type 1": "Rock",
            "Type 2": "Dragon",
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
            "Name": "Amaura",
            "Type 1": "Rock",
            "Type 2": "Ice",
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
            "Name": "Aurorus",
            "Type 1": "Rock",
            "Type 2": "Ice",
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
            "Name": "Sylveon",
            "Type 1": "Fairy",
            "Type 2": None,
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
            "Name": "Hawlucha",
            "Type 1": "Fighting",
            "Type 2": "Flying",
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
            "Name": "Dedenne",
            "Type 1": "Electric",
            "Type 2": "Fairy",
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
            "Name": "Carbink",
            "Type 1": "Rock",
            "Type 2": "Fairy",
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
            "Name": "Goomy",
            "Type 1": "Dragon",
            "Type 2": None,
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
            "Name": "Sliggoo",
            "Type 1": "Dragon",
            "Type 2": None,
            StatsEnum.HP: 68,
            StatsEnum.ATTACK: 75,
            StatsEnum.DEFENSE: 53,
            StatsEnum.SPECIAL_ATTACK: 83,
            StatsEnum.SPECIAL_DEFENSE: 113,
            StatsEnum.SPEED: 60
        },
        "Hisuian Sliggoo": {
            "Name": "Sliggoo",
            "Type 1": "Steel",
            "Type 2": "Dragon",
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
            "Name": "Goodra",
            "Type 1": "Dragon",
            "Type 2": None,
            StatsEnum.HP: 90,
            StatsEnum.ATTACK: 100,
            StatsEnum.DEFENSE: 70,
            StatsEnum.SPECIAL_ATTACK: 110,
            StatsEnum.SPECIAL_DEFENSE: 150,
            StatsEnum.SPEED: 80
        },
        "Hisuian Goodra": {
            "Name": "Goodra",
            "Type 1": "Steel",
            "Type 2": "Dragon",
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
            "Name": "Klefki",
            "Type 1": "Steel",
            "Type 2": "Fairy",
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
            "Name": "Phantump",
            "Type 1": "Ghost",
            "Type 2": "Grass",
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
            "Name": "TreveNonet",
            "Type 1": "Ghost",
            "Type 2": "Grass",
            StatsEnum.HP: 85,
            StatsEnum.ATTACK: 110,
            StatsEnum.DEFENSE: 76,
            StatsEnum.SPECIAL_ATTACK: 65,
            StatsEnum.SPECIAL_DEFENSE: 82,
            StatsEnum.SPEED: 56
        }
    },
    "0710": {
        "Average Size": {
            "Name": "Pumpkaboo",
            "Type 1": "Ghost",
            "Type 2": "Grass",
            StatsEnum.HP: 49,
            StatsEnum.ATTACK: 66,
            StatsEnum.DEFENSE: 70,
            StatsEnum.SPECIAL_ATTACK: 44,
            StatsEnum.SPECIAL_DEFENSE: 55,
            StatsEnum.SPEED: 51
        },
        "Small Size": {
            "Name": "Pumpkaboo",
            "Type 1": "Ghost",
            "Type 2": "Grass",
            StatsEnum.HP: 44,
            StatsEnum.ATTACK: 66,
            StatsEnum.DEFENSE: 70,
            StatsEnum.SPECIAL_ATTACK: 44,
            StatsEnum.SPECIAL_DEFENSE: 55,
            StatsEnum.SPEED: 56
        },
        "Large Size": {
            "Name": "Pumpkaboo",
            "Type 1": "Ghost",
            "Type 2": "Grass",
            StatsEnum.HP: 54,
            StatsEnum.ATTACK: 66,
            StatsEnum.DEFENSE: 70,
            StatsEnum.SPECIAL_ATTACK: 44,
            StatsEnum.SPECIAL_DEFENSE: 55,
            StatsEnum.SPEED: 46
        },
        "Super Size": {
            "Name": "Pumpkaboo",
            "Type 1": "Ghost",
            "Type 2": "Grass",
            StatsEnum.HP: 59,
            StatsEnum.ATTACK: 66,
            StatsEnum.DEFENSE: 70,
            StatsEnum.SPECIAL_ATTACK: 44,
            StatsEnum.SPECIAL_DEFENSE: 55,
            StatsEnum.SPEED: 41
        }
    },
    "0711": {
        "Average Size": {
            "Name": "Gourgeist",
            "Type 1": "Ghost",
            "Type 2": "Grass",
            StatsEnum.HP: 65,
            StatsEnum.ATTACK: 90,
            StatsEnum.DEFENSE: 122,
            StatsEnum.SPECIAL_ATTACK: 58,
            StatsEnum.SPECIAL_DEFENSE: 75,
            StatsEnum.SPEED: 84
        },
        "Small Size": {
            "Name": "Gourgeist",
            "Type 1": "Ghost",
            "Type 2": "Grass",
            StatsEnum.HP: 55,
            StatsEnum.ATTACK: 85,
            StatsEnum.DEFENSE: 122,
            StatsEnum.SPECIAL_ATTACK: 58,
            StatsEnum.SPECIAL_DEFENSE: 75,
            StatsEnum.SPEED: 99
        },
        "Large Size": {
            "Name": "Gourgeist",
            "Type 1": "Ghost",
            "Type 2": "Grass",
            StatsEnum.HP: 75,
            StatsEnum.ATTACK: 95,
            StatsEnum.DEFENSE: 122,
            StatsEnum.SPECIAL_ATTACK: 58,
            StatsEnum.SPECIAL_DEFENSE: 75,
            StatsEnum.SPEED: 69
        },
        "Super Size": {
            "Name": "Gourgeist",
            "Type 1": "Ghost",
            "Type 2": "Grass",
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
            "Name": "Bergmite",
            "Type 1": "Ice",
            "Type 2": None,
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
            "Name": "Avalugg",
            "Type 1": "Ice",
            "Type 2": None,
            StatsEnum.HP: 95,
            StatsEnum.ATTACK: 117,
            StatsEnum.DEFENSE: 184,
            StatsEnum.SPECIAL_ATTACK: 44,
            StatsEnum.SPECIAL_DEFENSE: 46,
            StatsEnum.SPEED: 28
        },
        "Hisuian Avalugg": {
            "Name": "Avalugg",
            "Type 1": "Ice",
            "Type 2": "Rock",
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
            "Name": "Noibat",
            "Type 1": "Flying",
            "Type 2": "Dragon",
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
            "Name": "Noivern",
            "Type 1": "Flying",
            "Type 2": "Dragon",
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
            "Name": "Xerneas",
            "Type 1": "Fairy",
            "Type 2": None,
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
            "Name": "Yveltal",
            "Type 1": "Dark",
            "Type 2": "Flying",
            StatsEnum.HP: 126,
            StatsEnum.ATTACK: 131,
            StatsEnum.DEFENSE: 95,
            StatsEnum.SPECIAL_ATTACK: 131,
            StatsEnum.SPECIAL_DEFENSE: 98,
            StatsEnum.SPEED: 99
        }
    },
    "0718": {
        "50% Forme": {
            "Name": "Zygarde",
            "Type 1": "Dragon",
            "Type 2": "Ground",
            StatsEnum.HP: 108,
            StatsEnum.ATTACK: 100,
            StatsEnum.DEFENSE: 121,
            StatsEnum.SPECIAL_ATTACK: 81,
            StatsEnum.SPECIAL_DEFENSE: 95,
            StatsEnum.SPEED: 95
        },
        "10% Forme": {
            "Name": "Zygarde",
            "Type 1": "Dragon",
            "Type 2": "Ground",
            StatsEnum.HP: 54,
            StatsEnum.ATTACK: 100,
            StatsEnum.DEFENSE: 71,
            StatsEnum.SPECIAL_ATTACK: 61,
            StatsEnum.SPECIAL_DEFENSE: 85,
            StatsEnum.SPEED: 115
        },
        "Complete Forme": {
            "Name": "Zygarde",
            "Type 1": "Dragon",
            "Type 2": "Ground",
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
            "Name": "Diancie",
            "Type 1": "Rock",
            "Type 2": "Fairy",
            StatsEnum.HP: 50,
            StatsEnum.ATTACK: 100,
            StatsEnum.DEFENSE: 150,
            StatsEnum.SPECIAL_ATTACK: 100,
            StatsEnum.SPECIAL_DEFENSE: 150,
            StatsEnum.SPEED: 50
        },
        "Mega Diancie": {
            "Name": "Diancie",
            "Type 1": "Rock",
            "Type 2": "Fairy",
            StatsEnum.HP: 50,
            StatsEnum.ATTACK: 160,
            StatsEnum.DEFENSE: 110,
            StatsEnum.SPECIAL_ATTACK: 160,
            StatsEnum.SPECIAL_DEFENSE: 110,
            StatsEnum.SPEED: 110
        }
    },
    "0720": {
        "Hoopa Confined": {
            "Name": "Hoopa",
            "Type 1": "Psychic",
            "Type 2": "Ghost",
            StatsEnum.HP: 80,
            StatsEnum.ATTACK: 110,
            StatsEnum.DEFENSE: 60,
            StatsEnum.SPECIAL_ATTACK: 150,
            StatsEnum.SPECIAL_DEFENSE: 130,
            StatsEnum.SPEED: 70
        },
        "Hoopa Unbound": {
            "Name": "Hoopa",
            "Type 1": "Psychic",
            "Type 2": "Dark",
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
            "Name": "Volcanion",
            "Type 1": "Fire",
            "Type 2": "Water",
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
            "Name": "Rowlet",
            "Type 1": "Grass",
            "Type 2": "Flying",
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
            "Name": "Dartrix",
            "Type 1": "Grass",
            "Type 2": "Flying",
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
            "Name": "Decidueye",
            "Type 1": "Grass",
            "Type 2": "Ghost",
            StatsEnum.HP: 78,
            StatsEnum.ATTACK: 107,
            StatsEnum.DEFENSE: 75,
            StatsEnum.SPECIAL_ATTACK: 100,
            StatsEnum.SPECIAL_DEFENSE: 100,
            StatsEnum.SPEED: 70
        },
        "Hisuian Decidueye": {
            "Name": "Decidueye",
            "Type 1": "Grass",
            "Type 2": "Fighting",
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
            "Name": "Litten",
            "Type 1": "Fire",
            "Type 2": None,
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
            "Name": "Torracat",
            "Type 1": "Fire",
            "Type 2": None,
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
            "Name": "Incineroar",
            "Type 1": "Fire",
            "Type 2": "Dark",
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
            "Name": "Popplio",
            "Type 1": "Water",
            "Type 2": None,
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
            "Name": "Brionne",
            "Type 1": "Water",
            "Type 2": None,
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
            "Name": "Primarina",
            "Type 1": "Water",
            "Type 2": "Fairy",
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
            "Name": "Pikipek",
            "Type 1": "Normal",
            "Type 2": "Flying",
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
            "Name": "Trumbeak",
            "Type 1": "Normal",
            "Type 2": "Flying",
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
            "Name": "Toucannon",
            "Type 1": "Normal",
            "Type 2": "Flying",
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
            "Name": "Yungoos",
            "Type 1": "Normal",
            "Type 2": None,
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
            "Name": "Gumshoos",
            "Type 1": "Normal",
            "Type 2": None,
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
            "Name": "Grubbin",
            "Type 1": "Bug",
            "Type 2": None,
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
            "Name": "Charjabug",
            "Type 1": "Bug",
            "Type 2": "Electric",
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
            "Name": "Vikavolt",
            "Type 1": "Bug",
            "Type 2": "Electric",
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
            "Name": "Crabrawler",
            "Type 1": "Fighting",
            "Type 2": None,
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
            "Name": "Crabominable",
            "Type 1": "Fighting",
            "Type 2": "Ice",
            StatsEnum.HP: 97,
            StatsEnum.ATTACK: 132,
            StatsEnum.DEFENSE: 77,
            StatsEnum.SPECIAL_ATTACK: 62,
            StatsEnum.SPECIAL_DEFENSE: 67,
            StatsEnum.SPEED: 43
        }
    },
    "0741": {
        "Baile Style": {
            "Name": "Oricorio",
            "Type 1": "Fire",
            "Type 2": "Flying",
            StatsEnum.HP: 75,
            StatsEnum.ATTACK: 70,
            StatsEnum.DEFENSE: 70,
            StatsEnum.SPECIAL_ATTACK: 98,
            StatsEnum.SPECIAL_DEFENSE: 70,
            StatsEnum.SPEED: 93
        },
        "Pom-Pom Style": {
            "Name": "Oricorio",
            "Type 1": "Electric",
            "Type 2": "Flying",
            StatsEnum.HP: 75,
            StatsEnum.ATTACK: 70,
            StatsEnum.DEFENSE: 70,
            StatsEnum.SPECIAL_ATTACK: 98,
            StatsEnum.SPECIAL_DEFENSE: 70,
            StatsEnum.SPEED: 93
        },
        "Pa'u Style": {
            "Name": "Oricorio",
            "Type 1": "Psychic",
            "Type 2": "Flying",
            StatsEnum.HP: 75,
            StatsEnum.ATTACK: 70,
            StatsEnum.DEFENSE: 70,
            StatsEnum.SPECIAL_ATTACK: 98,
            StatsEnum.SPECIAL_DEFENSE: 70,
            StatsEnum.SPEED: 93
        },
        "Sensu Style": {
            "Name": "Oricorio",
            "Type 1": "Ghost",
            "Type 2": "Flying",
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
            "Name": "Cutiefly",
            "Type 1": "Bug",
            "Type 2": "Fairy",
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
            "Name": "Ribombee",
            "Type 1": "Bug",
            "Type 2": "Fairy",
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
            "Name": "Rockruff",
            "Type 1": "Rock",
            "Type 2": None,
            StatsEnum.HP: 45,
            StatsEnum.ATTACK: 65,
            StatsEnum.DEFENSE: 40,
            StatsEnum.SPECIAL_ATTACK: 30,
            StatsEnum.SPECIAL_DEFENSE: 40,
            StatsEnum.SPEED: 60
        },
        "Own Tempo Rockruff": {
            "Name": "Rockruff",
            "Type 1": "Rock",
            "Type 2": None,
            StatsEnum.HP: 45,
            StatsEnum.ATTACK: 65,
            StatsEnum.DEFENSE: 40,
            StatsEnum.SPECIAL_ATTACK: 30,
            StatsEnum.SPECIAL_DEFENSE: 40,
            StatsEnum.SPEED: 60
        }
    },
    "0745": {
        "Midday Form": {
            "Name": "Lycanroc",
            "Type 1": "Rock",
            "Type 2": None,
            StatsEnum.HP: 75,
            StatsEnum.ATTACK: 115,
            StatsEnum.DEFENSE: 65,
            StatsEnum.SPECIAL_ATTACK: 55,
            StatsEnum.SPECIAL_DEFENSE: 65,
            StatsEnum.SPEED: 112
        },
        "Midnight Form": {
            "Name": "Lycanroc",
            "Type 1": "Rock",
            "Type 2": None,
            StatsEnum.HP: 85,
            StatsEnum.ATTACK: 115,
            StatsEnum.DEFENSE: 75,
            StatsEnum.SPECIAL_ATTACK: 55,
            StatsEnum.SPECIAL_DEFENSE: 75,
            StatsEnum.SPEED: 82
        },
        "Dusk Form": {
            "Name": "Lycanroc",
            "Type 1": "Rock",
            "Type 2": None,
            StatsEnum.HP: 75,
            StatsEnum.ATTACK: 117,
            StatsEnum.DEFENSE: 65,
            StatsEnum.SPECIAL_ATTACK: 55,
            StatsEnum.SPECIAL_DEFENSE: 65,
            StatsEnum.SPEED: 110
        }
    },
    "0746": {
        "Solo Form": {
            "Name": "Wishiwashi",
            "Type 1": "Water",
            "Type 2": None,
            StatsEnum.HP: 45,
            StatsEnum.ATTACK: 20,
            StatsEnum.DEFENSE: 20,
            StatsEnum.SPECIAL_ATTACK: 25,
            StatsEnum.SPECIAL_DEFENSE: 25,
            StatsEnum.SPEED: 40
        },
        "School Form": {
            "Name": "Wishiwashi",
            "Type 1": "Water",
            "Type 2": None,
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
            "Name": "Mareanie",
            "Type 1": "Poison",
            "Type 2": "Water",
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
            "Name": "Toxapex",
            "Type 1": "Poison",
            "Type 2": "Water",
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
            "Name": "Mudbray",
            "Type 1": "Ground",
            "Type 2": None,
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
            "Name": "Mudsdale",
            "Type 1": "Ground",
            "Type 2": None,
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
            "Name": "Dewpider",
            "Type 1": "Water",
            "Type 2": "Bug",
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
            "Name": "Araquanid",
            "Type 1": "Water",
            "Type 2": "Bug",
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
            "Name": "Fomantis",
            "Type 1": "Grass",
            "Type 2": None,
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
            "Name": "Lurantis",
            "Type 1": "Grass",
            "Type 2": None,
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
            "Name": "Morelull",
            "Type 1": "Grass",
            "Type 2": "Fairy",
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
            "Name": "Shiinotic",
            "Type 1": "Grass",
            "Type 2": "Fairy",
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
            "Name": "Salandit",
            "Type 1": "Poison",
            "Type 2": "Fire",
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
            "Name": "Salazzle",
            "Type 1": "Poison",
            "Type 2": "Fire",
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
            "Name": "Stufful",
            "Type 1": "Normal",
            "Type 2": "Fighting",
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
            "Name": "Bewear",
            "Type 1": "Normal",
            "Type 2": "Fighting",
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
            "Name": "Bounsweet",
            "Type 1": "Grass",
            "Type 2": None,
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
            "Name": "Steenee",
            "Type 1": "Grass",
            "Type 2": None,
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
            "Name": "Tsareena",
            "Type 1": "Grass",
            "Type 2": None,
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
            "Name": "Comfey",
            "Type 1": "Fairy",
            "Type 2": None,
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
            "Name": "Oranguru",
            "Type 1": "Normal",
            "Type 2": "Psychic",
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
            "Name": "Passimian",
            "Type 1": "Fighting",
            "Type 2": None,
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
            "Name": "Wimpod",
            "Type 1": "Bug",
            "Type 2": "Water",
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
            "Name": "Golisopod",
            "Type 1": "Bug",
            "Type 2": "Water",
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
            "Name": "Sandygast",
            "Type 1": "Ghost",
            "Type 2": "Ground",
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
            "Name": "Palossand",
            "Type 1": "Ghost",
            "Type 2": "Ground",
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
            "Name": "Pyukumuku",
            "Type 1": "Water",
            "Type 2": None,
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
            "Name": "Type: Null",
            "Type 1": "Normal",
            "Type 2": None,
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
            "Name": "Silvally",
            "Type 1": "Normal",
            "Type 2": None,
            StatsEnum.HP: 95,
            StatsEnum.ATTACK: 95,
            StatsEnum.DEFENSE: 95,
            StatsEnum.SPECIAL_ATTACK: 95,
            StatsEnum.SPECIAL_DEFENSE: 95,
            StatsEnum.SPEED: 95
        }
    },
    "0774": {
        "Meteor Form": {
            "Name": "Minior",
            "Type 1": "Rock",
            "Type 2": "Flying",
            StatsEnum.HP: 60,
            StatsEnum.ATTACK: 60,
            StatsEnum.DEFENSE: 100,
            StatsEnum.SPECIAL_ATTACK: 60,
            StatsEnum.SPECIAL_DEFENSE: 100,
            StatsEnum.SPEED: 60
        },
        "Core Form": {
            "Name": "Minior",
            "Type 1": "Rock",
            "Type 2": "Flying",
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
            "Name": "Komala",
            "Type 1": "Normal",
            "Type 2": None,
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
            "Name": "Turtonator",
            "Type 1": "Fire",
            "Type 2": "Dragon",
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
            "Name": "Togedemaru",
            "Type 1": "Electric",
            "Type 2": "Steel",
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
            "Name": "Mimikyu",
            "Type 1": "Ghost",
            "Type 2": "Fairy",
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
            "Name": "Bruxish",
            "Type 1": "Water",
            "Type 2": "Psychic",
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
            "Name": "Drampa",
            "Type 1": "Normal",
            "Type 2": "Dragon",
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
            "Name": "Dhelmise",
            "Type 1": "Ghost",
            "Type 2": "Grass",
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
            "Name": "Jangmo-o",
            "Type 1": "Dragon",
            "Type 2": None,
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
            "Name": "Hakamo-o",
            "Type 1": "Dragon",
            "Type 2": "Fighting",
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
            "Name": "Kommo-o",
            "Type 1": "Dragon",
            "Type 2": "Fighting",
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
            "Name": "Tapu Koko",
            "Type 1": "Electric",
            "Type 2": "Fairy",
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
            "Name": "Tapu Lele",
            "Type 1": "Psychic",
            "Type 2": "Fairy",
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
            "Name": "Tapu Bulu",
            "Type 1": "Grass",
            "Type 2": "Fairy",
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
            "Name": "Tapu Fini",
            "Type 1": "Water",
            "Type 2": "Fairy",
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
            "Name": "Cosmog",
            "Type 1": "Psychic",
            "Type 2": None,
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
            "Name": "Cosmoem",
            "Type 1": "Psychic",
            "Type 2": None,
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
            "Name": "Solgaleo",
            "Type 1": "Psychic",
            "Type 2": "Steel",
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
            "Name": "Lunala",
            "Type 1": "Psychic",
            "Type 2": "Ghost",
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
            "Name": "Nihilego",
            "Type 1": "Rock",
            "Type 2": "Poison",
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
            "Name": "Buzzwole",
            "Type 1": "Bug",
            "Type 2": "Fighting",
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
            "Name": "Pheromosa",
            "Type 1": "Bug",
            "Type 2": "Fighting",
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
            "Name": "Xurkitree",
            "Type 1": "Electric",
            "Type 2": None,
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
            "Name": "Celesteela",
            "Type 1": "Steel",
            "Type 2": "Flying",
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
            "Name": "Kartana",
            "Type 1": "Grass",
            "Type 2": "Steel",
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
            "Name": "Guzzlord",
            "Type 1": "Dark",
            "Type 2": "Dragon",
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
            "Name": "Necrozma",
            "Type 1": "Psychic",
            "Type 2": None,
            StatsEnum.HP: 97,
            StatsEnum.ATTACK: 107,
            StatsEnum.DEFENSE: 101,
            StatsEnum.SPECIAL_ATTACK: 127,
            StatsEnum.SPECIAL_DEFENSE: 89,
            StatsEnum.SPEED: 79
        },
        "Dusk Mane Necrozma": {
            "Name": "Necrozma",
            "Type 1": "Psychic",
            "Type 2": "Steel",
            StatsEnum.HP: 97,
            StatsEnum.ATTACK: 157,
            StatsEnum.DEFENSE: 127,
            StatsEnum.SPECIAL_ATTACK: 113,
            StatsEnum.SPECIAL_DEFENSE: 109,
            StatsEnum.SPEED: 77
        },
        "Dawn Wings Necrozma": {
            "Name": "Necrozma",
            "Type 1": "Psychic",
            "Type 2": "Ghost",
            StatsEnum.HP: 97,
            StatsEnum.ATTACK: 113,
            StatsEnum.DEFENSE: 109,
            StatsEnum.SPECIAL_ATTACK: 157,
            StatsEnum.SPECIAL_DEFENSE: 127,
            StatsEnum.SPEED: 77
        },
        "Ultra Necrozma": {
            "Name": "Necrozma",
            "Type 1": "Psychic",
            "Type 2": "Dragon",
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
            "Name": "Magearna",
            "Type 1": "Steel",
            "Type 2": "Fairy",
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
            "Name": "Marshadow",
            "Type 1": "Fighting",
            "Type 2": "Ghost",
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
            "Name": "Poipole",
            "Type 1": "Poison",
            "Type 2": None,
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
            "Name": "Naganadel",
            "Type 1": "Poison",
            "Type 2": "Dragon",
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
            "Name": "Stakataka",
            "Type 1": "Rock",
            "Type 2": "Steel",
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
            "Name": "Blacephalon",
            "Type 1": "Fire",
            "Type 2": "Ghost",
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
            "Name": "Zeraora",
            "Type 1": "Electric",
            "Type 2": None,
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
            "Name": "Meltan",
            "Type 1": "Steel",
            "Type 2": None,
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
            "Name": "Melmetal",
            "Type 1": "Steel",
            "Type 2": None,
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
            "Name": "Grookey",
            "Type 1": "Grass",
            "Type 2": None,
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
            "Name": "Thwackey",
            "Type 1": "Grass",
            "Type 2": None,
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
            "Name": "Rillaboom",
            "Type 1": "Grass",
            "Type 2": None,
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
            "Name": "Scorbunny",
            "Type 1": "Fire",
            "Type 2": None,
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
            "Name": "Raboot",
            "Type 1": "Fire",
            "Type 2": None,
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
            "Name": "Cinderace",
            "Type 1": "Fire",
            "Type 2": None,
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
            "Name": "Sobble",
            "Type 1": "Water",
            "Type 2": None,
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
            "Name": "Drizzile",
            "Type 1": "Water",
            "Type 2": None,
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
            "Name": "Inteleon",
            "Type 1": "Water",
            "Type 2": None,
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
            "Name": "Skwovet",
            "Type 1": "Normal",
            "Type 2": None,
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
            "Name": "Greedent",
            "Type 1": "Normal",
            "Type 2": None,
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
            "Name": "Rookidee",
            "Type 1": "Flying",
            "Type 2": None,
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
            "Name": "Corvisquire",
            "Type 1": "Flying",
            "Type 2": None,
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
            "Name": "Corviknight",
            "Type 1": "Flying",
            "Type 2": "Steel",
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
            "Name": "Blipbug",
            "Type 1": "Bug",
            "Type 2": None,
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
            "Name": "Dottler",
            "Type 1": "Bug",
            "Type 2": "Psychic",
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
            "Name": "Orbeetle",
            "Type 1": "Bug",
            "Type 2": "Psychic",
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
            "Name": "Nickit",
            "Type 1": "Dark",
            "Type 2": None,
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
            "Name": "Thievul",
            "Type 1": "Dark",
            "Type 2": None,
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
            "Name": "Gossifleur",
            "Type 1": "Grass",
            "Type 2": None,
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
            "Name": "Eldegoss",
            "Type 1": "Grass",
            "Type 2": None,
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
            "Name": "Wooloo",
            "Type 1": "Normal",
            "Type 2": None,
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
            "Name": "Dubwool",
            "Type 1": "Normal",
            "Type 2": None,
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
            "Name": "Chewtle",
            "Type 1": "Water",
            "Type 2": None,
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
            "Name": "Drednaw",
            "Type 1": "Water",
            "Type 2": "Rock",
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
            "Name": "Yamper",
            "Type 1": "Electric",
            "Type 2": None,
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
            "Name": "Boltund",
            "Type 1": "Electric",
            "Type 2": None,
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
            "Name": "Rolycoly",
            "Type 1": "Rock",
            "Type 2": None,
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
            "Name": "Carkol",
            "Type 1": "Rock",
            "Type 2": "Fire",
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
            "Name": "Coalossal",
            "Type 1": "Rock",
            "Type 2": "Fire",
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
            "Name": "Applin",
            "Type 1": "Grass",
            "Type 2": "Dragon",
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
            "Name": "Flapple",
            "Type 1": "Grass",
            "Type 2": "Dragon",
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
            "Name": "Appletun",
            "Type 1": "Grass",
            "Type 2": "Dragon",
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
            "Name": "Silicobra",
            "Type 1": "Ground",
            "Type 2": None,
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
            "Name": "Sandaconda",
            "Type 1": "Ground",
            "Type 2": None,
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
            "Name": "Cramorant",
            "Type 1": "Flying",
            "Type 2": "Water",
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
            "Name": "Arrokuda",
            "Type 1": "Water",
            "Type 2": None,
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
            "Name": "Barraskewda",
            "Type 1": "Water",
            "Type 2": None,
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
            "Name": "Toxel",
            "Type 1": "Electric",
            "Type 2": "Poison",
            StatsEnum.HP: 40,
            StatsEnum.ATTACK: 38,
            StatsEnum.DEFENSE: 35,
            StatsEnum.SPECIAL_ATTACK: 54,
            StatsEnum.SPECIAL_DEFENSE: 35,
            StatsEnum.SPEED: 40
        }
    },
    "0849": {
        "Amped Form": {
            "Name": "Toxtricity",
            "Type 1": "Electric",
            "Type 2": "Poison",
            StatsEnum.HP: 75,
            StatsEnum.ATTACK: 98,
            StatsEnum.DEFENSE: 70,
            StatsEnum.SPECIAL_ATTACK: 114,
            StatsEnum.SPECIAL_DEFENSE: 70,
            StatsEnum.SPEED: 75
        },
        "Low Key Form": {
            "Name": "Toxtricity",
            "Type 1": "Electric",
            "Type 2": "Poison",
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
            "Name": "Sizzlipede",
            "Type 1": "Fire",
            "Type 2": "Bug",
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
            "Name": "Centiskorch",
            "Type 1": "Fire",
            "Type 2": "Bug",
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
            "Name": "Clobbopus",
            "Type 1": "Fighting",
            "Type 2": None,
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
            "Name": "Grapploct",
            "Type 1": "Fighting",
            "Type 2": None,
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
            "Name": "Sinistea",
            "Type 1": "Ghost",
            "Type 2": None,
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
            "Name": "Polteageist",
            "Type 1": "Ghost",
            "Type 2": None,
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
            "Name": "Hatenna",
            "Type 1": "Psychic",
            "Type 2": None,
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
            "Name": "Hattrem",
            "Type 1": "Psychic",
            "Type 2": None,
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
            "Name": "Hatterene",
            "Type 1": "Psychic",
            "Type 2": "Fairy",
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
            "Name": "Impidimp",
            "Type 1": "Dark",
            "Type 2": "Fairy",
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
            "Name": "Morgrem",
            "Type 1": "Dark",
            "Type 2": "Fairy",
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
            "Name": "Grimmsnarl",
            "Type 1": "Dark",
            "Type 2": "Fairy",
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
            "Name": "Obstagoon",
            "Type 1": "Dark",
            "Type 2": "Normal",
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
            "Name": "Perrserker",
            "Type 1": "Steel",
            "Type 2": None,
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
            "Name": "Cursola",
            "Type 1": "Ghost",
            "Type 2": None,
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
            "Name": "Sirfetch'd",
            "Type 1": "Fighting",
            "Type 2": None,
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
            "Name": "Mr. Rime",
            "Type 1": "Ice",
            "Type 2": "Psychic",
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
            "Name": "Runerigus",
            "Type 1": "Ground",
            "Type 2": "Ghost",
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
            "Name": "Milcery",
            "Type 1": "Fairy",
            "Type 2": None,
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
            "Name": "Alcremie",
            "Type 1": "Fairy",
            "Type 2": None,
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
            "Name": "Falinks",
            "Type 1": "Fighting",
            "Type 2": None,
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
            "Name": "Pincurchin",
            "Type 1": "Electric",
            "Type 2": None,
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
            "Name": "Snom",
            "Type 1": "Ice",
            "Type 2": "Bug",
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
            "Name": "Frosmoth",
            "Type 1": "Ice",
            "Type 2": "Bug",
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
            "Name": "Stonjourner",
            "Type 1": "Rock",
            "Type 2": None,
            StatsEnum.HP: 100,
            StatsEnum.ATTACK: 125,
            StatsEnum.DEFENSE: 135,
            StatsEnum.SPECIAL_ATTACK: 20,
            StatsEnum.SPECIAL_DEFENSE: 20,
            StatsEnum.SPEED: 70
        }
    },
    "0875": {
        "Ice Face": {
            "Name": "Eiscue",
            "Type 1": "Ice",
            "Type 2": None,
            StatsEnum.HP: 75,
            StatsEnum.ATTACK: 80,
            StatsEnum.DEFENSE: 110,
            StatsEnum.SPECIAL_ATTACK: 65,
            StatsEnum.SPECIAL_DEFENSE: 90,
            StatsEnum.SPEED: 50
        },
        "Noice Face": {
            "Name": "Eiscue",
            "Type 1": "Ice",
            "Type 2": None,
            StatsEnum.HP: 75,
            StatsEnum.ATTACK: 80,
            StatsEnum.DEFENSE: 70,
            StatsEnum.SPECIAL_ATTACK: 65,
            StatsEnum.SPECIAL_DEFENSE: 50,
            StatsEnum.SPEED: 130
        }
    },
    "0876": {
        "Male": {
            "Name": "Indeedee",
            "Type 1": "Psychic",
            "Type 2": "Normal",
            StatsEnum.HP: 60,
            StatsEnum.ATTACK: 65,
            StatsEnum.DEFENSE: 55,
            StatsEnum.SPECIAL_ATTACK: 105,
            StatsEnum.SPECIAL_DEFENSE: 95,
            StatsEnum.SPEED: 95
        },
        "Female": {
            "Name": "Indeedee",
            "Type 1": "Psychic",
            "Type 2": "Normal",
            StatsEnum.HP: 70,
            StatsEnum.ATTACK: 55,
            StatsEnum.DEFENSE: 65,
            StatsEnum.SPECIAL_ATTACK: 95,
            StatsEnum.SPECIAL_DEFENSE: 105,
            StatsEnum.SPEED: 85
        }
    },
    "0877": {
        "Full Belly Mode": {
            "Name": "Morpeko",
            "Type 1": "Electric",
            "Type 2": "Dark",
            StatsEnum.HP: 58,
            StatsEnum.ATTACK: 95,
            StatsEnum.DEFENSE: 58,
            StatsEnum.SPECIAL_ATTACK: 70,
            StatsEnum.SPECIAL_DEFENSE: 58,
            StatsEnum.SPEED: 97
        },
        "Hangry Mode": {
            "Name": "Morpeko",
            "Type 1": "Electric",
            "Type 2": "Dark",
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
            "Name": "Cufant",
            "Type 1": "Steel",
            "Type 2": None,
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
            "Name": "Copperajah",
            "Type 1": "Steel",
            "Type 2": None,
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
            "Name": "Dracozolt",
            "Type 1": "Electric",
            "Type 2": "Dragon",
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
            "Name": "Arctozolt",
            "Type 1": "Electric",
            "Type 2": "Ice",
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
            "Name": "Dracovish",
            "Type 1": "Water",
            "Type 2": "Dragon",
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
            "Name": "Arctovish",
            "Type 1": "Water",
            "Type 2": "Ice",
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
            "Name": "Duraludon",
            "Type 1": "Steel",
            "Type 2": "Dragon",
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
            "Name": "Dreepy",
            "Type 1": "Dragon",
            "Type 2": "Ghost",
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
            "Name": "Drakloak",
            "Type 1": "Dragon",
            "Type 2": "Ghost",
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
            "Name": "Dragapult",
            "Type 1": "Dragon",
            "Type 2": "Ghost",
            StatsEnum.HP: 88,
            StatsEnum.ATTACK: 120,
            StatsEnum.DEFENSE: 75,
            StatsEnum.SPECIAL_ATTACK: 100,
            StatsEnum.SPECIAL_DEFENSE: 75,
            StatsEnum.SPEED: 142
        }
    },
    "0888": {
        "Hero of Many Battles": {
            "Name": "Zacian",
            "Type 1": "Fairy",
            "Type 2": None,
            StatsEnum.HP: 92,
            StatsEnum.ATTACK: 120,
            StatsEnum.DEFENSE: 115,
            StatsEnum.SPECIAL_ATTACK: 80,
            StatsEnum.SPECIAL_DEFENSE: 115,
            StatsEnum.SPEED: 138
        },
        "Crowned Sword": {
            "Name": "Zacian",
            "Type 1": "Fairy",
            "Type 2": "Steel",
            StatsEnum.HP: 92,
            StatsEnum.ATTACK: 150,
            StatsEnum.DEFENSE: 115,
            StatsEnum.SPECIAL_ATTACK: 80,
            StatsEnum.SPECIAL_DEFENSE: 115,
            StatsEnum.SPEED: 148
        }
    },
    "0889": {
        "Hero of Many Battles": {
            "Name": "Zamazenta",
            "Type 1": "Fighting",
            "Type 2": None,
            StatsEnum.HP: 92,
            StatsEnum.ATTACK: 120,
            StatsEnum.DEFENSE: 115,
            StatsEnum.SPECIAL_ATTACK: 80,
            StatsEnum.SPECIAL_DEFENSE: 115,
            StatsEnum.SPEED: 138
        },
        "Crowned Shield": {
            "Name": "Zamazenta",
            "Type 1": "Fighting",
            "Type 2": "Steel",
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
            "Name": "Eternatus",
            "Type 1": "Poison",
            "Type 2": "Dragon",
            StatsEnum.HP: 140,
            StatsEnum.ATTACK: 85,
            StatsEnum.DEFENSE: 95,
            StatsEnum.SPECIAL_ATTACK: 145,
            StatsEnum.SPECIAL_DEFENSE: 95,
            StatsEnum.SPEED: 130
        },
        "Eternamax": {
            "Name": "Eternatus",
            "Type 1": "Poison",
            "Type 2": "Dragon",
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
            "Name": "Kubfu",
            "Type 1": "Fighting",
            "Type 2": None,
            StatsEnum.HP: 60,
            StatsEnum.ATTACK: 90,
            StatsEnum.DEFENSE: 60,
            StatsEnum.SPECIAL_ATTACK: 53,
            StatsEnum.SPECIAL_DEFENSE: 50,
            StatsEnum.SPEED: 72
        }
    },
    "0892": {
        "Single Strike Style": {
            "Name": "Urshifu",
            "Type 1": "Fighting",
            "Type 2": "Dark",
            StatsEnum.HP: 100,
            StatsEnum.ATTACK: 130,
            StatsEnum.DEFENSE: 100,
            StatsEnum.SPECIAL_ATTACK: 63,
            StatsEnum.SPECIAL_DEFENSE: 60,
            StatsEnum.SPEED: 97
        },
        "Rapid Strike Style": {
            "Name": "Urshifu",
            "Type 1": "Fighting",
            "Type 2": "Water",
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
            "Name": "Zarude",
            "Type 1": "Dark",
            "Type 2": "Grass",
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
            "Name": "Regieleki",
            "Type 1": "Electric",
            "Type 2": None,
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
            "Name": "Regidrago",
            "Type 1": "Dragon",
            "Type 2": None,
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
            "Name": "Glastrier",
            "Type 1": "Ice",
            "Type 2": None,
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
            "Name": "Spectrier",
            "Type 1": "Ghost",
            "Type 2": None,
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
            "Name": "Calyrex",
            "Type 1": "Psychic",
            "Type 2": "Grass",
            StatsEnum.HP: 100,
            StatsEnum.ATTACK: 80,
            StatsEnum.DEFENSE: 80,
            StatsEnum.SPECIAL_ATTACK: 80,
            StatsEnum.SPECIAL_DEFENSE: 80,
            StatsEnum.SPEED: 80
        },
        "Ice Rider": {
            "Name": "Calyrex",
            "Type 1": "Psychic",
            "Type 2": "Ice",
            StatsEnum.HP: 100,
            StatsEnum.ATTACK: 165,
            StatsEnum.DEFENSE: 150,
            StatsEnum.SPECIAL_ATTACK: 85,
            StatsEnum.SPECIAL_DEFENSE: 130,
            StatsEnum.SPEED: 50
        },
        "Shadow Rider": {
            "Name": "Calyrex",
            "Type 1": "Psychic",
            "Type 2": "Ghost",
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
            "Name": "Wyrdeer",
            "Type 1": "Normal",
            "Type 2": "Psychic",
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
            "Name": "Kleavor",
            "Type 1": "Bug",
            "Type 2": "Rock",
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
            "Name": "Ursaluna",
            "Type 1": "Ground",
            "Type 2": "Normal",
            StatsEnum.HP: 130,
            StatsEnum.ATTACK: 140,
            StatsEnum.DEFENSE: 105,
            StatsEnum.SPECIAL_ATTACK: 45,
            StatsEnum.SPECIAL_DEFENSE: 80,
            StatsEnum.SPEED: 50
        },
        "Bloodmoon": {
            "Name": "Ursaluna",
            "Type 1": "Ground",
            "Type 2": "Normal",
            StatsEnum.HP: 113,
            StatsEnum.ATTACK: 70,
            StatsEnum.DEFENSE: 120,
            StatsEnum.SPECIAL_ATTACK: 135,
            StatsEnum.SPECIAL_DEFENSE: 65,
            StatsEnum.SPEED: 52
        }
    },
    "0902": {
        "Male": {
            "Name": "Basculegion",
            "Type 1": "Water",
            "Type 2": "Ghost",
            StatsEnum.HP: 120,
            StatsEnum.ATTACK: 112,
            StatsEnum.DEFENSE: 65,
            StatsEnum.SPECIAL_ATTACK: 80,
            StatsEnum.SPECIAL_DEFENSE: 75,
            StatsEnum.SPEED: 78
        },
        "Female": {
            "Name": "Basculegion",
            "Type 1": "Water",
            "Type 2": "Ghost",
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
            "Name": "Sneasler",
            "Type 1": "Fighting",
            "Type 2": "Poison",
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
            "Name": "Overqwil",
            "Type 1": "Dark",
            "Type 2": "Poison",
            StatsEnum.HP: 85,
            StatsEnum.ATTACK: 115,
            StatsEnum.DEFENSE: 95,
            StatsEnum.SPECIAL_ATTACK: 65,
            StatsEnum.SPECIAL_DEFENSE: 65,
            StatsEnum.SPEED: 85
        }
    },
    "0905": {
        "Incarnate Forme": {
            "Name": "Enamorus",
            "Type 1": "Fairy",
            "Type 2": "Flying",
            StatsEnum.HP: 74,
            StatsEnum.ATTACK: 115,
            StatsEnum.DEFENSE: 70,
            StatsEnum.SPECIAL_ATTACK: 135,
            StatsEnum.SPECIAL_DEFENSE: 80,
            StatsEnum.SPEED: 106
        },
        "Therian Forme": {
            "Name": "Enamorus",
            "Type 1": "Fairy",
            "Type 2": "Flying",
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
            "Name": "Sprigatito",
            "Type 1": "Grass",
            "Type 2": None,
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
            "Name": "Floragato",
            "Type 1": "Grass",
            "Type 2": None,
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
            "Name": "Meowscarada",
            "Type 1": "Grass",
            "Type 2": "Dark",
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
            "Name": "Fuecoco",
            "Type 1": "Fire",
            "Type 2": None,
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
            "Name": "Crocalor",
            "Type 1": "Fire",
            "Type 2": None,
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
            "Name": "Skeledirge",
            "Type 1": "Fire",
            "Type 2": "Ghost",
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
            "Name": "Quaxly",
            "Type 1": "Water",
            "Type 2": None,
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
            "Name": "Quaxwell",
            "Type 1": "Water",
            "Type 2": None,
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
            "Name": "Quaquaval",
            "Type 1": "Water",
            "Type 2": "Fighting",
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
            "Name": "Lechonk",
            "Type 1": "Normal",
            "Type 2": None,
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
            "Name": "Oinkologne",
            "Type 1": "Normal",
            "Type 2": None,
            StatsEnum.HP: 110,
            StatsEnum.ATTACK: 100,
            StatsEnum.DEFENSE: 75,
            StatsEnum.SPECIAL_ATTACK: 59,
            StatsEnum.SPECIAL_DEFENSE: 80,
            StatsEnum.SPEED: 65
        },
        "Female": {
            "Name": "Oinkologne",
            "Type 1": "Normal",
            "Type 2": None,
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
            "Name": "Tarountula",
            "Type 1": "Bug",
            "Type 2": None,
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
            "Name": "Spidops",
            "Type 1": "Bug",
            "Type 2": None,
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
            "Name": "Nymble",
            "Type 1": "Bug",
            "Type 2": None,
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
            "Name": "Lokix",
            "Type 1": "Bug",
            "Type 2": "Dark",
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
            "Name": "Pawmi",
            "Type 1": "Electric",
            "Type 2": None,
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
            "Name": "Pawmo",
            "Type 1": "Electric",
            "Type 2": "Fighting",
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
            "Name": "Pawmot",
            "Type 1": "Electric",
            "Type 2": "Fighting",
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
            "Name": "Tandemaus",
            "Type 1": "Normal",
            "Type 2": None,
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
            "Name": "Maushold",
            "Type 1": "Normal",
            "Type 2": None,
            StatsEnum.HP: 74,
            StatsEnum.ATTACK: 75,
            StatsEnum.DEFENSE: 70,
            StatsEnum.SPECIAL_ATTACK: 65,
            StatsEnum.SPECIAL_DEFENSE: 75,
            StatsEnum.SPEED: 111
        },
        "Family of Three": {
            "Name": "Maushold",
            "Type 1": "Normal",
            "Type 2": None,
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
            "Name": "Fidough",
            "Type 1": "Fairy",
            "Type 2": None,
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
            "Name": "Dachsbun",
            "Type 1": "Fairy",
            "Type 2": None,
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
            "Name": "Smoliv",
            "Type 1": "Grass",
            "Type 2": "Normal",
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
            "Name": "Dolliv",
            "Type 1": "Grass",
            "Type 2": "Normal",
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
            "Name": "Arboliva",
            "Type 1": "Grass",
            "Type 2": "Normal",
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
            "Name": "Squawkabilly",
            "Type 1": "Normal",
            "Type 2": "Flying",
            StatsEnum.HP: 82,
            StatsEnum.ATTACK: 96,
            StatsEnum.DEFENSE: 51,
            StatsEnum.SPECIAL_ATTACK: 45,
            StatsEnum.SPECIAL_DEFENSE: 51,
            StatsEnum.SPEED: 92
        },
        "Blue Plumage": {
            "Name": "Squawkabilly",
            "Type 1": "Normal",
            "Type 2": "Flying",
            StatsEnum.HP: 82,
            StatsEnum.ATTACK: 96,
            StatsEnum.DEFENSE: 51,
            StatsEnum.SPECIAL_ATTACK: 45,
            StatsEnum.SPECIAL_DEFENSE: 51,
            StatsEnum.SPEED: 92
        },
        "Yellow Plumage": {
            "Name": "Squawkabilly",
            "Type 1": "Normal",
            "Type 2": "Flying",
            StatsEnum.HP: 82,
            StatsEnum.ATTACK: 96,
            StatsEnum.DEFENSE: 51,
            StatsEnum.SPECIAL_ATTACK: 45,
            StatsEnum.SPECIAL_DEFENSE: 51,
            StatsEnum.SPEED: 92
        },
        "White Plumage": {
            "Name": "Squawkabilly",
            "Type 1": "Normal",
            "Type 2": "Flying",
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
            "Name": "Nacli",
            "Type 1": "Rock",
            "Type 2": None,
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
            "Name": "Naclstack",
            "Type 1": "Rock",
            "Type 2": None,
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
            "Name": "Garganacl",
            "Type 1": "Rock",
            "Type 2": None,
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
            "Name": "Charcadet",
            "Type 1": "Fire",
            "Type 2": None,
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
            "Name": "Armarouge",
            "Type 1": "Fire",
            "Type 2": "Psychic",
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
            "Name": "Ceruledge",
            "Type 1": "Fire",
            "Type 2": "Ghost",
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
            "Name": "Tadbulb",
            "Type 1": "Electric",
            "Type 2": None,
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
            "Name": "Bellibolt",
            "Type 1": "Electric",
            "Type 2": None,
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
            "Name": "Wattrel",
            "Type 1": "Electric",
            "Type 2": "Flying",
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
            "Name": "Kilowattrel",
            "Type 1": "Electric",
            "Type 2": "Flying",
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
            "Name": "Maschiff",
            "Type 1": "Dark",
            "Type 2": None,
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
            "Name": "Mabosstiff",
            "Type 1": "Dark",
            "Type 2": None,
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
            "Name": "Shroodle",
            "Type 1": "Poison",
            "Type 2": "Normal",
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
            "Name": "Grafaiai",
            "Type 1": "Poison",
            "Type 2": "Normal",
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
            "Name": "Bramblin",
            "Type 1": "Grass",
            "Type 2": "Ghost",
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
            "Name": "Brambleghast",
            "Type 1": "Grass",
            "Type 2": "Ghost",
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
            "Name": "Toedscool",
            "Type 1": "Ground",
            "Type 2": "Grass",
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
            "Name": "Toedscruel",
            "Type 1": "Ground",
            "Type 2": "Grass",
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
            "Name": "Klawf",
            "Type 1": "Rock",
            "Type 2": None,
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
            "Name": "Capsakid",
            "Type 1": "Grass",
            "Type 2": None,
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
            "Name": "Scovillain",
            "Type 1": "Grass",
            "Type 2": "Fire",
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
            "Name": "Rellor",
            "Type 1": "Bug",
            "Type 2": None,
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
            "Name": "Rabsca",
            "Type 1": "Bug",
            "Type 2": "Psychic",
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
            "Name": "Flittle",
            "Type 1": "Psychic",
            "Type 2": None,
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
            "Name": "Espathra",
            "Type 1": "Psychic",
            "Type 2": None,
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
            "Name": "Tinkatink",
            "Type 1": "Fairy",
            "Type 2": "Steel",
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
            "Name": "Tinkatuff",
            "Type 1": "Fairy",
            "Type 2": "Steel",
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
            "Name": "Tinkaton",
            "Type 1": "Fairy",
            "Type 2": "Steel",
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
            "Name": "Wiglett",
            "Type 1": "Water",
            "Type 2": None,
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
            "Name": "Wugtrio",
            "Type 1": "Water",
            "Type 2": None,
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
            "Name": "Bombirdier",
            "Type 1": "Flying",
            "Type 2": "Dark",
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
            "Name": "Finizen",
            "Type 1": "Water",
            "Type 2": None,
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
            "Name": "Palafin",
            "Type 1": "Water",
            "Type 2": None,
            StatsEnum.HP: 100,
            StatsEnum.ATTACK: 70,
            StatsEnum.DEFENSE: 72,
            StatsEnum.SPECIAL_ATTACK: 53,
            StatsEnum.SPECIAL_DEFENSE: 62,
            StatsEnum.SPEED: 100
        },
        "Hero Form": {
            "Name": "Palafin",
            "Type 1": "Water",
            "Type 2": None,
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
            "Name": "Varoom",
            "Type 1": "Steel",
            "Type 2": "Poison",
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
            "Name": "Revavroom",
            "Type 1": "Steel",
            "Type 2": "Poison",
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
            "Name": "Cyclizar",
            "Type 1": "Dragon",
            "Type 2": "Normal",
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
            "Name": "Orthworm",
            "Type 1": "Steel",
            "Type 2": None,
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
            "Name": "Glimmet",
            "Type 1": "Rock",
            "Type 2": "Poison",
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
            "Name": "Glimmora",
            "Type 1": "Rock",
            "Type 2": "Poison",
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
            "Name": "Greavard",
            "Type 1": "Ghost",
            "Type 2": None,
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
            "Name": "Houndstone",
            "Type 1": "Ghost",
            "Type 2": None,
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
            "Name": "Flamigo",
            "Type 1": "Flying",
            "Type 2": "Fighting",
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
            "Name": "Cetoddle",
            "Type 1": "Ice",
            "Type 2": None,
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
            "Name": "Cetitan",
            "Type 1": "Ice",
            "Type 2": None,
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
            "Name": "Veluza",
            "Type 1": "Water",
            "Type 2": "Psychic",
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
            "Name": "Dondozo",
            "Type 1": "Water",
            "Type 2": None,
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
            "Name": "Tatsugiri",
            "Type 1": "Dragon",
            "Type 2": "Water",
            StatsEnum.HP: 68,
            StatsEnum.ATTACK: 50,
            StatsEnum.DEFENSE: 60,
            StatsEnum.SPECIAL_ATTACK: 120,
            StatsEnum.SPECIAL_DEFENSE: 95,
            StatsEnum.SPEED: 82
        },
        "Droopy Form": {
            "Name": "Tatsugiri",
            "Type 1": "Dragon",
            "Type 2": "Water",
            StatsEnum.HP: 68,
            StatsEnum.ATTACK: 50,
            StatsEnum.DEFENSE: 60,
            StatsEnum.SPECIAL_ATTACK: 120,
            StatsEnum.SPECIAL_DEFENSE: 95,
            StatsEnum.SPEED: 82
        },
        "Stretchy Form": {
            "Name": "Tatsugiri",
            "Type 1": "Dragon",
            "Type 2": "Water",
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
            "Name": "Annihilape",
            "Type 1": "Fighting",
            "Type 2": "Ghost",
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
            "Name": "Clodsire",
            "Type 1": "Poison",
            "Type 2": "Ground",
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
            "Name": "Farigiraf",
            "Type 1": "Normal",
            "Type 2": "Psychic",
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
            "Name": "Dudunsparce",
            "Type 1": "Normal",
            "Type 2": None,
            StatsEnum.HP: 125,
            StatsEnum.ATTACK: 100,
            StatsEnum.DEFENSE: 80,
            StatsEnum.SPECIAL_ATTACK: 85,
            StatsEnum.SPECIAL_DEFENSE: 75,
            StatsEnum.SPEED: 55
        },
        "Three-Segment Form": {
            "Name": "Dudunsparce",
            "Type 1": "Normal",
            "Type 2": None,
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
            "Name": "Kingambit",
            "Type 1": "Dark",
            "Type 2": "Steel",
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
            "Name": "Great Tusk",
            "Type 1": "Ground",
            "Type 2": "Fighting",
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
            "Name": "Scream Tail",
            "Type 1": "Fairy",
            "Type 2": "Psychic",
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
            "Name": "Brute Bonnet",
            "Type 1": "Grass",
            "Type 2": "Dark",
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
            "Name": "Flutter Mane",
            "Type 1": "Ghost",
            "Type 2": "Fairy",
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
            "Name": "Slither Wing",
            "Type 1": "Bug",
            "Type 2": "Fighting",
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
            "Name": "Sandy Shocks",
            "Type 1": "Electric",
            "Type 2": "Ground",
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
            "Name": "Iron Treads",
            "Type 1": "Ground",
            "Type 2": "Steel",
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
            "Name": "Iron Bundle",
            "Type 1": "Ice",
            "Type 2": "Water",
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
            "Name": "Iron Hands",
            "Type 1": "Fighting",
            "Type 2": "Electric",
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
            "Name": "Iron Jugulis",
            "Type 1": "Dark",
            "Type 2": "Flying",
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
            "Name": "Iron Moth",
            "Type 1": "Fire",
            "Type 2": "Poison",
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
            "Name": "Iron Thorns",
            "Type 1": "Rock",
            "Type 2": "Electric",
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
            "Name": "Frigibax",
            "Type 1": "Dragon",
            "Type 2": "Ice",
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
            "Name": "Arctibax",
            "Type 1": "Dragon",
            "Type 2": "Ice",
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
            "Name": "Baxcalibur",
            "Type 1": "Dragon",
            "Type 2": "Ice",
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
            "Name": "Gimmighoul",
            "Type 1": "Ghost",
            "Type 2": None,
            StatsEnum.HP: 45,
            StatsEnum.ATTACK: 30,
            StatsEnum.DEFENSE: 70,
            StatsEnum.SPECIAL_ATTACK: 75,
            StatsEnum.SPECIAL_DEFENSE: 70,
            StatsEnum.SPEED: 10
        },
        "Roaming Form": {
            "Name": "Gimmighoul",
            "Type 1": "Ghost",
            "Type 2": None,
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
            "Name": "Gholdengo",
            "Type 1": "Steel",
            "Type 2": "Ghost",
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
            "Name": "Wo-Chien",
            "Type 1": "Dark",
            "Type 2": "Grass",
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
            "Name": "Chien-Pao",
            "Type 1": "Dark",
            "Type 2": "Ice",
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
            "Name": "Ting-Lu",
            "Type 1": "Dark",
            "Type 2": "Ground",
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
            "Name": "Chi-Yu",
            "Type 1": "Dark",
            "Type 2": "Fire",
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
            "Name": "Roaring Moon",
            "Type 1": "Dragon",
            "Type 2": "Dark",
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
            "Name": "Iron Valiant",
            "Type 1": "Fairy",
            "Type 2": "Fighting",
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
            "Name": "Koraidon",
            "Type 1": "Fighting",
            "Type 2": "Dragon",
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
            "Name": "Miraidon",
            "Type 1": "Electric",
            "Type 2": "Dragon",
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
            "Name": "Walking Wake",
            "Type 1": "Water",
            "Type 2": "Dragon",
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
            "Name": "Iron Leaves",
            "Type 1": "Grass",
            "Type 2": "Psychic",
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
            "Name": "Dipplin",
            "Type 1": "Grass",
            "Type 2": "Dragon",
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
            "Name": "Poltchageist",
            "Type 1": "Grass",
            "Type 2": "Ghost",
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
            "Name": "Sinistcha",
            "Type 1": "Grass",
            "Type 2": "Ghost",
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
            "Name": "Okidogi",
            "Type 1": "Poison",
            "Type 2": "Fighting",
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
            "Name": "Munkidori",
            "Type 1": "Poison",
            "Type 2": "Psychic",
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
            "Name": "Fezandipiti",
            "Type 1": "Poison",
            "Type 2": "Fairy",
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
            "Name": "Ogerpon",
            "Type 1": "Grass",
            "Type 2": None,
            StatsEnum.HP: 80,
            StatsEnum.ATTACK: 120,
            StatsEnum.DEFENSE: 84,
            StatsEnum.SPECIAL_ATTACK: 60,
            StatsEnum.SPECIAL_DEFENSE: 96,
            StatsEnum.SPEED: 110
        },
        "Wellspring Mask": {
            "Name": "Ogerpon",
            "Type 1": "Grass",
            "Type 2": "Water",
            StatsEnum.HP: 80,
            StatsEnum.ATTACK: 120,
            StatsEnum.DEFENSE: 84,
            StatsEnum.SPECIAL_ATTACK: 60,
            StatsEnum.SPECIAL_DEFENSE: 96,
            StatsEnum.SPEED: 110
        },
        "Hearthflame Mask": {
            "Name": "Ogerpon",
            "Type 1": "Grass",
            "Type 2": "Fire",
            StatsEnum.HP: 80,
            StatsEnum.ATTACK: 120,
            StatsEnum.DEFENSE: 84,
            StatsEnum.SPECIAL_ATTACK: 60,
            StatsEnum.SPECIAL_DEFENSE: 96,
            StatsEnum.SPEED: 110
        },
        "Cornerstone Mask": {
            "Name": "Ogerpon",
            "Type 1": "Grass",
            "Type 2": "Rock",
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
            "Name": "Archaludon",
            "Type 1": "Steel",
            "Type 2": "Dragon",
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
            "Name": "Hydrapple",
            "Type 1": "Grass",
            "Type 2": "Dragon",
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
            "Name": "Gouging Fire",
            "Type 1": "Fire",
            "Type 2": "Dragon",
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
            "Name": "Raging Bolt",
            "Type 1": "Electric",
            "Type 2": "Dragon",
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
            "Name": "Iron Boulder",
            "Type 1": "Rock",
            "Type 2": "Psychic",
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
            "Name": "Iron Crown",
            "Type 1": "Steel",
            "Type 2": "Psychic",
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
            "Name": "Terapagos",
            "Type 1": "Normal",
            "Type 2": None,
            StatsEnum.HP: 90,
            StatsEnum.ATTACK: 65,
            StatsEnum.DEFENSE: 85,
            StatsEnum.SPECIAL_ATTACK: 65,
            StatsEnum.SPECIAL_DEFENSE: 85,
            StatsEnum.SPEED: 60
        },
        "Terastal Form": {
            "Name": "Terapagos",
            "Type 1": "Normal",
            "Type 2": None,
            StatsEnum.HP: 95,
            StatsEnum.ATTACK: 95,
            StatsEnum.DEFENSE: 110,
            StatsEnum.SPECIAL_ATTACK: 105,
            StatsEnum.SPECIAL_DEFENSE: 110,
            StatsEnum.SPEED: 85
        },
        "Stellar Form": {
            "Name": "Terapagos",
            "Type 1": "Normal",
            "Type 2": None,
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
            "Name": "Pecharunt",
            "Type 1": "Poison",
            "Type 2": "Ghost",
            StatsEnum.HP: 88,
            StatsEnum.ATTACK: 88,
            StatsEnum.DEFENSE: 160,
            StatsEnum.SPECIAL_ATTACK: 88,
            StatsEnum.SPECIAL_DEFENSE: 88,
            StatsEnum.SPEED: 88
        }
    }
}
