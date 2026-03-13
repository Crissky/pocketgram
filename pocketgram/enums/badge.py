from enum import Enum


class BadgeEnum(Enum):
    @classmethod
    def from_name(cls, name: str):
        for subclass in cls.__subclasses__():
            try:
                return subclass[name]
            except KeyError:
                continue
        raise ValueError(f"Badge '{name}' não encontrada")


class KantoBadgeEnum(BadgeEnum):
    BOULDER = "🪨ROCHA"
    CASCADE = "💧CASCATA"
    THUNDER = "⚡TROVÃO"
    RAINBOW = "🌈ARCO-ÍRIS"
    SOUL = "🩷ALMA"
    MARSH = "🪙LAMA"
    VOLCANO = "🔥VULCÃO"
    EARTH = "🌱TERRA"
