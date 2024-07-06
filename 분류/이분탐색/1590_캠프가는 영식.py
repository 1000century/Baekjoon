"""
24.03.17 02:13

크거나 같은 값을 구해야 함>> upperbound
인 줄 알았는데 좀 애매하게 푼듯
"""
N,T = map(int,input().split())
S=[]
for _ in range(N):
	s,i,c = map(int,input().split())
	x = 0
	for _ in range(c):
		S.append(s+x)
		x = x + i
S.sort()

def youngsik(S,T):
	low = 0
	high = len(S)-1 # 닫힌구간
	while low <=high:
		mid = (low+high)//2
		if T<S[mid]:
			high = mid -1
		elif T>S[mid]:
			low = mid + 1
		else:
			return 0
	if low>=len(S) or T > S[low]:
		return -1
	else:
		return S[low]-T
print(youngsik(S,T))