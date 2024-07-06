# (세현)

N,S = map(int,input().split())
arr = list(map(int,input().split()))

s,e = 0,0
now = arr[0] # 한 개의 숫자로 S보다 커지는 가능성 염두에 두기.
ans = 1000000000

while True:
  # 정답 갱신
	if now >=S:
		ans = min(ans,e-s+1)

	# 범위 조정
	if now > S:
		now = now - arr[s]
		s = s + 1
	else:
		if e == N-1:
			break
		if now == S:
			now = now - arr[s]
			s,e = s+1,e+1
			now = now + arr[e]
		else:
			e = e + 1
			now = now + arr[e]

if ans == 1000000000:
	print(0)
else:
	print(ans)