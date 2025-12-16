import unittest

from repository.mongo.models.model import Model


class TestModel(unittest.TestCase):
    def setUp(self):
        self.model1 = Model()
        self.model2 = Model()

    def test_singleton(self):
        self.assertIs(self.model1, self.model2)
