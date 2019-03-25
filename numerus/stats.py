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


    @property
    def max(self):
        return max(self._values)


    @property
    def min(self):
        return min(self._values)


    @property
    def range(self):
        return self.max - self.min


    def deviation(self, value):
        return value - self.mean


    @property
    def variance(self):
        msd =  sum(self.deviation(val) ** 2 for val in self._values)
        return msd / (len(self) - 1)


    @property
    def pop_variance(self):
        msd =  sum(self.deviation(val) ** 2 for val in self._values)
        return msd / len(self)


    @property
    def st_dev(self):
        return self.variance ** 0.5


    @property
    def pop_st_dev(self):
        return self.pop_variance ** 0.5


    def zscore(self, value):
        return (value - self.mean) / self.st_dev


    def percentile(self, value):
        below = len([v for v in self._values if v < value])
        return int((below / len(self._values)) * 100)


    def quartile(self, value):
        below = len([v for v in self._values if v < value])
        return min((int((below / len(self._values)) * 4) + 1, 4))
