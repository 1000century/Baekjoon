A = int(input())
B = int(input())
C = int(input())

N = A * B * C
L = list(str(N))
L.extend(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'])
print(L.count('0')-1)
print(L.count('1')-1)
print(L.count('2')-1)
print(L.count('3')-1)
print(L.count('4')-1)
print(L.count('5')-1)
print(L.count('6')-1)
print(L.count('7')-1)
print(L.count('8')-1)
print(L.count('9')-1)
