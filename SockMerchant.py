# HackerRank
#  - Algorithms > Implementation > Sock Merchant
#  22/12/17

def calcPairs(listOfCost, listOfUnique):
    totalPairs = 0
    for each in listOfUnique:
        count = 0
        for cost in listOfCost:
            if cost == each:
                count +=1
            else:
                pass
        noOfPairs = int(count/2)
        if noOfPairs > 0:
            totalPairs += noOfPairs
        else:
            pass
    return totalPairs

input() #Reading n
costs = list(map(int, input().strip().split(" ")))
unique = list(set(costs))
pairs = calcPairs(costs, unique)
print(pairs)