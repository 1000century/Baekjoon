"""
24.03.11 23:56~24:09
"""
L = int(input())
chara = input()
sum=0
for i in range(len(chara)):
	sum = sum + ((ord(chara[i])-96)*(31**i)) 

print(sum%1234567891)