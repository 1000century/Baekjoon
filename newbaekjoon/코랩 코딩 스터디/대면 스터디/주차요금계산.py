# (세현)

def solution(fees, records):
	answer = []
	parkinglot = {}
	fare ={}
	li = []
	for record in records:
		time, num, inout = record.split()
		if fare.get(num) == None:
			parkinglot[num] = time
			fare[num] = 0
			li.append(num)
		else:
			if parkinglot.get(num) != None:
				intime = parkinglot[num]
				fare[num] = fare[num] + int(time[0:2])*60 + int(time[3:]) - int(intime[0:2])*60-int(intime[3:])
				del parkinglot[num]
			else:
				parkinglot[num] = time
	for car in parkinglot:
		intime = parkinglot[car]
		time = "23:59"
		fare[car] = fare[car] + int(time[0:2])*60 + int(time[3:]) - int(intime[0:2])*60-int(intime[3:])
	li.sort()
	for car in li:
		if fare[car] <=fees[0]:
			answer.append(fees[1])
		else:
			moretime = fare[car]-fees[0]
			if moretime % fees[2] ==0:
				more = fees[-1]*(moretime//fees[2])
			else:
				more = fees[-1]*((moretime//fees[2])+1)
			answer.append(fees[1] + more)

	return answer
fees = [180, 5000, 10, 600]	
records =["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]	
print(solution(fees,records))