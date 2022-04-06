n='1'
try:
    n= float(n)
    #raise ValueError("string cant convert to float")
except ValueError as e:
    print(e.args)
else:
    print("no Exception")