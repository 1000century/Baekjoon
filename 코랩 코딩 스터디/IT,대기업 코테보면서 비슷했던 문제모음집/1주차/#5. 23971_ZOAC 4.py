# (세현)

H,W,N,M = map(int,input().split())

a = W // (M+1) + (W%(M+1) != 0)
b = H // (N+1) + (H%(N+1) != 0)

print(a*b)