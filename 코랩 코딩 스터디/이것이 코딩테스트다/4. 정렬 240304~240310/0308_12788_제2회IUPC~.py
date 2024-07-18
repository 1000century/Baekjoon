
"""
3/8 12:45~10:57
"""
# part 1. 데이터 입력받기
def main():
    N = int(input()) # N은 CTP 회원 수
    M,K = map(int,input().split()) # M은 팀의수, K는 팀원의 수
    pen = list(map(int,input().split()))
    pen.sort(reverse=True)
    print(jungeun(pen,M,K))

# part 2
def jungeun(pen,M,K):
    num = M * K
    saram = 0
    while num>0 :
        if saram == len(pen):
            saram = "STRESS"
            return saram
        else:
            num = num - pen[saram]
            saram = saram + 1
    return saram

# part 3. 실행 함수
if __name__ == "__main__":
    main()
