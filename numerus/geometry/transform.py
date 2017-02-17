from ..checks import are_numeric

def translate(points, x, y, z):
    if not are_numeric(x, y, z):
        raise TypeError("Translation parameters must be numeric, not '%s'" % (
         str((x, y, z))
        ))
    return tuple([tuple([px + x, py + y, pz + z]) for px, py, pz in points])
