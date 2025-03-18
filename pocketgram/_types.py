from pocketgram.enums._types import TypesEnum


class Types:
    '''Classe que agrega as funções relacionadas aos Tipos dos Monstrinhos.
    '''

    def __init__(
        self,
        type_1: TypesEnum,
        type_2: TypesEnum = None,
    ):
        self.type_1 = type_1
        self.type_2 = type_2
