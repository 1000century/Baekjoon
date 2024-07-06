S = list(input())
count = 0
for i in range(26):
	if chr(i+97) in S:
		print(S.index(chr(i+97)),end= " ")
	else:
		print(-1, end=" ")
	
# 딕셔너리로 풀면 빠를듯? import package
