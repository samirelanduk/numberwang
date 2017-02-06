"""Tools for statistical analysis and measures of probability."""

from collections import Counter
from .checks import are_numeric

def mean(*values):
    """Returns the arithmetic mean of a set of values.

    :param \*values: The numbers you wish to find the mean of.
    :rtype: ``float``"""

    if not values:
        raise TypeError("Cannot take mean of no values")
    if not are_numeric(*values):
        raise TypeError("'%s' contains non-numeric data" % str(values))
    return sum(values) / len(values)


def median(*values):
    """Returns the median of a set of values.

    :param \*values: The numbers you wish to find the median of.
    :rtype: ``float``"""

    if not values:
        raise TypeError("Cannot take mean of no values")
    if not are_numeric(*values):
        raise TypeError("'%s' contains non-numeric data" % str(values))
    values = sorted(values)
    length = len(values)
    if length % 2:
        return values[int((length / 2) - 0.5)]
    else:
        midway = int(length / 2)
        return (values[midway - 1] + values[midway]) / 2


def mode(*values):
    """Returns the mode of a set of values. If there is more than one mode, the
    function will return ``None``.

    :param \*values: The numbers you wish to find the mode of.
    :rtype: ``float``"""

    if not values:
        raise TypeError("Cannot take mode of no values")
    if not are_numeric(*values):
        raise TypeError("'%s' contains non-numeric data" % str(values))
    values = Counter(values)
    highest_frequency = max(values.values())
    values = [value for value in values if values[value] == highest_frequency]
    if len(values) == 1:
        return values[0]
