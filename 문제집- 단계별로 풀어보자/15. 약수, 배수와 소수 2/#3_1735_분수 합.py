import sys
a1, b1 = map(int,sys.stdin.readline().strip().split())
a2, b2 = map(int,sys.stdin.readline().strip().split())
## a1 분자 b1 분모
## a2 분자 b2 분모

h = a1*b2 + a2*b1   ## 일단 그냥 통분 >>  최소공배수로 만드는게 아니라 그냥 분모 곱해서
t = b1 * b2         ## 5/6 + 5/8 이라면
                    ## 분모인(t)에는 6 * 8
                    ## 분자인 (h)에는 5*8 + 6*8
                    ## 얘를 약분해줘야 함..


B = [h,t]           ## B 집합은 약분해주기 전의 분자 분모인데

while True:         ## 유클리드 호제법 일단 가능한한 계속 쓸거임
    m = min(B)
    M = max(B)
    if m == 0:              ## 종료조건은 유클리드 호제법쓷보면 나머지가 0이 될때
        print(h // M, t//M) ## 그때의 나눈 수가 최대공약수가 된다고 함. 그래서 그걸로 약분해줌
        break
    else:
        B = [m, M%m]