"""
3/6 18:45~
3/8 18:45~19:45 얘도 시간초과
3/8 19:45~20:30
아이디어: L을 sort하고 크기가 작은 순으로 0 -1 1 2 -2 3 -3 으로 넣으면 됨
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
    count = 1
    minus = 1
    before = 0
    easiest = []
    easiest.append(L[0])

    for i in L:
        next = before + ((-1)**minus)*count
        easiest.insert(next,i)
        count = count + 1
        minus = minus + 1
        before = next

    # 이 부분을 위랑 합칠 수도 있을 거 같긴한데..
    diff = 0
    for i in range(len(easiest)-1):
        diff = max(diff,max(easiest[i]-easiest[i+1],easiest[i+1]-easiest[i]))
    print(diff)

# part 3. 실행 함수
if __name__ == "__main__":
    main()
