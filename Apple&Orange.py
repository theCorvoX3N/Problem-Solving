(s, t) = map(int, input().strip().split(" "))
(a, b) = map(int, input().strip().split(" "))
(m, n) = map(int, input().strip().split(" "))
distance_apple = list(map(int, input().strip().split(" ")))
distance_orange = list(map(int, input().strip().split(" ")))

def check_apple(x):
    return ((x+a>=s)and (x+a<=t))

def check_orange(x):
    return ((x+b>=s)and (x+b<=t))
apples = sum(map(check_apple, distance_apple))
print(apples)
oranges = sum(map(check_orange, distance_orange))
print(oranges)