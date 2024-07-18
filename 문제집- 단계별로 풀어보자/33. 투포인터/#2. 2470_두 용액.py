N = int(input())
liquids = list(map(int,input().split()))
liquids.sort()
s = 0
e = N-1

value = 2000000000

while s <e:
	temp_value = liquids[s] + liquids[e]
	if temp_value == 0:
		ans = [liquids[s],liquids[e]]
		break

	if abs(temp_value) <value:
		ans = [liquids[s],liquids[e]]
		value = abs(temp_value)

	if liquids[s] + liquids[e] > 0:
		e = e-1
	else:
		s = s + 1
print(*ans)