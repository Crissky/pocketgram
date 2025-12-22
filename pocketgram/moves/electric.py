from pocketgram.enums._types import TypesEnum
from pocketgram.enums.move_category import MoveCategoryEnum
from pocketgram.enums.move_name import MoveNameEnum
from pocketgram.moves.base_move import BaseMove


# =============================================================================
# GEN 1
# =============================================================================
class thunder(BaseMove):
    def __init__(self, used_pp: int):
        description = (
            "A wicked thunderbolt is dropped on the target to inflict damage. "
            "This may also leave the target with paralysis."
        )

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
        description = (
            "The target is attacked with an electrified punch. "
            "This may also leave the target with paralysis."
        )

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
    def __init__(self, used_pp: int):
        description = (
            "The user attacks the target with a jolt of "
            "electricity. This may also leave the target with paralysis."
        )

        super().__init__(
            name=MoveNameEnum.THUNDER_SHOCK.value,
            description=description,
            _type=TypesEnum.ELECTRIC,
            category=MoveCategoryEnum.SPECIAL,
            used_pp=used_pp,
            max_pp=30,
            power=40,
            accuracy=100,
            priority=0,
            effect_list=None,
            makes_contact=False,
        )


class thunder_wave(BaseMove):
    def __init__(self, used_pp: int):
        description = (
            "The user launches a weak jolt of electricity "
            "that paralyzes the target."
        )

        super().__init__(
            name=MoveNameEnum.THUNDER_WAVE.value,
            description=description,
            _type=TypesEnum.ELECTRIC,
            category=MoveCategoryEnum.STATUS,
            used_pp=used_pp,
            max_pp=20,
            power=None,
            accuracy=90,
            priority=0,
            effect_list=None,
            makes_contact=False,
        )


class thunderbolt(BaseMove):
    def __init__(self, used_pp: int):
        description = (
            "The user attacks the target with a strong electric "
            "blast. This may also leave the target with paralysis."
        )

        super().__init__(
            name=MoveNameEnum.THUNDERBOLT.value,
            description=description,
            _type=TypesEnum.ELECTRIC,
            category=MoveCategoryEnum.SPECIAL,
            used_pp=used_pp,
            max_pp=15,
            power=90,
            accuracy=100,
            priority=0,
            effect_list=None,
            makes_contact=False,
        )
