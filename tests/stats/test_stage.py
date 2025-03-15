import pytest
import unittest

from pocketgram.enums.stats import BattleStatsEnum
from pocketgram.enums.stats import StatsEnum
from pocketgram.stats.stage import StageStats


class TestStage(unittest.TestCase):

    def test_init(self):
        '''Testa o construtor da classe StageStats usando valores limites.
        '''

        stage_stats = StageStats(
            hp=6, attack=-6, defense=6, special_attack=-6,
            special_defense=6, speed=-6, accuracy=6, evasiveness=-6
        )

        self.assertEqual(stage_stats[StatsEnum.HP], 6)
        self.assertEqual(stage_stats[StatsEnum.ATTACK], -6)
        self.assertEqual(stage_stats[StatsEnum.DEFENSE], 6)
        self.assertEqual(stage_stats[StatsEnum.SPECIAL_ATTACK], -6)
        self.assertEqual(stage_stats[StatsEnum.SPECIAL_DEFENSE], 6)
        self.assertEqual(stage_stats[StatsEnum.SPEED], -6)
        self.assertEqual(stage_stats[BattleStatsEnum.ACCURACY], 6)
        self.assertEqual(stage_stats[BattleStatsEnum.EVASIVENESS], -6)

    def test_init_with_default_values(self):
        '''Testa o construtor da classe StageStats usando valores padrão.
        '''

        stage_stats = StageStats()

        self.assertEqual(stage_stats[StatsEnum.HP], 0)
        self.assertEqual(stage_stats[StatsEnum.ATTACK], 0)
        self.assertEqual(stage_stats[StatsEnum.DEFENSE], 0)
        self.assertEqual(stage_stats[StatsEnum.SPECIAL_ATTACK], 0)
        self.assertEqual(stage_stats[StatsEnum.SPECIAL_DEFENSE], 0)
        self.assertEqual(stage_stats[StatsEnum.SPEED], 0)
        self.assertEqual(stage_stats[BattleStatsEnum.ACCURACY], 0)
        self.assertEqual(stage_stats[BattleStatsEnum.EVASIVENESS], 0)

    def test_init_stat_gt_max_value(self):
        '''Teste que verifica se a exceção é lançada quando o valor
        de algum stat iniciado é maior que 6.
        '''

        expected_match = 'Attack não pode ser maior que 6.'
        with pytest.raises(ValueError, match=expected_match):
            StageStats(
                hp=0, attack=7, defense=0, special_attack=0,
                special_defense=0, speed=0, accuracy=0, evasiveness=0
            )

    def test_init_stat_lt_mix_value(self):
        '''Teste que verifica se a exceção é lançada quando o valor
        de algum stat iniciado é menor que -6.
        '''

        expected_match = 'Attack não pode ser menor que -6.'
        with pytest.raises(ValueError, match=expected_match):
            StageStats(
                hp=0, attack=-7, defense=0, special_attack=0,
                special_defense=0, speed=0, accuracy=0, evasiveness=0
            )

    def test_get_set_classes(self):
        '''Teste que verifica se a property get_set_classes retorna uma tupla
        que contém StatsEnum e BattleStatsEnum.
        '''

        stage_stats = StageStats()
        result = stage_stats.get_set_classes

        self.assertIsInstance(result, tuple)
        self.assertIn(StatsEnum, result)
        self.assertIn(BattleStatsEnum, result)
        self.assertEqual(len(result), 2)

    def test_getitem_invalid_key_type(self):
        '''Teste que verifica se a exceção é lançada quando a chave passada
        para o método __getitem__ não é do tipo StatsEnum.
        '''

        stage_stats = StageStats()
        expected_text = 'não é do tipo StatsEnum/BattleStatsEnum'
        with self.assertRaises(TypeError) as context:
            stage_stats['invalid_key']
        self.assertIn(expected_text, str(context.exception))

    def test_setitem(self):
        '''Teste que verifica se o método __setitem__ funciona corretamente.
        '''

        stage_stats = StageStats()
        stage_stats[StatsEnum.HP] = 5
        stage_stats[StatsEnum.ATTACK] = 5
        stage_stats[StatsEnum.DEFENSE] = 5
        stage_stats[StatsEnum.SPECIAL_ATTACK] = 5
        stage_stats[StatsEnum.SPECIAL_DEFENSE] = 5
        stage_stats[StatsEnum.SPEED] = 5
        stage_stats[BattleStatsEnum.ACCURACY] = 5
        stage_stats[BattleStatsEnum.EVASIVENESS] = 5

        self.assertEqual(stage_stats[StatsEnum.HP], 5)
        self.assertEqual(stage_stats[StatsEnum.ATTACK], 5)
        self.assertEqual(stage_stats[StatsEnum.DEFENSE], 5)
        self.assertEqual(stage_stats[StatsEnum.SPECIAL_ATTACK], 5)
        self.assertEqual(stage_stats[StatsEnum.SPECIAL_DEFENSE], 5)
        self.assertEqual(stage_stats[StatsEnum.SPEED], 5)
        self.assertEqual(stage_stats[BattleStatsEnum.ACCURACY], 5)
        self.assertEqual(stage_stats[BattleStatsEnum.EVASIVENESS], 5)

    def test_setitem_invalid_key_type(self):
        '''Teste que verifica se a exceção é lançada quando a chave passada
        para o método __setitem__ não é do tipo StatsEnum.
        '''

        stage_stats = StageStats()
        expected_text = 'não é do tipo StatsEnum/BattleStatsEnum'
        with self.assertRaises(TypeError) as context:
            stage_stats['invalid_key'] = 1
        self.assertIn(expected_text, str(context.exception))

    def test_setitem_stat_gt_max_value(self):
        '''Teste que verifica se a exceção é lançada quando o valor
        de algum stat é definido para maior que 6.
        '''

        stage_stats = StageStats()
        all_stats_enum = list(StatsEnum) + list(BattleStatsEnum)
        for enum_obj in all_stats_enum:
            expected_match = f'{enum_obj.value} não pode ser maior que 6.'
            with pytest.raises(ValueError, match=expected_match):
                stage_stats[enum_obj] = 7

    def test_setitem_stat_lt_mix_value(self):
        '''Teste que verifica se a exceção é lançada quando o valor
        de algum stat é definido para menor que -6.
        '''

        stage_stats = StageStats()
        all_stats_enum = list(StatsEnum) + list(BattleStatsEnum)
        for enum_obj in all_stats_enum:
            expected_match = f'{enum_obj.value} não pode ser menor que -6.'
            with pytest.raises(ValueError, match=expected_match):
                stage_stats[enum_obj] = -7

    def test_total(self):
        '''Testa se a property total retorna o valor total dos stats.
        '''

        stage_stats_0 = StageStats(
            hp=0, attack=0, defense=0, special_attack=0,
            special_defense=0, speed=0, accuracy=0, evasiveness=0
        )
        stage_stats_1 = StageStats(
            hp=6, attack=6, defense=6, special_attack=6,
            special_defense=6, speed=6, accuracy=6, evasiveness=6
        )
        stage_stats_2 = StageStats(
            hp=-6, attack=-6, defense=-6, special_attack=-6,
            special_defense=-6, speed=-6, accuracy=-6, evasiveness=-6
        )

        self.assertEqual(stage_stats_0.total, 0)
        self.assertEqual(stage_stats_1.total, 48)
        self.assertEqual(stage_stats_2.total, -48)
