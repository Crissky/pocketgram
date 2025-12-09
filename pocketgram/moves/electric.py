from pocketgram.enums._types import TypesEnum
from pocketgram.enums.move_category import MoveCategoryEnum
from pocketgram.enums.move_name import MoveNameEnum
from pocketgram.moves.base_move import BaseMove


# =============================================================================
# GEN 1
# =============================================================================
class thunder(BaseMove):
    def __init__(self, used_pp: int):
        description = 'An attack that may cause paralysis.'

        super().__init__(
            name=MoveNameEnum.THUNDER.value,
            description=description,
            _type=TypesEnum.ELECTRIC,
            category=MoveCategoryEnum.SPECIAL,
            used_pp=used_pp,
            max_pp=10,
            power=110,
            accuracy=70,
            priority=0,
            effect_list=None,
            makes_contact=False,
        )


class thunder_punch(BaseMove):
    def __init__(self, used_pp: int):
        description = 'An electric punch. It may paralyze.'

        super().__init__(
            name=MoveNameEnum.THUNDER_PUNCH.value,
            description=description,
            _type=TypesEnum.ELECTRIC,
            category=MoveCategoryEnum.PHYSICAL,
            used_pp=used_pp,
            max_pp=15,
            power=75,
            accuracy=100,
            priority=0,
            effect_list=None,
            makes_contact=True,
        )


class thunder_shock(BaseMove):
    ...


class thunder_wave(BaseMove):
    ...


class thunderbolt(BaseMove):
    ...
