import unittest

from pocketgram.constants.pocket_monster import POCKET_MONSTERS_DICT
from pocketgram.enums._types import TypesEnum
from pocketgram.enums.pocket_monster import PocketMonsterParamEnum
from pocketgram.enums.stats import StatsEnum


class TestPocketMonsterDict(unittest.TestCase):

    def test_number_keys(self):
        '''Teste que analisa os números (chaves) do POCKET_MONSTERS_DICT.
        '''

        length_pocket_monsters = len(POCKET_MONSTERS_DICT.keys())
        self.assertEqual(length_pocket_monsters, 1025)
        for index, key in enumerate(POCKET_MONSTERS_DICT.keys(), start=1):
            self.assertEqual(f'{index:04}', key)

    def test_form(self):
        '''Teste que analisa os tipos das formas do POCKET_MONSTERS_DICT.
        '''

        for pocket_monsters_dict in POCKET_MONSTERS_DICT.values():
            form_types = (str, type(None))
            for form_key in pocket_monsters_dict.keys():
                self.assertIsInstance(form_key, form_types)

    def test_stats(self):
        '''Testa se as estatísticas dos monstros são do tipo correta.
        '''

        for pocket_monsters_dict in POCKET_MONSTERS_DICT.values():
            for pm_dict in pocket_monsters_dict.values():
                for stat_enum in StatsEnum:
                    self.assertIsInstance(pm_dict[stat_enum], int)

    def test_name(self):
        '''Testa se os nomes dos monstros são do tipo correto.
        '''

        for pocket_monsters_dict in POCKET_MONSTERS_DICT.values():
            for pm_dict in pocket_monsters_dict.values():
                self.assertIsInstance(
                    pm_dict[PocketMonsterParamEnum.NAME], str
                )

    def test_type_1(self):
        '''Testa se os tipos 1 dos monstros são do tipo correto.
        '''

        for pocket_monsters_dict in POCKET_MONSTERS_DICT.values():
            for pm_dict in pocket_monsters_dict.values():
                self.assertIsInstance(
                    pm_dict[PocketMonsterParamEnum.TYPE_1], TypesEnum
                )

    def test_type_2(self):
        '''Testa se os tipos 2 dos monstros são do tipo correto.
        '''

        for pocket_monsters_dict in POCKET_MONSTERS_DICT.values():
            type_2_types = (TypesEnum, type(None))
            for pm_dict in pocket_monsters_dict.values():
                self.assertIsInstance(
                    pm_dict[PocketMonsterParamEnum.TYPE_2], type_2_types
                )
