N = int(input())
tower = list(map(int,input().split()))
receive = [0]
for i in range(1,len(tower)):
	tower[i]
	receiver = 0
	
	# case 1) 현재 타워가 바로 전 타워보다 더 높은 경우
	if tower[i-1]<tower[i]:
		if tower[receive[i-1]]>tower[i]:
			receiver = receive[-1]
		else:
			for k in range(receive[i-1]-1,-1,-1):
				if tower[k] >= tower[i]:
					receiver = k+1
					break
	
	# case 2) 현재 타워보다 바로 전 타워가 더 높은 경우
	else: # tower[i-1] >= tower[i]
		receiver = i-1+1

	receive.append(receiver)

print(*receive)