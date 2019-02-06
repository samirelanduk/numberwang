from unittest import TestCase
import numerus

class Test(TestCase):

    def test(self):
        # Identity function
        func = numerus.Function()
        self.assertEqual(func(1), 1)
        self.assertEqual(func(-23.5), -23.5)
