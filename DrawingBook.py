# HackerRank
#  - Algorithms > Implementation > Drawing Book
# 22/12/17

import math

n = int(input())
p = int(input())

if p - 1 < n - p:
    print(math.ceil((p - 1) / 2))
else:
    if n - p == 1 and not (n % 2 == 0):
        print(0)
    elif n - p > 1 and p % 2 == 0:
        print(math.floor((n-p)/2))
    else:
        print(math.ceil((n - p) / 2))