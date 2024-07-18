import re
from itertools import permutations

def chk(banned_id, combination):
	for b_id, uid in zip(banned_id, combination):
		if len(b_id) != len(uid):
			return -1
		for b_char, u_char in zip(b_id, uid):
			if b_char != '*' and b_char != u_char:
				return -1
	return True

def solution(user_id, banned_id):
	val = set()
	for arr in permutations(user_id, len(banned_id)):
		if chk(banned_id, arr) == True:
			val.add(tuple(sorted(arr)))
	return len(val)

