# HackerRank
#  - Algorithms > Implementation > Birthday Chocolate
#  15/12/17

n = int(input())
numbers_on_squares = list(map(int, input().strip().split(" ")))
(d, m) = map(int, input().strip().split(" "))

def check(index):
    ind =index
    i = 1
    amount = 0
    while i <= m:
        if ind <len(numbers_on_squares):
            amount += numbers_on_squares[ind]
            ind += 1
            i += 1
        else:
            break

    if amount == d:
        return 1
    else:
        return 0

total = 0
i=0
while i<len(numbers_on_squares):
    total += check(i)
    i += 1
print(total)