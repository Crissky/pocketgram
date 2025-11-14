from pocketgram.enums._types import TypesEnum
from pocketgram.enums.move_category import MoveCategoryEnum
from pocketgram.enums.move_name import MoveNameEnum
from pocketgram.moves.base_move import BaseMove


# GEN 1
class leech_life(BaseMove):
    def __init__(self, used_pp: int):
        description = 'Steals 1/2 of the damage inflicted.'

        super().__init__(
            name=MoveNameEnum.LEECH_LIFE.value,
            description=description,
            _type=TypesEnum.BUG,
            category=MoveCategoryEnum.PHYSICAL,
            used_pp=used_pp,
            max_pp=10,
            power=80,
            accuracy=100,
            priority=0,
            effect_list=None,
            makes_contact=True,
        )


class pin_missile(BaseMove):
    ...


class string_shot(BaseMove):
    ...


class twineedle(BaseMove):
    ...
