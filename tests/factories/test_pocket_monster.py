import unittest

from pocketgram.enums.form import FormEnum
from pocketgram.enums.natures import NaturesEnum
from pocketgram.factories.pocket_monster import pocket_monster_factory
from pocketgram.pocket_monster import PocketMonster


class TestPocketMonsterFactory(unittest.TestCase):

    @unittest.skip("Teste ignorado temporariamente até ser corrigido.")
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
            form=form
        )

        self.assertIsInstance(pocket_monster, PocketMonster)
        self.assertEqual(pocket_monster.number, number)
        self.assertEqual(pocket_monster.level, level)
        self.assertEqual(pocket_monster.nature, nature)
        self.assertEqual(pocket_monster.ev_hp, ev_hp)
        self.assertEqual(pocket_monster.ev_attack, ev_attack)
        self.assertEqual(pocket_monster.ev_defense, ev_defense)
        self.assertEqual(pocket_monster.ev_special_attack, ev_special_attack)
        self.assertEqual(pocket_monster.ev_special_defense, ev_special_defense)
        self.assertEqual(pocket_monster.ev_speed, ev_speed)
        self.assertEqual(pocket_monster.form, form)
