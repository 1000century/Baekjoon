from itertools import product
def solution(users, emoticons):
	answer = [0,0]

	for discount in product([90,80,70,60],repeat = len(emoticons)):
		hogu = 0 # 각 case별 이모티콘플러스 구매자 수
		revenue = 0 # 각 case별 모든 유저의 구매액의 합

		for criteria,budget in users:
			purchase = 0 # 각 유저의 구매액
			for i in range(len(discount)):
				if 100 - discount[i] >= criteria:
					purchase = purchase + int(emoticons[i]*discount[i]//100)
			
			# 이모티콘 플러스 구매하는 경우
			if purchase >= budget:
				hogu = hogu + 1
			
			# 개별 이모티콘 구매하는 경우
			else:
				revenue = revenue + purchase
		
		# 리스트 끼리의 max함수 >> 첫번째 요소 비교 후 같으면 두번째 요소 비교하는 식
		ans_case = [hogu,revenue]
		answer = max(answer,ans_case)
		
	return answer

users = [[40, 10000], [25, 10000]]
emotions = [7000, 9000]	
print(solution(users,emotions))

users = [[40, 2900], [23, 10000], [11, 5200], [5, 5900], [40, 3100], [27, 9200], [32, 6900]]	
emotions = [1300, 1500, 1600, 4900]	
print(solution(users,emotions))


