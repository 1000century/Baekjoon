# (세현)
# 인덱스 정하는 거 어려웠음.

N,K=map(int,input().split())
arr= list(map(int,input().split()))
letter  = [0]*(100001)

s,e = -1,0
ans = 1
while e<N:
	letter[arr[e]] = letter[arr[e]] +1
	if letter[arr[e]]>K:
		s = s+1
		while arr[s] != arr[e]:
			letter[arr[s]] = letter[arr[s]]-1
			s = s +1
		letter[arr[s]] = letter[arr[s]]-1
	ans = max(ans,e-s)
	e = e+1
print(ans)