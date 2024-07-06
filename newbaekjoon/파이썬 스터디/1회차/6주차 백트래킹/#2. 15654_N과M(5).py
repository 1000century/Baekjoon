N,M = map(int,input().split())
A =list(map(int,input().split()))
A.sort()
def back(N,M,arr,visited):
   if len(arr) == M:
      print(*arr, sep=' ')
      return 
   for i in range(1,N+1):
      if visited[i] ==0:
         arr.append(A[i-1])
         visited[i] = 1
         back(N,M,arr,visited)
         visited[i] = 0
         arr.pop()
visited =[0]*(N+1)
back(N,M,[],visited)