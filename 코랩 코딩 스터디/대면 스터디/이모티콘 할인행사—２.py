def solution(users, emoticons):
	discounts = [90,80,70,60]
	case = [0] * len(emoticons)
	def backtrack(idx,hogu,revenue):
		ans_hogu,ans_revenue = hogu, revenue
		if idx == len(emoticons):
			
			hogu = 0 # 각 case별 이모티콘플러스 구매자 수
			revenue = 0 # 각 case별 모든 유저의 구매액의 합

			for criteria,budget in users:
				purchase = 0 # 각 유저의 구매액
				for i in range(len(case)):
					if 100 - case[i] >= criteria:
						purchase = purchase + int(emoticons[i]*case[i]//100)
				
				# 이모티콘 플러스 구매하는 경우
				if purchase >= budget:
					hogu = hogu + 1
				
				# 개별 이모티콘 구매하게 되는 경우
				else:
					revenue = revenue + purchase
			
			# 이모티콘 플러스 구매자가 이전보다 더 많은 경우
			if hogu > ans_hogu:
				ans_hogu = hogu
				ans_revenue = revenue
			# 이모티콘 플러스 구매자 수는 동일  +  판매액이 더 많은 경우
			elif hogu == ans_hogu and revenue > ans_revenue:
				ans_revenue = revenue
		else:
			for discount in discounts:
				case[i] = discount
				backtrack(idx+1,ans_hogu,ans_revenue)
				case[i] = 0
	backtrack(0,0,0)
	answer = [ans_hogu,ans_revenue]

	return answer

users = [[40, 10000], [25, 10000]]
emotions = [7000, 9000]	
print(solution(users,emotions))

users = [[40, 2900], [23, 10000], [11, 5200], [5, 5900], [40, 3100], [27, 9200], [32, 6900]]	
emotions = [1300, 1500, 1600, 4900]	
print(solution(users,emotions))


