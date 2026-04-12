from typing import TYPE_CHECKING

from pocketgram.stats.stats import Stats


if TYPE_CHECKING:
    from pocketgram.pocket_monster import PocketMonster


class BaseStats(Stats):
    """Valores base dos stats que compõem o valor final dos Stats."""

    def __init__(self, pocket_monster: "PocketMonster"):
        super().__init__(
            pocket_monster=pocket_monster, max_value=255, prefix="base_"
        )


if __name__ == "__main__":
    from types import SimpleNamespace
    from pocketgram.enums.stats import StatsEnum

    pm = SimpleNamespace(
        **{
            f"base_{s.name.lower()}": n*5
            for n, s in enumerate(StatsEnum, start=1)
        }
    )
    base_stats = BaseStats(pocket_monster=pm)
    for s in StatsEnum:
        print(s, base_stats[s])

    print(base_stats)
