# HackerRank
#  - Algorithms > Implementation > Forming a Magic Square
# 26/12/17

import sys

s = []
for s_i in range(3):
   s.append(list(map(int, input().strip().split(" "))))

possiblePermutations = [
            [[8, 1, 6], [3, 5, 7], [4, 9, 2]],# 1
            [[6, 1, 8], [7, 5, 3], [2, 9, 4]],# 2
            [[4, 9, 2], [3, 5, 7], [8, 1, 6]],# 3
            [[2, 9, 4], [7, 5, 3], [6, 1, 8]],# 4
            [[8, 3, 4], [1, 5, 9], [6, 7, 2]],# 5
            [[4, 3, 8], [9, 5, 1], [2, 7, 6]],# 6
            [[6, 7, 2], [1, 5, 9], [8, 3, 4]],# 7
            [[2, 7, 6], [9, 5, 1], [4, 3, 8]],# 8
        ]

minCost = sys.maxsize

for possible in range(8):
    squareCost = 0
    for row in range(3):
        for col in range(3):
            squareCost += abs(s[row][col] - possiblePermutations[possible][row][col])
    minCost = min(minCost, squareCost)

print(minCost)



