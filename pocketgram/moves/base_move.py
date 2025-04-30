from abc import ABC
from typing import List

from pocketgram.enums._types import TypesEnum
from pocketgram.enums.move_category import MoveCategoryEnum
from pocketgram.move_effects.base_move_effect import BaseMoveEffect


class BaseMove(ABC):
    '''Classe abstrata que representa a base para as classes de Movimentos.
    '''

    def __init__(
        self,
        name: str,
        _type: TypesEnum,
        category: MoveCategoryEnum,
        used_pp: int,
        max_pp: int,
        power: int,
        accuracy: int,
        priority: int,
        effect_list: List[BaseMoveEffect] = None,
        makes_contact: bool = False,
    ):
        '''
        Args:
            name: Nome do Movimento.
            type: Enum com o tipo do Movimento.
            category: Categoria do Movimento.
            used_pp: Valor de PP que já foi utilizado.
            max_pp: Valro máximo do PP.
            power: Poder do Movimento.
            accuracy: Acurácia do Movimento
            priority: Nível de prioridade do Movimento (Afeta ordem de ataque).
            effect_list: Efeitos que o Movimento realiza ao ser utilizado.
            makes_contact: Indica se o Movimento faz de contato físico.
        '''

        self._name = name
        self._type = _type
        self._category = category
        self._used_pp = used_pp
        self._max_pp = max_pp
        self._power = power
        self._accuracy = accuracy
        self._priority = priority
        self._effect_list = effect_list or []
        self._makes_contact = makes_contact
