
def twice(func):
    def twiceAction(n1,n2):
        print("function will run twice")
        func(n1,n2)
        func(n1,n2)
    return twiceAction


@twice
def multiply(num1, num2):
    print(num1 * num2)


multiply(5,3)