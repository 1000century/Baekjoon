import sys
input = sys.stdin.readline

N,M = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]

tv = []
every = 0

for n in range(N):
	for m in range(M):
		if 1<=arr[n][m] <=5:
			tv.append((n,m,arr[n][m]))
		elif arr[n][m] == 0:
			every = every + 1

def solution(every):
	cnt = 0
	def dfs(area,i):
		nonlocal cnt
		if i == len(tv):
			cnt = max(cnt,len(area))
			return 
		n,m,type = tv[i]
		if type == 1:
			for d in ['up','down','left','right']:
				newarea=  set()
				if d == 'up':
					for nn in range(n,-1,-1):
						if arr[nn][m] == 6:
							break
						if arr[nn][m] == 0:
							newarea.add((nn,m))
					areawithnewarea = area | newarea
					dfs(areawithnewarea, i+1)
				elif d == 'down':
					for nn in range(n,N):
						if arr[nn][m] == 6:
							break
						if arr[nn][m] == 0:
							newarea.add((nn,m))
					areawithnewarea = area | newarea
					dfs(areawithnewarea, i+1)
				elif d == 'right':
					for mm in range(m+1,M):
						if arr[n][mm] == 6:
							break
						if arr[n][mm] == 0:
							newarea.add((n,mm))
					areawithnewarea = area | newarea
					dfs(areawithnewarea, i+1)
				elif d == 'left':
					for mm in range(m-1,-1,-1):
						if arr[n][mm] == 6:
							break
						if arr[n][mm] == 0:
							newarea.add((n,mm))
					areawithnewarea = area | newarea
					dfs(areawithnewarea, i+1)
	
		if type == 2:
			for d in ['updown','leftright']:
				newarea=  set()
				if d == 'updown':
					for nn in range(n,-1,-1):
						if arr[nn][m] == 6:
							break
						if arr[nn][m] == 0:
							newarea.add((nn,m))
					for nn in range(n,N):
						if arr[nn][m] == 6:
							break
						if arr[nn][m] == 0:
							newarea.add((nn,m))
					areawithnewarea = area | newarea
					dfs(areawithnewarea, i+1)


				elif d == 'leftright':
					for mm in range(m+1,M):
						if arr[n][mm] == 6:
							break
						if arr[n][mm] == 0:
							newarea.add((n,mm))

					for mm in range(m-1,-1,-1):
						if arr[n][mm] == 6:
							break
						if arr[n][mm] == 0:
							newarea.add((n,mm))
					areawithnewarea = area | newarea
					dfs(areawithnewarea, i+1)
	


		if type == 3:
			for d in ['upright','rightdown','downleft','leftup']:
				newarea=  set()
				if d == 'upright':
					for nn in range(n,-1,-1):
						if arr[nn][m] == 6:
							break
						if arr[nn][m] == 0:
							newarea.add((nn,m))
					for mm in range(m+1,M):
						if arr[n][mm] == 6:
							break
						if arr[n][mm] == 0:
							newarea.add((n,mm))
					areawithnewarea = area | newarea
					dfs(areawithnewarea, i+1)
				elif d == 'rightdown':
					for mm in range(m+1,M):
						if arr[n][mm] == 6:
							break
						if arr[n][mm] == 0:
							newarea.add((n,mm))
					for nn in range(n,N):
						if arr[nn][m] == 6:
							break
						if arr[nn][m] == 0:
							newarea.add((nn,m))
					areawithnewarea = area | newarea
					dfs(areawithnewarea, i+1)
				elif d == 'downleft':
					for nn in range(n,N):
						if arr[nn][m] == 6:
							break
						if arr[nn][m] == 0:
							newarea.add((nn,m))
					for mm in range(m-1,-1,-1):
						if arr[n][mm] == 6:
							break
						if arr[n][mm] == 0:
							newarea.add((n,mm))	
					areawithnewarea = area | newarea
					dfs(areawithnewarea, i+1)
				elif d == 'leftup':
					for mm in range(m-1,-1,-1):
						if arr[n][mm] == 6:
							break
						if arr[n][mm] == 0:
							newarea.add((n,mm))
					for nn in range(n,-1,-1):
						if arr[nn][m] == 6:
							break
						if arr[nn][m] == 0:
							newarea.add((nn,m))
					areawithnewarea = area | newarea
					dfs(areawithnewarea, i+1)


		if type == 4:
			for d in ['a','b','c','d']:
				if d == 'a':
					newarea=  set()
					for nn in range(n,-1,-1):
						if arr[nn][m] == 6:
							break
						if arr[nn][m] == 0:
							newarea.add((nn,m))
					for mm in range(m+1,M):
						if arr[n][mm] == 6:
							break
						if arr[n][mm] == 0:
							newarea.add((n,mm))

					for nn in range(n,N):
						if arr[nn][m] == 6:
							break
						if arr[nn][m] == 0:
							newarea.add((nn,m))

					areawithnewarea = area | newarea
					dfs(areawithnewarea, i+1)
				if d == 'b':
					newarea=  set()
					for nn in range(n,-1,-1):
						if arr[nn][m] == 6:
							break
						if arr[nn][m] == 0:
							newarea.add((nn,m))
					for mm in range(m+1,M):
						if arr[n][mm] == 6:
							break
						if arr[n][mm] == 0:
							newarea.add((n,mm))


					for mm in range(m-1,-1,-1):
						if arr[n][mm] == 6:
							break
						if arr[n][mm] == 0:
							newarea.add((n,mm))	
					areawithnewarea = area | newarea
					dfs(areawithnewarea, i+1)
				if d == 'c':
					newarea=  set()
					for nn in range(n,-1,-1):
						if arr[nn][m] == 6:
							break
						if arr[nn][m] == 0:
							newarea.add((nn,m))

					for nn in range(n,N):
						if arr[nn][m] == 6:
							break
						if arr[nn][m] == 0:
							newarea.add((nn,m))
					for mm in range(m-1,-1,-1):
						if arr[n][mm] == 6:
							break
						if arr[n][mm] == 0:
							newarea.add((n,mm))	
					areawithnewarea = area | newarea
					dfs(areawithnewarea, i+1)

				if d == 'd':
					newarea=  set()

					for mm in range(m+1,M):
						if arr[n][mm] == 6:
							break
						if arr[n][mm] == 0:
							newarea.add((n,mm))

					for nn in range(n,N):
						if arr[nn][m] == 6:
							break
						if arr[nn][m] == 0:
							newarea.add((nn,m))
					for mm in range(m-1,-1,-1):
						if arr[n][mm] == 6:
							break
						if arr[n][mm] == 0:
							newarea.add((n,mm))	
					areawithnewarea = area | newarea
					dfs(areawithnewarea, i+1)
	
		if type == 5:
			newarea=  set()
			for nn in range(n,-1,-1):
				if arr[nn][m] == 6:
					break
				if arr[nn][m] == 0:
					newarea.add((nn,m))
			for mm in range(m+1,M):
				if arr[n][mm] == 6:
					break
				if arr[n][mm] == 0:
					newarea.add((n,mm))

			for nn in range(n,N):
				if arr[nn][m] == 6:
					break
				if arr[nn][m] == 0:
					newarea.add((nn,m))
			for mm in range(m-1,-1,-1):
				if arr[n][mm] == 6:
					break
				if arr[n][mm] == 0:
					newarea.add((n,mm))	
			areawithnewarea = area | newarea
			dfs(areawithnewarea, i+1)

	dfs(set(),0)
	print(every-cnt)

solution(every)