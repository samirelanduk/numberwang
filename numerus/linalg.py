class Vector:

    def __init__(self, *values):
        self._values = tuple(values)


    @property
    def values(self):
        return self._values


    def add(self, other):
        values = [x + y for x, y in zip(self._values, other._values)]
        return Vector(*values)


    def scale(self, scalar):
        values = [v * scalar for v in self._values]
        return Vector(*values)
