# HackerRank
#  - Algorithms > Implementation > Electronics Shop
# 24/12/17

(s, n ,m) = map(int, input().strip().split(" "))
keyboardPrices = list(map(int, input().strip().split(" ")))
usbPrices =  list(map(int, input().strip().split(" ")))

total = 0

for i in range(n):
    for j in range(m):
        cost = keyboardPrices[i] + usbPrices[j]
        if total < cost and cost <=s:
            total = cost
        else:
            pass

if total:
    print(total)
else:
    print(-1)
