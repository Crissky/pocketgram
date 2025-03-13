from enum import Enum


class StatsEnum(Enum):
    '''Enum que representa as stats dos monstrinhos

    HP: Pontos de Vida
    Attack: Usado no cálculo do dano de Movimentos Físicos.
    Defense: Usado no cálculo do dano de Movimentos Físicos.
    Special Attack: Usado no cálculo do dano de Movimentos Especiais.
    Special Defense: Usado no cálculo do dano de Movimentos Especiais.
    Speed: Usando para definir a ordem de ataque.
    '''

    HP = 'HP'
    ATTACK = 'Attack'
    DEFENSE = 'Defense'
    SPECIAL_ATTACK = 'Special Attack'
    SPECIAL_DEFENSE = 'Special Defense'
    SPEED = 'Speed'
