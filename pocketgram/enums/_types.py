from enum import Enum


class TypesEnum(Enum):
    BUG = 'Bug'
    DARK = 'Dark'
    DRAGON = 'Dragon'
    ELECTRIC = 'Electric'
    FAIRY = 'Fairy'
    FIGHTING = 'Fighting'
    FIRE = 'Fire'
    FLYING = 'Flying'
    GHOST = 'Ghost'
    GRASS = 'Grass'
    GROUND = 'Ground'
    ICE = 'Ice'
    NORMAL = 'Normal'
    POISON = 'Poison'
    PSYCHIC = 'Psychic'
    ROCK = 'Rock'
    STEEL = 'Steel'
    WATER = 'Water'


class TypesEmojiEnum(Enum):
    BUG = '🐛'
    DARK = '🌑'
    DRAGON = '🐲'
    ELECTRIC = '⚡'
    FAIRY = '🧚'
    FIGHTING = '🥊'
    FIRE = '🔥'
    FLYING = '🦅'  # 🪽
    GHOST = '👻'
    GRASS = '🍃'
    GROUND = '🟤'
    ICE = '❄️'
    NORMAL = '⭐'
    POISON = '☠️'
    PSYCHIC = '👁️‍🗨️'  # 🔮🧿🪬👁️
    ROCK = '🪨'
    STEEL = '⚙️'
    WATER = '💧'


class TypesSuperEffectiveEnum(Enum):
    BUG = [TypesEnum.DARK, TypesEnum.GRASS, TypesEnum.PSYCHIC]
    DARK = [TypesEnum.GHOST, TypesEnum.PSYCHIC]
    DRAGON = [TypesEnum.DRAGON]
    ELECTRIC = [TypesEnum.FLYING, TypesEnum.WATER]
    FAIRY = [TypesEnum.DARK, TypesEnum.DRAGON, TypesEnum.FAIRY]
    FIGHTING = [
        TypesEnum.DARK, TypesEnum.ICE, TypesEnum.NORMAL,
        TypesEnum.ROCK, TypesEnum.STEEL
    ]
    FIRE = [TypesEnum.BUG, TypesEnum.GRASS, TypesEnum.ICE, TypesEnum.STEEL]
    FLYING = [TypesEnum.BUG, TypesEnum.FIGHTING, TypesEnum.GRASS]
    GHOST = [TypesEnum.GHOST, TypesEnum.PSYCHIC]
    GRASS = [TypesEnum.GROUND, TypesEnum.ROCK, TypesEnum.WATER]
    GROUND = [
        TypesEnum.ELECTRIC, TypesEnum.FIRE, TypesEnum.POISON,
        TypesEnum.ROCK, TypesEnum.STEEL
    ]
    ICE = [TypesEnum.DRAGON, TypesEnum.FLYING, TypesEnum.GRASS,
           TypesEnum.GROUND
           ]
    NORMAL = []
    POISON = [TypesEnum.FAIRY, TypesEnum.GRASS]
    PSYCHIC = [TypesEnum.FIGHTING, TypesEnum.POISON]
    ROCK = [TypesEnum.BUG, TypesEnum.FIRE, TypesEnum.FLYING, TypesEnum.ICE]
    STEEL = [TypesEnum.FAIRY, TypesEnum.ICE, TypesEnum.ROCK]
    WATER = [TypesEnum.FIRE, TypesEnum.GROUND, TypesEnum.ROCK]


class TypesNotVeryEffectiveEnum(Enum):
    BUG = [
        TypesEnum.FAIRY, TypesEnum.FIGHTING, TypesEnum.FIRE, TypesEnum.FLYING,
        TypesEnum.GHOST, TypesEnum.POISON, TypesEnum.STEEL
    ]
    DARK = [TypesEnum.DARK, TypesEnum.FAIRY, TypesEnum.FIGHTING]
    DRAGON = [TypesEnum.STEEL]
    ELECTRIC = [TypesEnum.DRAGON, TypesEnum.ELECTRIC, TypesEnum.GRASS]
    FAIRY = [TypesEnum.FIRE, TypesEnum.POISON, TypesEnum.STEEL]
    FIGHTING = [
        TypesEnum.BUG, TypesEnum.FAIRY, TypesEnum.FLYING,
        TypesEnum.POISON, TypesEnum.PSYCHIC
    ]
    FIRE = [TypesEnum.DRAGON, TypesEnum.FIRE, TypesEnum.ROCK, TypesEnum.WATER]
    FLYING = [TypesEnum.ELECTRIC, TypesEnum.ROCK, TypesEnum.STEEL]
    GHOST = [TypesEnum.DARK]
    GRASS = [
        TypesEnum.BUG, TypesEnum.DRAGON, TypesEnum.FIRE, TypesEnum.FLYING,
        TypesEnum.GRASS, TypesEnum.POISON, TypesEnum.STEEL
    ]
    GROUND = [TypesEnum.BUG, TypesEnum.GRASS]
    ICE = [TypesEnum.FIRE, TypesEnum.ICE, TypesEnum.STEEL, TypesEnum.WATER]
    NORMAL = [TypesEnum.ROCK, TypesEnum.STEEL]
    POISON = [
        TypesEnum.GHOST, TypesEnum.GROUND, TypesEnum.POISON, TypesEnum.ROCK
    ]
    PSYCHIC = [TypesEnum.PSYCHIC, TypesEnum.STEEL]
    ROCK = [TypesEnum.FIGHTING, TypesEnum.GROUND, TypesEnum.STEEL]
    STEEL = [
        TypesEnum.ELECTRIC, TypesEnum.FIRE, TypesEnum.STEEL, TypesEnum.WATER
    ]
    WATER = [TypesEnum.DRAGON, TypesEnum.GRASS, TypesEnum.WATER]


class TypesNoEffectiveEnum(Enum):
    BUG = []
    DARK = []
    DRAGON = [TypesEnum.FAIRY]
    ELECTRIC = [TypesEnum.GROUND]
    FAIRY = []
    FIGHTING = [TypesEnum.GHOST]
    FIRE = []
    FLYING = []
    GHOST = [TypesEnum.NORMAL]
    GRASS = []
    GROUND = [TypesEnum.FLYING]
    ICE = []
    NORMAL = [TypesEnum.GHOST]
    POISON = [TypesEnum.STEEL]
    PSYCHIC = [TypesEnum.DARK]
    ROCK = []
    STEEL = []
    WATER = []
