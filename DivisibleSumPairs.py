# HackerRank
#  - Algorithms > Implementation > Divisible Sum Pairs
# 16/12/17

(n, k) = map(int, input().strip().split(" "))
array = list(map(int, input().strip().split(" ")))

def check(i,j):
    if (array[i] + array[j]) % k == 0:
        return 1
    else:
        return 0

total = 0
for i in range(n):
    j= i+1
    while j<n:
        total += check(i, j)
        j += 1

print(total)