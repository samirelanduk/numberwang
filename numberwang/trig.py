from math import radians, degrees, sin, asin, cos, acos, sqrt
from .checks import is_numeric

def sine_law(side1=None, angle1=None, side2=None, angle2=None):
    if side1 is not None and not is_numeric(side1):
        raise TypeError("side1 must be a number, not '%s'" % str(side1))
    if side2 is not None and not is_numeric(side2):
        raise TypeError("side2 must be a number, not '%s'" % str(side2))
    if angle1 is not None and not is_numeric(angle1):
        raise TypeError("angle1 must be a number, not '%s'" % str(angle1))
    if angle2 is not None and not is_numeric(angle2):
        raise TypeError("angle2 must be a number, not '%s'" % str(angle2))
    if [side1, angle1, side2, angle2].count(None) != 1:
        raise TypeError("You must supply precisely three arguments to sine_law()")

    if side1 is None:
        return (side2 * sin(radians(angle1))) / sin(radians(angle2))
    elif side2 is None:
        return (side1 * sin(radians(angle2))) / sin(radians(angle1))
    elif angle1 is None:
        return degrees(asin((side1 * sin(radians(angle2))) / side2))
    elif angle2 is None:
        return degrees(asin((side2 * sin(radians(angle1))) / side1))


def cosine_law(side1, side2, side3=None, angle=None):
    if not is_numeric(side1):
        raise TypeError("side1 must be a number, not '%s'" % str(side1))
    if not is_numeric(side2):
        raise TypeError("side2 must be a number, not '%s'" % str(side2))
    if side3 is not None and not is_numeric(side3):
        raise TypeError("side3 must be a number, not '%s'" % str(side3))
    if angle is not None and not is_numeric(angle):
        raise TypeError("angle must be a number, not '%s'" % str(angle))
    if side3 is not None and angle is not None:
        raise TypeError("side3 and angle both supplied")
    if side3 is None and angle is None:
        raise TypeError("You must supply either an angle or a side3")

    if side3 is None:
        return sqrt(
         ((side1 ** 2) + (side2 ** 2)) - (2 * side1 * side2 * cos(radians(angle)))
        )
    elif angle is None:
        return degrees(acos(
         ((side3 ** 2) - ((side1 ** 2) + (side2 ** 2))) / (-2 * side1 * side2)
        ))
