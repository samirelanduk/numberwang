from unittest import TestCase
import numerus.calculus as calculus

class Test(TestCase):

    def test(self):
        # Identity function
        func = calculus.Function()
        self.assertEqual(func(1), 1)
        self.assertEqual(func(-23.5), -23.5)

        # f(x) = x + 7
        func = calculus.Add(7)
        self.assertEqual(func(-3), 4)
        self.assertEqual(func(0), 7)

        # f(x) = 3x
        func = calculus.Multiply(3)
        self.assertEqual(func(2), 6)
        self.assertEqual(func(-4), -12)

        # f(x) = 4x + 7
        func = calculus.Add(calculus.Multiply(4), 7)
        self.assertEqual(func(2), 15)
        self.assertEqual(func(-4), -9)

        # f(x) = x^3
        func = calculus.Power(3)
        self.assertEqual(func(2), 8)
        self.assertEqual(func(-4), -64)

        # f(x) = 4x^2
        func = calculus.Multiply(4, calculus.Power(2))
        self.assertEqual(func(2), 16)
        self.assertEqual(func(-4), 64)

        # f(x) = x^3 - 2x^2 + 9x + 2
        func = calculus.Add(
         calculus.Power(3),
         calculus.Add(
          calculus.Multiply(-2, calculus.Power(2)),
          calculus.Add(
           calculus.Multiply(9), 2
          )
         )
        )
        self.assertEqual(func(2), 20)

        # f(x) = 1/x^2
        func = calculus.Divide(1, calculus.Power(2))
        self.assertEqual(func(2), 0.25)

        # f(x) = (x^3 + 1) / (x^2 - 7x - 10)
        func = calculus.Divide(
         calculus.Add(calculus.Power(3), 1),
         calculus.Add(calculus.Power(2), calculus.Add(
          calculus.Multiply(-7), -10
         ))
        )
        self.assertEqual(func(2), 9/-20)

        # f(x) = 2^x
        func = calculus.Exponent(2)
        self.assertEqual(func(2), 4)
        self.assertEqual(func(3), 8)
        self.assertEqual(func(4), 16)
        self.assertEqual(func(5), 32)
