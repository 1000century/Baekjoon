N = int(input())
for n in range(0,N):
    print(" "*(N-n-1),"*"*(2*n+1),sep="")
for n in range(1,N):
    print(" "*n,"*"*(2*N-1-2*n),sep="")


