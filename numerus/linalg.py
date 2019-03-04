"""Linear Algebra utilities."""

class Vector:
    """A... vector.

    When you create a vector, it is automatically added to the VectorSpace of
    the relevant dimension number."""

    def __init__(self, *values):
        try:
            self._values = tuple(values[0])
        except: self._values = tuple(values)


    def __repr__(self):
        return f"<Vector {list(self._values)}>"


    @property
    def values(self):
        """The values of the vector.

        :rtype: ``tuple``"""

        return self._values


    def add(self, other):
        """Takes another vector, and returns the resultant Vector that is the
        sum of the two.

        :param Vector other: the other vector.
        :rtype: ``Vector``"""

        values = [x + y for x, y in zip(self._values, other._values)]
        return Vector(*values)


    def scale(self, scalar):
        """Returns a new vector that is a scaled version of this one.

        :param float scalar: the amount to scale by.
        :rtype: ``Vector``"""

        values = [v * scalar for v in self._values]
        return Vector(*values)
