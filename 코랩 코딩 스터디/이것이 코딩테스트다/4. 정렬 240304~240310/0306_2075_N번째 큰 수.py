
"""
3/6 14:14~14:26
메모리 제한 왜 있는거지?
"""

def main():
    N =int(input())
    A = []
    for _ in range(N):
        A.extend(list(map(int,input().split())))
        A.sort(reverse=True)
        A = A[0:N]
    print(A[N-1])


if __name__ == "__main__":
    main()
