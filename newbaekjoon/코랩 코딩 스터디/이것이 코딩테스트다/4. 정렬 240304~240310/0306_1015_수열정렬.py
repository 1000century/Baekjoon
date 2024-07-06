# 1차 시도 11:30~13:01
# >> 입력받는 수가 무조건 N보다 작은 줄 알았음
"""
예를 들어 N이 10이면 0부터 9까지만 입려괴는 줄 알았음
"""
# 2차 시도 13:01 ~14:00

def main():
    N =int(input())
    A = list(map(int,input().split()))
    nonnaerim(A)

def nonnaerim(A):
    B = sorted(list(set(A)))
    dicts = {}
    t = 0
    for x in range(len(B)):
        dicts[B[x]] = [t,A.count(B[x])]
        t = t + A.count(B[x])
    print(dicts)

    for element in A:
        print(dicts[element][0], end = " ")
        dicts[element] = [dicts[element][0]+1,dicts[element][1]-1]
            
if __name__ == "__main__":
    main()