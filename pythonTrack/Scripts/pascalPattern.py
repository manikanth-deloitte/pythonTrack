def pascal(n):
    pascal_list = []
    for i in range(n):
        temp_list = []
        for j in range(n):
            if j == 0:
                temp_list.append(1)
            elif i==0:
                temp_list.append(0)
            else:
                temp_list.append(pascal_list[i-1][j]+pascal_list[i-1][j-1])
        pascal_list.append(temp_list)
    return pascal_list


l = pascal(5)
print(l)
for i in range(len(l)):
    for j in range(len(l[i])):
        print(l[i][j], end=" ")
    print()