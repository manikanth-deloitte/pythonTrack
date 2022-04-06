def fibo(n):
    f1 = 0
    f2 = 1
    i=0
    while i < n:
        yield f1
        f3 = f1 + f2
        f1 = f2
        f2 = f3
        i += 1


fibo_values = fibo(10)
print(fibo_values)
print("fibonacci values using generators")
print(next(fibo_values))
print(next(fibo_values))
print(fibo_values.__next__())
for i in fibo_values:
    print(i)