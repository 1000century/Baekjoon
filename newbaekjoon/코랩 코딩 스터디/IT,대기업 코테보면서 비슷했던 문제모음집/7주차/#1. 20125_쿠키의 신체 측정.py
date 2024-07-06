# (세현)

import sys
input = sys.stdin.readline
N = int(input())
cookie = [input() for _ in range(N)]

# 심장
for i in range(N):
	if '*' in cookie[i]:
		armheight = i+1
		heart = [i+1,cookie[i].index('*')]
		break

# 팔
ltarm =heart[1]-cookie[armheight].index('*')
rtarm = cookie[armheight].rindex('*')-heart[1]
arm = [ltarm,rtarm] 

# 척추
for i in range(heart[0],N):
	if cookie[i][heart[1]] != '*':
		legstart = i
		break
lspine = legstart - armheight-1

# 다리
leg = [-1,-1]
for i in range(N-1,legstart-1,-1):
	if cookie[i][heart[1]-1] == '*':
		leg[0] = (i-legstart)+1
		break

for i in range(N-1,legstart-1,-1):
	if cookie[i][heart[1]+1] == '*':
		leg[1] = (i-legstart)+1
		break

print(*[i+1 for i in heart])
print(*arm,lspine,*leg)