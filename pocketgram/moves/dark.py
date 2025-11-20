from pocketgram.enums._types import TypesEnum
from pocketgram.enums.move_category import MoveCategoryEnum
from pocketgram.enums.move_name import MoveNameEnum
from pocketgram.moves.base_move import BaseMove


# =============================================================================
# GEN 1
# =============================================================================
class bite(BaseMove):
    def __init__(self, used_pp: int):
        description = 'An attack that may cause flinching.'

        super().__init__(
            name=MoveNameEnum.BITE.value,
            description=description,
            _type=TypesEnum.DARK,
            category=MoveCategoryEnum.PHYSICAL,
            used_pp=used_pp,
            max_pp=25,
            power=60,
            accuracy=100,
            priority=0,
            effect_list=None,
            makes_contact=True,
        )
