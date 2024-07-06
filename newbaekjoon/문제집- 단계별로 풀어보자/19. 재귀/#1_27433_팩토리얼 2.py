# 재귀함수로 푼 것

N = int(input())
def fact(x):
    if x == 0:
        return 1
    return x * fact(x-1)
print(fact(N))