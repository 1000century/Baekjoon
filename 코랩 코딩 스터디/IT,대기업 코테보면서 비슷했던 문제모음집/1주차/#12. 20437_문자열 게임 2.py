# (세현)

def wordgame2(word,k):
	dp = {chr(i): [] for i in range(ord('a'), ord('z')+1)}
	ans = [-1]

	for i in range(len(word)):
		c = word[i]
		dp[c] = dp[c]+[i]

		if len(dp[c]) >=k:
			cnt = dp[c][-1]-dp[c][-k]+1
			if len(ans)== 1:
				ans = [cnt,cnt]
			else:
				ans = [min(ans[0],cnt),max(ans[-1],cnt)]

	print(*ans, sep=' ')


T = int(input())

for _ in range(T):
	word = input()
	k = int(input())
	wordgame2(word,k)
