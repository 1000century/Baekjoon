# (세현)

N = int(input())

alpha = {"A":0, "B":0, "C":0, "D":0, "E":0, "F":0, "G":0, 
		 "H":0, "I":0, "J":0, "K":0, "L":0, "M":0, "N":0,
		 "O":0, "P":0, "Q":0, "R":0, "S":0, "T":0, "U":0,
		 "V":0, "W":0, "X":0, "Y":0, "Z":0,}

for _ in range(N):
	X = input()
	for i in range(1,len(X)+1):
		alpha[X[-i]] = alpha[X[-i]] + 10**(i-1)

alpha_list = sorted(alpha.items(), key = lambda x:x[1], reverse=True)
ans = 0
for i in range(0,9):
	ans = ans +alpha_list[i][1]*(9-i)
print(ans)

