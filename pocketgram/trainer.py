from dataclasses import dataclass, field
from typing import List

from pocketgram.enums.badge import BadgeEnum
from repository.mongo.base import MongoBase


@dataclass
class Trainer(MongoBase):

    user_id: str
    user_name: str
    badge_list: List[Union[BadgeEnum, str]] = field(default_factory=list)

    def __post_init__(self):
        super().__post_init__()

        for index, bagde_enum in enumerate(self.badge_list):
            if isinstance(bagde_enum, str):
                self.badge_list[index] = BadgeEnum(bagde_enum)

            if not isinstance(self.badge_list[index], BadgeEnum):
                raise TypeError(
                    f"O badge_list[{index}] não é um BadgeEnum válido. "
                    f"Tipo: {type(bagde_enum)}"
                )

