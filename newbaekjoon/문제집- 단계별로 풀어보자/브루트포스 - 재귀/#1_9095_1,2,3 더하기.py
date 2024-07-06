"""돌 여러 개 사이에 막대 넣기"""

def group(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    else:
        result = 0
        result = group(n-1) + group(n-2) + group(n-3)
        return result

import sys
N = int(sys.stdin.readline().strip())
for _ in range(N):
    A = int(sys.stdin.readline().strip())
    ans = group(A)
    print(ans)