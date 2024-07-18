class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

# Node 클래스는 스택에 저장될 데이터를 나타냄
# 노드에는 데이터와 next 변수를 가진다.
# 일단 초기값에서 next 변수는 None을 가리킨다.

# Stack 클래스는 실제 스택 자료구조를 구현하는 역할

class Stack:
    def __init__(self):
        self.head = None
# self.head는 스택의 맨 위를 가리키는 포인터
# 초기 상태는 None으로 설정하였다.

    def push(self,data):
        node = Node(data)      # 새로 넣는 데이터에 node객체 생성
        node.next = self.head  # 데이터 간의 화살표 만들고     
        self.head = node       # head 포인터를 새로 넣는 데이터로 옮김

        return data
        # 수업에서는 이 코드가 없었는데 이렇게 해야
        # 해당 데이터를 반환하게 됨
        # 데이터를 반환한다는 것은 그냥 기억한다일 뿐 print되는 것 아님


따라서 is_empty 메서드는 self.head가 None인지를 검사하여 스택이 비어있으면 True를 반환하고, 그렇지 않으면 False를 반환합니다.

stack = Stack()
print(stack.push(3))
