n = int(input("enter the value of n:"))

# upside down right angle triangle
print("upside down right angle triangle")
for i in range(n):
    for j in range(n-i-1):
        print(end=" ")
    for k in range(i):
        if k==0 or k==1 or k==n:
            print("*", end="")
        # elif k!=0 or k!= 1 or k!=n:
        #     if k==0 or k==n:
        #         print("*",end="")
        #     else:
        #         print(end=" ")
    print()

# triangle pattern
print("triangle pattern")
for i in range(1,n+1):
    for j in range(1,2*n):
        if i==n or i+j==n+1 or j-i==n-1:
            print("*", end="")
        else:
            print(end=" ")
    print()