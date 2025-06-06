from enum import Enum


class StatsEnum(Enum):
    '''Enum que representa as stats dos Monstrinhos

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


class BattleStatsEnum(Enum):
    ACCURACY = 'Accuracy'
    EVASIVENESS = 'Evasiveness'


ALL_STATS_ENUM_CLASSES = (StatsEnum, BattleStatsEnum)
