# HackerRank
#  - Algorithms > Implementation > Climbing the Leaderboard
# 01/01/18

playersOnLeaderboard = int(input())
scores = list(map(int, input().strip().split(" ")))
levelsBeated = int(input())
aliceScores = list(map(int, input().strip().split(" ")))

for each in aliceScores:
    scores.append(each)
    print(scores)
    ranks = list(set(sorted(scores, reverse=True)))
    print(ranks)
    print(ranks.index(each))
    scores.remove(each)
    print(scores)

