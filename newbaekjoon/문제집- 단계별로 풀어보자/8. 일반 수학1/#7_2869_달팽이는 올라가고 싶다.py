import sys
A,B,V = map(int,sys.stdin.readline().split())

days = (V-A) //(A-B)

if (V-A) % (A-B) != 0:
    days += 1
print(days+1)
