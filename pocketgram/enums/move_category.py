from enum import Enum


class MoveCategoryEnum(Enum):
    '''Enum que representa as categorias de Movimentos.

    Movimentos Físicos e Especiais são Movimentos de ataque
    que causarão dano ao oponente.

    Movimentos de Status, como o nome indica, mudam o status de um pokémon
    de alguma forma - por exemplo, aumentando ou diminuindo as
    estatísticas do atacante ou do oponente.
    '''

    PHYSICAL = 'Physical'
    SPECIAL = 'Special'
    STATUS = 'Status'
