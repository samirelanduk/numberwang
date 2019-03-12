class Variable:

    def __init__(self, *values):
        self._values = values


    def __len__(self):
        return len(self._values)


    def __iter__(self):
        return iter(self._values)


    def __getitem__(self, index):
        return self._values[index]


    @property
    def values(self):
        return self._values


    @property
    def length(self):
        return len(self._values)
