"""
stdin 안쓰면 시간초과
"""

class Queue:
	def __init__(self):
		self.list = []
	
	def push(self,num):
		self.list.append(num)

	def pop(self):
		if self.empty():
			return -1
		else:
			output = self.list[0]
			self.list = self.list[1:]

			return output
	def empty(self):
		if len(self.list) == 0:
			return 1
		else:
			return 0
	
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
q = Queue()
for _ in range(N):
	cmd_beta = sys.stdin.readline().rstrip().split()
	cmd = cmd_beta[0]

	if cmd == "pop":
		ans.append(q.pop())
	elif cmd == "size":
		ans.append(q.size())
	elif cmd == "empty":
		ans.append(q.empty())
	elif cmd == "front":
		ans.append(q.front())
	elif cmd == "back":
		ans.append(q.back())
	elif cmd == "push":
		x = cmd_beta[1]
		q.push(x)
print(*ans, sep='\n')

