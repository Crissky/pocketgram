
from random import randint

from pocketgram.stats.stats import Stats


class IVStats(Stats):
    '''IVs (Individual Values) dos stats que compõem o valor final dos Stats.
    Os IVs são valores aleatórios que variam entre 0-31.
    '''

    def __init__(
        self,
        hp: int = None,
        attack: int = None,
        defense: int = None,
        special_attack: int = None,
        special_defense: int = None,
        speed: int = None,
        random_init: bool = False
    ):
        if random_init is True:
            init_error = ''
            if hp is not None:
                init_error += f'hp ({hp}), '
            if attack is not None:
                init_error += f'attack ({attack}), '
            if defense is not None:
                init_error += f'defense ({defense}), '
            if special_attack is not None:
                init_error += f'special_attack ({special_attack}), '
            if special_defense is not None:
                init_error += f'special_defense ({special_defense}), '
            if speed is not None:
                init_error += f'speed ({speed}), '

            if init_error != '':
                init_error = init_error[:-2]
                raise ValueError(
                    f'Esses parâmetros não devem ser definidos junto com o '
                    f'random_init: {init_error}.'
                )

            hp = self.get_random_iv()
            attack = self.get_random_iv()
            defense = self.get_random_iv()
            special_attack = self.get_random_iv()
            special_defense = self.get_random_iv()
            speed = self.get_random_iv()

        if hp is None:
            raise ValueError('hp não foi definido.')
        if attack is None:
            raise ValueError('attack não foi definido.')
        if defense is None:
            raise ValueError('defense não foi definido.')
        if special_attack is None:
            raise ValueError('special_attack não foi definido.')
        if special_defense is None:
            raise ValueError('special_defense não foi definido.')
        if speed is None:
            raise ValueError('speed não foi definido.')

        super().__init__(
            hp=hp,
            attack=attack,
            defense=defense,
            special_attack=special_attack,
            special_defense=special_defense,
            speed=speed,
            max_value=31
        )

    def get_random_iv(self):
        return randint(0, 31)


if __name__ == '__main__':
    stats = IVStats(31, 0, 31, 31, 31, 31)
    print(stats)
    stats = IVStats(random_init=True)
    print(stats)
