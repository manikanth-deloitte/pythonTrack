# mini assignment 4 based on map and lamda functions

# 1.lamda function
def lamFun():
    val = lambda x, a, b, c: (a*(x**2))+(b*x)+c
    return val


# val = lambda x, a, b, c: (a*(x**2))+(b*x)+c
# print(val(1,2,3,4))
result1 = lamFun()
print("solution of ax^2+bx+c is: ", result1(1, 2, 3, 4))


# 2.Using map() function and lambda
list1 = ["Alaska", "Alabama", "Arizona", "Arkansas", "Colorado", "Montana", "Nevada"]
result2 = map(lambda x: [x.count("A"), x.count('a')], list1)
print("list of number of occurrence of both A and a: ", list(result2))
