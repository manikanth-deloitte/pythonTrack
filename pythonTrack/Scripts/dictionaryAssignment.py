# map the following list into dictionary
print("map the lists into dictionary")
Keys = ["Ten", "Twenty", "Thirty"]
Value = [10, 20, 30]
Dic = {}
for i in range(len(Keys)):
    Dic[Keys[i]] = Value[i]
print(Dic)
Dic_zip = dict(zip(Keys,Value))
print("merging lists using zip:\n", Dic_zip)
print()


# merge two dictionaries
print("merging two dictionaries")
dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
res = dict1 | dict2
print(res)
# using update method
dict1.update(dict2)
print(dict1)
print()

# Rename key city to location in the following dictionary
print("Rename key city to location in the given dictionary")
sampleDict = {
  "name": "Kelly",
  "age": 25,
  "salary": 8000,
  "city": "New york"
}
# sampleDict["location"]=sampleDict["city"]
# del sampleDict["city"]
sampleDict["location"] = sampleDict.pop("city")
print(sampleDict)
print()


# Convert Dictionary to list
print("convert Dictionary to list")
Dict = {"HuEx": [1, 3, 4],
        "is": [7, 6],
        "best": [4, 5]
        }
res_list = []
for key in Dict:
    temp_list = []
    temp_list.append(key)
    for i in Dict[key]:
        temp_list.append(i)
    res_list.append(temp_list)
print(res_list)

