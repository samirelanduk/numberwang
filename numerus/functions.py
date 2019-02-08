class Function:

    def __init__(self, *operations):
        self.operations = operations


    def __call__(self, arg):
        output = arg
        for op in self.operations: output = op(output)
        return output



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
