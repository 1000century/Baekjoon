import sys
input = sys.stdin.readline

def build_segment_tree(arr, seg_tree, start, end, node):
    if start == end:
        seg_tree[node] = 1
    else:
        mid = (start + end) // 2
        build_segment_tree(arr, seg_tree, start, mid, 2 * node + 1)
        build_segment_tree(arr, seg_tree, mid + 1, end, 2 * node + 2)
        seg_tree[node] = seg_tree[2 * node + 1] + seg_tree[2 * node + 2]

def update_segment_tree(seg_tree, start, end, idx, value, node):
    if start == end:
        seg_tree[node] += value
    else:
        mid = (start + end) // 2
        if start <= idx <= mid:
            update_segment_tree(seg_tree, start, mid, idx, value, 2 * node + 1)
        else:
            update_segment_tree(seg_tree, mid + 1, end, idx, value, 2 * node + 2)
        seg_tree[node] = seg_tree[2 * node + 1] + seg_tree[2 * node + 2]

def query_segment_tree(seg_tree, start, end, l, r, node):
    if r < start or end < l:
        return 0
    if l <= start and end <= r:
        return seg_tree[node]
    mid = (start + end) // 2
    left_query = query_segment_tree(seg_tree, start, mid, l, r, 2 * node + 1)
    right_query = query_segment_tree(seg_tree, mid + 1, end, l, r, 2 * node + 2)
    return left_query + right_query

import math

def permutation_index(perm, K):
    n = len(perm)
    seg_tree = [0] * (4 * K)
    build_segment_tree(range(1, K+1), seg_tree, 0, K-1, 0)
    
    index = 0
    for i in range(n):
        current = perm[i] - 1
        if current > 0:
            rank = query_segment_tree(seg_tree, 0, K-1, 0, current-1, 0)
        else:
            rank = 0
        index += (rank * math.factorial(K-1-i))%1000000007
        update_segment_tree(seg_tree, 0, K-1, current, -1, 0)
    
    return (index + 1)%1000000007

# 순열과 K값, 변경할 위치 a, b
K,N = map(int,input().split())
init_perm = list(map(int,input().split()))
for _ in range(N):
	a,b = map(int,input().split())
	perm = init_perm[:]
	# a와 b의 위치를 바꾼 후의 순열 순서를 구함
	perm[a-1], perm[b-1] = perm[b-1], perm[a-1]
	index = permutation_index(perm, K)
	print(index)
