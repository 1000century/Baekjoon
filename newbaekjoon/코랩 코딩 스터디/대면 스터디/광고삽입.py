def inttotime(time):
	x=str(time//3600)
	y=str((time%3600)//60)
	z=str(time%60)
	while len(x) < 2:
		x='0'+x
	while len(y) < 2:
		y='0'+y
	while len(z) < 2:
		z='0'+z
	return f"{x}:{y}:{z}"
	

def timetoint(play_time):
	return 3600 * int(play_time[0:2]) + 60 * int(play_time[3:5]) + int(play_time[6:8])

def solution(play_time, adv_time, logs):
	if play_time == adv_time:
		return "00:00:00"
	play_time=timetoint(play_time)
	adv_time=timetoint(adv_time)

	arr=[0]*(play_time+1)
	for i in logs:
		a,b=i.split('-')
		a,b=timetoint(a),timetoint(b)
		arr[a]=arr[a]+1
		arr[b]=arr[b]-1
	for i in range(1,len(arr)):
		arr[i]=arr[i]+arr[i-1]

	pre_sum=[0]
	total=0
	for i in range(len(arr)):
		total=total+arr[i]
		pre_sum.append(total)

	max_time=0
	answer=0
	for i in range(len(arr)+1):
		if i+1+adv_time >= len(pre_sum):
			break
		ins=pre_sum[i+adv_time]-pre_sum[i]
		if ins >max_time:
			max_time=ins
			answer=i

	return inttotime(answer)

print(solution("02:03:55","00:14:15",["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"]))