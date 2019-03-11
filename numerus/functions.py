class Function:
    """A mathematical function, which takes an input, and returns an output.

    When instantiated, zero or more 'operands' should be provided.

    A Function class also has a Python lambda associated which takes two
    arguments and returns a single value, called `func`.

    When a Function instance is called, these two things - the instance's
    operands and the class's `func` - are used together with the argument
    actually supplied, to determine the output.

    If the function instance has no operands, then the input is returned
    unchanged.

    If the function has one operand, then this value plus the input value are
    passed to `func` and the output of this is returned.

    If the function has more than one operand, then each of these operands is
    taken in turn - if it is another function the result of this function on the
    input value is used, otherwise the value itself is - and `func` is applied
    to each operand cumulatively.

    This base Function class acts as an identity function. Other subclasses are
    available."""

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



class Divide(Function):

    func = lambda s, a, b: a / b



class Power(Function):

    func = lambda s, a, b: a ** b



class Exponent(Function):

    func = lambda s, a, b: b ** a
