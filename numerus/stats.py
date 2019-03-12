from collections import Counter

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


    @property
    def mean(self):
        return sum(self) / len(self) if len(self) else None


    @property
    def median(self):
        values = sorted(self)
        if not values: return None
        index = len(self) // 2
        if len(self) % 2:
            return values[index]
        else:
            a, b = values[index - 1: index + 1]
            return (a + b) / 2


    @property
    def mode(self):
        if len(self) == 0: return None
        counter = Counter(self)
        most_common = counter.most_common(2)
        if len(most_common) == 1: return most_common[0][0]
        top_count = most_common[0][1]
        next_count = most_common[1][1]
        if top_count == next_count: return None
        return most_common[0][0]
