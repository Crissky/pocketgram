import logging
from typing import TYPE_CHECKING

from pocketgram.enums.stats import StatsEnum
from pocketgram.stats.stats import Stats


if TYPE_CHECKING:
    from pocketgram.pocket_monster import PocketMonster


logger = logging.getLogger(__name__)


class EVStats(Stats):
    '''EVs (Effort Values) dos stats que compõem o valor final dos Stats.
    Os EVs são valores que iniciam em zero e podem ir até 255.
    '''

    def __init__(self, pocket_monster: "PocketMonster"):
        super().__init__(
            pocket_monster=pocket_monster, max_value=255, prefix="ev_"
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
        return self.total

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
            logger.warning(warning_text)
            return None

        self[key] += value


if __name__ == '__main__':
    from types import SimpleNamespace

    pm = SimpleNamespace(
        **{
            f"ev_{s.name.lower()}": n*10
            for n, s in enumerate(StatsEnum, start=1)
        }
    )
    ev_stats = EVStats(pocket_monster=pm)
    for s in StatsEnum:
        print(s, ev_stats[s])

    print(ev_stats)
