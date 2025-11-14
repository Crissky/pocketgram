from abc import ABC, abstractmethod
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from pocketgram.pocket_monster import PocketMonster


class BaseMoveEffect(ABC):
    '''Classe abstrata que representa a base para as classes dos Efeitos dos
    Movimentos.
    '''

    def __init__(self, duration: int = 1):
        '''
        Args:
            duration: Número de turnos que o efeito irá durar.
        '''

        self.duration = int(duration)

    @abstractmethod
    def pre_hit_apply(
        self,
        power: int,
        total_power: int,
        *targets: 'PocketMonster',
    ):
        '''Aplica o efeito no alvo antes do ataque seja realizado.

        Args:
            target: O alvo em que o efeito será aplicado.
            power: Poder base do movimento.
            total_power: Poder total do movimento, incluindo os stats.
        '''

        pass

    @abstractmethod
    def hit_apply(
        self,
        power: int,
        total_power: int,
        *targets: 'PocketMonster',
    ):
        '''Aplica o efeito no alvo se ele foi atingido pelo movimento.

        Args:
            target: O alvo em que o efeito será aplicado.
            power: Poder base do movimento.
            total_power: Poder total do movimento, incluindo os stats.
        '''

        pass

    @abstractmethod
    def pos_hit_apply(
        self,
        damage: int,
        power: int,
        total_power: int,
        *targets: 'PocketMonster',
    ):
        '''Aplica o efeito no alvo após o alvo ser atingido.

        Args:
            target: O alvo em que o efeito será aplicado.
            damage: Dano causado no pelo ataque.
            power: Poder base do movimento.
            total_power: Poder total do movimento, incluindo os stats.
        '''

        pass
