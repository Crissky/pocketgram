from pocketgram.enums._types import TypesEnum


class Types:
    '''Classe que agrega as funções relacionadas aos Tipos dos Monstrinhos.
    '''

    def __init__(
        self,
        type_1: TypesEnum,
        type_2: TypesEnum = None,
    ):
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
