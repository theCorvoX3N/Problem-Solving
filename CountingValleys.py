# HackerRank
#  - Algorithms > Implementation > Counting Valleys
# 23/12/17

n = int(input())
steps = input()
levels = [0]*n
i=0

for step in steps:
    if step == 'U':
        if i == 0:
            levels[i] = 1
            i += 1
        else:
            levels[i] = levels[i-1]+1
            i += 1
    else:
        if i == 0:
            levels[i] = -1
            i += 1
        else:
            levels[i] = levels[i-1]-1
            i+=1

valley = 'none'
countValleys = 0
for level in levels:
    if level == -1 and ( valley == 'none' or valley == 'end' ):
        valley = 'start'
    elif valley == 'start' and level == 0:
        valley = 'end'
        countValleys += 1
    else:
        pass

print(countValleys)