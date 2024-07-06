N = int(input())
A = list(map(int,input().split()))

Udp = [1]*N
Ddp = [1]*N

for i in range(0,N-1):
	if A[i] < A[i+1]:
		Udp[i+1] = Udp[i] + 1
	elif A[i] > A[i+1]:
		Ddp[i+1] = Ddp[i] + 1
	else:
		Udp[i+1] = Udp[i] + 1
		Ddp[i+1] = Ddp[i] + 1

print(max(max(Ddp),max(Udp)))