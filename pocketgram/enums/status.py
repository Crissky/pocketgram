from enum import Enum


class MajorStatusEnum(Enum):
    BADLY_POISONED = 'Badly Poisoned'
    BURN = 'Burn'
    FREEZE = 'Freeze'
    PARALYSIS = 'Paralysis'
    POISON = 'Poison'
    SLEEP = 'Sleep'


class MinorStatusEnum(Enum):
    CONFUSION = 'Confusion'
