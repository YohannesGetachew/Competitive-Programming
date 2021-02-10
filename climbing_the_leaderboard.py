def climbingLeaderboard(ranked, player):
    ranked = list(dict.fromkeys(ranked))
    ranked.sort(reverse=True)
    results = []
    for score in player:
        while len(ranked) != 0 and score >= ranked[-1]:
            ranked.pop()
        results.append(len(ranked)+1)
    return results


print(climbingLeaderboard([98, 34, 62], [20, 100, 0]))
