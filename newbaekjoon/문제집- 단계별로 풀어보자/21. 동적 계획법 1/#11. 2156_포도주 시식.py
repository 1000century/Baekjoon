"""
24.03.20 01:05~

1) answer: 300
4
100
100
100
100

2) answer: 2000
5
0
1000
1000
1000
0

3) answer: 400
6
100
100
0
0
100
100

4) answer: 13
6
1
2
3
6
4
1

5) answer: 0
1
0

6) answer: 117
2
63
54

7) answer: 20
4
10
10
1
0

8) answer: 20
3
10
1
10

9) answer: 4
6
1
1
0
0
1
1
"""
N = int(input())

A = [0]
for _ in range(N):
      A.append(int(input()))

if N == 1:
      print(A[-1])
      exit()

X = [[0,0] for _ in range(N+1)]
X[1] = [A[1],A[1]]
X[2] = [A[2],+A[1]+A[2]]
for i in range(3,N+1):
      X[i][0] = max(max(X[i-2]),max(X[i-3])) + A[i] # 이전 잔을 마시지 않음
      X[i][1] = X[i-1][0] + A[i] #이전 잔을 마신 경우
#print(X)

print(max(max(X[N]),max(X[N-1])))  # 마지막 잔까지 고려했을 때의 최대값