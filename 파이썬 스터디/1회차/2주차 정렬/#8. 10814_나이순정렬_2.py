"""
sort()에서 key를 지정해주면 key가 동일할 때 남은 거끼리 sort를 자동으로 해주는 게 아니라
들어온 순서대로 저장된다.
"""


N = int(input())

attendance = []
for _ in range(N):
	y, n = input().split()
	y = int(y)
	attendance.append([y,n])

attendance.sort(key=lambda x:x[0])
for i in attendance:
	print(i[0],i[1])