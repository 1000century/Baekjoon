# (세현)

word = input().upper() + "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

words = {}
for i in word:
	words[i] = words.get(i,0) + 1

onetwo = sorted(words, key=lambda x:words[x], reverse=True)[:2]
if words[onetwo[0]] == words[onetwo[1]]:
	print("?")
else:
	print(onetwo[0])
