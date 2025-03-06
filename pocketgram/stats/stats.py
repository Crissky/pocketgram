from pocketgram.enum.stats import StatsEnum


class Stats:
    '''Classe base para os demais Stats

    `max_value` é o valor máximo que cada stat pode ter, exibido como "MAX".
    '''

    def __init__(
        self,
        hp: int,
        attack: int,
        defense: int,
        special_attack: int,
        special_defense: int,
        speed: int,
        max_value: int,
    ):

        self.max_value = int(max_value)
        self[StatsEnum.HP] = int(hp)
        self[StatsEnum.ATTACK] = int(attack)
        self[StatsEnum.DEFENSE] = int(defense)
        self[StatsEnum.SPECIAL_ATTACK] = int(special_attack)
        self[StatsEnum.SPECIAL_DEFENSE] = int(special_defense)
        self[StatsEnum.SPEED] = int(speed)

    @property
    def TOTAL(self) -> int:
        return int(
            self.hp +
            self.attack +
            self.defense +
            self.special_attack +
            self.special_defense +
            self.speed
        )

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return (
            f'{self.__class__.__name__}('
            f'{StatsEnum.HP.value}={self.hp}, '
            f'{StatsEnum.ATTACK.value}={self.attack}, '
            f'{StatsEnum.DEFENSE.value}={self.defense}, '
            f'{StatsEnum.SPECIAL_ATTACK.value}={self.special_attack}, '
            f'{StatsEnum.SPECIAL_DEFENSE.value}={self.special_defense}, '
            f'{StatsEnum.SPEED.value}={self.speed}, '
            f'MAX={self.max_value}, '
            f'TOTAL={self.TOTAL}'
            f')'
        )

    def __getitem__(self, key: StatsEnum):
        if not isinstance(key, StatsEnum):
            error_text = f'Chave "{key}" não é do tipo {StatsEnum.__name__}.'
            raise TypeError(error_text)

        if key == StatsEnum.HP:
            return self.hp
        elif key == StatsEnum.ATTACK:
            return self.attack
        elif key == StatsEnum.DEFENSE:
            return self.defense
        elif key in StatsEnum.SPECIAL_ATTACK:
            return self.special_attack
        elif key in StatsEnum.SPECIAL_DEFENSE:
            return self.special_defense
        elif key == StatsEnum.SPEED:
            return self.speed
        else:
            raise KeyError(f'Chave "{key}" não encontrada.')

    def __setitem__(self, key: StatsEnum, value: int):
        value = int(value)

        if not isinstance(key, StatsEnum):
            error_text = f'Chave "{key}" não é do tipo {StatsEnum.__name__}.'
            raise TypeError(error_text)

        # Não pode setar um valor maior que o max_value
        if value > self.max_value:
            raise ValueError(
                f'{key.value} não pode ser maior que {self.max_value}.'
            )
        # Não pode setar um valor negativo
        if value < 0:
            raise ValueError(f'{key.value} não pode ser negativo.')

        if key == StatsEnum.HP:
            self.hp = value
        elif key == StatsEnum.ATTACK:
            self.attack = value
        elif key == StatsEnum.DEFENSE:
            self.defense = value
        elif key == StatsEnum.SPECIAL_ATTACK:
            self.special_attack = value
        elif key == StatsEnum.SPECIAL_DEFENSE:
            self.special_defense = value
        elif key == StatsEnum.SPEED:
            self.speed = value
        else:
            raise KeyError(f'Chave "{key}" não encontrada.')


if __name__ == '__main__':
    stats = Stats(100, 100, 100, 100, 100, 100, 100)
    print(stats)
