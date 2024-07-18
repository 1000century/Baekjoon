# (세현)
"""
그리디
첫번째 스위치 누르는 경우, 첫번째 스우치 누르지 않는 경우 비교
이렇게 푸는 이유는, 첫번째 스위치를 누를지 말지를 미리 결정하고 들어가면
이번 스위치를 누를지 말지를 바로 앞번의 스위치 상태만 보고 결정할 수 있기 때문
"""
N = int(input())
lights = list(map(int,input().strip().replace('',' ').split()))
target = list(map(int,input().strip().replace('',' ').split()))

change = [int(lights[i] != target[i]) for i in range(N)]

# 첫 번째 스위치 안누르는 경우
try1 = change[:]
push = 0
for i in range(1,N):
	if try1[i-1] ==1:
		push = push + 1
		try1[i-1], try1[i]= 0, 1-try1[i]
		if i != N-1:
			try1[i+1] = 1 - try1[i+1]

# 첫 번째 스위치 누르는 경우
try2 = change[:]
try2[0],try2[1] = 1-try2[0],1-try2[1]
twopush = 1
for i in range(1,N):
	if try2[i-1] == 1:
		twopush = twopush + 1
		try2[i-1],try2[i] = 0, 1-try2[i]
		if i != N-1:
			try2[i+1] = 1-try2[i+1]

push = int(1e9) if try1[-1] == 1 else push
twopush = int(1e9) if try2[-1] == 1 else twopush

ans = min(push,twopush)
if ans == int(1e9):
	print(-1)
else:
	print(ans)