from math import floor
from typing import List, Union

from pocketgram._types import Types
from pocketgram.enums._types import TypesEnum
from pocketgram.enums.form import FormEnum
from pocketgram.enums.natures import NaturesEnum
from pocketgram.enums.stats import StatsEnum
from pocketgram.stats.base import BaseStats
from pocketgram.stats.ev import EVStats
from pocketgram.stats.iv import IVStats
from pocketgram.stats.nature import Nature
from pocketgram.stats.stage import StageStats


class PocketMonster:
    def __init__(
        self,
        number: int,
        level: int,
        name: str,
        nickname: str,
        nature: Union[NaturesEnum, str],
        _types: Union[List[Union[TypesEnum, str]], Union[TypesEnum, str]],
        base_hp: int,
        base_attack: int,
        base_defense: int,
        base_special_attack: int,
        base_special_defense: int,
        base_speed: int,
        ev_hp: int,
        ev_attack: int,
        ev_defense: int,
        ev_special_attack: int,
        ev_special_defense: int,
        ev_speed: int,
        iv_hp: int = None,
        iv_attack: int = None,
        iv_defense: int = None,
        iv_special_attack: int = None,
        iv_special_defense: int = None,
        iv_speed: int = None,
        iv_random_init: bool = False,
        stage_hp: int = 0,
        stage_attack: int = 0,
        stage_defense: int = 0,
        stage_special_attack: int = 0,
        stage_special_defense: int = 0,
        stage_speed: int = 0,
        stage_accuracy: int = 0,
        stage_evasiveness: int = 0,
        form: Union[FormEnum, str] = None,
    ):
        check_form = isinstance(form, FormEnum) or form is None
        self._number = number
        self.level = level
        self._name = name
        self._nickname = nickname
        self._nature = Nature(nature=nature)
        _types = _types if isinstance(_types, list) else [_types]
        self._types = Types(*_types)
        self._form = form if check_form else FormEnum[form]

        self._base_stats = BaseStats(
            hp=base_hp,
            attack=base_attack,
            defense=base_defense,
            special_attack=base_special_attack,
            special_defense=base_special_defense,
            speed=base_speed,
        )
        self._ev_stats = EVStats(
            hp=ev_hp,
            attack=ev_attack,
            defense=ev_defense,
            special_attack=ev_special_attack,
            special_defense=ev_special_defense,
            speed=ev_speed,
        )
        self._iv_stats = IVStats(
            hp=iv_hp,
            attack=iv_attack,
            defense=iv_defense,
            special_attack=iv_special_attack,
            special_defense=iv_special_defense,
            speed=iv_speed,
            random_init=iv_random_init,
        )
        self._stage_stats = StageStats(
            hp=stage_hp,
            attack=stage_attack,
            defense=stage_defense,
            special_attack=stage_special_attack,
            special_defense=stage_special_defense,
            speed=stage_speed,
            accuracy=stage_accuracy,
            evasiveness=stage_evasiveness,
        )

    @property
    def name(self) -> str:
        return self._nickname or self._name

    @property
    def number(self) -> str:
        return f'{self._number:03d}'

    @property
    def total(self) -> int:
        ''' Retorna a soma de todos os stats.
        '''

        return sum([self[enum] for enum in StatsEnum])

    # HP = floor(
        # 0.01 x (2 x Base + IV + floor(0.25 x EV)) x Level) + Level + 10
    # Other Stats = (floor(
        # 0.01 x (2 x Base + IV + floor(0.25 x EV)) x Level) + 5) x Nature
    def __getitem__(self, key: StatsEnum) -> int:
        base = self._base_stats[key]
        ev = floor(0.25 * self._ev_stats[key])
        iv = self._iv_stats[key]
        level = self.level
        plus_value = level + 10 if key == StatsEnum.HP else 5
        nature = self._nature[key]
        stat = (2 * base) + iv + ev

        result = floor(0.01 * stat * level)
        result = (result + plus_value) * nature

        return int(result)

    def __str__(self):
        stats_text = ', '.join([f'{e.value}={self[e]}' for e in StatsEnum])
        form_text = f'form={self._form.value}, ' if self._form else ''
        form_text = form_text.format(pocket_monster=self._name)
        return (
            f'{self.__class__.__name__}('
            f'number={self.number}, '
            f'level={self.level}, '
            f'name={self._name}, '
            f'{form_text}'
            f'nickname={self._nickname}, '
            f'nature={self._nature.value}, '
            f'{stats_text}, '
            f'TOTAL={self.total}'
            f')'
        )

    def __repr__(self):
        return self.__str__()


if __name__ == '__main__':
    pika_stats = dict(
        base_hp=35, base_attack=55, base_defense=40,
        base_special_attack=50, base_special_defense=50, base_speed=90,
        ev_hp=85, ev_attack=85, ev_defense=85,
        ev_special_attack=85, ev_special_defense=85, ev_speed=85,
        iv_hp=31, iv_attack=31, iv_defense=31, iv_special_attack=31,
        iv_special_defense=31, iv_speed=31,
    )
    pm1 = PocketMonster(
        number=25,
        level=100,
        name='Pikachu',
        nickname='Pika Modesta',
        nature=NaturesEnum.MODEST,
        _types=TypesEnum.ELECTRIC,
        **pika_stats
    )
    pm2 = PocketMonster(
        number=25,
        level=100,
        name='Pikachu',
        nickname='Pika Durinha',
        nature=NaturesEnum.HARDY,
        _types=TypesEnum.ELECTRIC,
        form=FormEnum.PARTNER,
        **pika_stats
    )
    print('base_stats:', pm1._base_stats)
    print('iv_stats:', pm1._iv_stats)
    print('ev_stats:', pm1._ev_stats)
    print(pm1)
    print(pm2)
