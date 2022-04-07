class FormulaError(Exception):
    def __init__(self, data):
        self.data = data

    def __str__(self):
        return repr(self.data)


def error():
    while True:
        exp = input("enter string:")
        if exp == 'quit': break
        l = exp.split()
        print(l, l[1],type(l[1]))
        try:
            if len(l) != 3:
                raise FormulaError("given input must contain 3 elements")
            elif l[1] not in ('+', '-'):
                raise FormulaError("given input contain + or - symbol")
            else:
                l[0] = float(l[0])
                l[2] = float(l[2])
        except FormulaError as e:
            print(e.data)
        except ValueError as e:
            print(e.args)
        else:
            res = eval(exp)
            print(res)

error()
