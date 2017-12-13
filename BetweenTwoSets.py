# HackerRank
#  - Algorithms > Implementation > Between Two Sets
# 13/12/17

(n ,m) = map(int, input().strip().split(" "))
a = list(map(int, input().strip().split(" ")))
b = list(map(int, input().strip().split(" ")))

x = max(a)
i = 0
count = 0

while x <= min(b):
    if sum(list(map(lambda y : x%y==0, a))) == len(a) and sum(list(map(lambda y: y%x ==0, b))) == len(b):
        count += 1
    else:
        pass
    x += 1
print(count)