# 22:28~
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.head = None
        self.length = 0

    # 원소 삽입
    def push(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node
        self.length += 1

    # 원소 추출하기
    def pop_two(self):
        if not self.is_empty():
            data = self.head.data
            self.head = self.head.next
            return data
        else:
            return -1

    def pop_five(self):
        if self.is_empty():
            return -1

        # 머리(head) 위치에서 노드 꺼내기
        data = self.head.data

        return data

    # 스택이 비어있는지 확인
    def is_empty(self):
        return self.head is None

    def get_length(self):
        return self.length
    
stack = Stack()


N = int(input())
for _ in range(1, N+1):
    command = input().strip()
    if command == "2":
        result = stack.pop_two()
        print(result)
        
    elif command == "3":
        length = stack.get_length()
        print(length)
    elif command == "4":
        if stack.is_empty():
            print(1)
        else:
            print(0)
    elif command == "5":
        result = stack.pop_five()
        print(result)
    else:
        a = int(command.split(" ")[-1])
        stack.push(a)
        
        







    