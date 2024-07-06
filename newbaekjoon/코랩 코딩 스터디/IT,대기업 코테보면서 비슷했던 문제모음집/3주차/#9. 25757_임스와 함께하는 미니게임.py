import sys
input = sys.stdin.readline
N,Y = input().split()
N = int(N)
players = set()
for _ in range(N):
	players.add(input())

if Y == "Y":
	print((len(players))//1)
if Y == "F":
	print((len(players))//2)
if Y == "O":
	print((len(players))//3)