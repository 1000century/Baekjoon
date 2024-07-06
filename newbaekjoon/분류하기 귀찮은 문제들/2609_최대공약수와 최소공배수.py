import sys
A,B = map(int,sys.stdin.readline().strip().split())
m = min(A,B)
for i in range(1,m+1):
    if A % (m+1-i) == 0 and B % (m+1-i) ==0:
        G = m+1-i
        print(G)
        break
print(A*B//G)

