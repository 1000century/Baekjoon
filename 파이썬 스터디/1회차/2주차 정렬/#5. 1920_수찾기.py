"""
import 안썼는데도 168ms
확실히 set 쓰는 게 in 함수 쓸 때는 빠른듯
"""


N = int(input())
A = set(list(map(int,input().split())))
## set(map(int,input().split()) >> 이렇게 해도 된대

M = int(input())
B = list(map(int,input().split()))

for i in B:
	if i in A:
		print(1)
	else:
		print(0)