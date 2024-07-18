import sys
from itertools import combinations

L, C = map(int,sys.stdin.readline().strip().split())
chrs = sys.stdin.readline().strip().split()
chrs = sorted(chrs)
vowel = ["a","e","i","o","u"]
count = 0
mo = []
ja = []

for i in chrs:
    if i in vowel:
        mo.append(i)
    else:
        ja.append(i)

def correct(A):
    mo_count = 1
    ja_count = 2
    for i in A:
        if i in vowel:
            mo_count = mo_count - 1
        else:
            ja_count = ja_count - 1
    if mo_count <= 0 and ja_count <= 0:
        A = sorted(A)
        return A
    else:
        return None

comb = combinations(chrs,L)
for i in comb:
    result = correct(list(i))
    if result != None:
        for _ in result:
            print(_,end="")
        print()