# (세현)
N = int(input())
lt = list(map(int,input().split()))
ans = []
for i in range(N,0,-1):
	ans.insert(lt[i-1],i)
print(*ans)
