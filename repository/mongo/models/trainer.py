from pocketgram.trainer import Trainer
from repository.mongo import CollectionEnum
from repository.mongo.models.model import Model


class TrainerModel(Model):
    _class = property(lambda self: Trainer)
    collection = property(lambda self: CollectionEnum.TRAINER.value)
