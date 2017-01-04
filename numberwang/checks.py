def is_numeric(number):
    if isinstance(number, bool):
        return False
    elif isinstance(number, int) or isinstance(number, float):
        return True
    else:
        return False
