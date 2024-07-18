# (세현)

# 문자열 인덱스 슬라이싱 vs pop
# 문자열 인덱스 슬라이싱 쓰면 시간초과

char = str(input())
boom = list(str(input()))
st = []
for i in char:
	st.append(i)
	while len(st) >= len(boom) and st[-len(boom):]==boom:
		del st[-len(boom):]

if st:
	print(*st,sep='')
else:
	print("FRULA")