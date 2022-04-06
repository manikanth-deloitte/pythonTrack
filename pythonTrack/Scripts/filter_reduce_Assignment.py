from functools import reduce


# filter assignment
lst1=[-1000, 500, -600, 700, 5000, -90000, -17500]


def is_positive(num):
    return num>0


convert = list(filter(is_positive, map(abs, lst1)))
print("negative to positive conversion: ", convert)


# using reduce function
def multiplication(a,b):
    return a*b


lst = [1, 2, 3, 4]
result2 = reduce(multiplication, lst)
print("result: ", result2,"\n")


# using zip function
lst1=["Netflix", "Hulu", "Sling", "Hbo"]
lst2=[198, 166, 237, 125]
Dictionary = dict(zip(lst1, lst2))
print("print dictionary using zip function\nDictionary:", Dictionary)
