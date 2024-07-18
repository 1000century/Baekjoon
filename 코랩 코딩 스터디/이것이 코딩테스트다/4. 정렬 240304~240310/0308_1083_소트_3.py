N = int(input())
X = list(map(int, input().split()))
S = int(input())

for i in range(N):
    max_range = min(i+S, N-1) # 제일 끝 수 찾고
    M_index = i + X[i:max_range+1].index(max(X[i:max_range+1]))
    
    if M_index == i:
        continue
    
    for j in range(M_index, i, -1): # 뒤에서부터 오면서 자리 바꿈
        X[j], X[j-1] = X[j-1], X[j]
    
    S = S - (M_index - i) # 움직인 칸수만큼 빼고나서
    
    if S <= 0:
        break

for i in X:
    print(i, end = " ")