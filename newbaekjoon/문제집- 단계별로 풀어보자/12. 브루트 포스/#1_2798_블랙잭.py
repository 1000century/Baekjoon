N , M = map(int,input().split())
A  = list(map(int,input().split()))
problem_data = []

for _ in range(0,N-2):
    for i in range(_+1,N-1):
        for j in range(i+1,N):
            count = A[_] + A[i] + A[j]
            key = str(A[_]) + ' ' + str(A[i]) + ' ' + str(A[j])
            if count > M:
                distance = 100*M
            else:
                distance = M - count
            case = {"세수":key, "합":count,"거리":distance}
            problem_data.append(case)

min_prob = min(problem_data, key = lambda x: x["거리"])
print(min_prob["합"])

