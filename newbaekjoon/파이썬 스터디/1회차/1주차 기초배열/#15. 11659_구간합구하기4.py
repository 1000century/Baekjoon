
"""
11:15~11:18 python3로 하면 시간초과 pypy3로 해도 시간초과
1125~1131: 누적합
"""
import sys
N, M = map(int,sys.stdin.readline().split())
X = list(map(int,sys.stdin.readline().split()))
sume = [0] * (N+1)
for i in range(1,N+1):
	sume[i] = sume[i-1] + X[i-1]

for _ in range(M):
	i,j = map(int,sys.stdin.readline().split())
	print(sume[j]-sume[i-1])