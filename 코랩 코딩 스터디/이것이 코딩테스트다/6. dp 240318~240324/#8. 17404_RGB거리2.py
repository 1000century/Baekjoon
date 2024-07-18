"""
만들 수 있는 동전 개수의 최솟값 강의 듣다가 갑자기 떠오름
어차피 시간복잡도는 N*M 정도면 할만함
따라서 R,G,B 3개의 색깔 을 각각 N번 씩 돌린 거 정도는 가능하다
"""
# (세현)
N = int(input())
X = []
for _ in range(N):
	X.append(list(map(int,input().split())))

first = X[0]
second = X[1]

# red,green,blue는 처음 0번집과 1번집의 색깔 비용을 합한 것.
# 				 >> 이후로는 2번집부터 고려하면 됨
# 2002는 초기화를 위한 최대값(비싸니까 절대 선택하지 않도록)
red = [[2002,first[0]+second[1],first[0]+second[2]]]
green = [[first[1]+second[0],2002,first[1]+second[2]]]
blue = [[first[2]+second[0],first[2]+second[1],2002]]

# 처음에 R을 선택한 경우
ans = []
for i in range(2,N):
	before = red[-1]
	now = X[i]
	Ri = min(now[0]+before[1],now[0]+before[2])
	Gi = min(now[1]+before[0],now[1]+before[2])
	Bi = min(now[2]+before[0],now[2]+before[1])
	red.append([Ri,Gi,Bi])
Rans = red[-1]
ans.append(Rans[1])
ans.append(Rans[2]) # 마지막에서 R을 선택하면 안됨

# 처음에 G을 선택한 경우
for i in range(2,N):
	before = green[-1]
	now = X[i]
	Ri = min(now[0]+before[1],now[0]+before[2])
	Gi = min(now[1]+before[0],now[1]+before[2])
	Bi = min(now[2]+before[0],now[2]+before[1])
	green.append([Ri,Gi,Bi])
Gans = green[-1]
ans.append(Gans[0])
ans.append(Gans[2]) # 마지막에서 G을 선택하면 안됨

# 처음에 B을 선택한 경우
for i in range(2,N):
	before = blue[-1]
	now = X[i]
	Ri = min(now[0]+before[1],now[0]+before[2])
	Gi = min(now[1]+before[0],now[1]+before[2])
	Bi = min(now[2]+before[0],now[2]+before[1])
	blue.append([Ri,Gi,Bi])
Bans = blue[-1]
ans.append(Bans[0])
ans.append(Bans[1])  # 마지막에서 B을 선택하면 안됨


print(min(ans))