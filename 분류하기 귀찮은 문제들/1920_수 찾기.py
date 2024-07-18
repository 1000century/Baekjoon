import sys
N = int(sys.stdin.readline().strip())
A = list(map(int,sys.stdin.readline().strip().split()))
M = int(sys.stdin.readline().strip())

chk = list(map(int,sys.stdin.readline().strip().split()))
m_dict = {chk[i] : i for i in range(M)}
a_dict = {i:0 for i in A}
ans = [0] * M

for i in m_dict:
	if i in a_dict:
		ans[m_dict[i]] = 1
for i in ans:
	print(i)
