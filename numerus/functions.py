class Function:

    func = lambda a, b: 0

    def __init__(self, *operands):
        self.operands = operands


    def __call__(self, arg):
        if len(self.operands) == 0:
            return arg
        elif len(self.operands) == 1:
            return self.func(arg, self.operands[0])
        else:
            value = self.operands[0]
            value = value(arg) if isinstance(value, Function) else value
            for op in self.operands[1:]:
                op = op(arg) if isinstance(op, Function) else op
                value = self.func(value, op)
            return value



class Add(Function):

    func = lambda s, a, b: a + b



class Multiply(Function):

    func = lambda s, a, b: a * b



class Power(Function):

    func = lambda s, a, b: a ** b
