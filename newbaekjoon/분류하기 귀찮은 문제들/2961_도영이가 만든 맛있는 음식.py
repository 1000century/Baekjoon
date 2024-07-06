N = int(input())
food = [list(map(int,input().split())) for _ in range(N)]

ans = int(1e9)
for subset in range(1,1<<N):
	쓴 = 1
	신 = 0
	for j in range(N):
		if subset & (1<<j) != 0:
			쓴 = 쓴 *food[j][0]
			신 = 신 + food[j][1]
	ans = min(ans,abs(쓴-신))
print(ans)

"""
N = 3 일 때, subset이 의미하는 바
001: 첫 번째 재료만 사용
010: 두 번째 재료만 사용
100: 세 번째 재료만 사용
011: 첫 번째와 두 번째 재료 사용
101: 첫 번째와 세 번째 재료 사용
110: 두 번째와 세 번째 재료 사용
111: 모든 재료 사용

"""