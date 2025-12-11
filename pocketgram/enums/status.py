from enum import Enum


class StatusEnum(Enum):
    ...


class MajorStatusEnum(StatusEnum):
    BADLY_POISONED = 'Badly Poisoned'
    BURN = 'Burn'
    FREEZE = 'Freeze'
    PARALYSIS = 'Paralysis'
    POISON = 'Poison'
    SLEEP = 'Sleep'


class MinorStatusEnum(StatusEnum):
    CONFUSION = 'Confusion'
