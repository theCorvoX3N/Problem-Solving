# HackerRank
#  - Algorithms > Implementation > Migratory Birds
# 17/12/17
# same logic , less code

input()
count = [0]*6
for each in map(int, input().strip().split(" ")):
    count[each] +=1
print(count.index(max(count)))