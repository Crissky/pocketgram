from enum import Enum
from typing import Tuple

from pocketgram.enums.stats import StatsEnum


class Stats:
    '''Classe base para os demais Stats

    `max_value` é o valor máximo que cada stat pode ter, exibido como "MAX".
    '''

    __slots__ = [
        'max_value', 'min_value'
    ] + [f'_{enum.name.lower()}' for enum in StatsEnum]

    def __init__(
        self,
        hp: int,
        attack: int,
        defense: int,
        special_attack: int,
        special_defense: int,
        speed: int,
        max_value: int,
        min_value: int = 0,
    ):
        if max_value <= 0:
            raise ValueError('max_value deve ser maior que 0.')
        if min_value >= max_value:
            raise ValueError(
                f'max_value deve ser maior que min_value. '
                f'max_value={max_value}, min_value={min_value}.'
            )

        self.max_value = int(max_value)
        self.min_value = int(min_value)
        self[StatsEnum.HP] = hp
        self[StatsEnum.ATTACK] = attack
        self[StatsEnum.DEFENSE] = defense
        self[StatsEnum.SPECIAL_ATTACK] = special_attack
        self[StatsEnum.SPECIAL_DEFENSE] = special_defense
        self[StatsEnum.SPEED] = speed

    @property
    def total(self) -> int:
        ''' Retorna a soma de todos os stats.
        '''

        return sum([
            self[enum_obj]
            for enum_class in self.get_set_classes
            for enum_obj in enum_class
        ])

    @property
    def stats_map(self) -> dict:
        ''' Retorna um dicionário com os nomes dos stats com base no StatsEnum.
        {<StatsEnum>: _StatsEnum.name.lower}
        '''

        return {
            enum_obj: f'_{enum_obj.name.lower()}'
            for enum_class in self.get_set_classes
            for enum_obj in enum_class
        }

    @property
    def get_set_classes(self) -> Tuple[Enum]:
        ''' Retorna uma tupla com as classes dos Enums usados nos Gets e Sets
        '''

        return (StatsEnum,)

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        stats_text = ', '.join([
            f'{enum_obj.value}={self[enum_obj]}'
            for enum_class in self.get_set_classes
            for enum_obj in enum_class
        ])
        return (
            f'{self.__class__.__name__}('
            f'{stats_text}, '
            f'MAX={self.max_value}, '
            f'MIN={self.min_value}, '
            f'TOTAL={self.total}'
            f')'
        )

    def __getitem__(self, key: StatsEnum):
        if not isinstance(key, self.get_set_classes):
            enum_names = '/'.join([e.__name__ for e in self.get_set_classes])
            error_text = f'Chave "{key}" não é do tipo {enum_names}.'

            raise TypeError(error_text)

        try:
            stat_name = self.stats_map[key]
            return getattr(self, stat_name)
        except KeyError:
            raise KeyError(f'Chave "{key}" não encontrada.')

    def __setitem__(self, key: StatsEnum, value: int):
        value = int(value)

        if not isinstance(key, self.get_set_classes):
            enum_names = '/'.join([e.__name__ for e in self.get_set_classes])
            error_text = f'Chave "{key}" não é do tipo {enum_names}.'

            raise TypeError(error_text)

        # Validando o range de value
        if value > self.max_value:
            raise ValueError(
                f'{key.value} não pode ser maior que {self.max_value}.'
            )
        elif value < self.min_value:
            raise ValueError(
                f'{key.value} não pode ser menor que {self.min_value}.'
            )

        try:
            stat_name = self.stats_map[key]
            setattr(self, stat_name, value)
        except KeyError:
            raise KeyError(f'Chave "{key}" não encontrada.')


if __name__ == '__main__':
    stats = Stats(100, 100, 100, 100, 100, 100, 100)
    print(stats)
    print(stats.stats_map)
    print('hp:', stats._hp)
    print('attack:', stats._attack)
    print('defense:', stats._defense)
    print('special_attack:', stats._special_attack)
    print('special_defense:', stats._special_defense)
    print('speed:', stats._speed)
