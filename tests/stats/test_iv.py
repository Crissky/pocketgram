
from pocketgram.enums.stats import StatsEnum
from pocketgram.stats.iv import IVStats
import pytest
import unittest


class TestIv(unittest.TestCase):

    def test_init(self):
        '''Teste que verifica se o construtor retorna os valores corretos
        quando os stats são passados como parâmetros.
        '''

        iv_stats_0 = IVStats(
            hp=0, attack=0, defense=0,
            special_attack=0, special_defense=0, speed=0,
        )
        iv_stats_31 = IVStats(
            hp=31, attack=31, defense=31,
            special_attack=31, special_defense=31, speed=31,
        )
        for stat_enum in StatsEnum:
            self.assertEqual(iv_stats_0[stat_enum], 0)
            self.assertEqual(iv_stats_31[stat_enum], 31)
            self.assertIsInstance(iv_stats_0[stat_enum], int)
            self.assertIsInstance(iv_stats_31[stat_enum], int)

    def test_random_init(self):
        '''Teste que verifica se o construtor retorna os valores corretos,
        entre (0-31), quando usado random_init True.
        '''

        iv_stats_random_init = IVStats(random_init=True)
        for stat_enum in StatsEnum:
            self.assertGreaterEqual(iv_stats_random_init[stat_enum], 0)
            self.assertLessEqual(iv_stats_random_init[stat_enum], 31)

    def test_init_conflict_values_with_random_init(self):
        '''Teste que verifica se o construtor retorna uma exceção quando os
        valores passados junto com random_init True.
        '''

        self.assertRaises(ValueError, IVStats, hp=31, random_init=True)
        with pytest.raises(ValueError) as exc_info:
            IVStats(
                hp=10, attack=20, defense=30,
                special_attack=40, special_defense=50, speed=60,
                random_init=True
            )

        expected_error_message = (
            'Esses parâmetros não devem ser definidos junto com o '
            'random_init: hp=10, attack=20, defense=30, '
            'special_attack=40, special_defense=50, speed=60.'
        )
        assert str(exc_info.value) == expected_error_message

    def test_init_invalid_values(self):
        '''Teste que verifica se o construtor retorna uma exceção quando os
        valores passados são inválidos.

        Os valores inválidos são menores que 0, maiores que 31 e None quando
        random_init não é True.
        '''

        args = {stat_enum.name.lower(): 10 for stat_enum in StatsEnum}

        self.assertRaises(ValueError, IVStats, hp=-1)
        self.assertRaises(ValueError, IVStats, attack=32)
        self.assertRaises(ValueError, IVStats)
        for stat_enum in StatsEnum:
            args_copy = args.copy()
            args_copy.pop(stat_enum.name.lower())
            self.assertRaises(ValueError, IVStats, **args_copy)

    def test_get_random_iv_1(self):
        '''Teste que verifica se o método get_random_iv retorna um valor
        '''

        iv_stats = IVStats(random_init=True)
        for _ in range(1000):
            random_iv = iv_stats.get_random_iv()
            self.assertGreaterEqual(random_iv, 0)
            self.assertLessEqual(random_iv, 31)
            self.assertIsInstance(random_iv, int)
