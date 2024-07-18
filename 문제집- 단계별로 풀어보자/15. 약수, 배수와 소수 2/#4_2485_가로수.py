N = int(input())

first_spot = int(input())            # first spot

second_spot = int(input())          # second spot
first_distance = second_spot - first_spot

now_spot = second_spot              ## 두번째 기준
now_distance = first_distance       ## 두번째 기준


G_now = now_distance
A = [first_distance]
for _ in range(N-2):
    prev_distance = G_now   ##  한번 더 갔으니 원래 now 였던게 prev로 바뀜
    prev_spot = now_spot

    now_spot = int(input())
    now_distance = now_spot - prev_spot
    A.append(now_distance)

    ##### prev_distance랑 now_distance의 최대공약수를 구해야함
    D = [now_distance, prev_distance]
    while True:  ## 유클리드 호제법 일단 가능한한 계속 쓸거임

        m = min(D)
        M = max(D)
        if m == 0:  ## 종료조건은 유클리드 호제법쓷보면 나머지가 0이 될때
            G_now = M ## 그때의 나눈 수가 최대공약수가 된다고 함. 그래서 그걸로 약분해줌
            break
        else:
            D = [m, M % m]
count = 0
for i in A:
    count = count + i//G_now

print(count-len(A))