"""
stdin 써야 통과 (1192ms)
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class doublelinkedlist:
    def __init__(self):
        self.head = Node(None)
        self.tail = Node(None)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.cursor = self.tail

    def insert(self, data):
        new_node = Node(data)
        prev_node = self.cursor.prev
        new_node.prev = prev_node
        new_node.next = self.cursor
        prev_node.next = new_node
        self.cursor.prev = new_node

    def delete(self):
        if self.cursor.prev != self.head:
            prev_node = self.cursor.prev
            pre_prev_node = prev_node.prev
            pre_prev_node.next = self.cursor
            self.cursor.prev = pre_prev_node

    def moveL(self):
        if self.cursor.prev != self.head:
            self.cursor = self.cursor.prev

    def moveR(self):
        if self.cursor != self.tail:
            self.cursor = self.cursor.next

    def print_linkedlist(self):
        temp = self.head.next
        while temp != self.tail:
            print(temp.data, end="")
            temp = temp.next

dl = doublelinkedlist()

import sys
input = sys.stdin.readline

text_list = list(input().rstrip())
N = int(input().rstrip())

for i in range(len(text_list)):
	dl.insert(text_list[i])

for _ in range(N):
	rawCMD = input().split()
	cmd = rawCMD[0]
	if len(rawCMD) == 2:
		num = rawCMD[1]
	if cmd == "L":
		dl.moveL()
	elif cmd == "D":
		dl.moveR()
	elif cmd == "B":
		dl.delete()
	elif cmd == "P":
		dl.insert(num)
dl.print_linkedlist()
