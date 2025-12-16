from dataclasses import dataclass
from datetime import datetime
from typing import Union

from bson import ObjectId


@dataclass(kw_only=True)
class MongoBase:
    _id: Union[ObjectId, str] = None
    created_at: datetime = None
    updated_at: datetime = None

    def __post_init__(self):
        if self._id is None or isinstance(self._id, str):
            self._id = ObjectId(self._id)
        elif not isinstance(self._id, ObjectId):
            raise TypeError(
                f"O _id passado é do tipo inválido. ({type(self._id)})"
            )

        if self.created_at is not None and not isinstance(
            self.created_at, datetime
        ):
            raise TypeError(
                "O created_at passado é do tipo inválido. "
                f"({type(self.created_at)})"
            )

        if self.updated_at is not None and not isinstance(
            self.updated_at, datetime
        ):
            raise TypeError(
                "O updated_at passado é do tipo inválido. "
                f"({type(self.updated_at)})"
            )
