# HackerRank
#  - Algorithms > Implementation > Cats and a Mouse
# 25/12/17

q = int(input().strip())
result = []
for each in range(q):
    (x, y, z) = map(int, input().strip().split(' '))
    if abs(x - z) < abs(y - z):
        result.append("Cat A")
    elif abs(y - z) < abs(x - z):
        result.append("Cat B")
    else:
        result.append("Mouse C")

for message in result:
    print(message)