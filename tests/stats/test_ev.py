
import pytest
import unittest

from pocketgram.enum.stats import StatsEnum
from pocketgram.stats.ev import EVStats


class TestEv(unittest.TestCase):
    expected_max_ev = 510

    def test_init(self):
        '''Teste que verifica a inicialização de EVStats para
        cada um dos stats, current_ev e remaining_ev.
        '''

        ev_stats = EVStats(100, 100, 100, 100, 100, 10)
        assert ev_stats[StatsEnum.HP] == 100
        assert ev_stats[StatsEnum.ATTACK] == 100
        assert ev_stats[StatsEnum.DEFENSE] == 100
        assert ev_stats[StatsEnum.SPECIAL_ATTACK] == 100
        assert ev_stats[StatsEnum.SPECIAL_DEFENSE] == 100
        assert ev_stats[StatsEnum.SPEED] == 10
        assert ev_stats.current_ev == 510
        assert ev_stats.remaining_ev == 0

    def test_init_stat_gt_max_value(self):
        '''Teste a inicialização de EVStats com valores que excedem o
        valor máximo de EV permitido, levantando a exceção ValueError.

        Este teste verifica quando a soma de todos os valores de EV passado
        para o construtor EVStats excede o valor máximo permitido de 510. A
        exceção ValueError é esperada com uma mensagem adequada.
        '''

        expected = 'O valor total dos EVs não pode ser maior que 510. '
        with self.assertRaises(ValueError) as context:
            EVStats(255, 255, 1, 0, 0, 0)

        self.assertIn(expected, str(context.exception))

    def test_add_ev(self):
        '''Teste que verifica o método add_ev para adicionar um valor de EV.
        '''

        ev_stats = EVStats(0, 0, 0, 0, 0, 0)

        for stat_enum in StatsEnum:
            ev_stats.add_ev(stat_enum, 10)

        for stat_enum in StatsEnum:
            self.assertEqual(ev_stats[stat_enum], 10)

    def test_add_ev_greater_than_remaining_ev(self):
        '''Teste que verifica o método add_ev para adicionar um valor de EV que
        é maior que o valor restante de EV (remaining_ev).

        O teste verifica o warning que alerta para a não alteração do EV, além
        de verificar se todos os EV permanecem com os valores iniciais.
        '''

        expected_log = 'O valor não pode ser maior que o valor restante do EV.'
        stats = EVStats(100, 100, 100, 100, 100, 0)
        initial_stats_map = {enum: stats[enum] for enum in StatsEnum}

        with self.assertLogs(level='WARNING') as log:
            stats.add_ev(StatsEnum.HP, 11)

        for stat_enum, initial_value in initial_stats_map.items():
            self.assertEqual(stats[stat_enum], initial_value)

        self.assertIn(expected_log, log.output[0])

    def test_add_ev_negative_value(self):
        '''Teste que verifica o método add_ev para adicionar um valor negativo.
        '''

        ev_stats = EVStats(10, 10, 10, 10, 10, 10)
        expected_match = 'O valor do EV não pode ser negativo.'
        with pytest.raises(ValueError, match=expected_match):
            ev_stats.add_ev(StatsEnum.HP, -1)

    def test_max_ev(self):
        '''Teste que verifica se o valor máximo de EV é 510.
        '''

        ev_stats = EVStats(0, 0, 0, 0, 0, 0)
        assert ev_stats.max_ev == self.expected_max_ev

    def test_remaining_ev(self):
        '''Teste que verifica se o valor restante dos EVs estão sendo
        calculados corretamente.
        '''

        stats_arg = (10, 20, 30, 40, 50, 60)
        stats = EVStats(*stats_arg)
        expected_remaining_ev = self.expected_max_ev - sum(stats_arg)
        assert stats.remaining_ev == expected_remaining_ev

    def test_show_ev(self):
        '''Teste que verifica se o método show_ev está retornando a string
        corretamente
        '''

        stats_arg = (100, 100, 100, 100, 100, 0)
        stats_sum = sum(stats_arg)
        remaining_ev = self.expected_max_ev - stats_sum
        ev_stats = EVStats(*stats_arg)
        show_ev = ev_stats.show_ev
        expected_output = (
            f'EVs: {stats_sum}/{self.expected_max_ev}'
            f'({remaining_ev} restantes)'
        )
        self.assertEqual(show_ev, expected_output)
