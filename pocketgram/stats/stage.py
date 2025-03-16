from enum import Enum
from typing import Tuple, Union

from pocketgram.enums.stats import BattleStatsEnum, StatsEnum
from pocketgram.stats.stats import Stats


class StageStats(Stats):
    '''Stage Stats representam as estatísticas que aumentam ou diminuem
    durante a batalha.

    Cada stat pode aumentar no máximo em +6 estágios e
    diminuir no máximo -6 estágios.
    '''

    def __init__(
        self,
        hp: int = 0,
        attack: int = 0,
        defense: int = 0,
        special_attack: int = 0,
        special_defense: int = 0,
        speed: int = 0,
        accuracy: int = 0,
        evasiveness: int = 0,
    ):
        super().__init__(
            hp=hp,
            attack=attack,
            defense=defense,
            special_attack=special_attack,
            special_defense=special_defense,
            speed=speed,
            max_value=6,
            min_value=-6
        )
        self[BattleStatsEnum.ACCURACY] = accuracy
        self[BattleStatsEnum.EVASIVENESS] = evasiveness

    @property
    def get_set_classes(self) -> Tuple[Enum]:
        ''' Retorna uma tupla com as classes dos Enums usados nos Gets e Sets
        '''

        super_enum = super().get_set_classes

        return (*super_enum, BattleStatsEnum)

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
            raise ValueError('HP não possui multiplicador.')

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
    stats = StageStats(
        hp=-1,
        attack=0,
        defense=1,
        special_attack=2,
        special_defense=3,
        speed=4,
        accuracy=5,
        evasiveness=6,
    )
    print(stats)
