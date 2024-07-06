N = 20
total_score = 0
total_weight = 0
scoreboard = {'A+': 4.5, 'A0': 4.0, 'B+': 3.5, 'B0': 3.0, 'C+': 2.5, 'C0': 2.0, 'D+': 1.5, 'D0': 1.0, 'P': 99, 'F': 0}
for _ in range(20):
    s = input().split(" ")
    if s[2] != "P":
        weight = float(s[1])
        score = scoreboard.get(s[2])
        total_score = total_score + weight*score
        total_weight = total_weight + weight
    if s[2] == "P":
        total_score == total_score
result = total_score / total_weight
print(result)