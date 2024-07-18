"""
길찾기게임
https://school.programmers.co.kr/learn/courses/30/lessons/42892
"""

nodes = [[8, 6, 7], [3, 5, 4], [11, 5, 2], [1, 3, 6], [5, 3, 1], [13, 3, 3], [2, 2, 9], [7, 2, 8], [6, 1, 5]]
# 노드를 깊이와 위치에 따라 정렬
nodes.sort(key=lambda x: (x[1], x[0]))

# 트리 구성을 위해 각 노드를 연결
tree = {}
for x, depth, name in nodes:
    if depth not in tree:
        tree[depth] = {}
    tree[depth][x] = {'name': name, 'left': None, 'right': None}

# 부모-자식 노드 연결
for depth in sorted(tree.keys()):
    if depth + 1 in tree:
        child_nodes = iter(sorted(tree[depth + 1].items()))
        x, current_node = next(child_nodes)
        for parent_x, parent_node in sorted(tree[depth].items()):
            while x is not None and x < parent_x:
                parent_node['left'] = current_node
                try:
                    x, current_node = next(child_nodes)
                except StopIteration:
                    x, current_node = None, None
            parent_node['right'] = current_node
            if x is not None:
                try:
                    x, current_node = next(child_nodes)
                except StopIteration:
                    break

# 전위 순회 함수
def preorder(node):
    if node is None:
        return []
    return [node['name']] + preorder(node.get('left')) + preorder(node.get('right'))

# 루트 노드 찾기 (가장 작은 깊이의 첫 번째 노드)
root = next(iter(tree[min(tree.keys())].values()))

# 전위 순회 결과 출력
print(preorder(root))
