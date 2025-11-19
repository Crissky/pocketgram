from pocketgram.enums._types import TypesEnum
from pocketgram.enums.move_category import MoveCategoryEnum
from pocketgram.enums.move_name import MoveNameEnum
from pocketgram.moves.base_move import BaseMove


# =============================================================================
# GEN 1
# =============================================================================
class dragon_rage(BaseMove):
    def __init__(self, used_pp: int):
        description = 'Always inflicts 40HP damage.'

        super().__init__(
            name=MoveNameEnum.DRAGON_RAGE.value,
            description=description,
            _type=TypesEnum.DRAGON,
            category=MoveCategoryEnum.SPECIAL,
            used_pp=used_pp,
            max_pp=10,
            power=None,
            accuracy=100,
            priority=0,
            effect_list=None,
            makes_contact=False,
        )
