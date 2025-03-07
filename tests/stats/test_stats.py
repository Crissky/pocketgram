import pytest
import unittest

from pocketgram.enum.stats import StatsEnum
from pocketgram.stats.stats import Stats


class TestStats(unittest.TestCase):

    def test_init_and_getitem(self):
        '''Teste que verifica se os valores de stats são corretos quando
        um valor é passado para o construtor e retornado pelo `get item`.
        '''

        # Inicializa a classe Stats
        stats = Stats(
            hp=50,
            attack=60,
            defense=70,
            special_attack=80,
            special_defense=90,
            speed=100,
            max_value=100
        )

        # # Verifica se todos os atributos foram definidos corretamente
        self.assertEqual(stats[StatsEnum.HP], 50)
        self.assertEqual(stats[StatsEnum.ATTACK], 60)
        self.assertEqual(stats[StatsEnum.DEFENSE], 70)
        self.assertEqual(stats[StatsEnum.SPECIAL_ATTACK], 80)
        self.assertEqual(stats[StatsEnum.SPECIAL_DEFENSE], 90)
        self.assertEqual(stats[StatsEnum.SPEED], 100)
        self.assertEqual(stats.max_value, 100)

        # Verifica se nenhum atributo excede o max_value
        for stat_enum in StatsEnum:
            self.assertLessEqual(stats[stat_enum], stats.max_value)

    def test_init_stat_gt_max_value(self):
        '''Teste que verifica se a exceção é lançada quando o valor
        de algum stat iniciado é maior que o max_value.
        '''

        expected_match = 'HP não pode ser maior que 50.'
        with pytest.raises(ValueError, match=expected_match):
            Stats(51, 50, 50, 50, 50, 50, max_value=50)

    def test_init_max_value_int_validation(self):
        '''Teste que verifica se o método __init__ está convertendo
        corretamente o parâmetro max_value para inteiro.
        '''

        stats = Stats(50, 50, 50, 50, 50, 50, max_value=50.5)
        assert stats.max_value == 50

    def test_init_negative_stat_value(self):
        ''' Teste que verifica se a exceção é lançada pelo método __init__
        quando um valor negativo é passado.
        '''

        expected_match_1 = 'HP não pode ser negativo.'
        expected_match_2 = 'max_value deve ser maior que 0.'
        with pytest.raises(ValueError, match=expected_match_1):
            Stats(-1, 50, 50, 50, 50, 50, max_value=100)
        with pytest.raises(ValueError, match=expected_match_2):
            Stats(50, 50, 50, 50, 50, 50, max_value=-100)

    def test_getitem_invalid_key_type(self):
        '''Teste que verifica se a exceção é lançada quando a chave passada
        para o método __getitem__ não é do tipo StatsEnum.
        '''

        stats = Stats(50, 50, 50, 50, 50, 50, max_value=100)
        with self.assertRaises(TypeError) as context:
            stats['invalid_key']
        self.assertIn('não é do tipo StatsEnum', str(context.exception))

    def test_setitem_and_getitem(self):
        '''Teste que verifica se o método __setitem__ está funcionando
        corretamente.
        '''

        stats = Stats(0, 0, 0, 0, 0, 0, max_value=100)
        stats_map = {
            stat_enum: i * 10
            for i, stat_enum in enumerate(StatsEnum, start=1)
        }

        for stat_enum, value in stats_map.items():
            stats[stat_enum] = value

        for stat_enum in StatsEnum:
            self.assertEqual(stats[stat_enum], stats_map[stat_enum])

    def test_setitem_int_validation(self):
        '''Teste que verifica se o método __setitem__ está funcionando
        corretamente.
        '''

        stats = Stats(0, 0, 0, 0, 0, 0, max_value=100)
        stats_map = {
            stat_enum: i * 10.1
            for i, stat_enum in enumerate(StatsEnum, start=1)
        }

        for stat_enum, value in stats_map.items():
            stats[stat_enum] = value

        for stat_enum in StatsEnum:
            self.assertEqual(stats[stat_enum], int(stats_map[stat_enum]))

    def test_setitem_invalid_key_type(self):
        '''Teste que verifica se a exceção é lançada quando a chave passada
        para o método __setitem__ não é do tipo StatsEnum.
        '''

        stats = Stats(50, 50, 50, 50, 50, 50, max_value=100)
        with self.assertRaises(TypeError) as context:
            stats['invalid_key'] = 50
        self.assertIn('não é do tipo StatsEnum', str(context.exception))

    def test_setitem_stat_gt_max_value(self):
        '''Teste que verifica se a exceção é lançada quando o valor
        de algum stat é maior que o max_value.
        '''

        stats = Stats(50, 50, 50, 50, 50, 50, max_value=100)
        for stat_enum in StatsEnum:
            expected_match = f'{stat_enum.value} não pode ser maior que 100.'
            with pytest.raises(ValueError, match=expected_match):
                stats[stat_enum] = 101

    def test_setitem_negative_stat_value(self):
        '''Teste que verifica se a exceção é lançada quando o valor
        de algum stat é negativo.
        '''

        stats = Stats(50, 50, 50, 50, 50, 50, max_value=100)
        for stat_enum in StatsEnum:
            expected_match = f'{stat_enum.value} não pode ser negativo.'
            with pytest.raises(ValueError, match=expected_match):
                stats[stat_enum] = -1

    def test_total(self):
        '''Teste que verifica se o método total está retornando
        corretamente a soma de todos os stats.
        '''

        stats = Stats(50, 50, 50, 50, 50, 50, max_value=100)
        assert stats.total == 300

    def test_stats_map(self):
        '''Teste que verifica se o método stats_map está retornando
        corretamente o dicionário de stats.
        '''

        stats = Stats(50, 50, 50, 50, 50, 50, max_value=100)
        stats_map = stats.stats_map
        for stat_enum in StatsEnum:
            assert stats_map[stat_enum] == f'_{stat_enum.name.lower()}'
