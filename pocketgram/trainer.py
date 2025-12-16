from dataclasses import dataclass, field
from typing import List

from pocketgram.enums.badge import BadgeEnum
from repository.mongo.base import MongoBase


@dataclass
class Trainer(MongoBase):

    user_id: str
    user_name: str
    badge_list: List[BadgeEnum] = field(default_factory=list)
