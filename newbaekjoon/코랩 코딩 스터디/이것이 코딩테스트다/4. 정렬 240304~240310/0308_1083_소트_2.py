"""
3/7 11:58~

아이디어
앞에서부터 (1번인덱스,2번인덱스) 두 개씩 비교하면 시간초과 나옴

0번인덱스부터 for문을 돌림
	(여기서 while문을 왜 썼는지 기억이 안남)
	인덱스번호 + S번째(혹은인덱스번호+ N-1번쨰>> S가 N-1보다 큰 경우에서 반례 새김) 사이에서
	최대값을 맨 앞으로 옮기고, S에서 옮겨진 번호만큼 빼줌

	최대값 옮기기 전에 확인해야 하는 것이 해당 인덱스번호가 최대값인지를 확인하고 맞으면 while문을 깨버림

"""
import time
N = int(input())
X = list(map(int,input().split()))
S = int(input())

for i in range(len(X)): # len(X)대신 N써도 되는데 N변형 할거여서 헷갈릴까봐
	while min(S,N-1) > 0:
		if S>N-1: # S가 N보다 크면 indexerror 생김
			range_end_num = N-1
		else:
			range_end_num = S

		range_max = max(X[i:i+range_end_num+1]) ## 여기서 범위 설정 잘못해줘서 계속 max() arg is an empty sequence 걸림
		
		# 딱 자기 차례에서 최대라면 그냥 넘어감
		if range_max == X[i]:
			break

		S = S - (X.index(range_max)-i)
		del X[X.index(range_max)]
		X.insert(i,range_max)
	N = N - 1 # 얘 위치에 대해서 좀 생각해봐야 할듯 / 하다보니까 이거 왜 해줬는지를 까먹음

for i in X:
	print(i, end=" ")