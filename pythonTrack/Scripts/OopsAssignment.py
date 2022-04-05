from collections import Counter


class StringClass:
    def __init__(self,string):
        self.string = input("enter the string: ")

    def length(self):
        return len(self.string)

    def listOfCharacters(self,s1):
        self.s1=s1
        return list(self.s1)


class PairsPossible(StringClass):
    def __init__(self,str_pair):
        self.str_pair = str_pair

    def pairsList(self):
        str_list = list(self.str_pair)
        pairsList = []
        for i in range(len(str_list)):
            for j in range(len(str_list)):
                pairsList.append([str_list[i], str_list[j]])
        return pairsList

    def displayPairs(self):
        print("pairs of string:")
        for pairs in self.pairsList:
            print(pairs, end=" ")


class SearchCommonElements(PairsPossible):
    def __init__(self):
        PairsPossible.__init__()
        self.arr1 = Counter(list(self.s1))
        self.arr2 = Counter(list(self.str_pair))

    def common(self):
        commonDict = dict(self.arr1.items()&self.arr2.items())
        res=[]
        for (key,val) in commonDict.items():
            for i in range(0, val):
                res.append(key)
        return res


class EqualSumPairs(SearchCommonElements):

    def count(self):
        l = PairsPossible.pairsList()
        res=[]
        for pair in l:
            Sum = 0
            for j in range(len(pair)):
                Sum = Sum + int(pair[j])
            if Sum not in res:
                res.append(Sum)
        print("count of total number of pairs which has sum which is not equal to other pairs:",len(res))

    def displaySearchCommon(self):
        display_list = SearchCommonElements.common()
        print("result of searchCommonElements class:", display_list)


String_obj = StringClass('123')
length = String_obj.length()
list_chars = String_obj.listOfCharacters('123')
print("length of String:",length)
print("list of characters: ",list_chars)

pair_obj = PairsPossible('234')
pair_obj.displayPairs()

# common_ele = pair_obj.common()
# print("commom elements of two strings:", common_ele)

sumPirs_obj = EqualSumPairs('234')
sumPirs_obj.count()
sumPirs_obj.displaySearchCommon()


