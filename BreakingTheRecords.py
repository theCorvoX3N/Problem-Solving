# HackerRank
#  - Algorithms > Implementation > Breaking the Records
# 14/12/17

n = int(input())
scores = list(map(int, input().strip().split(" ")))

most = int(scores[0])
least = int(scores[0])


def check_most(score):
    global most
    if score > most:
        most = score
        return 1
    else:
        return 0


def check_least(score):
    global least
    if score < least:
        least = score
        return 1
    else:
        return 0


print(sum(list(map(check_most, scores))), end=' ')
print(sum(list(map(check_least, scores))))


