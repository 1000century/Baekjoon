"""
10:05~10:07
"""

N  = input()

endfix = []
for i in range(len(N)):
	endfix.append(N[i:])
endfix.sort()
for i in endfix:
	print(i)
