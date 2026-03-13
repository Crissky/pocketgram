import unittest

from pocketgram.enums.badge import BadgeEnum, KantoBadgeEnum
from pocketgram.trainer import Trainer


class TestTrainer(unittest.TestCase):

    def test_init(self):
        trainer = Trainer(user_id="123456", user_name="Ash")

        self.assertEqual(trainer.user_id, "123456")
        self.assertEqual(trainer.user_name, "Ash")
        self.assertEqual(trainer.badge_list, [])

    def test_init_with_badges(self):
        trainer = Trainer(
            user_id="123456",
            user_name="Ash",
            badge_list=[KantoBadgeEnum.BOULDER, KantoBadgeEnum.CASCADE],
        )

        self.assertEqual(len(trainer.badge_list), 2)
        self.assertEqual(trainer.badge_list[0], KantoBadgeEnum.BOULDER)
        self.assertEqual(trainer.badge_list[1], KantoBadgeEnum.CASCADE)

    def test_init_with_string_badges(self):
        """Teste que verifica se badges passadas como strings são
        convertidas para BadgeEnum.
        """

        trainer = Trainer(
            user_id="123456",
            user_name="Ash",
            badge_list=["BOULDER", "CASCADE"],
        )

        self.assertEqual(len(trainer.badge_list), 2)
        self.assertIsInstance(trainer.badge_list[0], BadgeEnum)
        self.assertIsInstance(trainer.badge_list[1], BadgeEnum)
        self.assertEqual(trainer.badge_list[0], KantoBadgeEnum.BOULDER)
        self.assertEqual(trainer.badge_list[1], KantoBadgeEnum.CASCADE)

    def test_init_empty_user_id(self):
        with self.assertRaises(ValueError):
            Trainer(user_id="", user_name="Ash")

    def test_init_none_user_id(self):
        with self.assertRaises(ValueError):
            Trainer(user_id=None, user_name="Ash")

    def test_init_invalid_badge_type(self):
        """Teste que verifica se um TypeError é levantado quando
        um item da badge_list não é um BadgeEnum válido.
        """

        with self.assertRaises(TypeError):
            Trainer(user_id="123456", user_name="Ash", badge_list=[123])

    def test_user_id_conversion_to_string(self):
        trainer = Trainer(user_id=123456, user_name="Ash")

        self.assertIsInstance(trainer.user_id, str)
        self.assertEqual(trainer.user_id, "123456")

    def test_user_name_conversion_to_string(self):
        trainer = Trainer(user_id="123456", user_name=123)

        self.assertIsInstance(trainer.user_name, str)
        self.assertEqual(trainer.user_name, "123")

    def test_str(self):
        trainer = Trainer(
            user_id="123456",
            user_name="Ash",
            badge_list=[KantoBadgeEnum.BOULDER, KantoBadgeEnum.CASCADE],
        )

        result = str(trainer)

        self.assertIn("Treinador: Ash", result)
        self.assertIn("ID: 123456", result)
        self.assertIn("Badges:", result)
        self.assertIn("🪨ROCHA", result)
        self.assertIn("💧CASCATA", result)

    def test_str_without_badges(self):
        trainer = Trainer(user_id="123456", user_name="Ash")

        result = str(trainer)

        self.assertIn("Treinador: Ash", result)
        self.assertIn("ID: 123456", result)
        self.assertIn("Badges:", result)
