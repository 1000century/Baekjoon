# 풀이1. dfs(while문)를 이용한 풀이
# 파이썬의 set는 내부적으로 dictionary처럼 이루어지만 특이하게 list, deque처럼 pop이 있다.
# 하지만 set.pop()은 랜덤하게 요소를 반환하므로 좋은 풀이는 아니다.
# 그럼에도 >>>>> bfs, dfs에서 dp처럼 경로를 저장하는 게 필요하다면 array로 set을 써서 해결가능
#                이경우 alpha = "A"+"C" = AC 이런식으로 저장했는데 만약 "AA" + "BB" 이런식으로 저장해야 한다면 다른 풀이 찾아야함.

# 풀이2. dfs를 재귀로 구현 + 방문체크를 했다가 방문체크를 취소하기.

import sys
input = sys.stdin.readline

R,C = map(int,input().split())
X = [list(input()) for _ in range(R)]

def dfs(r,c,cnt,ans = 0):
	ans = max(ans,cnt+1)
	alphabet[X[r][c]] = 1
	for nr,nc in [(r+1,c),(r-1,c),(r,c+1),(r,c-1)]:
		if (0<=nr<R and 0<=nc<C) and (alphabet[X[nr][nc]]==0):
			ans = max(ans,dfs(nr,nc,cnt+1))
	alphabet[X[r][c]] = 0 # 들어갔다가 나올 떄 방문안 한걸로 바꿈.
	return ans

alphabet = {"A":0, "B":0, "C":0, "D":0, "E":0, "F":0, "G":0,
		 "H":0, "I":0, "J":0, "K":0, "L":0, "M":0, "N":0,
		 "O":0, "P":0, "Q":0, "R":0, "S":0, "T":0, "U":0,
		 "V":0, "W":0, "X":0, "Y":0, "Z":0,}


print(dfs(0,0,0))

