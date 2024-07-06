N = int(input())

a = list(map(int,input().split()))
M = max(a)
sum = 0
for i in a:
	sum = sum + i
print(sum*100/(M*N))