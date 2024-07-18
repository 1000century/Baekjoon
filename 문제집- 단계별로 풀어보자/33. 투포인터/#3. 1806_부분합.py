#1) 부분합 리스트 구하고 투포인터

N,S = map(int,input().split())
num= list(map(int,input().split()))
numbers = [0]
for i in range(N):
	numbers.append(num[i]+numbers[i])
begin = 0
end = 1

succession = int(1e9)

while end <=N:
	if end == begin:
		end = end + 1
		continue
	temp = numbers[end] - numbers[begin]
	if temp >=S:
		succession = min(succession,end-begin)

	if temp == S:
		begin = begin + 1
		end = end + 1

	elif temp >S:
		begin = begin + 1
	elif temp < S:
		end = end + 1


if succession == int(1e9):
	print(0)
else:
	print(succession)