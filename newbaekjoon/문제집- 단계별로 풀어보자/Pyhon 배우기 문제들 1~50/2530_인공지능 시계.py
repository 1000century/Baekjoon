H,M,S = map(int,input().split())
D = int(input())

present = H*3600 + M * 60 + S

after = present + D


H = (after // 3600) % 24
M = (after%3600) // 60
S = (after%3600) % 60
print(H,M,S)