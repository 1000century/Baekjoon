import sys
input = sys.stdin.readline

string = input().strip()
class Node:
    def __init__(self, value, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev

head = Node(None)
cur_node = head
for i in range(0, len(string)):
    cur_node.next = Node(string[i], prev=cur_node)
    cur_node = cur_node.next

cursor = cur_node
n = int(input())
for i in range(n):
    cmd = input().split()
    if cmd[0] == "L":
        if cursor.prev != None:
            cursor = cursor.prev
    elif cmd[0] == "D":
        if cursor.next != None:
            cursor = cursor.next
    elif cmd[0] == "B":
        if cursor.prev != None:
            cursor.prev.next = cursor.next
            if cursor.next != None:
                cursor.next.prev = cursor.prev
            cursor = cursor.prev
    elif cmd[0] == "P":
        cursor.next = Node(cmd[1], cursor.next, cursor)
        if cursor.next.next != None:
            cursor.next.next.prev = cursor.next
        cursor = cursor.next
        
node = head
while node:
    if node.value != None:
        print(node.value,end="")
    node = node.next
