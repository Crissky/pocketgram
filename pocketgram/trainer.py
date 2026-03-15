from dataclasses import dataclass, field
from typing import List, Union

from pocketgram.enums.badge import BadgeEnum
from repository.mongo.base import MongoBase


@dataclass
class Trainer(MongoBase):
    user_id: str
    user_name: str
    badge_list: List[Union[BadgeEnum, str]] = field(default_factory=list)

    def __post_init__(self):
        super().__post_init__()

        if not self.user_id:
            raise ValueError(f"O user_id '{self.user_id}' não é inválido.")
        else:
            self.user_id = str(self.user_id)
        if self.user_name is not None:
            self.user_name = str(self.user_name)

        for index, bagde_str in enumerate(self.badge_list):
            if isinstance(bagde_str, str):
                self.badge_list[index] = BadgeEnum.from_name(bagde_str)

            if not isinstance(self.badge_list[index], BadgeEnum):
                raise TypeError(
                    f"O badge_list[{index}] não é um BadgeEnum válido. "
                    f"Tipo: {type(bagde_str)}"
                )

    def __str__(self):
        text = f"Treinador: {self.user_name}\n"
        text += f"ID: {self.user_id}\n"
        text += "Badges:\n"
        for badge in self.badge_list:
            text += f"  - {badge.value}\n"

        return text
