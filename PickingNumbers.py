# HackerRank
#  - Algorithms > Implementation > Picking Numbers
# 31/12/17

n = int(input())
arrayOfNumbers = list(map(int, input().strip().split(" ")))


arrayOfNumbers.sort()  # arrange in increasing order
numbers = list(set(arrayOfNumbers))  # convert to a list of unique values

maxLength = 0
for i in range(len(numbers)):
    count = 0
    for each in arrayOfNumbers:
        if each - numbers[i] in range(2): # count the numbers with differences +1 and 0
            count +=1
        else:
            pass
    if maxLength < count:
        maxLength = count
    else:
        pass

print(maxLength)



