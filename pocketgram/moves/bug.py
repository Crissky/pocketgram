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
    def __init__(self, used_pp: int):
        description = 'Fires pins that strike 2-5 times.'

        super().__init__(
            name=MoveNameEnum.PIN_MISSILE.value,
            description=description,
            _type=TypesEnum.BUG,
            category=MoveCategoryEnum.PHYSICAL,
            used_pp=used_pp,
            max_pp=20,
            power=25,
            accuracy=95,
            priority=0,
            effect_list=None,
            makes_contact=False,
        )


class string_shot(BaseMove):
    def __init__(self, used_pp: int):
        description = 'A move that lowers the foe’s SPEED.'

        super().__init__(
            name=MoveNameEnum.STRING_SHOT.value,
            description=description,
            _type=TypesEnum.BUG,
            category=MoveCategoryEnum.STATUS,
            used_pp=used_pp,
            max_pp=40,
            power=None,
            accuracy=95,
            priority=0,
            effect_list=None,
            makes_contact=False,
        )


class twineedle(BaseMove):
    def __init__(self, used_pp: int):
        description = 'Jabs the foe twice using stingers.'

        super().__init__(
            name=MoveNameEnum.TWINEEDLE.value,
            description=description,
            _type=TypesEnum.BUG,
            category=MoveCategoryEnum.PHYSICAL,
            used_pp=used_pp,
            max_pp=20,
            power=25,
            accuracy=100,
            priority=0,
            effect_list=None,
            makes_contact=False,
        )
