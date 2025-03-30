import unittest


from pocketgram.constants.pocket_monster import POCKET_MONSTERS_DICT
from pocketgram.enums.stats import StatsEnum


class TestPocketMonsterDict(unittest.TestCase):

    def test_number_keys(self):
        '''Teste que analisa os números (chaves) do POCKET_MONSTERS_DICT
        '''

        length_pocket_monsters = len(POCKET_MONSTERS_DICT.keys())
        self.assertEqual(length_pocket_monsters, 1025)
        for index, key in enumerate(POCKET_MONSTERS_DICT.keys(), start=1):
            self.assertEqual(f'{index:04}', key)

    def test_stats(self):
        '''Testa se as estatísticas dos monstros são do tipo correta
        '''

        for pocket_monsters_dict in POCKET_MONSTERS_DICT.values():
            for pm_dict in pocket_monsters_dict.values():
                for stat_enum in StatsEnum:
                    self.assertIsInstance(pm_dict[stat_enum], int)
