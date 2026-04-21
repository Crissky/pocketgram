import unittest

from types import SimpleNamespace

from pocketgram.enums.stats import StatsEnum
from pocketgram.stats.base import BaseStats


class TestBase(unittest.TestCase):

    def test_init(self):
        '''Teste que verifica que se inicializa corretamente o objeto BaseStats
        '''

        pocket_monster = SimpleNamespace(
            base_hp=35, base_attack=55, base_defense=40,
            base_special_attack=50, base_special_defense=50, base_speed=90
        )
        base_stats = BaseStats(pocket_monster=pocket_monster)

        self.assertEqual(base_stats[StatsEnum.HP], 35)
        self.assertEqual(base_stats[StatsEnum.ATTACK], 55)
        self.assertEqual(base_stats[StatsEnum.DEFENSE], 40)
        self.assertEqual(base_stats[StatsEnum.SPECIAL_ATTACK], 50)
        self.assertEqual(base_stats[StatsEnum.SPECIAL_DEFENSE], 50)
        self.assertEqual(base_stats[StatsEnum.SPEED], 90)

    def test_init_negative_values(self):
        '''Teste que verifica se a inicialização com um valor negativo
        levanta uma excessão.
        '''

        expected = 'HP=-1 > MIN=0'
        with self.assertRaises(ValueError) as context:
            pocket_monster = SimpleNamespace(
                base_hp=-1, base_attack=0, base_defense=0,
                base_special_attack=0, base_special_defense=0, base_speed=0
            )
            BaseStats(pocket_monster=pocket_monster)

        self.assertIn(expected, str(context.exception))

    def test_init_out_of_bounds_values(self):
        '''Teste que inicializa BaseStats com valores fora dos limites
        permitidos (255).
        '''

        expected = 'HP=256 > MAX=255'
        with self.assertRaises(ValueError) as context:
            pocket_monster = SimpleNamespace(
                base_hp=256, base_attack=0, base_defense=0,
                base_special_attack=0, base_special_defense=0, base_speed=0
            )
            BaseStats(pocket_monster=pocket_monster)

        self.assertIn(expected, str(context.exception))
