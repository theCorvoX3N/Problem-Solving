# HackerRank
#  - Algorithms > Implementation > The Hurdle Race
#  28/01/18

n, k = map(int, input().strip().split(" "))
heights = list(map(int, input().strip().split(" ")))

if k > max(heights):
    print(0)
else:
    print(max(heights) - k)