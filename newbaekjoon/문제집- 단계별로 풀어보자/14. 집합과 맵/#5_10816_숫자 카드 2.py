# (세현)

import sys
N = map(int,sys.stdin.readline())
nums = list(map(int,sys.stdin.readline().split()))
dict = {}
for _ in nums:
    if dict.get(_) == None:
        dict[_] = 1
    else:
        dict[_] = dict[_] + 1

M = map(int,sys.stdin.readline())
check = list(map(int,map(int,sys.stdin.readline().split())))
for _ in check:
    if dict.get(_) == None:
        print(0, end=" ")
    else:
        print(dict[_], end=" ")