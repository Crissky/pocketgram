from pocketgram.enums._types import TypesEnum
from pocketgram.enums.move_category import MoveCategoryEnum
from pocketgram.enums.move_name import MoveNameEnum
from pocketgram.move_effects.drain_move_effect import HalfDrainMoveEffect
from pocketgram.moves.base_move import BaseMove


# =============================================================================
# GEN 1
# =============================================================================
class leech_life(BaseMove):
    def __init__(self, used_pp: int):
        description = (
            "The user drains the target’s blood. "
            "The user’s HP is restored by up to half "
            "the damage taken by the target."
        )

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
            effect_list=[HalfDrainMoveEffect],
            makes_contact=True,
        )


class pin_missile(BaseMove):
    def __init__(self, used_pp: int):
        description = (
            "The user attacks by shooting sharp spikes at the target. "
            "This move hits two to five times in a row."
        )

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
        description = (
            "The user blows silk from its mouth that binds "
            "opposing Pokémon and harshly lowers their Speed stats."
        )

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
        description = (
            "This move can’t be used. It’s recommended that this "
            "move is forgotten. Once forgotten, this move can’t be remembered."
        )

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
