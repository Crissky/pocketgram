import unittest

from pocketgram.enums.form import FormEnum
from pocketgram.enums.natures import NaturesEnum
from pocketgram.enums.pocket_monster import PocketMonsterParamEnum
from pocketgram.enums.stats import StatsEnum
from pocketgram.factories.pocket_monster import pocket_monster_factory
from pocketgram.pocket_monster import PocketMonster


class TestPocketMonsterFactory(unittest.TestCase):

    def test_pocket_monster_factory_1(self):
        '''Teste se pocket_monster_factory cria uma instância de PocketMonster
        com atributos corretos.

        Este teste verifica se a função factory inicializa corretamente um
        PocketMonster com os parâmetros fornecidos e retorna uma instância
        com os atributos esperados.
        '''

        number = 150
        level = 100
        nature = NaturesEnum.ADAMANT
        ev_hp = 0
        ev_attack = 0
        ev_defense = 0
        ev_special_attack = 0
        ev_special_defense = 0
        ev_speed = 0
        form = FormEnum.MEGA_X

        pocket_monster = pocket_monster_factory(
            number=number,
            level=level,
            nature=nature,
            ev_hp=ev_hp,
            ev_attack=ev_attack,
            ev_defense=ev_defense,
            ev_special_attack=ev_special_attack,
            ev_special_defense=ev_special_defense,
            ev_speed=ev_speed,
            iv_random_init=True,
            nickname='Frieza',
            form=form
        )

        self.assertIsInstance(pocket_monster, PocketMonster)
        self.assertEqual(
            pocket_monster[PocketMonsterParamEnum.NUMBER], f'{number:04}'
        )
        self.assertEqual(pocket_monster[PocketMonsterParamEnum.LEVEL], level)
        self.assertEqual(pocket_monster[PocketMonsterParamEnum.NATURE], nature)
        self.assertEqual(
            pocket_monster._ev_stats[StatsEnum.HP], ev_hp
        )
        self.assertEqual(
            pocket_monster._ev_stats[StatsEnum.ATTACK], ev_attack
        )
        self.assertEqual(
            pocket_monster._ev_stats[StatsEnum.DEFENSE], ev_defense
        )
        self.assertEqual(
            pocket_monster._ev_stats[StatsEnum.SPECIAL_ATTACK],
            ev_special_attack
        )
        self.assertEqual(
            pocket_monster._ev_stats[StatsEnum.SPECIAL_DEFENSE],
            ev_special_defense
        )
        self.assertEqual(
            pocket_monster._ev_stats[StatsEnum.SPEED], ev_speed
        )
        self.assertEqual(pocket_monster[PocketMonsterParamEnum.FORM], form)
