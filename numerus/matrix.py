class Matrix:

    def __init__(self, *rows):
        clean_rows = []
        for row in rows:
            if not isinstance(row, list) and not isinstance(row, tuple):
                raise TypeError("Matrix needs lists or tuples")
            clean_rows.append(tuple(row))
        self._rows = tuple(clean_rows)
