# 시도 1) 쿠폰집합, 시작번호별로 먹을 수 있는 접시개수 dp, 먹었는지 체크하는 리스트 다 넣음
#		  처음에 시간 1000ms 나오길래 뭐지 했는데 나중에 알고보니까 stdin 썼을 때 제일 빠름

N,d,k,c = map(int,input().split())
# N: 접시 수
# d: 초밥종류개수
# k: 연속해서 먹는 접시 수
# c: 쿠폰번호

table = []
eaten = [0]*(d+1)
dp = [0]*N
coupon_dp = set()
for i in range(N):
	x = int(input())
	table.append(x)
	if x == c:
		for j in range(i-k+1,i+1):
			j = j%N
			coupon_dp.add(j)

count = 1
for j in range(0,k):
	eaten[table[j]] = eaten[table[j]] + 1
	if eaten[table[j]] == 1:
		count = count + 1
dp[0] = count

#print("table_____", table)
#print("dp________", dp)
#print("eaten_____", eaten)

for i in range(k,N+k-1):

	before = table[(i-k)]
	new = table[i%N]
	count = dp[i-k]

	eaten[before] = eaten[before]-1
	eaten[new] = eaten[new] + 1
	if before != new:
		if eaten[before]==0:
			count = count - 1
		if eaten[new] == 1:
			count = count + 1

	
	dp[i-k+1] = count

#print(max(dp))
#print("Dp",dp)
#print("coupon_dp:::::::::::::", coupon_dp)
if not coupon_dp:
	print(max(dp))
else:
	for j in coupon_dp:
		dp[j] = dp[j]-1
	print(max(dp))



