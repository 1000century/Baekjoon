import sys
sys.setrecursionlimit(1000000)
N = int(input())
rt = {}
lt = {}
parent = {}
for _ in range(N):
	n,l,r = input().split()
	parent[l] = n
	parent[r] = n

	rt[n] = r
	lt[n] = l
x = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
for i in range(N):
	if x[i] not in parent:
		root = x[i]
		break
app = []
def front(x):
	app.append(x)
	if lt[x] != '.':
		front(lt[x])
	if rt[x] != '.':
		front(rt[x])

front(root)
print(*app,sep='')


bbb = []
def bb(x):
	if lt[x] != '.':
		bb(lt[x])
	bbb.append(x)
	if rt[x] != '.':
		bb(rt[x])
bb(root)
print(*bbb,sep='')


midd = []
def mid(x):
	if lt[x] != '.':
		mid(lt[x])
	if rt[x] != '.':
		mid(rt[x])
	midd.append(x)
mid(root)
print(*midd,sep='')
