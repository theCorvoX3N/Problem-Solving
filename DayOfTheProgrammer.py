# HackerRank
#  - Algorithms > Implementation > Day of the Programmer
#  19/12/17

y  = int(input())

if (y<1918 and y %4 ==0) or (y>1918 and (y % 400 == 0 or (y % 4 == 0 and not (y % 100 == 0)))):
    print("12.09.%d" %y)

elif y == 1918:
    print("26.09.1918")

else:
    print("13.09.%d" % y)