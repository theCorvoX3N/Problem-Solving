# HackerRank
#  - Algorithms > Implementation > Electronics Shop
# 24/12/17

(s, n ,m) = map(int, input().strip().split(" "))
keyboardPrices = list(map(int, input().strip().split(" ")))
usbPrices =  list(map(int, input().strip().split(" ")))

total = 0

for i in range(n):
    for j in range(m):
        if total < (keyboardPrices[i] + usbPrices[j]):
            print("%d < keyboard%d + usb%d"%(total, keyboardPrices[i],usbPrices[j]))
            total = keyboardPrices[i] + usbPrices[j]
        else:
            pass

if not(total):
    print(total)
else:
    print(-1)
