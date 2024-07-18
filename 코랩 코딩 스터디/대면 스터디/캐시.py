# (세현)
# cf) deque >> maxlen

from collections import deque
def solution(cacheSize, cities):
	answer = 0
	q = deque([])

	for city in cities:
		city = city.lower()
		if city not in q:
			answer = answer +5
			q.appendleft(city)
			if len(q)>cacheSize:
				q.pop()
			continue
		answer = answer +1
		q.remove(city)
		q.appendleft(city)

	return answer