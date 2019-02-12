class Set:

    def __init__(self, name, check):
        self.name = name
        self.check = check


    def __contains__(self, obj):
        return self.check(obj)

naturals = Set("Natural numbers", lambda o: isinstance(o, int) and o > 0)

wholes = Set("Whole numbers", lambda o: isinstance(o, int) and o >= 0)

integers = Set("Integers", lambda o: isinstance(o, int))

rationals = Set("Rational numbers", lambda o: isinstance(o, (int, float)))
