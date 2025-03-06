from pocketgram.stats.stats import Stats


class BaseStats(Stats):
    '''Valores base dos stats que compõem o valor final dos Stats.
    '''

    def __init__(
        self,
        hp: int,
        attack: int,
        defense: int,
        special_attack: int,
        special_defense: int,
        speed: int,
    ):
        super().__init__(
            hp=hp,
            attack=attack,
            defense=defense,
            special_attack=special_attack,
            special_defense=special_defense,
            speed=speed,
            max_value=255
        )


if __name__ == '__main__':
    stats = BaseStats(35, 55, 40, 50, 50, 90)
    print(stats)
