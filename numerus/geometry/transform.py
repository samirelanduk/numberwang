def translate(points, x, y, z):
    return tuple([tuple([px + x, py + y, pz + z]) for px, py, pz in points])
