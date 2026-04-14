
from random import randint, choices
from typing import TYPE_CHECKING

from pocketgram.enums.stats import StatsEnum
from pocketgram.stats.stats import Stats


if TYPE_CHECKING:
    from pocketgram.pocket_monster import PocketMonster


class IVStats(Stats):
    '''IVs (Individual Values) dos stats que compõem o valor final dos Stats.
    Os IVs são valores aleatórios que variam entre 0-31.
    '''

    def __init__(
        self,
        pocket_monster: "PocketMonster",
        random_init: bool = False
    ):
        super().__init__(
            pocket_monster=pocket_monster,
            max_value=31,
            prefix='iv_'
        )
        if random_init is True:
            init_error = ''
            if self[StatsEnum.HP] is not None:
                init_error += f'hp={self[StatsEnum.HP]}, '
            if self[StatsEnum.ATTACK] is not None:
                init_error += f'attack={self[StatsEnum.ATTACK]}, '
            if self[StatsEnum.DEFENSE] is not None:
                init_error += f'defense={self[StatsEnum.DEFENSE]}, '
            if self[StatsEnum.SPECIAL_ATTACK] is not None:
                init_error += f'special_attack={self[StatsEnum.SPECIAL_ATTACK]}, '
            if self[StatsEnum.SPECIAL_DEFENSE] is not None:
                init_error += f'special_defense={self[StatsEnum.SPECIAL_DEFENSE]}, '
            if self[StatsEnum.SPEED] is not None:
                init_error += f'speed={self[StatsEnum.SPEED]}, '

            if init_error != '':
                init_error = init_error[:-2]
                raise ValueError(
                    f'Esses parâmetros não devem ser definidos junto com o '
                    f'random_init: {init_error}.'
                )

            self[StatsEnum.HP] = self.get_random_iv()
            self[StatsEnum.ATTACK] = self.get_random_iv()
            self[StatsEnum.DEFENSE] = self.get_random_iv()
            self[StatsEnum.SPECIAL_ATTACK] = self.get_random_iv()
            self[StatsEnum.SPECIAL_DEFENSE] = self.get_random_iv()
            self[StatsEnum.SPEED] = self.get_random_iv()

        init_stats_error = ''
        if self[StatsEnum.HP] is None:
            init_stats_error += 'hp, '
        if self[StatsEnum.ATTACK] is None:
            init_stats_error += 'attack, '
        if self[StatsEnum.DEFENSE] is None:
            init_stats_error += 'defense, '
        if self[StatsEnum.SPECIAL_ATTACK] is None:
            init_stats_error += 'special_attack, '
        if self[StatsEnum.SPECIAL_DEFENSE] is None:
            init_stats_error += 'special_defense, '
        if self[StatsEnum.SPEED] is None:
            init_stats_error += 'speed, '
        if init_stats_error != '':
            raise ValueError(
                f'Os seguintes parâmetros não foram definidos: '
                f'{init_stats_error[:-2]}.'
            )

    def get_random_iv(self):
        values = list(range(32))
        weights = [i+v for i, v in enumerate(values, start=1)]

        return choices(values, weights=weights)[0]


if __name__ == '__main__':
    from types import SimpleNamespace
    pm = SimpleNamespace(
        **{
            f"iv_{s.name.lower()}": n*6
            for n, s in enumerate(StatsEnum, start=1)
        }
    )
    pm_none = SimpleNamespace(
        **{
            f"iv_{s.name.lower()}": None for s in StatsEnum
        }
    )

    iv_stats = IVStats(pocket_monster=pm)
    for s in StatsEnum:
        print(s, iv_stats[s])

    print(iv_stats)

    iv_stats_none = IVStats(pocket_monster=pm_none, random_init=True)
    for s in StatsEnum:
        print(s, iv_stats_none[s])

    print(iv_stats_none)