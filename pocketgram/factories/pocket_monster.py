from typing import Union

from pocketgram.constants.pocket_monster import POCKET_MONSTERS_DICT
from pocketgram.enums.form import FormEnum
from pocketgram.enums.natures import NaturesEnum
from pocketgram.enums.stats import StatsEnum
from pocketgram.pocket_monster import PocketMonster


def pocket_monster_factory(
    number: int,
    level: int,
    nature: Union[NaturesEnum, str],
    ev_hp: int,
    ev_attack: int,
    ev_defense: int,
    ev_special_attack: int,
    ev_special_defense: int,
    ev_speed: int,
    iv_hp: int = None,
    iv_attack: int = None,
    iv_defense: int = None,
    iv_special_attack: int = None,
    iv_special_defense: int = None,
    iv_speed: int = None,
    iv_random_init: bool = False,
    stage_hp: int = 0,
    stage_attack: int = 0,
    stage_defense: int = 0,
    stage_special_attack: int = 0,
    stage_special_defense: int = 0,
    stage_speed: int = 0,
    stage_accuracy: int = 0,
    stage_evasiveness: int = 0,
    nickname: str = None,
    form: Union[FormEnum, str] = None,
) -> PocketMonster:
    forms_dict = POCKET_MONSTERS_DICT[number]
    pocket_monster_dict = forms_dict[form]
    name = pocket_monster_dict['Name']
    _types = [pocket_monster_dict['Type 1'], pocket_monster_dict['Type 2']]
    base_hp = pocket_monster_dict[StatsEnum.HP]
    base_attack = pocket_monster_dict[StatsEnum.ATTACK]
    base_defense = pocket_monster_dict[StatsEnum.DEFENSE]
    base_special_attack = pocket_monster_dict[StatsEnum.SPECIAL_ATTACK]
    base_special_defense = pocket_monster_dict[StatsEnum.SPECIAL_DEFENSE]
    base_speed = pocket_monster_dict[StatsEnum.SPEED]

    return PocketMonster(
        number=number,
        level=level,
        name=name,
        nature=nature,
        _types=_types,
        base_hp=base_hp,
        base_attack=base_attack,
        base_defense=base_defense,
        base_special_attack=base_special_attack,
        base_special_defense=base_special_defense,
        base_speed=base_speed,
        ev_hp=ev_hp,
        ev_attack=ev_attack,
        ev_defense=ev_defense,
        ev_special_attack=ev_special_attack,
        ev_special_defense=ev_special_defense,
        ev_speed=ev_speed,
        iv_hp=iv_hp,
        iv_attack=iv_attack,
        iv_defense=iv_defense,
        iv_special_attack=iv_special_attack,
        iv_special_defense=iv_special_defense,
        iv_speed=iv_speed,
        iv_random_init=iv_random_init,
        stage_hp=stage_hp,
        stage_attack=stage_attack,
        stage_defense=stage_defense,
        stage_special_attack=stage_special_attack,
        stage_special_defense=stage_special_defense,
        stage_speed=stage_speed,
        stage_accuracy=stage_accuracy,
        stage_evasiveness=stage_evasiveness,
        nickname=nickname,
        form=form,
    )
