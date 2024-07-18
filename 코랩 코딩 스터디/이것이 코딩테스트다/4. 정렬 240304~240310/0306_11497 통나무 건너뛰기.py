
"""
3/6 18:45~
"""
import copy
# part 1. 데이터 입력받기
def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        L = list(map(int,input().split()))
        L.sort()
        log(L,N)

# part 2
def log(L,N):
    print(L)
    logjump = []
    logjump.append(L[0])
    logjump.append(L[-1])
    temporary = copy.deepcopy(logjump)
    for i in range(1,N-1): # 인덱스 0부터 N-1까지 중에서 이미 인덱스 0과 끝은 썼으니 1~N-2까지
        diff_i=99999999999999999
        for j in range(1,len(logjump)+1):
            logjump.insert(j,L[i]) # j자리에 L[i] 삽입
            diff_j = max(logjump[-1],logjump[0]) - min(logjump[-1],logjump[0])
            for k in range(1,len(logjump)): # 각 원소간 차이 계산
                d = max(logjump[k],logjump[k-1])-min(logjump[k],logjump[k-1]) # 앞 뒤 차이
                if d >= diff_j:
                    diff_j = d
                    temporary = copy.deepcopy(logjump)
                    print(diff_j,temporary)
            del logjump[j]
        if diff_j < diff_i:
            diff_i = diff_j
            logjump = copy.deepcopy(temporary)
        print(logjump)
    print("최종",logjump)



# part 3. 실행 함수
if __name__ == "__main__":
    main()
