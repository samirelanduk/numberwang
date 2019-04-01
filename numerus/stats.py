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



class RandomVariable:
    """Generates a value from a sample space of possible values, each with an
    associated probability."""

    def __init__(self, *outcomes):
        self._mapping = [[outcome, 1 / len(outcomes)] for outcome in outcomes]


    def __call__(self, outcome):
        event = outcome if isinstance(outcome, Event) else Event(outcome)
        probability = 0
        for pair in self._mapping:
            if pair[0] in event: probability += pair[1]
        return probability


    @property
    def sample_space(self):
        """All the possible outcomes."""

        return set(pair[0] for pair in self._mapping)



class Event:
    """One or more simple events. They are essentially containers of outcomes -
    an outcome is either in an event or it is not."""

    def __init__(self, *simple_events, callable=None):
        self._callable = callable if callable else lambda o: o in simple_events


    def __contains__(self, outcome):
        return self._callable(outcome)


    def __or__(self, event):
        return Event(
         callable=lambda o: bool(self._callable(o)) or bool(event._callable(o))
        )


    def __and__(self, event):
        return Event(
         callable=lambda o: bool(self._callable(o)) and bool(event._callable(o))
        )


    @property
    def complement(self):
        return Event(callable=lambda o: not self._callable(o))
