from enum import Enum
from typing import Tuple, TYPE_CHECKING

from pocketgram.enums.stats import StatsEnum
from pocketgram.functions.enumeration import get_attr_name_from_enum

if TYPE_CHECKING:
    from pocketgram.pocket_monster import PocketMonster


class Stats:
    """Classe base para os demais Stats

    `max_value` é o valor máximo que cada stat pode ter, exibido como "MAX".
    """

    __slots__ = ["pocket_monster", "max_value", "min_value", "prefix", "sufix"]

    def __init__(
        self,
        pocket_monster: "PocketMonster",
        max_value: int,
        min_value: int = 0,
        prefix: str = "",
        sufix: str = "",
    ):
        if max_value <= 0:
            raise ValueError("max_value deve ser maior que 0.")
        if min_value >= max_value:
            raise ValueError(
                f"max_value deve ser maior que min_value. "
                f"max_value={max_value}, min_value={min_value}."
            )

        self.pocket_monster = pocket_monster
        self.max_value = int(max_value)
        self.min_value = int(min_value)
        self.prefix = prefix
        self.sufix = sufix
        self.check_stats()

    def check_stats(self):
        errors = []
        for enum_cls in self.get_set_classes:
            for enum in enum_cls:
                value = self[enum]
                if isinstance(value, (int)) and value > self.max_value:
                    errors.append(
                        f"{enum.name}={value} > MAX={self.max_value}"
                    )
                elif isinstance(value, (int)) and value < self.min_value:
                    errors.append(
                        f"{enum.name}={value} > MIN={self.min_value}"
                    )
                elif not isinstance(value, (int, type(None))):
                    errors.append(f"{enum.name}={value} is not int")

        if errors:
            raise ValueError(
                f"{self.__class__.__name__} Error: "
                f"Os seguintes stats estão fora do intervalo "
                f"[{self.min_value}, {self.max_value}]:\n\t"
                + "\n\t".join(errors)
            )

    @property
    def total(self) -> int:
        """Retorna a soma de todos os stats."""

        return sum(
            [
                self[enum_obj]
                for enum_class in self.get_set_classes
                for enum_obj in enum_class
            ]
        )

    @property
    def stats_map(self) -> dict:
        """Retorna um dicionário com os nomes dos stats com base no StatsEnum.
        {<StatsEnum>: _StatsEnum.name.lower}
        """

        return {
            enum_obj: get_attr_name_from_enum(
                enum_obj, prefix=self.prefix, sufix=self.sufix
            )
            for enum_class in self.get_set_classes
            for enum_obj in enum_class
        }

    @property
    def get_set_classes(self) -> Tuple[Enum]:
        """Retorna uma tupla com as classes dos Enums usados nos Gets e Sets"""

        return (StatsEnum,)

    @property
    def stats_text(self):
        """Retorna uma string com os stats e seus valores,
        separados por vírgula.
        """

        return ", ".join(
            [
                f"{enum_obj.value}={self[enum_obj]}"
                for enum_class in self.get_set_classes
                for enum_obj in enum_class
            ]
        )

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return (
            f"{self.__class__.__name__}("
            f"{self.stats_text}, "
            f"MAX={self.max_value}, "
            f"MIN={self.min_value}, "
            f"TOTAL={self.total}"
            f")"
        )

    def __getitem__(self, key: StatsEnum):
        if not isinstance(key, self.get_set_classes):
            enum_names = "/".join([e.__name__ for e in self.get_set_classes])
            error_text = f'Chave "{key}" não é do tipo {enum_names}.'

            raise TypeError(error_text)

        try:
            stat_name = self.stats_map[key]
            return getattr(self.pocket_monster, stat_name)
        except KeyError:
            raise KeyError(f'Chave "{key}" não encontrada.')

    def __setitem__(self, key: StatsEnum, value: int):
        value = int(value)

        if not isinstance(key, self.get_set_classes):
            enum_names = "/".join([e.__name__ for e in self.get_set_classes])
            error_text = f'Chave "{key}" não é do tipo {enum_names}.'

            raise TypeError(error_text)

        # Validando o range de value
        if value > self.max_value:
            raise ValueError(
                f"{key.value} não pode ser maior que {self.max_value}."
            )
        elif value < self.min_value:
            raise ValueError(
                f"{key.value} não pode ser menor que {self.min_value}."
            )

        try:
            stat_name = self.stats_map[key]
            setattr(self.pocket_monster, stat_name, value)
        except KeyError:
            raise KeyError(f'Chave "{key}" não encontrada.')


if __name__ == "__main__":
    from types import SimpleNamespace

    pm = SimpleNamespace(
        **{s.name.lower(): n for n, s in enumerate(StatsEnum, start=1)}
    )
    stats = Stats(pocket_monster=pm, max_value=31)
    for s in StatsEnum:
        print(s, stats[s])

    print(stats)
