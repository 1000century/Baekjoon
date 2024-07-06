"""
#1 isalpha
#2 dict.get(a) == None:
"""

import sys

rl = sys.stdin.readline

N,M = map(int,rl().split())

poke1 = {}
poke2 = {}

for i in range(1,N+1):
	a = rl().rstrip()
	i = str(i)
	poke1[i] = a
	poke2[a] = i
for _ in range(M):
	quiz  = rl().rstrip()

	if quiz.isalpha() != 1: 
		print(poke1[quiz])
	else:
		print(poke2[quiz])