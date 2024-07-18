
"""
09:39~09:45
채점 시간이 너무 오래 걸리네
input >> 1844
sys.stdin >> 1808
sys.stdout >> 1368
"""
import sys
N, M = map(int,sys.stdin.readline().split())
X = []
X.extend(list(map(int,sys.stdin.readline().split())))
X.extend(list(map(int,sys.stdin.readline().split())))

X.sort()
for item in X:
    sys.stdout.write(str(item) + ' ')
sys.stdout.write('\n')