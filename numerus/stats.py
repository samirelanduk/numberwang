from collections import Counter
from math import factorial
from functools import reduce
import operator
import itertools

def permutations(n, r=None):
    """Returns the number of ways of arranging r elements of a set of size n in
    a given order - the number of permuatations."""

    if r is None: return factorial(n)
    return factorial(n) / factorial(n - r)


def combinations(n, r=None):
    """Returns the number of ways of combining r elements of a set of size n,
    where order doesn't matter."""

    r = n if r is None else r
    return factorial(n) / (factorial(r) * factorial(n - r))


def multiplications(*counts):
    """Returns the product of the integers given - useful for calculating the
    number of simple events in a multi-stage process."""

    return reduce(operator.mul, counts, 1)


def permutate(collection, r=None):
    """Generates all the permutations of a given iterable, of a given length.
    It is essentially a wrapper around the built-in ``itertools.permutations``.
    """

    return itertools.permutations(collection, r=r)


def combine(collection, r=None):
    """Generates all the combinations of a given iterable, of a given length.
    It is essentially a wrapper around the built-in ``itertools.combinations``.
    """

    n = len(tuple(collection))
    r = n if r is None else r
    for combination in itertools.combinations(collection, r=r):
        yield frozenset(combination)


def multiply(*collections):
    """Generates all the multiplications of some iterables. For example, passing
    ``["A", "B"]`` and ``["+", "_"]`` would yield ``("A", "+")``,
    ``("A", "-")``, ``("B", "+")`` and ``("B", "-")``."""

    for prod in itertools.product(*collections):
        yield prod



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



class Event:
    """One or more outcomes."""

    def __init__(self, sample_space, *outcomes):
        self._outcomes = set(outcomes)
        self._sample_space = sample_space


    def __contains__(self, outcome):
        return outcome in self._outcomes


    def __or__(self, event):
        return Event(self._sample_space, *(self._outcomes | event._outcomes))


    def __and__(self, event):
        return Event(self._sample_space, *(self._outcomes & event._outcomes))


    @property
    def complement(self):
        return Event(
         self._sample_space, *(self._sample_space._outcomes - self._outcomes)
        )


    @property
    def outcomes(self):
        return set(self._outcomes)


    @property
    def count(self):
        return len(self._outcomes)


    def mutually_exclusive_with(self, event):
        return not self._outcomes & event._outcomes


    def exhaustive_with(self, event):
        return self._outcomes | event._outcomes == self._sample_space._outcomes



class SampleSpace(Event):
    """The set of possible outcomes of some experiment."""

    def __init__(self, *outcomes):
        Event.__init__(self, self, *outcomes)


    def event(self, *outcomes):
        if len(outcomes) == 1 and callable(outcomes[0]):
            outcomes = set(o for o in self._outcomes if outcomes[0](o))
        return Event(self, *outcomes)
