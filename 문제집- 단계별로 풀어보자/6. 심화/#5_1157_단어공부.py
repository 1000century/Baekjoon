word = input()
word = word.upper()


group = []
for _ in range(len(word)):
    group.append(word[_])
acccc = set(group)
hehe = list(acccc)

counts_per_alphabet = []
for _ in range(len(hehe)):
    counts_per_alphabet.append(group.count(hehe[_]))

if counts_per_alphabet.count(max(counts_per_alphabet)) >= 2:
    print("?")
else:
    print(hehe[counts_per_alphabet.index(max(counts_per_alphabet))])



# 역대급으로 스파게티로 꼬아버렷네...
