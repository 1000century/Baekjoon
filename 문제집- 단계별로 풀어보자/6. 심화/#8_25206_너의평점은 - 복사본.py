## 시간 44ms (딕션어리 써서 4ms만큼 빨라짐)

N = 20
total_score = 0
total_weight = 0
scoreboard = {'A+': 4.5, 'A0': 4.0, 'B+': 3.5, 'B0': 3.0, 'C+': 2.5, 'C0': 2.0, 'D+': 1.5, 'D0': 1.0, 'P': 0, 'F': 0}
weightboard = {'A+': 1, 'A0': 1, 'B+': 1, 'B0': 1, 'C+': 1, 'C0': 1, 'D+': 1, 'D0': 1, 'P': 0, 'F': 1}
for _ in range(20):
    s = input().split(" ")
    # 점수 * 과목당 학점
    total_score = total_score + scoreboard.get(s[2]) * weightboard.get(s[2]) * float(s[1])
    # 유효학점 = P면 0 나머지는 1 * 과목당학점
    total_weight = total_weight + weightboard.get(s[2]) * float(s[1])
result = total_score / total_weight
print(result)