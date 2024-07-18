a,b,c = map(int, input().split(" "))
p = [a, b, c]

p.sort()
k = p[-1]
if a == b and a != c:
    l = a
elif b == c and b != a:
    l = b
elif c == a and c != b:
    l = c

if a == b == c:
    print(10000+1000*a)
elif a != b and b!=c and c!=a:
    print(k*100)
else:
    print(1000+l*100)
