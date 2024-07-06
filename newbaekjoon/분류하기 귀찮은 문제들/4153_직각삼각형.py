import sys
while True:
    N = sys.stdin.readline().strip()
    if N == "0 0 0":
        exit()
    a,b,c = map(int,N.split())
    if a*a -b*b-c*c == 0:
        print("right")
    elif b*b -a*a-c*c == 0:
        print("right")
    elif c * c - a * a - b * b == 0:
        print("right")
    else:
        print("wrong")
