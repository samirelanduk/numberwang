from math import radians, sin, cos
from ..checks import are_numeric
from ..matrices.matrix import create_vertex, Matrix

def translate(points, x, y, z):
    if not are_numeric(x, y, z):
        raise TypeError("Translation parameters must be numeric, not '%s'" % (
         str((x, y, z))
        ))
    return tuple([tuple([px + x, py + y, pz + z]) for px, py, pz in points])


def rotate(points, axis, angle):
    angle = radians(angle)
    points = [create_vertex(*point) for point in points]
    matrix = None
    if axis == "x":
        matrix = Matrix(
         (1, 0, 0),
         (0, cos(angle), -sin(angle)),
         (0, sin(angle),  cos(angle))
        )
    elif axis == "y":
        matrix = Matrix(
         (cos(angle), 0, sin(angle)),
         (0, 1, 0),
         (-sin(angle), 0, cos(angle))
        )
    elif axis == "z":
        matrix = Matrix(
         (cos(angle), -sin(angle), 0),
         (sin(angle), cos(angle), 0),
         (0, 0, 1)
        )
    new_points = [matrix * point for point in points]
    return tuple([point.columns()[0] for point in new_points])
