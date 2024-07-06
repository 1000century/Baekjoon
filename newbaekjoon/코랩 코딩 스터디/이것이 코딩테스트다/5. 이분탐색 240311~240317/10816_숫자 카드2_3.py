# (세현)
"""
시간초과 계속 나오는 문제
24.03.15 10:48~16:41
python3에서는 25%에서 시간초과
pypy3 에서는 63%에서 시간초과

N과 M이 모두 최대 500,000이므로 NM은 25*10**10입니다.
주어진 시간 제한 안에 할 수 있는 연산>>> 10**8번

이분탐색 개념으로 풀거면 그냥 이분탐색이 아닌 
upperbound lowerbound를 이용해서 풀어야 함 >> 3024ms
반례)
1
1
2
1 1

마지막에 계속 틀렸던 이유: low를 return 해야하는데 middle을 return 했음!
"""
import sys
input = sys.stdin.readline
N = int(input())
collect = list(map(int,input().split()))
collect.sort()
# print(collect)

M = int(input())
isit = list(map(int,input().split()))

# LowerBound >> 여러개라면 가장 작은 값을 갖는 인덱스
# 같을 때 low는 고정하고 high값만 줄임

def lower_bound(array, target):
    low, high = 0, len(array)  ### >> 반열린구간으로 정의
    while low < high:				# >>닫힌구간으로 바꿀거면 while 부등호 를 등호포함
        mid = (low + high) // 2
        if array[mid] < target:
            low = mid + 1
        else:
            high = mid				# >> 닫힌구간으로 바꿀거면 high = mid -1
    return low

def upper_bound(array, target):
    low, high = 0, len(array)  ### >> 반열린구간으로 정의
    while low < high:
        mid = (low + high) // 2
        if array[mid] <= target:
            low = mid + 1
        else:
            high = mid
    return low

for target in isit:
    begin = lower_bound(collect, target)
    end = upper_bound(collect, target)
    print(end - begin, end=" ")
