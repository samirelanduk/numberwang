from .checks import is_numeric

def mean(*values):
    if not values:
        raise TypeError("Cannot take mean of no values")
    for value in values:
        if not is_numeric(value):
            raise TypeError("'%s' is not numeric" % str(value))
    return sum(values) / len(values)
