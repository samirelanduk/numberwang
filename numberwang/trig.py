from math import radians, degrees, sin, asin
from .checks import is_numeric

def sine_law(side1=None, angle1=None, side2=None, angle2=None):
    if side1 is not None and not is_numeric(side1):
        raise TypeError("side1 must be a number, not '%s'" % str(side1))
    if side2 is not None and not is_numeric(side1):
        raise TypeError("side12must be a number, not '%s'" % str(side2))
    if angle1 is not None and not is_numeric(side1):
        raise TypeError("angle1 must be a number, not '%s'" % str(angle1))
    if angle2 is not None and not is_numeric(side1):
        raise TypeError("angle2 must be a number, not '%s'" % str(angle2))
    if [side1, angle1, side2, angle2].count(None) != 1:
        raise TypeError("You must supply precisely three arguments to sine_law()")

    if side2 is None:
        return (side1 * sin(radians(angle2))) / sin(radians(angle1))
    elif angle2 is None:
        return degrees(asin((side2 * sin(radians(angle1))) / side1))
