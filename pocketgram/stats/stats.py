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
        # Validações: todos os valores devem ser positivos.
        if hp < 0:
            raise ValueError('hp não pode ser um valor negativo.')
        if attack < 0:
            raise ValueError('attack não pode ser um valor negativo.')
        if defense < 0:
            raise ValueError('defense não pode ser um valor negativo.')
        if special_attack < 0:
            raise ValueError('special_attack não pode ser um valor negativo.')
        if special_defense < 0:
            raise ValueError('special_defense não pode ser um valor negativo.')
        if speed < 0:
            raise ValueError('speed não pode ser um valor negativo.')

        # Validações: todos os valores devem ser menor/igual que o max_value
        if max_value:
            if hp > max_value:
                raise ValueError('hp é maior que o max_value.')
            if attack > max_value:
                raise ValueError('attack é maior que o max_value.')
            if defense > max_value:
                raise ValueError('defense é maior que o max_value.')
            if special_attack > max_value:
                raise ValueError('special_attack é maior que o max_value.')
            if special_defense > max_value:
                raise ValueError('special_defense é maior que o max_value.')
            if speed > max_value:
                raise ValueError('speed é maior que o max_value.')

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

    def __getitem__(self, key: StatsEnum):
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


if __name__ == '__main__':
    stats = Stats(100, 100, 100, 100, 100, 100, 100)
    print(stats)
