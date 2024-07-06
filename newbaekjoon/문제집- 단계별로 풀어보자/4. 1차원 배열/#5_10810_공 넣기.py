# 23.10.03 01:38 ~ 12:26

a = list(map(int,input().split(" ")))
result = []
for _ in range(a[0]):
    result.append(0)
    
import sys

for _ in range(a[1]):
    cmd = sys.stdin.readline().strip().split(" ")
    cmd = [int(x) for x in cmd]
    ccc = [(p,cmd[2]) for p in range(cmd[0],cmd[1]+1)]
    
    ### ccc = [(3,2),(4,2),(5,2)]
    for p in ccc:
        pax = p[0]-1
        qax = p[1]
        result[pax] = qax
for v in result:
    print(v, end=" ")
        


 
   
    