import unittest

from pocketgram.enums.stats import StatsEnum
from pocketgram.stats.base import BaseStats


class TestBase(unittest.TestCase):

    def test_init(self):
        '''Teste que verifica que se inicializa corretamente o objeto BaseStats
        '''

        base_stats = BaseStats(
            hp=35, attack=55, defense=40,
            special_attack=50, special_defense=50, speed=90
        )

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

        with self.assertRaises(ValueError):
            BaseStats(
                hp=-1, attack=0, defense=0,
                special_attack=0, special_defense=0, speed=0
            )

    def test_init_out_of_bounds_values(self):
        '''Teste que inicializa BaseStats com valores fora dos limites
        permitidos (255).
        '''

        with self.assertRaises(ValueError):
            BaseStats(
                hp=256, attack=0, defense=0,
                special_attack=0, special_defense=0, speed=0
            )
