def solution(cap, n, deliveries, pickups):
	deliveries = [0] + deliveries
	pickups = [0] + pickups
	

	distance = 0
	initial_delivery = n
	initial_pickups = n

	while True:
		if sum(deliveries[:initial_delivery+1]) !=0:
			get = 0
			for i in range(initial_delivery,-1,-1):
				if deliveries[i]:
					initial_delivery = i
					break
			
			while sum(deliveries[:initial_delivery+1])!=0:
				if get + deliveries[i] >cap:
					deliveries[i] = deliveries[i]-(cap-get)
					break
				else:
					get, deliveries[i] = get+deliveries[i],0
					i = i -1
		else:
			initial_delivery = 0

		if sum(pickups) != 0:
			take = 0
			for j in range(initial_pickups,-1,-1):
				if pickups[j]:
					initial_pickups = j
					break

			while sum(pickups) !=0:
				if take + pickups[j] > cap:
					pickups[j] = pickups[j] - (cap-take)
					break
				else:
					take,pickups[j] = take+pickups[j],0
					j = j -1
		else:
			initial_pickups = 0
		
		distance = distance + 2* max(initial_pickups, initial_delivery)

		initial_delivery = i
		initial_pickups = j

		if initial_delivery == 0 and initial_pickups == 0:
			break
		if sum(deliveries)+sum(pickups) == 0:
			break

	return distance

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