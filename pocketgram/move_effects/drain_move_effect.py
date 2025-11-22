from typing import TYPE_CHECKING, List

from pocketgram.move_effects.base_move_effect import BaseMoveEffect


if TYPE_CHECKING:
    from pocketgram.moves.base_move import BaseMove
    from pocketgram.pocket_monster import PocketMonster


class DrainBaseMoveEffect(BaseMoveEffect):
    '''Classe 'abstrata' que representa a base para as classes com efeitos
    de drenar Pontos de Vida.
    '''

    def __new__(cls, *args, **kwargs):
        if cls is DrainBaseMoveEffect:
            raise TypeError(
                f"{cls.__name__} não pode ser instanciada diretamente."
            )
        return super().__new__(cls)

    def __init__(self, duration: int = 1, percent_drain: float = 1.0):
        '''
        Args:
            duration: Número de turnos que o efeito irá durar.
            percent_drain: Porcentagem de dano que irá curar.
        '''

        self.duration = int(duration)
        self.percent_drain = float(percent_drain)

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

        heal = int(damage * self.percent_drain)
        total_heal = move_user.heal_damage(heal)

        return f'{move_user.name} curou {total_heal} de HP.'
