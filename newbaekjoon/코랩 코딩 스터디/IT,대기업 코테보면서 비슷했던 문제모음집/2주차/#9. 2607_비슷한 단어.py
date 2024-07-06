N = int(input())
word_temp = input()
cnt = 0
for _ in range(N-1):
	stacka = []
	stackb = []
	x = input()
	word = {i:word_temp.count(i) for i in word_temp}

	for i in x:
		if word.get(i) == None:
			stacka.append(i)
		else:
			word[i] = word[i] -1
	print(x, word,stacka,stackb)
	
	# 같은 구성이거나
	if stacka ==[] and sum(word.values()) ==0:
		cnt = cnt + 1
		continue
	# 더하거나
	if len(stacka) + len(stackb) == 0 and sum(word.values()) == 1:
		cnt = cnt + 1
		continue

	# 빼거나
	if len(stacka) + len(stackb) == 1 and sum(word.values()) ==0:
		cnt = cnt +1
		continue

	# 바꾸거나 - 1
	if len(stacka) ==0 and len(stackb) == 2 and sum(word.values())==2:
		cnt = cnt + 1
		continue

	# 바꾸거나 - 2
	if len(stacka) == 1 and len(stacka) == 1 and sum(word.values()) ==2:
		cnt = cnt + 1
		continue
	


print(cnt)
