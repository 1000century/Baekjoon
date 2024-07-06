
def solution(cap, n, deliveries, pickups):
	deliveries = [0] + deliveries
	pickups = [0] + pickups
	if deliveries[-1]:
		i = n
	else:
		i= n-1
	if pickups[-1]:
		pi = n
	else:
		pi = n-1

	distance = 0
	while True:
		if sum(deliveries) == 0:
			distance = distance + pi
		else:

			distance = distance + i
			get = 0
			while sum(deliveries)!=0:
				if get + deliveries[i] >cap:
					deliveries[i] = deliveries[i]-(cap-get)
					break
				else:
					get, deliveries[i] = get+deliveries[i],0
					i = i -1
					distance = distance + 1
			
		if sum(pickups) == 0:
			distance = distance + i
		else:
			take = 0
			while sum(pickups) !=0:
				if take + pickups[pi] > cap:
					pickups[pi] = pickups[pi] - (cap-get)
					break
				else:
					take,pickups[pi] = take+pickups[pi],0
					if pi <= i and sum(deliveries)!=0:
						distance = distance + 1
					pi = pi -1
			distance = distance + pi
			

		print("<<<< 중간점검>>>>")
		print(deliveries,"배달", sum(deliveries))
		print(pickups, "수거",sum(pickups))
		print(distance, "거리")

		if sum(pickups)+sum(deliveries) == 0:
			break
	

	answer = distance

	return answer

print("testcase-------------------")
cap = 4
n = 5
deliveries = [1, 0, 3, 1, 2]	
pickups = [0, 3, 0, 4, 0]	
print(solution(cap,n,deliveries,pickups))

print("testcase-------------------")
caps = 2
n = 7
deliveries =[1, 0, 2, 0, 1, 0, 2]	
pickups = [0, 2, 0, 1, 0, 2, 0]	
print(solution(caps,n,deliveries,pickups))

print("testcase-------------------")
cap = 15
n = 5
deliveries = [1, 2,3,4,5]	
pickups = [1,2,3,4,5]	
print(solution(cap,n,deliveries,pickups))