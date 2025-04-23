from enum import Enum


class NaturesEnum(Enum):
    '''Enum que representa Natures Monstrinhos.

    Cada Natureza aumenta um dos stats em 10% e reduz outro em 10%
    (quando atinge o nível 100).

    No entanto, existem cinco Naturezas neutras que aumentam e diminuem
    o mesmo status, não tendo efeito real nos atributos.
    '''

    ADAMANT = 'Adamant'
    BASHFUL = 'Bashful'
    BOLD = 'Bold'
    BRAVE = 'Brave'
    CALM = 'Calm'
    CAREFUL = 'Careful'
    DOCILE = 'Docile'
    GENTLE = 'Gentle'
    HARDY = 'Hardy'
    HASTY = 'Hasty'
    IMPISH = 'Impish'
    JOLLY = 'Jolly'
    LAX = 'Lax'
    LONELY = 'Lonely'
    MILD = 'Mild'
    MODEST = 'Modest'
    NAIVE = 'Naive'
    NAUGHTY = 'Naughty'
    QUIET = 'Quiet'
    QUIRKY = 'Quirky'
    RASH = 'Rash'
    RELAXED = 'Relaxed'
    SASSY = 'Sassy'
    SERIOUS = 'Serious'
    TIMID = 'Timid'


class NatureParamEnum(Enum):
    NATURE = 'nature'
    STAT_MODIFIERS = 'stat_modifiers'
