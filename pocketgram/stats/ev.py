import logging
from pocketgram.enum.stats import StatsEnum
from pocketgram.stats.stats import Stats


logging.basicConfig(
    format='(%(asctime)s) - %(levelname)s - %(message)s',
    datefmt='%d/%m/%y %H:%M:%S'
)


class EVStats(Stats):
    '''EVs (Effort Values) dos stats que compõem o valor final dos Stats.
    Os EVs são valores que iniciam em zero e podem ir até 255.
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

        if self.current_ev > self.MAX_EV:
            raise ValueError(
                f'O valor total dos EVs não pode ser maior que 510. '
                f'Valor atual: {self.current_ev}.'
            )

    @property
    def MAX_EV(self) -> int:
        return 510

    @property
    def current_ev(self) -> int:
        return int(
            self.hp +
            self.attack +
            self.defense +
            self.special_attack +
            self.special_defense +
            self.speed
        )

    @property
    def remaining_ev(self) -> int:
        return self.MAX_EV - self.current_ev

    @property
    def show_ev(self) -> str:
        return (
            f'EVs: {self.current_ev}/{self.MAX_EV}'
            f'({self.remaining_ev} restantes)'
        )

    def add_ev(self, key: StatsEnum, value: int):
        value = int(value)

        if value < 0:
            raise ValueError('O valor do EV não pode ser negativo.')
        if value > self.remaining_ev:
            warning_text = (
                f'O valor não pode ser maior que o valor restante do EV.'
                f'\nValor: {value}.'
                f'\n{self.show_ev}.'
            )
            logging.warning(warning_text)
            return None

        self[key] += value


if __name__ == '__main__':
    stats = EVStats(0, 0, 0, 0, 0, 0)
    print(stats)
    print('remaining_ev:', stats.remaining_ev)
    stats = EVStats(100, 100, 100, 100, 100, 0)
    print(stats)
    print('remaining_ev:', stats.remaining_ev)
    stats.add_ev(StatsEnum.HP, 10)
