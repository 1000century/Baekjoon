
"""
3/6 16:30~16:45
"""
# part 1. 데이터 입력받기
def main():
    W,H = map(int,input().split())
    N = int(input())
    w = [0,H]
    h = [0,W]

    for _ in range(N):
        wh,s = map(int,input().split())
        if wh == 0:
            w.append(s)
        else:
            h.append(s)

    square(w,h)

# part 2. 함수 설정
def square(w,h):
    w.sort()
    h.sort()

    w_BIG = w[0]
    h_BIG = h[0]

    for i in range(len(w)-1):
        w_BIG = max(w_BIG,w[i+1]-w[i])

    for i in range(len(h)-1):
        h_BIG = max(h_BIG,h[i+1]-h[i])

    print(h_BIG * w_BIG)


# part 3. 실행 함수
if __name__ == "__main__":
    main()
