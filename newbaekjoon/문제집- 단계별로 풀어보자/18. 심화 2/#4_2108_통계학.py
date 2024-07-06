import math
import sys
N = int(sys.stdin.readline().strip())
A = []
dict = {}
for _ in range(N):
    new = int(sys.stdin.readline().strip())
    A.append(new)
    if new in dict:
        dict[new] += 1
    else:
        dict[new] = 1
A = sorted(A)
sum = 0
for i in A:
    sum = sum + i
print(round(sum/N))

middle = A[(N-1)//2]
print(middle)
max_value = max(dict.values())
max_keys = [key for key, value in dict.items() if value == max_value]  # 가장 작은 값과 일치하는 모든 키 찾기
max_keys = sorted(max_keys)
if len(max_keys) == 1:
    freq = max_keys[0]
else:
    freq = max_keys[1]
print(freq)

range = A[-1] - A[0]

print(range)
