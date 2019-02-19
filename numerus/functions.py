class Function:

    def __call__(self, arg):
        return arg



class Add:

    def __init__(self, *operands):
        self.operands = operands

    def __call__(self, arg):
        if len(self.operands) == 1:
            return arg + self.operands[0]
        else:
            value = 0
            for op in self.operands:
                try:
                    value += op(arg)
                except:
                    value += op
            return value



class Multiply:

    def __init__(self, *operands):
        self.operands = operands


    def __call__(self, arg):
        if len(self.operands) == 1:
            return arg * self.operands[0]
        else:
            value = 1
            for op in self.operands:
                try:
                    value *= op(arg)
                except:
                    value *= op
            return value



class Power:

    def __init__(self, *operands):
        self.operands = operands


    def __call__(self, arg):
        if len(self.operands) == 1:
            return arg ** self.operands[0]
        else:
            value = 0
            for op in self.operands:
                try:
                    value **= op(arg)
                except:
                    value **= op
            return value
