"""
내일로 여행
https://www.acmicpc.net/problem/13168

1092ms
>> 아이디어
플로이드 워셜

"""

# 무료 :무궁화호, ITX-새마을, ITX-청춘
# 절반: S-train, V-train
# 할인x : KTX, 지하철, 그 외
import sys
input = sys.stdin.readline
INF = int(1e9)

N,R = map(int,input().split())
city = list(input().split())
city = set(city)
graph_nail = {}
graph_none = {}

for i in city:
	graph_nail[i] = {c:INF for c in city}
	graph_none[i] = {c:INF for c in city}
	graph_nail[i][i] = 0
	graph_none[i][i] = 0

M = int(input())
travel = list(input().split())
K = int(input()) # 교통수단 개수

for _ in range(K):
	type,st,en,c = input().split()
	c = int(c)
	graph_none[st][en] = min(graph_none[st][en],c)
	graph_none[en][st] = min(graph_none[en][st],c)
	if type in {"ITX-Saemaeul", "ITX-Cheongchun","Mugunghwa"}:
		graph_nail[st][en] = 0
		graph_nail[en][st] = 0
	elif type in {"V-Train","S-Train"}:
		graph_nail[st][en] = min(graph_nail[st][en],c/2)
		graph_nail[en][st] = min(graph_nail[en][st],c/2)
	else: # 지하철, 버스 KTX
		graph_nail[st][en] = min(graph_nail[st][en],c)
		graph_nail[en][st] = min(graph_nail[en][st],c)

for m in city:
	for st in city:
		for en in city:
			graph_none[st][en] = min(graph_none[st][en],graph_none[st][m] + graph_none[m][en])

for m in city:
	for st in city:
		for en in city:
			graph_nail[st][en] = min(graph_nail[st][en],graph_nail[st][m] + graph_nail[m][en])


diff = graph_none[travel[-1]][travel[0]] - (R + graph_nail[travel[-1]][travel[0]])
for i in range(M-1):
	st,en = travel[i],travel[i+1]
	diff = diff + graph_none[st][en] - graph_nail[st][en]
if diff>0:
	print("Yes")
else:
	print("No")