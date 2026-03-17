import logging

from pocketgram.trainer import Trainer
from repository.mongo.models.trainer import TrainerModel


logger = logging.getLogger(__name__)


def save_trainer(trainer: Trainer) -> Trainer:
    if not isinstance(trainer, Trainer):
        raise TypeError("trainer precisa ser um Trainer.")

    trainer_model = TrainerModel()
    trainer_model.save(trainer)
    saved_trainer = get_trainer_by_id(trainer.user_id)
    logger.info(
        f"Trainer '{saved_trainer.user_name}' salvo com "
        f"USER ID '{saved_trainer.user_id}'"
    )

    return saved_trainer


def get_trainer_by_id(user_id: str) -> Trainer:
    if not isinstance(user_id, str):
        raise TypeError("user_id precisa ser uma string.")

    trainer_model = TrainerModel()
    trainer = trainer_model.get(query={"user_id": user_id})

    return trainer


def exists_trainer(user_id: str) -> bool:
    if not isinstance(user_id, str):
        raise TypeError("user_id precisa ser uma string.")
    trainer_model = TrainerModel()

    return trainer_model.exists(_id=user_id)
