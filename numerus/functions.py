class Function:

    def __init__(self, *operations):
        self.operations = operations


    def __call__(self, arg):
        output = arg
        terms = []
        for op in self.operations:
            try:
                terms.append(Function(*op)(arg))
            except:
                output = op(output)
        return sum(terms) + output



class Operation:

    def __init__(self, *args):
        pass


    def __call__(self, value):
        pass



class Add:

    def __init__(self, value):
        self.value = value


    def __call__(self, value):
        return value + self.value



class Multiply:

    def __init__(self, value):
        self.value = value


    def __call__(self, value):
        return value * self.value



class Power:

    def __init__(self, value):
        self.value = value


    def __call__(self, value):
        return value ** self.value
