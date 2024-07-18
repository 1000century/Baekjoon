# (세현)
# 쉬워보이는데 뭔가 오래 걸린 문제
# lt(1~a-1까지) + max(a,b) +rt(b-1 ~ 1까지) 이렇게 구성해두고
# 추가해야 하는 건물 개수만큼 lt의 0번인덱스 다음에 1 삽입

N,a,b = map(int,input().split())
if a+b-1>N:
	print(-1)
	exit()

lt = [i for i in range(1,a)] + [max(a,b)]
mid = [1]*(N-a-b+1)
rt = [i for i in range(b-1,0,-1)]

print(lt[0],*mid,*lt[1:],*rt)