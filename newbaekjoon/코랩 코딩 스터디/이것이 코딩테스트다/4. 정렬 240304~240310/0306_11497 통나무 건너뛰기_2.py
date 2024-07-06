
"""
3/6 18:45~
3/8 18:45~19:45
얘도 시간초과
"""
import copy
# part 1. 데이터 입력받기, 기본 함수 설정
def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        L = list(map(int,input().split()))
        log(L,N)

def level(a,b):
    return max(a,b)-min(a,b)

# part 2
def log(L,N):
    L.sort()
    easiest = []
    easiest.append(L[0])
    easiest.append(L[0])
    L.pop(0)
    for i in L:
        M = 99999999999999
        where_to_insert = 1
        for j in range(1,len(easiest)):
            i_before_after = max(level(easiest[j],i), level(easiest[j-1],i))
            if i_before_after < M:
                M = i_before_after
                where_to_insert = j
        easiest.insert(where_to_insert,i)
    print(M) #### 마지막 꺼에는 모든 것이 다 들어있으니까 얘를 추출하면 됨 따로 변수 설정안해도 됨




# part 3. 실행 함수
if __name__ == "__main__":
    main()
