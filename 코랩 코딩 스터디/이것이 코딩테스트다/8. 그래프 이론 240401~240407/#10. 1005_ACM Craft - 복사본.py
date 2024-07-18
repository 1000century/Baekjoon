import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

def test(i):
	if temp[i] == 1:
		return D[i]
	
	else:
		timex = []
		for x in stack[i]:
			D[x] = test(x)
			temp[x] = 1
			timex.append(D[x])
		return max(timex) + D[i]

T = int(sys.stdin.readline())

for _ in range(T):
	N, K = map(int, input().split())
	D = [0] + list(map(int, input().split()))
	W = int(input())

	temp = [1] * (N + 1)
	stack = [[] for _ in range(N+1)]

	for i in range(K):
		X, Y = map(int, input().split())
		temp[Y] = 0
		stack[Y] = stack[Y] + [X]
	print(test(W))
