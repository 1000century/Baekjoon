# (세현)
# 투포인터 >> index 정하기 까다로움

N = int(input())
nums = list(map(int,input().split()))

s,e = 0,0
count = 0
dic = set()

while e < N:
	if nums[e] not in dic:
		dic.add(nums[e])
		count = count + len(dic)

		e = e + 1

	else:
		dic.remove(nums[s])
		s = s + 1

print(count)	
