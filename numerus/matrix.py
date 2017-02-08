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
