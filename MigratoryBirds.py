# HackerRank
#  - Algorithms > Implementation > Migratory Birds
# 17/12/17

n = int(input())
types = list(map(int, input().strip().split(" ")))

def check(type, ID):
    id_count = 0
    for each in types:
        if each == ID:
            id_count +=1
        else:
            pass
    return id_count

def findMostCommon(listOfCounts):
    max = listOfCounts[0]
    type = 1
    for each in listOfCounts:
        if each > max:
            max = each
            type = listOfCounts.index(each)+1
        else:
            pass
    return type

common = {}

counts = list(map(check, types, range(1,6)))
mostCommon = findMostCommon(counts)
print(mostCommon)