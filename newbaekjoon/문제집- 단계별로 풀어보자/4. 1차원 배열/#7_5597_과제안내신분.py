# X대학 M교수님은 프로그래밍 수업을 맡고 있다.
# 교실엔 학생이 30명이 있는데,
# 학생 명부엔 각 학생별로 1번부터 30번까지 출석번호가 붙어 있다.
#  제출 안 한 학생 2명의 출석번호를 구하는 프로그램

# 입력은 총 28줄로 각 제출자(학생)의 출석번호 n(1 ≤ n ≤ 30)가 한 줄에 하나씩 주어진다.
# 출석번호에 중복은 없다.
submitted = []
for _ in range(28):
    submitted.append(int(input()))

total = list(range(1,31))
#출력은 2줄이다.
# 1번째 줄엔 제출하지 않은 학생의 출석번호 중 가장 작은 것을 출력하고,
# 2번째 줄에선 그 다음 출석번호를 출력한다.

for i in submitted:
    if i in total:
        total.remove(i)
print(min(total),max(total),sep="\n")