from random import randint
from typing import TYPE_CHECKING, List

from pocketgram.move_effects.base_move_effect import BaseMoveEffect


if TYPE_CHECKING:
    from pocketgram.moves.base_move import BaseMove
    from pocketgram.pocket_monster import PocketMonster


class MultiHitBaseMoveEffect(BaseMoveEffect):
    '''Classe 'abstrata' que representa a base para as classes com efeitos
    de atacar mais de uma vez por turno.
    '''

    def __new__(cls, *args, **kwargs):
        if cls is MultiHitBaseMoveEffect:
            raise TypeError(
                f"{cls.__name__} não pode ser instanciada diretamente."
            )
        return super().__new__(cls)

    def __init__(
            self,
            duration: int = 1,
            min_hit_times: int = 1,
            max_hit_times: int = 2
    ):
        '''
        Args:
            duration: Número de turnos que o efeito irá durar.
            min_hit_times: Número mínimo de vezes que pode atingir o alvo.
            max_hit_times: Número máximo de vezes que pode atingir o alvo.
        '''

        self.duration = int(duration)
        self.min_hit_times = int(min_hit_times)
        self.max_hit_times = int(max_hit_times)

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

        total_hit_times = randint(self.min_hit_times, self.max_hit_times)
        report_msg = (
            f'{move_user.name} atingiu {total_hit_times} vezes o alvo.'
        )

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

        pass


class DoubleHitBaseMoveEffect(MultiHitBaseMoveEffect):
    '''Classe de efeito de Ataque Duplo.
    '''

    def __init__(self, duration: int = 1):
        super.__init__(duration=duration, min_hit_times=2, max_hit_times=2)
