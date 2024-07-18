import sys
N,M = map(int,sys.stdin.readline().split())
dict ={}
for _ in range(N):
	addr,pw = sys.stdin.readline().split()
	dict[addr]= pw
for _ in range(M):
	address = sys.stdin.readline().rstrip()
	print(dict[address])
