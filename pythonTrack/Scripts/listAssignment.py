from collections import Counter


# count duplicates in list
def duplicateCount(arr):
    for ele in arr:
        dic = Counter(ele)
        for key in dic:
            if dic[key] > 1:
                print(key, "->", dic[key])


l = [[1, 1, 3, 2], [9, 8, 8, 1], [0, 4, 5, 0, 0, 4]]
print("Return all the duplicate values from list of arraylist")
duplicateCount(l)
print()

# Merge two lists
print("Merge two lists")
list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]
output_list = []
for i in range(len(list2)):
    for j in range(len(list1)):
        s = list1[i]+list2[j]
        output_list.append(s)
print(output_list)
print()


# extend by adding subList
print("extending by adding subList")
nested_list = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
sub_list = ["h", "i", "j"]
nested_list[2][1][2].extend(sub_list)
print([nested_list])