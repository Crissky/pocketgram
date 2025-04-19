from typing import Union

from pocketgram.enums._types import TypesEnum
from pocketgram.enums.pocket_monster import PocketMonsterParamEnum


class Types:
    '''Classe que agrega as funções relacionadas aos Tipos dos Monstrinhos.
    '''

    def __init__(
        self,
        type_1: Union[TypesEnum, str],
        type_2: Union[TypesEnum, str] = None,
    ):

        if type_1 == type_2:
            type_2 = None
        if isinstance(type_1, str):
            type_1 = TypesEnum[type_1]
        if isinstance(type_2, str):
            type_2 = TypesEnum[type_2]
        if not isinstance(type_1, TypesEnum):
            raise TypeError(f'Tipo "{type_1}" não é válido.')
        if not isinstance(type_2, (TypesEnum, type(None))):
            raise TypeError(f'Tipo "{type_2}" não é válido.')

        self._type_1 = type_1
        self._type_2 = type_2

    @property
    def primary(self) -> TypesEnum:
        '''Retorna o tipo primário do Monstrinho.
        '''

        return self._type_1

    @property
    def secondary(self) -> TypesEnum:
        '''Retorna o tipo secundário do Monstrinho.
        '''

        return self._type_2

    def __getitem__(self, key: PocketMonsterParamEnum) -> TypesEnum:
        '''Retorna o tipo do Monstrinho.
        '''

        if key == PocketMonsterParamEnum.TYPE_1:
            return self.primary
        elif key == PocketMonsterParamEnum.TYPE_2:
            return self.secondary
        else:
            raise KeyError(f'Tipo "{key}" não encontrada.')


if __name__ == '__main__':
    types = Types('FIRE', 'FLYING')
    print(types.primary)
    print(types.secondary)
    print(types[PocketMonsterParamEnum.TYPE_1])
    print(types[PocketMonsterParamEnum.TYPE_2])
