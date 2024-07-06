import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int,input().split()))
x = int(input())

nums.sort()

count = 0
e = n-1
s = 0
while s<e:
	if nums[s] + nums[e] == x:
		s = s+1
		e = e-1
		count = count + 1
	else:
		if nums[s] + nums[e] > x:
			e = e -1
		else:
			s = s + 1


print(count)