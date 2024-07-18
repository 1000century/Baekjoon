import sys
input = sys.stdin.readline

N = int(sys.stdin.readline())
A = []
for _ in range(N):
	x,h = map(int,sys.stdin.readline().split())
	how_long = (h-1)//2
	A.append([x,how_long])
A.sort()
time = 10**100

for i in range(len(A)-1):
	distance = A[i+1][0]-A[i][0]-1
	sum_move_distance = A[i+1][1]+A[i][1]
	min_move_distance = min(A[i+1][1],A[i][1])
	if distance < sum_move_distance:
		if (distance) / 2 <= min_move_distance: #ex(20, 15 15): (21,15,15) (21,10,11)
			duration = (distance)//2
#			print("1번","duration", duration, "distance", distance)
		else:
			duration = distance-min_move_distance
#			print("2번","duration", duration, "distance", distance)
		time = min(time,duration)

if time == 10**100:
	print("forever")
else:
	print(time)