from pocketgram.enum.stats import StatsEnum


class Stats:
    '''Classe base para os demais Stats'''

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
        if max_value:
            if max_value < hp:
                raise ValueError('hp é maior que o max_value')
            if max_value < attack:
                raise ValueError('attack é maior que o max_value')
            if max_value < defense:
                raise ValueError('defense é maior que o max_value')
            if max_value < special_attack:
                raise ValueError('special_attack é maior que o max_value')
            if max_value < special_defense:
                raise ValueError('special_defense é maior que o max_value')
            if max_value < speed:
                raise ValueError('speed é maior que o max_value')

        self.hp = int(hp)
        self.attack = int(attack)
        self.defense = int(defense)
        self.special_attack = int(special_attack)
        self.special_defense = int(special_defense)
        self.speed = int(speed)
        self.max_value = int(max_value)

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
            f'MAX={self.max_value})'
        )

    def __getitem__(self, key: str):
        key = key.upper()

        if key == StatsEnum.HP.name:
            return self.hp
        elif key == StatsEnum.ATTACK.name:
            return self.attack
        elif key == StatsEnum.DEFENSE.name:
            return self.defense
        elif key in StatsEnum.SPECIAL_ATTACK.name:
            return self.special_attack
        elif key in StatsEnum.SPECIAL_DEFENSE.name:
            return self.special_defense
        elif key == StatsEnum.SPEED.name:
            return self.speed
        else:
            raise KeyError(f'Chave "{key}" não encontrada.')

    def __setitem__(self, key: str, value: int):
        key = key.upper()
        value = int(value)

        if key == StatsEnum.HP.name:
            self.hp = value
        elif key == StatsEnum.ATTACK.name:
            self.attack = value
        elif key == StatsEnum.DEFENSE.name:
            self.defense = value
        elif key == StatsEnum.SPECIAL_ATTACK.name:
            self.special_attack = value
        elif key == StatsEnum.SPECIAL_DEFENSE.name:
            self.special_defense = value
        elif key == StatsEnum.SPEED.name:
            self.speed = value


if __name__ == '__main__':
    stats = Stats(100, 100, 100, 100, 100, 100, 100)
    print(stats)
