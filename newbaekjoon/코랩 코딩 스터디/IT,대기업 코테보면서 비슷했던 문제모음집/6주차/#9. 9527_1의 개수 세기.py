# (세현)

def calculate(n): # 2의 n-1승 까지의 1의 모든 개수
	if n == 1:
		return 1
	return (n-1) * (2**(n-2)) + 1

def binary(n):
	num = ''
	while n != 0:
		if n%2 != 0:
			num = str(1) + num
		else:
			num = str(0) + num
		n = n//2
	return num

def solution(n,ans=0,count=0,rest=0):
	num = binary(n)
	for idx in range(len(num)-1,-1,-1):
		count = count + 1
		if num[idx] == "1":
			ans = ans + calculate(count)
			if idx != 0:
				ans = ans + rest
				rest = rest + 2**(count-1)
	ans = ans + rest
	
	return ans

a,b = map(int,input().split())
print(solution(b)-solution(a-1))