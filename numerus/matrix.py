from .exceptions import MatrixError

class Matrix:

    def __init__(self, *rows):
        if not rows:
            raise TypeError("Matrix needs at least one row")
        clean_rows = []
        row_length = -1
        for row in rows:
            if not isinstance(row, list) and not isinstance(row, tuple):
                raise TypeError("Matrix needs lists or tuples")
            if row_length != -1 and len(row) != row_length:
                raise ValueError("All Matrix rows must be of equal length")
            row_length = len(row)
            clean_rows.append(tuple(row))
        if row_length == 0:
            raise TypeError("Matrix rows cannot be empty")
        self._rows = tuple(clean_rows)


    def __repr__(self):
        return "<Matrix (%i×%i)>" % (len(self._rows), len(self._rows[0]))


    def __eq__(self, other):
        if not isinstance(other, Matrix) or self.size() != other.size():
            return False
        for index, row in enumerate(self._rows):
            if row != other._rows[index]:
                return False
        return True



    def __add__(self, other):
        if not can_add(self, other):
            raise MatrixError("Cannot add %s and %s." % (str(self), str(other)))
        new_rows = []
        for rindex, row in enumerate(self._rows):
            other_row = other._rows[rindex]
            new_row = [val + other_row[vindex] for vindex, val in enumerate(row)]
            new_rows.append(new_row)
        return Matrix(*new_rows)


    def __sub__(self, other):
        if not can_add(self, other):
            raise MatrixError(
             "Cannot subtract %s from %s." % (str(other), str(self))
            )
        new_rows = []
        for rindex, row in enumerate(self._rows):
            other_row = other._rows[rindex]
            new_row = [val - other_row[vindex] for vindex, val in enumerate(row)]
            new_rows.append(new_row)
        return Matrix(*new_rows)


    def __mul__(self, other):
        if not can_multiply(self, other):
            raise MatrixError("Cannot multiply %s and %s." % (str(self), str(other)))
        new_rows = []
        columns = other.columns()
        for rindex, row in enumerate(self._rows):
            new_row = []
            for column in columns:
                new_row.append(sum([val * column[index] for index, val in enumerate(row)]))
            new_rows.append(new_row)
        return Matrix(*new_rows)


    def rows(self):
        return self._rows


    def columns(self):
        return tuple([tuple(
         [row[n] for row in self._rows]
        ) for n in range(len(self._rows[0]))])


    def size(self):
        return (len(self.rows()), len(self.columns()))



def create_vertex(*values):
    return Matrix(*[(value,) for value in values])


def can_add(matrix1, matrix2):
    return matrix1.size() == matrix2.size()


def can_multiply(matrix1, matrix2):
    return matrix1.size()[1] == matrix2.size()[0]
