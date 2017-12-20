# HackerRank
#  - Algorithms > Implementation > Bon Appétit
#  20/12/17

(n, k) = map(int, input().strip().split(" "))
costs = list(map(int, input().strip().split(" ")))
chargedMoney = int(input())

if not(sum(costs)/2 == chargedMoney):
    print("Bon Appetit")
else:
    print(int(costs[k]/2))