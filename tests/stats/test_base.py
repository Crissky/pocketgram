import unittest
from pocketgram.enums.stats import StatsEnum
from pocketgram.stats.base import BaseStats


class TestBase(unittest.TestCase):

    def test_init_(self):
        '''Teste que verifica que se inicializa corretamente o objeto BaseStats
        '''

        base_stats = BaseStats(
            hp=35,
            attack=55,
            defense=40,
            special_attack=50,
            special_defense=50,
            speed=90
        )
        assert base_stats[StatsEnum.HP] == 35
        assert base_stats[StatsEnum.ATTACK] == 55
        assert base_stats[StatsEnum.DEFENSE] == 40
        assert base_stats[StatsEnum.SPECIAL_ATTACK] == 50
        assert base_stats[StatsEnum.SPECIAL_DEFENSE] == 50
        assert base_stats[StatsEnum.SPEED] == 90

    def test_init_negative_values(self):
        '''Teste que verifica se a inicialização com um valor negativo
        levanta uma excessão.
        '''

        with self.assertRaises(ValueError):
            BaseStats(-1, 0, 0, 0, 0, 0)

    def test_init_out_of_bounds_values(self):
        '''Teste que inicializa BaseStats com valores fora dos limites
        permitidos (255).
        '''

        with self.assertRaises(ValueError):
            BaseStats(256, 0, 0, 0, 0, 0)
