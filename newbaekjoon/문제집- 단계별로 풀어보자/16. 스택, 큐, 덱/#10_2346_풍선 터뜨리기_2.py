import sys
from collections import deque
que = deque([])
N = int(sys.stdin.readline())
elements = sys.stdin.readline().split()
for i in range(len(elements)):

    que.append([i+1,int(elements[i])])

steps = que[0][1] ## 몇 칸 갈까요? 풍선안의 수
numb = que[0][0]  ## 원래 몇번째 숫자였을까? 풍선번호
que.popleft()
print(numb,end ="")
if N==1:
    exit()
for _ in range(N-1):
    if steps > 0:
        for kk in range(0,steps-1):
            a =que[0]
            que.popleft()
            que.append(a)
        steps = que[0][1]
        numb = que[0][0]
        que.popleft()
        print("",numb,end="")
    elif steps < 0:
        for kk in range(steps,-1):
            a =que[-1]
            que.pop()
            que.appendleft(a)
        steps = que[-1][1]
        numb = que[-1][0]
        que.pop()
        print("",numb,end="")


