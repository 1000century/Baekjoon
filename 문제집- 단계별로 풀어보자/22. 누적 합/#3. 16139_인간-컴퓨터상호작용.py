# pypy3로만 통과
import sys
input = sys.stdin.readline

S = input()
q = int(input())
Z = {
'a': [0],'b': [0],'c': [0],'d': [0],'e': [0],'f': [0],'g': [0],'h': [0],'i': [0],'j': [0],'k': [0],'l': [0],'m': [0],'n': [0],'o': [0],'p': [0],'q': [0],'r': [0],'s': [0],'t': [0],'u': [0],'v': [0],'w': [0],'x': [0],'y': [0],'z': [0]}

for i in range(len(S)):
	s = S[i]
	for key,value in Z.items():
		prev = value[-1]
		if key == s:
			value.append(prev + 1)
		else:
			value.append(prev)

#print(Z)
for _ in range(q):
	a,l,r = input().split()
	l = int(l)
	r = int(r)
	temp = Z[a]
	print(temp[r+1]-temp[l])