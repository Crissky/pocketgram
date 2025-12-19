from pocketgram.trainer import Trainer
from repository.mongo.models.trainer import TrainerModel


def save_trainer(trainer: Trainer) -> Trainer:
    if not isinstance(trainer, Trainer):
        raise TypeError("trainer precisa ser um Trainer.")

    trainer_model = TrainerModel()
    trainer_model.save(trainer)

    return get_trainer_by_id(trainer.user_id)


def get_trainer_by_id(user_id: str) -> Trainer:
    if not isinstance(user_id, str):
        raise TypeError("user_id precisa ser uma string.")

    trainer_model = TrainerModel()
    trainer = trainer_model.get(query={"user_id": user_id})

    return trainer
