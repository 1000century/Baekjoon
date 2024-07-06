"""
시작시간 : 24.03.10 16.58 ~ 20:56

sys.stdout.wrtie 는 좀 에바네
"""
import sys

N = int(sys.stdin.readline())
A = set(sys.stdin.readline().split())
M = int(sys.stdin.readline())
B= list(sys.stdin.readline().split())


for x in B:
	if x in A:
		sys.stdout.write(str(1)+'\n')
	else:
		sys.stdout.write(str(0)+'\n')


"""# A = 1,2,3,4,5
for element in B:
# N = 5 라면 (2 /3) > ()
	if element >A[-1] or element < A[0]:
		print(0)
		continue
	K = A[:]
	index = N
	while True:
		if index // 2 == 0 and element in K:
			print(1)
			break
		elif index //2 == 0 and element not in K:
			print(0)
			break
			
		index = len(K) // 2
		if element == K[index]:
			print(1)
#			print("index", index, "K", K)

			break
		else:
			if element > K[index]:
				K = K[index+1:]
#				print("index", index, "K", K, 123)

			else:
				K = K[:index]
#				print("index", index, "K", K,345)
"""