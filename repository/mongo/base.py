from dataclasses import asdict, dataclass, fields
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
        if not isinstance(self._id, ObjectId):
            raise TypeError(
                f"O _id passado é do tipo inválido. ({type(self._id)})"
            )

        if isinstance(self.created_at, (datetime, type(None))):
            raise TypeError(
                "O created_at passado é do tipo inválido. "
                f"({type(self.created_at)})"
            )

        if isinstance(self.updated_at, (datetime, type(None))):
            raise TypeError(
                "O updated_at passado é do tipo inválido. "
                f"({type(self.updated_at)})"
            )

    def to_dict(self):
        data = asdict(self)
        self_fields = fields(self)

        return {f.name: data[f.name] for f in self_fields if f.init}
