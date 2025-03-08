from typing import Dict, List, Union

from pocketgram.enums.natures import NaturesEnum
from pocketgram.enums.stats import StatsEnum
from pocketgram.stats.stats import Stats


class Nature(Stats):
    __slots__ = ['_nature', '_stat_modifiers']
    _DECREASES = {
        StatsEnum.HP: frozenset(),
        StatsEnum.ATTACK: frozenset([
            NaturesEnum.HARDY, NaturesEnum.BOLD, NaturesEnum.MODEST,
            NaturesEnum.CALM, NaturesEnum.TIMID,
        ]),
        StatsEnum.DEFENSE: frozenset([
            NaturesEnum.LONELY, NaturesEnum.DOCILE, NaturesEnum.MILD,
            NaturesEnum.GENTLE, NaturesEnum.HASTY,
        ]),
        StatsEnum.SPECIAL_ATTACK: frozenset([
            NaturesEnum.ADAMANT, NaturesEnum.IMPISH, NaturesEnum.BASHFUL,
            NaturesEnum.CAREFUL, NaturesEnum.JOLLY,
        ]),
        StatsEnum.SPECIAL_DEFENSE: frozenset([
            NaturesEnum.NAUGHTY, NaturesEnum.LAX, NaturesEnum.RASH,
            NaturesEnum.QUIRKY, NaturesEnum.NAIVE,
        ]),
        StatsEnum.SPEED: frozenset([
            NaturesEnum.BRAVE, NaturesEnum.RELAXED, NaturesEnum.QUIET,
            NaturesEnum.SASSY, NaturesEnum.SERIOUS,
        ]),
    }
    _INCREASES = {
        StatsEnum.HP: frozenset(),
        StatsEnum.ATTACK: frozenset([
            NaturesEnum.HARDY, NaturesEnum.LONELY, NaturesEnum.ADAMANT,
            NaturesEnum.NAUGHTY, NaturesEnum.BRAVE,
        ]),
        StatsEnum.DEFENSE: frozenset([
            NaturesEnum.BOLD, NaturesEnum.DOCILE, NaturesEnum.IMPISH,
            NaturesEnum.LAX, NaturesEnum.RELAXED,
        ]),
        StatsEnum.SPECIAL_ATTACK: frozenset([
            NaturesEnum.MODEST, NaturesEnum.MILD, NaturesEnum.BASHFUL,
            NaturesEnum.RASH, NaturesEnum.QUIET,
        ]),
        StatsEnum.SPECIAL_DEFENSE: frozenset([
            NaturesEnum.CALM, NaturesEnum.GENTLE, NaturesEnum.CAREFUL,
            NaturesEnum.QUIRKY, NaturesEnum.SASSY,
        ]),
        StatsEnum.SPEED: frozenset([
            NaturesEnum.TIMID, NaturesEnum.HASTY, NaturesEnum.JOLLY,
            NaturesEnum.NAIVE, NaturesEnum.SERIOUS,
        ]),
    }

    def __init__(self, nature: Union[NaturesEnum, str]):
        if isinstance(nature, str):
            nature = NaturesEnum[nature]
        if not isinstance(nature, NaturesEnum):
            raise TypeError('nature deve ser um NaturesEnum.')

        self._nature = nature
        self._stat_modifiers = self.calculate_stat_modifiers()

    def calculate_stat_modifiers(self) -> Dict[StatsEnum, float]:
        modifiers = {}
        for stat_enum in StatsEnum:
            modifiers[stat_enum] = 1.0
            if self._nature in self.increases[stat_enum]:
                modifiers[stat_enum] += 0.1
            if self._nature in self.decreases[stat_enum]:
                modifiers[stat_enum] -= 0.1

        return modifiers

    @property
    def increases(self) -> Dict[StatsEnum, List[NaturesEnum]]:
        return self._INCREASES

    @property
    def decreases(self) -> Dict[StatsEnum, List[NaturesEnum]]:
        return self._DECREASES

    @property
    def max_value(self) -> float:
        return 1.1

    @property
    def name(self) -> str:
        return self._nature.name

    @property
    def value(self) -> str:
        return self._nature.value

    def __str__(self):
        return f'{self._nature.value} ' + super().__str__()

    def __getitem__(self, key: StatsEnum) -> float:
        return self._stat_modifiers[key]

    def __setitem__(self, key: StatsEnum, value: int):
        raise AttributeError('Nature não pode ser alterada.')


if __name__ == '__main__':
    for nature_enum in NaturesEnum:
        nature = Nature(nature_enum)
        print(nature)
