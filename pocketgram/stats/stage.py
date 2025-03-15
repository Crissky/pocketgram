from enum import Enum
from typing import Tuple
from pocketgram.enums.stats import BattleStatsEnum
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
