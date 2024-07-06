N,M = map(int,input().split())
A = input()
B = input()
C = A + " " + B
G = list(map(int,C.split()))
G_1 = list(set(G))
print(2*len(G_1)-len(G))