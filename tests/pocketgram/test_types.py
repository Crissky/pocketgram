import pytest
import unittest

from pocketgram._types import Types
from pocketgram.enums._types import TypesEnum
from pocketgram.enums.pocket_monster import PocketMonsterParamEnum


class TestTypes(unittest.TestCase):

    def test_init_only_primary_type(self):
        '''Teste a inicialização da classe Types apenas com o tipo primário.
        Verifica se o tipo primário está definido corretamente e se o
        tipo secundário é None.
        '''

        primary_type = TypesEnum.NORMAL
        types = Types(type_1=primary_type)

        primary_type_str = 'NORMAL'
        types_str = Types(type_1=primary_type_str)

        self.assertEqual(types.primary, TypesEnum.NORMAL)
        self.assertIsNone(types.secondary)
        self.assertEqual(types_str.primary, TypesEnum.NORMAL)
        self.assertIsNone(types_str.secondary)

    def test_init_all_types(self):
        '''Teste a inicialização da classe Types com ambos os tipos.
        '''

        primary_type = TypesEnum.GRASS
        secondary_type = TypesEnum.POISON
        primary_type_str = 'GRASS'
        secondary_type_str = 'POISON'
        types = Types(type_1=primary_type, type_2=secondary_type)
        types_str = Types(type_1=primary_type_str, type_2=secondary_type_str)
        types_mix1 = Types(type_1=primary_type_str, type_2=secondary_type)
        types_mix2 = Types(type_1=primary_type, type_2=secondary_type_str)

        self.assertEqual(types.primary, TypesEnum.GRASS)
        self.assertEqual(types.secondary, TypesEnum.POISON)
        self.assertEqual(types_str.primary, TypesEnum.GRASS)
        self.assertEqual(types_str.secondary, TypesEnum.POISON)
        self.assertEqual(types_mix1.primary, TypesEnum.GRASS)
        self.assertEqual(types_mix1.secondary, TypesEnum.POISON)
        self.assertEqual(types_mix2.primary, TypesEnum.GRASS)
        self.assertEqual(types_mix2.secondary, TypesEnum.POISON)

    def test_init_invalid_type_1(self):
        '''Teste se a inicialização de Tipos com um type_1 inválido
        gerando um TypeError.
        '''

        with self.assertRaises(KeyError):
            Types(type_1='invalid_type')
        with self.assertRaises(TypeError):
            Types(type_1=[])
        with self.assertRaises(TypeError):
            Types(type_1=['invalid_type'])

    def test_init_invalid_type_2(self):
        '''Teste se a inicialização de Tipos com um type_2 inválido
        gerando um TypeError.
        '''

        with self.assertRaises(KeyError):
            Types(type_1=TypesEnum.NORMAL, type_2='invalid_type')
        with self.assertRaises(TypeError):
            Types(type_1=TypesEnum.NORMAL, type_2=[])
        with self.assertRaises(TypeError):
            Types(type_1=TypesEnum.NORMAL, type_2=['invalid_type'])
        with self.assertRaises(KeyError):
            Types(type_1='NORMAL', type_2='invalid_type')
        with self.assertRaises(TypeError):
            Types(type_1='NORMAL', type_2=[])
        with self.assertRaises(TypeError):
            Types(type_1='NORMAL', type_2=['invalid_type'])

    def test_getitem_primary_type(self):
        '''Teste se __getitem__ retorna o tipo primário quando fornecido
        PocketMonsterParamEnum.TYPE_1
        '''

        types = Types(type_1=TypesEnum.NORMAL, type_2=TypesEnum.FLYING)
        result = types[PocketMonsterParamEnum.TYPE_1]
        self.assertEqual(result, TypesEnum.NORMAL)

    def test_getitem_secondary_type(self):
        '''Teste se __getitem__ retorna o tipo secundário quando fornecido
        PocketMonsterParamEnum.TYPE_2
        '''

        types = Types(type_1=TypesEnum.NORMAL, type_2=TypesEnum.FLYING)
        result = types[PocketMonsterParamEnum.TYPE_2]
        self.assertEqual(result, TypesEnum.FLYING)

    def test_getitem_invalid_key(self):
        '''Teste se __getitem__ gera KeyError quando recebe uma chave inválida.
        '''

        types = Types(type_1=TypesEnum.NORMAL)
        with pytest.raises(KeyError):
            types[PocketMonsterParamEnum.NAME]
        with pytest.raises(KeyError):
            types['TYPE_1']
        with pytest.raises(KeyError):
            types['TYPE_2']

    def test_primary_returns_type_1(self):
        '''Teste se a propriedade primary retorna o atributo type_1 da
        instância Types.
        '''

        type_1a = TypesEnum.NORMAL
        type_1b = TypesEnum.NORMAL
        type_2b = TypesEnum.FLYING
        types_a = Types(type_1=type_1a)
        types_b = Types(type_1=type_1b, type_2=type_2b)

        self.assertEqual(types_a.primary, TypesEnum.NORMAL)
        self.assertEqual(types_b.primary, TypesEnum.NORMAL)

    def test_secondary_returns_correct_type(self):
        '''Teste se a propriedade secondary retorna o tipo secundário
        correto do Monstrinho.
        '''

        type_1 = TypesEnum.NORMAL
        type_2 = TypesEnum.FLYING
        types_a = Types(type_1=type_1, type_2=type_2)

        self.assertEqual(types_a.secondary, TypesEnum.FLYING)
