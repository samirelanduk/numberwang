from unittest import TestCase
from numberwang.trig import sine_law

class SineLawTests(TestCase):

    def test_can_get_side_from_other_side_and_two_angles(self):
        self.assertAlmostEqual(
         sine_law(side1=2, angle1=30, angle2=105),
         3.86,
         delta=0.005
        )


    def test_can_get_angle_given_other_angle_and_two_sides(self):
        self.assertAlmostEqual(
         sine_law(angle1=40, side1=30, side2=40),
         58.99,
         delta=0.005
        )


    def test_all_arguments_must_be_numeric(self):
        with self.assertRaises(TypeError):
            sine_law(side1="2", angle1=30, angle2=105)
        sine_law(side1=2.5, angle1=30, angle2=105)
        with self.assertRaises(TypeError):
            sine_law(side1=2, angle1="30", angle2=105)
        sine_law(side1=2, angle1=30.5, angle2=105)
        with self.assertRaises(TypeError):
            sine_law(side1=2, angle1=30, angle2="105")
        sine_law(side1=2, angle1=30, angle2=105.5)
        with self.assertRaises(TypeError):
            sine_law(angle1=40, side1=30, side2="40")
        sine_law(angle1=40, side1=30, side2=40.5)
