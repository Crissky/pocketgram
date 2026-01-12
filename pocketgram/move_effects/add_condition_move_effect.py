from typing import TYPE_CHECKING, Dict, List

from pocketgram.move_effects.base_move_effect import BaseMoveEffect
from pocketgram.status.status import Status


if TYPE_CHECKING:
    from pocketgram.moves.base_move import BaseMove
    from pocketgram.pocket_monster import PocketMonster


class AddConditionBaseMoveEffect(BaseMoveEffect):
    '''Classe 'abstrata' que representa a base para as classes com efeitos
    de adicionar uma condição.
    '''

    def __new__(cls, *args, **kwargs):
        if cls is AddConditionBaseMoveEffect:
            raise TypeError(
                f"{cls.__name__} não pode ser instanciada diretamente."
            )
        return super().__new__(cls)

    def __init__(
            self,
            duration: int = 1,
            conditions: List[Dict[Status, float]] = None,
    ):
        '''
        Args:
            duration: Número de turnos que o efeito irá durar.
            min_hit_times: Número mínimo de vezes que pode atingir o alvo.
            max_hit_times: Número máximo de vezes que pode atingir o alvo.
        '''

        self.duration = int(duration)
        self.conditions = conditions or []

    def pre_hit_apply(
        self,
        move: 'BaseMove',
        move_user: 'PocketMonster',
        allies: List['PocketMonster'],
        enemies: List['PocketMonster'],
    ) -> str:
        '''Aplica o efeito no alvo antes do ataque seja realizado.

        Args:
            target: O alvo em que o efeito será aplicado.
            power: Poder base do movimento.
            total_power: Poder total do movimento, incluindo os stats.
        '''

        pass

    def hit_apply(
        self,
        move: 'BaseMove',
        move_user: 'PocketMonster',
        allies: List['PocketMonster'],
        enemies: List['PocketMonster'],
    ) -> str:
        '''Aplica o efeito no alvo se ele foi atingido pelo movimento.

        Args:
            target: O alvo em que o efeito será aplicado.
            power: Poder base do movimento.
            total_power: Poder total do movimento, incluindo os stats.
        '''

        pass

    def pos_hit_apply(
        self,
        damage: int,
        move: 'BaseMove',
        move_user: 'PocketMonster',
        allies: List['PocketMonster'],
        enemies: List['PocketMonster'],
    ) -> str:
        '''Aplica o efeito no alvo após o alvo ser atingido.

        Args:
            target: O alvo em que o efeito será aplicado.
            damage: Dano causado no pelo ataque.
            power: Poder base do movimento.
            total_power: Poder total do movimento, incluindo os stats.
        '''

        # TODO ADICIONAR REGRA DE TESTE DE ADICIONAR UMA CONDIÇÃO
        pass
