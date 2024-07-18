# (세현)

def generate_combinations(combination, cal, nums):
	if cal["a"] ==0 and cal["s"]==0 and cal["m"] == 0 and cal["d"]==0:
		cases.append(combination)
		return
	
	for num in nums:
		if cal[num] > 0:
			cal[num] = cal[num] -1
			generate_combinations(combination + [num], cal, nums)
			cal[num] = cal[num] + 1

N = int(input())
A = list(map(int,input().split()))
X = list(map(int,input().split()))

cal = {}
type = ["a","s","m","d"]
for i in range(4):
	cal[type[i]] = X[i]

nums = list(cal.keys())
cases = []
generate_combinations([],cal,nums)

M = -1000000001
m = 1000000001
for case in cases:
	now = A[0]
	for i in range(N-1):
		if case[i] =="a":
			now = now+A[i+1]
		elif case[i] =="s":
			now = now-A[i+1]
		elif case[i] =="m":
			now = now*A[i+1]
		elif case[i] =="d":
			if now<0:
				now = -((-now)//A[i+1])
			else:
				now = now//A[i+1]
	M = max(M,now)
	m = min(m,now)
print(M)
print(m)