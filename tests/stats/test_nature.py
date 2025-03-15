import re

import pytest
import unittest

from random import choice

from pocketgram.enums.natures import NaturesEnum
from pocketgram.enums.stats import StatsEnum
from pocketgram.stats.nature import Nature


class TestNature(unittest.TestCase):

    def test_init_nature_enum(self):
        '''Teste que verifica a inicialização usando um NatureEnum.
        '''

        for nature_enum in NaturesEnum:
            nature = Nature(nature_enum)
            assert isinstance(nature._nature, NaturesEnum)
            assert nature._nature == nature_enum
            assert nature.name == nature_enum.name
            assert nature.value == nature_enum.value
            assert nature.max_value == 1.1

    def test_init_str(self):
        '''Teste que verifica a inicialização usando uma string.
        '''

        for nature_enum in NaturesEnum:
            nature = Nature(nature_enum.name)
            assert isinstance(nature._nature, NaturesEnum)
            assert nature._nature == nature_enum
            assert nature.name == nature_enum.name
            assert nature.value == nature_enum.value
            assert nature.max_value == 1.1

    def test_init_invalid_type(self):
        '''Teste que verifica se o construtor da classe retorna um erro
        quando passado um valor com tipo diferente de NatureEnum ou string.
        '''

        expected_match = re.escape('nature deve ser um NaturesEnum. (123)')
        with pytest.raises(TypeError, match=expected_match):
            Nature(nature=123)

    def test_getitem(self):
        '''Testa que verifica se o método __getitem__ retorna o valor correto
        para uma chave StatsEnum.
        '''

        nature = Nature(nature=NaturesEnum.ADAMANT)
        self.assertEqual(nature[StatsEnum.HP], 1.0)
        self.assertEqual(nature[StatsEnum.ATTACK], 1.1)
        self.assertEqual(nature[StatsEnum.DEFENSE], 1.0)
        self.assertEqual(nature[StatsEnum.SPECIAL_ATTACK], 0.9)
        self.assertEqual(nature[StatsEnum.SPECIAL_DEFENSE], 1.0)
        self.assertEqual(nature[StatsEnum.SPEED], 1.0)

    def test_getitem_invalid_key(self):
        '''Teste que verifica se o métoco __getitem__ levanta uma exceção
        KeyError quando passado uma chave inválida.
        '''

        nature = Nature(nature=NaturesEnum.ADAMANT)
        with pytest.raises(TypeError):
            nature['INVALID_KEY']
            nature[123]

    def test_setitem_raises_attribute_error(self):
        '''Teste que verifica se o método __setitem__ levanta uma exceção
        quando se tenta modificar alguma chave do objeto.
        '''

        nature = Nature(nature=NaturesEnum.ADAMANT)
        expected_match = 'Nature não pode ser alterada.'
        with pytest.raises(AttributeError, match=expected_match):
            nature[StatsEnum.ATTACK] = 1.2

    def test_str_returns_correct_string_representation(self):
        '''Teste que verifica se o método __str__ retorna a representação
        correta da nature como uma string.
        '''

        nature = Nature(nature=NaturesEnum.ADAMANT)
        expected_string = (
            f'{NaturesEnum.ADAMANT.value} ' + super(Nature, nature).__str__()
        )
        assert str(nature) == expected_string

    def test_calculate_stat_modifiers_2(self):
        '''Teste que verifica se o método calculate_stat_modifiers retorna
        os modificadores de stats corretos para uma nature.
        '''
        nature = Nature(nature=NaturesEnum.BOLD)
        modifiers = nature.calculate_stat_modifiers()

        self.assertEqual(modifiers[StatsEnum.HP], 1.0)
        self.assertEqual(modifiers[StatsEnum.ATTACK], 0.9)
        self.assertEqual(modifiers[StatsEnum.DEFENSE], 1.1)
        self.assertEqual(modifiers[StatsEnum.SPECIAL_ATTACK], 1.0)
        self.assertEqual(modifiers[StatsEnum.SPECIAL_DEFENSE], 1.0)
        self.assertEqual(modifiers[StatsEnum.SPEED], 1.0)

    def test_calculate_stat_modifiers_no_edge_cases(self):
        '''Teste que verifica se o método calculate_stat_modifiers retorna
        os modificadores de stats corretos para uma nature.
        '''

        nature = Nature(nature=choice(list(NaturesEnum)))
        modifiers = nature.calculate_stat_modifiers()
        assert isinstance(modifiers, dict)

        for stat_enum in StatsEnum:
            assert stat_enum in modifiers.keys()

        for value in modifiers.values():
            assert value in (0.9, 1.0, 1.1)

    def test_natures_decrease_invalid_input(self):
        '''Teste que verifica se o método natures_decrease levanta uma exceção
        quando passado um valor inválido.
        '''

        nature = Nature(nature=NaturesEnum.ADAMANT)
        expected_match = re.escape(
            'stat_enum deve ser um StatsEnum. (INVALID_INPUT)'
        )
        with pytest.raises(TypeError, match=expected_match):
            nature.natures_decrease('INVALID_INPUT')

    def test_natures_increase_invalid_input(self):
        '''Teste que verifica se o método natures_decrease levanta uma exceção
        quando passado um valor inválido.
        '''

        nature = Nature(nature=NaturesEnum.ADAMANT)
        expected_match = re.escape(
            'stat_enum deve ser um StatsEnum. (INVALID_INPUT)'
        )
        with pytest.raises(TypeError, match=expected_match):
            nature.natures_increase('INVALID_INPUT')
