from dataclasses import dataclass
from math import floor
from typing import List, Union

from pocketgram._types import Types
from pocketgram.enums._types import TypesEnum
from pocketgram.enums.form import FormEnum
from pocketgram.enums.natures import NaturesEnum
from pocketgram.enums.pocket_monster import PocketMonsterParamEnum
from pocketgram.enums.stats import StatsEnum
from pocketgram.functions.enumeration import get_attr_name_from_enum
from pocketgram.stats.base import BaseStats
from pocketgram.stats.ev import EVStats
from pocketgram.stats.iv import IVStats
from pocketgram.stats.nature import Nature
from pocketgram.stats.stage import StageStats
from repository.mongo.base import MongoBase


GET_AND_SET_ENUM_CLASSES = Union[StatsEnum, PocketMonsterParamEnum]


@dataclass
class PocketMonster(MongoBase):
    number: Union[int, str]
    level: int
    name: str
    nature: Union[NaturesEnum, str]
    _types: Union[List[Union[TypesEnum, str]]]
    base_hp: int
    base_attack: int
    base_defense: int
    base_special_attack: int
    base_special_defense: int
    base_speed: int
    ev_hp: int
    ev_attack: int
    ev_defense: int
    ev_special_attack: int
    ev_special_defense: int
    ev_speed: int
    iv_hp: int = None
    iv_attack: int = None
    iv_defense: int = None
    iv_special_attack: int = None
    iv_special_defense: int = None
    iv_speed: int = None
    iv_random_init: bool = False
    stage_hp: int = 0
    stage_attack: int = 0
    stage_defense: int = 0
    stage_special_attack: int = 0
    stage_special_defense: int = 0
    stage_speed: int = 0
    stage_accuracy: int = 0
    stage_evasiveness: int = 0
    nickname: str = None
    form: Union[FormEnum, str] = None
    damage_points: int = 0

    def __post_init__(self):
        super().__post_init__()
        
        if isinstance(self.form, str):
            self.form = FormEnum[self.form]
        if not isinstance(self._types, list):
            self._types = [self._types]
        pmpe = PocketMonsterParamEnum

        self[pmpe.NUMBER] = int(self.number)
        self[pmpe.LEVEL] = self.level
        self[pmpe.NAME] = self.name
        self[pmpe.NICKNAME] = self.nickname
        self[pmpe.NATURE] = Nature(nature=self.nature)
        self[pmpe.TYPES] = Types(*self._types)
        self[pmpe.FORM] = self.form
        self.damage_points = self.damage_points

        self[pmpe.BASE_STATS] = BaseStats(pocket_monster=self)
        self[pmpe.EV_STATS] = EVStats(pocket_monster=self)
        self[pmpe.IV_STATS] = IVStats(
            pocket_monster=self,
            random_init=self.iv_random_init
        )
        self[pmpe.STAGE_STATS] = StageStats(pocket_monster=self)

    def add_damage(self, damage: int) -> int:
        if damage < 0:
            raise ValueError('Damage precisa ser um inteiro positivo.')

        total_damage = min(self.damage_points + damage, self[StatsEnum.HP])
        difference = total_damage - self.damage_points
        self.damage_points = total_damage

        return difference

    def heal_damage(self, heal: int) -> int:
        if heal < 0:
            raise ValueError('Heal precisa ser um inteiro positivo.')

        total_heal = min(self.damage_points, heal)
        self.damage_points = max(self.damage_points - total_heal, 0)

        return total_heal

    @property
    def display_name(self) -> str:
        return (
            self[PocketMonsterParamEnum.NICKNAME]
            or
            self[PocketMonsterParamEnum.NAME]
        )

    @property
    def display_number(self) -> str:
        return f'{self[PocketMonsterParamEnum.NUMBER]:04d}'

    @property
    def total(self) -> int:
        ''' Retorna a soma de todos os stats.
        '''

        return sum([self[enum] for enum in StatsEnum])

    @property
    def primary_type(self) -> TypesEnum:
        return self[PocketMonsterParamEnum.TYPES].primary

    @property
    def secondary_type(self) -> TypesEnum:
        return self[PocketMonsterParamEnum.TYPES].secondary

    @property
    def current_hp(self) -> int:
        return max(self[StatsEnum.HP] - self.damage_points, 0)

    @property
    def current_hp_percent(self) -> float:
        return self.current_hp / self[StatsEnum.HP]

    @property
    def hp_text(self) -> str:
        return f'{self.current_hp}/{self[StatsEnum.HP]}'

    @property
    def is_alive(self) -> bool:
        return self.current_hp > 0

    # HP = floor(
        # 0.01 x (2 x Base + IV + floor(0.25 x EV)) x Level) + Level + 10
    # Other Stats = (floor(
        # 0.01 x (2 x Base + IV + floor(0.25 x EV)) x Level) + 5) x Nature
    def __get_stats(self, key):
        base = self[PocketMonsterParamEnum.BASE_STATS][key]
        ev = floor(0.25 * self[PocketMonsterParamEnum.EV_STATS][key])
        iv = self[PocketMonsterParamEnum.IV_STATS][key]
        level = self[PocketMonsterParamEnum.LEVEL]
        plus_value = level + 10 if key == StatsEnum.HP else 5
        nature = self[PocketMonsterParamEnum.NATURE][key]
        stat = (2 * base) + iv + ev

        result = floor(0.01 * stat * level)
        result = (result + plus_value) * nature

        return int(result)

    def __getitem__(self, key: GET_AND_SET_ENUM_CLASSES) -> int:
        if isinstance(key, StatsEnum):
            return self.__get_stats(key)
        elif key == PocketMonsterParamEnum.TYPE_1:
            return self[PocketMonsterParamEnum.TYPES].primary
        elif key == PocketMonsterParamEnum.TYPE_2:
            return self[PocketMonsterParamEnum.TYPES].secondary
        elif isinstance(key, PocketMonsterParamEnum):
            return getattr(self, get_attr_name_from_enum(key))
        else:
            raise TypeError(
                f'Chave "{key}" não é do tipo '
                f'{StatsEnum.__name__}/{PocketMonsterParamEnum.__name__}.'
            )

    def __setitem__(self, key: GET_AND_SET_ENUM_CLASSES, value: int) -> int:
        if isinstance(key, StatsEnum):
            raise AttributeError(
                f'Não é possível alterar o valor de {key.value}.'
            )
        elif isinstance(key, PocketMonsterParamEnum):
            setattr(self, get_attr_name_from_enum(key), value)

    def __str__(self):
        stats_text = ', '.join([f'{e.value}={self[e]}' for e in StatsEnum])
        form = self[PocketMonsterParamEnum.FORM]
        form_text = f'form={form.value}, ' if form else ''
        form_text = form_text.format(
            pocket_monster=self[PocketMonsterParamEnum.NAME]
        )
        return (
            f'{self.__class__.__name__}('
            f'number={self.display_number}, '
            f'level={self[PocketMonsterParamEnum.LEVEL]}, '
            f'name={self[PocketMonsterParamEnum.NAME]}, '
            f'{form_text}'
            f'nickname={self[PocketMonsterParamEnum.NICKNAME]}, '
            f'nature={self[PocketMonsterParamEnum.NATURE].value}, '
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
    print('base_stats:', pm1[PocketMonsterParamEnum.BASE_STATS])
    print('iv_stats:', pm1[PocketMonsterParamEnum.IV_STATS])
    print('ev_stats:', pm1[PocketMonsterParamEnum.EV_STATS])
    print(pm1)
    print(pm2)
