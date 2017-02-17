from unittest import TestCase
from numerus.geometry.transform import translate

class TransformationTest(TestCase):

    def setUp(self):
        self.points = [(1, 1, 0), (2, 1, 0), (3, 1, 0), (4, 1, 0), (5, 1, 0)]



class TranslationTests(TransformationTest):

    def test_can_translate(self):
        self.assertEqual(
         translate(self.points, 3, -2, 8),
         ((4, -1, 8), (5, -1, 8), (6, -1, 8), (7, -1, 8), (8, -1, 8))
        )
