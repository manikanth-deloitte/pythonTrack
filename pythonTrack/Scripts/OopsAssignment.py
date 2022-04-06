from collections import Counter


class StringClass:
    def __init__(self):
        self.str1 = input("enter the string: ")

    def length(self):
        return len(self.str1)

    def listOfCharacters(self):
        return list(self.str1)


class PairsPossible(StringClass):
    def __init__(self, str2):
        super().__init__()
        self.str2 = str2

    def pairsList(self):
        str_list = list(self.str2)
        pairs_list = []
        for i in range(len(str_list)):
            for j in range(len(str_list)):
                pairs_list.append([str_list[i], str_list[j]])
        return pairs_list

    def displayPairs(self):
        print("pairs of string:")
        self.l = self.pairsList()
        for pairs in self.l:
            print(pairs, end=" ")


class SearchCommonElements:
    def __init__(self,str3,str4):
        self.str3 = str3
        self.str4 = str4

    def common(self):
        self.d1 = dict(Counter(list(self.str3)))
        self.d2 = dict(Counter(list(self.str4)))
        self.commomDic = dict(self.d1.items()&self.d2.items())
        res = []
        for (k,v) in self.commomDic.items():
            for i in range(0,v):
                res.append(k)
        return list(set(res))


class EqualSumPairs(SearchCommonElements):
    def __init__(self,s1,s2):
        super().__init__(s1,s2)
        self.lst = self.common()
        print(self.lst)

    def display_common(self):
        print("common in two strings are: ", self.lst)

    def count(self,l):
        res=[]
        for pair in l:
            Sum = 0
            for j in range(len(pair)):
                Sum = Sum + int(pair[j])
            if Sum not in res:
                res.append(Sum)
        print("count of total number of pairs which has sum which is not equal to other pairs:",len(set(res)))


s2 = input("enter string2: ")
pair = PairsPossible(s2)
s1 = pair.str1
print("length of string:", pair.length())
print("string to list: ", pair.listOfCharacters())
pairlist = pair.pairsList()
pair.displayPairs()
ob = EqualSumPairs(s1,s2)
ob.display_common()
ob.count(pairlist)
