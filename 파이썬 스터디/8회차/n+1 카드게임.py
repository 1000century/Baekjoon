import sys
from itertools import combinations

sys.setrecursionlimit(10000)

def back(cards, coin, step, have, N):
	if not cards:
		return step
	
	if not have:
		return step

	max_step = step

	# 두 장 다 갖는 경우
	if coin >= 2:
		new_have = have[:] + cards[:2]
		for a, b in combinations(new_have, 2):
			if a + b == N + 1:
				temp = new_have[:]
				temp.remove(a)
				temp.remove(b)
				max_step = max(max_step, back(cards[2:], coin - 2, step + 1, temp, N))

	# 한 장만 갖는 경우
	if coin >= 1:
		for i in range(2):
			new_have = have[:] + [cards[i]]
			for a, b in combinations(new_have, 2):
				if a + b == N + 1:
					temp = new_have[:]
					temp.remove(a)
					temp.remove(b)
					max_step = max(max_step, back(cards[2:], coin - 1, step + 1, temp, N))

	# 두 장 다 버리는 경우
	new_have = have[:]
	for a, b in combinations(new_have, 2):
		if a + b == N + 1:
			temp = new_have[:]
			temp.remove(a)
			temp.remove(b)
			max_step = max(max_step, back(cards[2:], coin, step + 1, temp, N))

	return max_step

def solution(coin, cards):
	n = len(cards)
	initial_cards = cards[:n//3]
	remaining_cards = cards[n//3:]
	max_steps = back(remaining_cards, coin, 0, initial_cards, n)
	return max_steps + 1

n = 18
coin = 10
cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]	
solution(coin, cards)
