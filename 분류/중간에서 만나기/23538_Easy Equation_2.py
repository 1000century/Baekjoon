# 방법1
# 브루트포스 5,4,3 까지만 브루트포스하고 그다음엔 squar root로 계산
# >> 이건 pypy로만 통과됨

# 방법2
# meet in the middle >> 얘는 pypy python 모두 가능
# MITM으로 풀었지만 메모리초과 나왔던 문제 >> (제곱과 다섯제곱), (세제곱과 네제곱)으로 짝짓기!

from itertools import product
from bisect import bisect_left

def main():
    n = int(input())
    a = [[] for _ in range(4)]
    for i in range(4):
        k = 1
        while True:
            c = k ** (i + 2)
            if c > n:
                break
            a[i].append(c)
            k += 1
    
    b1 = [x + y for x, y in product(a[0], a[3]) if x + y <= 1e9]
    b2 = [x + y for x, y in product(a[1], a[2]) if x + y <= 1e9]
    
    b1.sort()
    b2.sort()

    ans = sum(bisect_left(b1, n - x) for x in b2)    
    print(ans)

if __name__ == "__main__":
    main()
