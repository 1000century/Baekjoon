"""
[[2, 3], [4, 3], [1, 1], [2, 1]]	
[2, 1, 1, 0]


[[4, 11], [1, 12], [8, 3], [12, 7], [4, 2], [7, 11], [4, 8], [9, 6], [10, 11], [6, 10], [3, 5], [11, 1], [5, 3], [11, 9], [3, 8]]
[4, 0, 1, 2]
"""
from collections import deque
import copy


	

def solution(edges):
	graph = {}
	start = []

	for edge in edges:
		st,en = edge[0],edge[1]
		if graph.get(st) == None:
			graph[st] = [en]
			start.append(st)
		else:
			graph[st] = graph[st]+[en]
		
		graph[st] = sorted(graph[st])
	print("#####graph",graph)
	start.sort()
	print("start",start)

	for v in start: # 시작노드
		if len(graph[v])<2:
			continue
		ans = [0,0,0,0]
		temp_graph = graph.deepcopy()
		for nv in graph[v]:
			chk_vertex = set()
			chk_edges = 0
			chk_vertex.add(nv)
			if graph.get(nv) ==None:
				ans[2] = ans[2] + 1
				continue
			x = graph[nv][0]
			while True:
				chk_edges = chk_edges + 1
				if temp_graph.get(x) == None:
					ans[2] = ans[2] + 1
					break
				else:
					if x in chk_vertex and temp_graph[x] == []:
						break
					if x not in chk_vertex:
						chk_vertex.add(x)
					print(temp_graph,x)
					x = temp_graph[x].pop(0)
				if len(chk_vertex) == chk_edges:
					ans[3] = ans[3] + 1
				elif len(chk_vertex) == chk_edges +1:
					ans[1] = ans[1] +1
					
		ans[0] = v
		print(ans)


print("------------testcase 1")
edges = [[2, 3], [4, 3], [1, 1], [2, 1]]	

print("최종",solution(edges))

print("_---------------------testcase 2")

edges = [[4, 11], [1, 12], [8, 3], [12, 7], [4, 2], [7, 11], [4, 8], [9, 6], [10, 11], [6, 10], [3, 5], [11, 1], [5, 3], [11, 9], [3, 8]]
[4, 0, 1, 2]

print(solution(edges))
