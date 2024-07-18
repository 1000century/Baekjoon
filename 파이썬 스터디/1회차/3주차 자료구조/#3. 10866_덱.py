"""
stdin 안쓰면 시간초과
"""

class deque:
	def __init__(self):
		self.list = []
	
	def empty(self):
		if len(self.list) == 0:
			return 1
		else:
			return 0
	
	def push_front(self,x):
		self.list = [x] + self.list
	
	def push_back(self,x):
		self.list.append(x)
	
	def pop_front(self):
		if self.empty():
			return -1
		else:
			num = self.list[0]
			self.list = self.list[1:]
			return num
	
	def pop_back(self):
		if self.empty():
			return -1
		else:
			num = self.list[-1]
			self.list = self.list[:-1]
			return num
	
	def size(self):
		return len(self.list)
	
	def front(self):
		if self.empty():
			return -1
		else:
			return self.list[0]
	
	def back(self):
		if self.empty():
			return -1
		else:
			return self.list[-1]

import sys
N = int(sys.stdin.readline().rstrip())
ans = []
q = deque()
for _ in range(N):
	cmd_beta = sys.stdin.readline().rstrip().split()
	cmd = cmd_beta[0]

	if cmd == "push_front":
		x = cmd_beta[1]
		q.push_front(x)
	elif cmd == "push_back":
		x = cmd_beta[1]
		q.push_back(x)
	elif cmd == "pop_front":
		ans.append(q.pop_front())
	elif cmd == "pop_back":
		ans.append(q.pop_back())
	elif cmd == "size":
		ans.append(q.size())
	elif cmd == "empty":
		ans.append(q.empty())
	elif cmd == "front":
		ans.append(q.front())
	elif cmd == "back":
		ans.append(q.back())

print(*ans, sep='\n')
