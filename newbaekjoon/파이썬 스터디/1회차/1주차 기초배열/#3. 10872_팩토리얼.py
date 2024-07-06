import sys
sys.setrecursionlimit(3000)


def main():
    N = int(input())
    print(factorial(N))
    
def factorial(N):
    if N == 0:
        return 1
    else:
        return N * factorial(N-1)
    
if __name__ == "__main__":
    main()