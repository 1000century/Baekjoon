# (세현)

import sys
input = sys.stdin.readline

p,m = map(int,input().split())
room, member = [],[]

for _ in range(p):
	l, n = input().split()
	l = int(l)
	doweneednewroom = 1

	for idx in range(len(room)):
		lv,cnt = room[idx]
		if lv-10<=l<=lv+10 and cnt<m:
			room[idx][1] = room[idx][1] + 1
			member[idx].append([l,n])
			doweneednewroom = 0
			break
	if doweneednewroom == 1:
		room.append([l,1])
		member.append([[l,n]])

# 각 방별로 멤버 출력
for i in member:
	i = sorted(i,key = lambda x:x[1])
	if len(i) == m:
		print("Started!")
	else:
		print("Waiting!")
	for lv,n in i:
		print(lv,n)
