## 못 풀었음

import sys
N = int(sys.stdin.readline().strip())
sangdams = []
for _ in range(N):
    Ti,Pi = map(int,sys.stdin.readline().strip())
    sangdams.append([Ti,Pi])

end = 0

for sang in sangdams:
    nexten = end + sang[0]
while N >= 0:
    if T <= N:
