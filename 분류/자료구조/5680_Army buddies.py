"""
stdin 쓰면 통과 (980ms)
"""

import sys
rl = sys.stdin.readline

while True:
	S, B = map(int,rl().split()) # S는 군인 수, B는 loss report
	if S == 0 and B ==0:
		break
	else:
		testcase = {}
		if S == 1:
			testcase[1] = [None,None]
		else:
			testcase[1] = [None,2]
			testcase[S] = [S-1,None]
			for i in range(2,S):
				testcase[i] = [i-1,i+1]
#		print("testcase", testcase)

		for _ in range(B):
			L,R = map(int,rl().split())
			newConnect = ["*","*"]

			# who is new LEFT buddy? / who is new RIGHT buddy?
			buddyL = testcase[L][0]
			buddyR = testcase[R][1]

			# LEFT buddy의 next_node 바꾸고 새롭게 연결 설정
			if buddyL != None:
				testcase[buddyL][1] = buddyR
				newConnect[0] = buddyL

			# RIGHT buddy의 prev_node 바꾸고 새롭게 연결 설정
			if buddyR != None:
				testcase[buddyR][0] = buddyL
				newConnect[1] = buddyR

			print(*newConnect)
#			print("새롭게 맺어진 친구의 쌍", *newConnect)

		print("-")
#		print("testcase 종료", "_")