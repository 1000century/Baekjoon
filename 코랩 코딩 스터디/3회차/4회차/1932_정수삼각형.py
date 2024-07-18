N = int(input())
arr = [int(input())]

for i in range(2,N+1):
	temp = list(map(int,input().split()))
	temp[0] = temp[0] + arr[0]
	temp[-1] = temp[-1] + arr[-1]
	for j in range(1,i-1):
		temp[j] = temp[j] + max(arr[j-1],arr[j])
	arr = temp[:]
print(max(arr))
