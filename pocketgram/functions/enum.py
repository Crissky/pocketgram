from enum import Enum


def get_attr_name_from_enum(enum_value: Enum) -> str:
    ''' Retorna o nome do atributo de um Enum, em snake_case, formatado para
    ser usando como atributo de uma classe.
    '''

    if not isinstance(enum_value, Enum):
        raise TypeError('O parâmetro deve ser um Enum.')

    return f'_{enum_value.name.lower()}'
