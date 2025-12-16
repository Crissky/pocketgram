import unittest

from pocketgram.enums.form import FormEnum


class TestFormEnum(unittest.TestCase):

    def test_formated_value_1(self):
        '''Teste se o método get_formated_value formata corretamente o valor
        com o pocket_monster fornecido.
        '''

        form = FormEnum.ALOLAN
        result = form.get_formated_value('Raichu')
        self.assertEqual(result, 'Alolan Raichu')

    def test_formated_value_2(self):
        '''Teste se o método get_formated_value formata corretamente o valor
        com o pocket_monster fornecido quando não há {pocket_monster} no value.
        '''

        form = FormEnum.ZERO_FORM
        result = form.get_formated_value('Palafin')
        self.assertEqual(result, 'Zero Form')
