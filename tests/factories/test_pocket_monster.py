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
        evs = pocket_monster._ev_stats

        self.assertIsInstance(pocket_monster, PocketMonster)
        self.assertEqual(
            pocket_monster[PocketMonsterParamEnum.NUMBER], f'{number:04}'
        )
        self.assertEqual(pocket_monster[PocketMonsterParamEnum.LEVEL], level)
        self.assertEqual(pocket_monster[PocketMonsterParamEnum.NATURE], nature)
        self.assertEqual(evs[StatsEnum.HP], ev_hp)
        self.assertEqual(evs[StatsEnum.ATTACK], ev_attack)
        self.assertEqual(evs[StatsEnum.DEFENSE], ev_defense)
        self.assertEqual(evs[StatsEnum.SPECIAL_ATTACK], ev_special_attack)
        self.assertEqual(evs[StatsEnum.SPECIAL_DEFENSE], ev_special_defense)
        self.assertEqual(evs[StatsEnum.SPEED], ev_speed)
        self.assertEqual(pocket_monster[PocketMonsterParamEnum.FORM], form)

    def test_pocket_monster_factory_2(self):
        '''Teste se pocket_monster_factory cria uma instância de PocketMonster
        com atributos corretos, passando os IVs.

        Este teste verifica se a função factory inicializa corretamente um
        PocketMonster com os parâmetros fornecidos e retorna uma instância
        com os atributos esperados.
        '''

        number = 6
        level = 100
        nature = NaturesEnum.ADAMANT
        ev_hp = 10
        ev_attack = 20
        ev_defense = 30
        ev_special_attack = 40
        ev_special_defense = 50
        ev_speed = 60
        iv_hp = 10
        iv_attack = 11
        iv_defense = 12
        iv_special_attack = 13
        iv_special_defense = 14
        iv_speed = 15
        form = FormEnum.MEGA_Y

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
            iv_hp=iv_hp,
            iv_attack=iv_attack,
            iv_defense=iv_defense,
            iv_special_attack=iv_special_attack,
            iv_special_defense=iv_special_defense,
            iv_speed=iv_speed,
            nickname='Foguinho',
            form=form
        )
        evs = pocket_monster._ev_stats
        ivs = pocket_monster._iv_stats

        self.assertIsInstance(pocket_monster, PocketMonster)
        self.assertEqual(
            pocket_monster[PocketMonsterParamEnum.NUMBER], f'{number:04}'
        )
        self.assertEqual(pocket_monster[PocketMonsterParamEnum.LEVEL], level)
        self.assertEqual(pocket_monster[PocketMonsterParamEnum.NATURE], nature)
        self.assertEqual(evs[StatsEnum.HP], ev_hp)
        self.assertEqual(evs[StatsEnum.ATTACK], ev_attack)
        self.assertEqual(evs[StatsEnum.DEFENSE], ev_defense)
        self.assertEqual(evs[StatsEnum.SPECIAL_ATTACK], ev_special_attack)
        self.assertEqual(evs[StatsEnum.SPECIAL_DEFENSE], ev_special_defense)
        self.assertEqual(evs[StatsEnum.SPEED], ev_speed)
        self.assertEqual(ivs[StatsEnum.HP], iv_hp)
        self.assertEqual(ivs[StatsEnum.ATTACK], iv_attack)
        self.assertEqual(ivs[StatsEnum.DEFENSE], iv_defense)
        self.assertEqual(ivs[StatsEnum.SPECIAL_ATTACK], iv_special_attack)
        self.assertEqual(ivs[StatsEnum.SPECIAL_DEFENSE], iv_special_defense)
        self.assertEqual(ivs[StatsEnum.SPEED], iv_speed)
        self.assertEqual(pocket_monster[PocketMonsterParamEnum.FORM], form)
