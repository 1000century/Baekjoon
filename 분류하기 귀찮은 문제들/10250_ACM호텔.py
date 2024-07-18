T = int(input())
for _ in range(T):
    H, W, N = map(int,input().split())
    y =  (N-1)//H +1 # 호
    if (N % H) ==0: # 층
        x = H
    else:
        x= N%H


    print(100*x+y)