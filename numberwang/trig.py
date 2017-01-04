from math import radians, degrees, sin, asin

def sine_law(side1=None, angle1=None, side2=None, angle2=None):
    if side2 is None:
        return (side1 * sin(radians(angle2))) / sin(radians(angle1))
    elif angle2 is None:
        return degrees(asin((side2 * sin(radians(angle1))) / side1))
