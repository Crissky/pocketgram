from enum import Enum
from typing import TYPE_CHECKING, Tuple, Union

from pocketgram.enums.stats import BattleStatsEnum, StatsEnum
from pocketgram.stats.stats import Stats


if TYPE_CHECKING:
    from pocketgram.pocket_monster import PocketMonster


class StageStats(Stats):
    '''Stage Stats representam as estatísticas que aumentam ou diminuem
    durante a batalha.

    Cada stat pode aumentar no máximo em +6 estágios e
    diminuir no máximo -6 estágios.
    '''

    def __init__(self, pocket_monster: "PocketMonster"):
        super().__init__(
            pocket_monster=pocket_monster,
            max_value=6,
            min_value=-6,
            prefix="stage_"
        )

    @property
    def get_set_classes(self) -> Tuple[Enum]:
        ''' Retorna uma tupla com as classes dos Enums usados nos Gets e Sets
        '''

        super_get_set_classes = super().get_set_classes

        return (*super_get_set_classes, BattleStatsEnum)

    @property
    def stats_text(self):
        ''' Retorna uma string com os stats e seus valores,
        separados por vírgula.
        '''

        return ', '.join([
            f'{enum_obj.value}={self[enum_obj]:+}'
            for enum_class in self.get_set_classes
            for enum_obj in enum_class
        ])

    def get_multiplier(
        self,
        stat_enum: Union[StatsEnum, BattleStatsEnum]
    ) -> float:
        ''' Retorna o multiplicador do stat.
        '''

        if stat_enum == StatsEnum.HP:
            return 1.0

        stat = self[stat_enum]
        if isinstance(stat_enum, StatsEnum):
            plus = 2.0
        elif isinstance(stat_enum, BattleStatsEnum):
            plus = 3.0

        stat_plus = abs(stat) + plus
        stat_multiplier = (
            stat_plus / plus
            if stat >= 0
            else plus / stat_plus
        )

        return stat_multiplier


if __name__ == '__main__':
    from itertools import chain
    from types import SimpleNamespace

    pm = SimpleNamespace(
        **{
            f"stage_{s.name.lower()}": n
            for n, s in enumerate(chain(StatsEnum, BattleStatsEnum), start=-2)
        }
    )
    stage_stats = StageStats(pocket_monster=pm)
    for s in chain(StatsEnum, BattleStatsEnum):
        print(s, stage_stats[s])
        print('MULTIPLIER', s.name, stage_stats.get_multiplier(s))

    print(stage_stats)
