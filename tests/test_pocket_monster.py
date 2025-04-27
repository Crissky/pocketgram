import pytest
import unittest

from pocketgram.enums._types import TypesEnum
from pocketgram.enums.natures import NatureParamEnum, NaturesEnum
from pocketgram.enums.pocket_monster import PocketMonsterParamEnum
from pocketgram.enums.stats import StatsEnum
from pocketgram.pocket_monster import PocketMonster


class TestPocketMonster(unittest.TestCase):

    def test_getitem_neutral_nature(self):
        '''Teste que o getitem funciona corretamente com uma Nature neutra.
        '''

        pm = PocketMonster(
            number=151, level=100,
            name='Mew', nickname='Testy',
            nature=NaturesEnum.HARDY, _types=TypesEnum.PSYCHIC,
            base_hp=100, base_attack=100, base_defense=100,
            base_special_attack=100, base_special_defense=100, base_speed=100,
            ev_hp=0, ev_attack=0, ev_defense=0,
            ev_special_attack=0, ev_special_defense=0, ev_speed=0,
            iv_hp=31, iv_attack=31, iv_defense=31,
            iv_special_attack=31, iv_special_defense=31, iv_speed=31
        )

        expected_hp = 341
        expected_other_stats = 236
        for stat_enum in StatsEnum:
            if stat_enum == StatsEnum.HP:
                self.assertEqual(pm[stat_enum], expected_hp)
            else:
                self.assertEqual(pm[stat_enum], expected_other_stats)

    def test_getitem_boosted_nature(self):
        '''Teste que o getitem funciona corretamente com uma Natture que
        altera stats.
        '''

        pm = PocketMonster(
            number=151, level=100,
            name='Mew', nickname='Testy',
            nature=NaturesEnum.MODEST, _types=TypesEnum.PSYCHIC,
            base_hp=100, base_attack=100, base_defense=100,
            base_special_attack=100, base_special_defense=100, base_speed=100,
            ev_hp=0, ev_attack=0, ev_defense=0,
            ev_special_attack=0, ev_special_defense=0, ev_speed=0,
            iv_hp=31, iv_attack=31, iv_defense=31,
            iv_special_attack=31, iv_special_defense=31, iv_speed=31
        )

        expected_hp = 341
        expected_increased_stat = 259
        expected_decreased_stat = 212
        expected_other_stats = 236
        for stat_enum in StatsEnum:
            if stat_enum == StatsEnum.HP:
                self.assertEqual(pm[stat_enum], expected_hp)
            elif stat_enum == StatsEnum.SPECIAL_ATTACK:
                self.assertEqual(pm[stat_enum], expected_increased_stat)
            elif stat_enum == StatsEnum.ATTACK:
                self.assertEqual(pm[stat_enum], expected_decreased_stat)
            else:
                self.assertEqual(pm[stat_enum], expected_other_stats)

    def test_getitem_invalid_enum(self):
        '''Teste levanta exceção quando uma chave de tipo inválido é passada.
        '''

        pm = PocketMonster(
            number=151, level=100,
            name='Mew', nickname='Testy',
            nature=NaturesEnum.HARDY, _types=TypesEnum.PSYCHIC,
            base_hp=100, base_attack=100, base_defense=100,
            base_special_attack=100, base_special_defense=100, base_speed=100,
            ev_hp=0, ev_attack=0, ev_defense=0,
            ev_special_attack=0, ev_special_defense=0, ev_speed=0,
            iv_hp=31, iv_attack=31, iv_defense=31,
            iv_special_attack=31, iv_special_defense=31, iv_speed=31
        )

        with pytest.raises(TypeError):
            pm['INVALID_STAT']

    def test_init_1(self):
        '''Teste a inicialização básica de uma instância PocketMonster
        com parâmetros mínimos necessários.
        Este teste verifica se um objeto PocketMonster pode ser criado
        com os atributos essenciais e se esses atributos estão
        corretamente definidos.
        '''

        number = 151
        level = 100
        name = 'Mew'
        nickname = 'Testy'
        nature_enum = NaturesEnum.MODEST
        _types = TypesEnum.PSYCHIC
        base_stats = {
            'base_hp': 100, 'base_attack': 100,
            'base_defense': 100, 'base_special_attack': 100,
            'base_special_defense': 100, 'base_speed': 100
        }
        ev_stats = {
            'ev_hp': 0, 'ev_attack': 0, 'ev_defense': 0,
            'ev_special_attack': 0, 'ev_special_defense': 0, 'ev_speed': 0
        }
        iv_stats = {
            'iv_hp': 0, 'iv_attack': 0, 'iv_defense': 0,
            'iv_special_attack': 0, 'iv_special_defense': 0, 'iv_speed': 0
        }

        pm = PocketMonster(
            number=number, level=level, name=name, nickname=nickname,
            nature=nature_enum, _types=_types,
            **base_stats, **ev_stats, **iv_stats
        )
        nature = pm[PocketMonsterParamEnum.NATURE]

        self.assertEqual(pm[PocketMonsterParamEnum.NUMBER], number)
        self.assertEqual(pm[PocketMonsterParamEnum.LEVEL], level)
        self.assertEqual(pm[PocketMonsterParamEnum.NAME], name)
        self.assertEqual(pm[PocketMonsterParamEnum.NICKNAME], nickname)
        self.assertEqual(nature[NatureParamEnum.NATURE], nature_enum)
        self.assertEqual(pm[PocketMonsterParamEnum.TYPE_1], TypesEnum.PSYCHIC)
        self.assertIsNone(pm[PocketMonsterParamEnum.TYPE_2])
        self.assertIsNone(pm.secondary_type)
        self.assertIsNone(pm._form)

        for stat_enum in StatsEnum:
            self.assertEqual(pm._base_stats[stat_enum], 100)
            self.assertEqual(pm._ev_stats[stat_enum], 0)
            self.assertEqual(pm._iv_stats[stat_enum], 0)

    def test_init_2(self):
        '''Teste a inicialização básica de uma instância PocketMonster
        com parâmetros mínimos necessários.
        Este teste verifica se um objeto PocketMonster pode ser criado
        com os atributos essenciais e se esses atributos estão
        corretamente definidos.
        '''

        number = 151
        level = 100
        name = 'Mew'
        nickname = 'Testy'
        nature = NaturesEnum.MODEST
        _types = TypesEnum.PSYCHIC
        base_stats = {
            'base_hp': 100, 'base_attack': 100,
            'base_defense': 100, 'base_special_attack': 100,
            'base_special_defense': 100, 'base_speed': 100
        }
        ev_stats = {
            'ev_hp': 85, 'ev_attack': 85, 'ev_defense': 85,
            'ev_special_attack': 85, 'ev_special_defense': 85, 'ev_speed': 85
        }
        iv_stats = {
            'iv_hp': 31, 'iv_attack': 31, 'iv_defense': 31,
            'iv_special_attack': 31, 'iv_special_defense': 31, 'iv_speed': 31
        }

        pm = PocketMonster(
            number=number, level=level, name=name, nickname=nickname,
            nature=nature, _types=_types, **base_stats, **ev_stats, **iv_stats
        )

        self.assertEqual(pm._number, number)
        self.assertEqual(pm._level, level)
        self.assertEqual(pm._name, name)
        self.assertEqual(pm._nickname, nickname)
        self.assertEqual(pm._nature._nature, nature)
        self.assertEqual(pm.primary_type, TypesEnum.PSYCHIC)
        self.assertIsNone(pm.secondary_type)
        self.assertIsNone(pm._form)

        for stat_enum in StatsEnum:
            self.assertEqual(pm._base_stats[stat_enum], 100)
            self.assertEqual(pm._ev_stats[stat_enum], 85)
            self.assertEqual(pm._iv_stats[stat_enum], 31)

    def test_repr(self):
        '''Teste se o método __repr__ retorna o mesmo resultado que
        o método __str__.
        '''

        pm = PocketMonster(
            number=151, level=100,
            name='Mew', nickname='Testy',
            nature=NaturesEnum.MODEST, _types=TypesEnum.PSYCHIC,
            base_hp=100, base_attack=100, base_defense=100,
            base_special_attack=100, base_special_defense=100, base_speed=100,
            ev_hp=0, ev_attack=0, ev_defense=0,
            ev_special_attack=0, ev_special_defense=0, ev_speed=0,
            iv_hp=31, iv_attack=31, iv_defense=31,
            iv_special_attack=31, iv_special_defense=31, iv_speed=31
        )

        self.assertEqual(repr(pm), str(pm))

    def test_invalid_form_input(self):
        '''Teste se fornecer o form como uma string inválida gera um KeyError.
        Isso testa o caso extremo em que o parâmetro de form é uma string
        que não corresponde a nenhum valor FormEnum.
        '''

        with pytest.raises(KeyError):
            PocketMonster(
                number=151, level=100,
                name='Mew', nickname='Testy',
                nature=NaturesEnum.MODEST, _types=TypesEnum.PSYCHIC,
                base_hp=100, base_attack=100, base_defense=100,
                base_special_attack=100, base_special_defense=100,
                base_speed=100,
                ev_hp=0, ev_attack=0, ev_defense=0,
                ev_special_attack=0, ev_special_defense=0, ev_speed=0,
                iv_hp=31, iv_attack=31, iv_defense=31,
                iv_special_attack=31, iv_special_defense=31, iv_speed=31,
                form='INVALID_FORM'
            )

    def test_name_returns_nickname_when_set(self):
        '''Teste se a propriedade name retorna o nickname quando definido.
        '''

        pm = PocketMonster(
            number=151, level=100,
            name='Mew', nickname='Testy',
            nature=NaturesEnum.MODEST, _types=TypesEnum.PSYCHIC,
            base_hp=100, base_attack=100, base_defense=100,
            base_special_attack=100, base_special_defense=100, base_speed=100,
            ev_hp=0, ev_attack=0, ev_defense=0,
            ev_special_attack=0, ev_special_defense=0, ev_speed=0,
            iv_hp=31, iv_attack=31, iv_defense=31,
            iv_special_attack=31, iv_special_defense=31, iv_speed=31
        )
        self.assertEqual(pm.name, 'Testy')

    def test_name_returns_when_nickname_unset(self):
        '''Teste se a propriedade name retorna o name quando
        o nickname não for definido.
        '''

        pm = PocketMonster(
            number=151, level=100,
            name='Mew',
            nature=NaturesEnum.MODEST, _types=TypesEnum.PSYCHIC,
            base_hp=100, base_attack=100, base_defense=100,
            base_special_attack=100, base_special_defense=100, base_speed=100,
            ev_hp=0, ev_attack=0, ev_defense=0,
            ev_special_attack=0, ev_special_defense=0, ev_speed=0,
            iv_hp=31, iv_attack=31, iv_defense=31,
            iv_special_attack=31, iv_special_defense=31, iv_speed=31
        )

        self.assertEqual(pm.name, 'Mew')

    def test_number_formatting(self):
        '''Teste se a propriedade number retorna uma representação em string
        de três dígitos com zeros a esquerda do número do PocketMonster.
        '''

        pm1 = PocketMonster(
            number=6, level=100,
            name='Charizard', nickname='Fuegon',
            nature=NaturesEnum.MODEST,
            _types=[TypesEnum.FIRE, TypesEnum.FLYING],
            base_hp=60, base_attack=90, base_defense=55,
            base_special_attack=90, base_special_defense=80, base_speed=110,
            ev_hp=0, ev_attack=0, ev_defense=0,
            ev_special_attack=0, ev_special_defense=0, ev_speed=0,
            iv_hp=31, iv_attack=31, iv_defense=31,
            iv_special_attack=31, iv_special_defense=31, iv_speed=31
        )
        pm2 = PocketMonster(
            number=25, level=100,
            name='Raichu', nickname='Fathunder',
            nature=NaturesEnum.MODEST, _types=TypesEnum.ELECTRIC,
            base_hp=78, base_attack=84, base_defense=78,
            base_special_attack=109, base_special_defense=85, base_speed=100,
            ev_hp=0, ev_attack=0, ev_defense=0,
            ev_special_attack=0, ev_special_defense=0, ev_speed=0,
            iv_hp=31, iv_attack=31, iv_defense=31,
            iv_special_attack=31, iv_special_defense=31, iv_speed=31
        )

        self.assertEqual(pm1.number, '006')
        self.assertEqual(pm2.number, '025')

    def test_total_returns_sum_of_all_stats(self):
        '''Teste se a propriedade total retorna a soma de todas as
        estatísticas de um PocketMonster.
        '''

        pm = PocketMonster(
            number=151, level=100,
            name='Mew', nickname='Testy',
            nature=NaturesEnum.MODEST, _types=TypesEnum.PSYCHIC,
            base_hp=100, base_attack=100, base_defense=100,
            base_special_attack=100, base_special_defense=100, base_speed=100,
            ev_hp=0, ev_attack=0, ev_defense=0,
            ev_special_attack=0, ev_special_defense=0, ev_speed=0,
            iv_hp=31, iv_attack=31, iv_defense=31,
            iv_special_attack=31, iv_special_defense=31, iv_speed=31
        )

        expected_total = sum([pm[enum] for enum in StatsEnum])

        self.assertEqual(pm.total, expected_total)

    def test_total_with_zero_stats(self):
        '''Teste o método total quando todas as estatísticas forem zero.
        Este é um caso extremo em que a soma deve ser zero.
        '''

        pm = PocketMonster(
            number=0, level=1,
            name='Zeerou', nickname='Zeresty',
            nature=NaturesEnum.MODEST, _types=TypesEnum.PSYCHIC,
            base_hp=0, base_attack=0, base_defense=0,
            base_special_attack=0, base_special_defense=0, base_speed=0,
            ev_hp=0, ev_attack=0, ev_defense=0,
            ev_special_attack=0, ev_special_defense=0, ev_speed=0,
            iv_hp=0, iv_attack=0, iv_defense=0,
            iv_special_attack=0, iv_special_defense=0, iv_speed=0
        )

        self.assertEqual(pm.total, 35)
