N,M = map(int,input().split())
result = []
for _ in range(N):
    result.append(_+1)
# 도현이는 바구니를 총 N개 가지고 있고
# 각각의 바구니에는 1번부터 N번까지 번호가 매겨져 있다
# 도현이는 앞으로 M번 공을 바꾸려고 한다. 도현이는 공을 바꿀 바구니 2개를 선택하고,
# 두 바구니에 들어있는 공을 서로 교환한다.
import sys
for _ in range(M):
    i, j = map(int,sys.stdin.readline().split())
    first = result[i-1]
    second = result[j-1]
    result[i-1] = second
    result[j-1] = first

for i in result:
    print(i, end=" ")

