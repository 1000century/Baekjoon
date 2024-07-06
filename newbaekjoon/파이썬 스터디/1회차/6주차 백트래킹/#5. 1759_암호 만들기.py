L,C = map(int,input().split())
ch = list(input().split())
ch.sort()

def combination(arr,index):
	if len(arr) == L:
		count = 0
		for i in arr:
			if i in "aeiou":
				count = count + 1
		if 1<=count<=L-2:
			print(*arr,sep='')
		return
	
	for i in range(index, C):
		arr.append(ch[i])
		combination(arr,i+1)
		arr.pop()

combination([],0)