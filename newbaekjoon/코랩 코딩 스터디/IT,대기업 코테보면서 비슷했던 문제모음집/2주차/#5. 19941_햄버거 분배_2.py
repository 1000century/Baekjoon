import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

# 1) 백트래킹으로 푸니까 시간초과
# 2) dfs로 해도 시간초과
N,K = map(int,input().split())
X = list(input().rstrip())
guys = []
ham = []
for i in range(len(X)):
	if X[i] =="P":
		guys.append(int(i))
		X[i] = 0
	else:
		ham.append(int(i))
		X[i] = 1

dp =[0]*len(X)
ham_dic = {}
new_ham = []
for i in ham:
	guyslist = []
	for j in guys:
		if abs(i-j)>K:
			continue
		guyslist.append(j)
	if guyslist:
		ham_dic[i] = guyslist
		new_ham.append(i)


visited = set()
ans = 0
def dfs(ham_index=0,count=0):
	global ans
	if ham_index == len(new_ham):
		return
	hamburger = new_ham[ham_index]
	for i in ham_dic[hamburger]:
		if i not in visited:
			visited.add(i)
			ans = max(ans,count + 1)
			dfs(ham_index+1,count+1)
			visited.remove(i)
		else:
			dfs(ham_index+1,count)
			ans = max(ans,count)
dfs()
print(ans)