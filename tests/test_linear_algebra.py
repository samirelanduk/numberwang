from unittest import TestCase
import numerus

class Test(TestCase):

    def test(self):
        vector1 = numerus.Vector(2, 4)
        self.assertEqual(vector1.values, (2, 4))

        vector2 = numerus.Vector([-1, 9])
        self.assertEqual(vector2.values, (-1, 9))

        vector3 = vector1.add(vector2)
        self.assertEqual(vector3.values, (1, 13))

        vector4 = vector3.scale(0.5)
        self.assertEqual(vector4.values, (0.5, 6.5))
