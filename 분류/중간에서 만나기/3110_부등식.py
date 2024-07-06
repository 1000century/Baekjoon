from itertools import product
from bisect import bisect_left
B,C,D = map(int,input().split())
a1,a2 = map(int,input().split())
e1,e2 = map(int,input().split())

arr_b = [i for i in range(int((B*a2)/a1),1001)]
arr_c = [i for i in range(int((B*a2)/a1),1001)]

b1 = [(b,c) for b,c in product(arr_b,arr_c) if (b/B)<(c/C)]
b1.sort()


