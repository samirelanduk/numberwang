from unittest import TestCase
import numerus

class Test(TestCase):

    def test(self):
        # Identity function
        func = numerus.Function()
        self.assertEqual(func(1), 1)
        self.assertEqual(func(-23.5), -23.5)

        # f(x) = x + 7
        func = numerus.Add(7)
        self.assertEqual(func(-3), 4)
        self.assertEqual(func(0), 7)

        # f(x) = 3x
        func = numerus.Multiply(3)
        self.assertEqual(func(2), 6)
        self.assertEqual(func(-4), -12)

        # f(x) = 4x + 7
        func = numerus.Add(numerus.Multiply(4), 7)
        self.assertEqual(func(2), 15)
        self.assertEqual(func(-4), -9)

        # f(x) = x^3
        func = numerus.Power(3)
        self.assertEqual(func(2), 8)
        self.assertEqual(func(-4), -64)

        # f(x) = 4x^2
        func = numerus.Multiply(4, numerus.Power(2))
        self.assertEqual(func(2), 16)
        self.assertEqual(func(-4), 64)

        # f(x) = x^3 - 2x^2 + 9x + 2
        func = numerus.Add(
         numerus.Power(3),
         numerus.Add(
          numerus.Multiply(-2, numerus.Power(2)),
          numerus.Add(
           numerus.Multiply(9), 2
          )
         )
        )
        self.assertEqual(func(2), 20)
