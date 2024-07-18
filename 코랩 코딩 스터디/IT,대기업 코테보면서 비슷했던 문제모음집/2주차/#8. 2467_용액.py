# (세현)

N = int(input())
solute = list(map(int,input().split()))
solute.sort()

def test():
	# ans_final: 최종 정답
	# ans_idx: 투포인터 중 첫번째 포인터(idx)에서의 정답
	# temp: 현재 이분탐색하고 있는 두 용액

	ans_final = [1000000000,1000000000]
	for idx in range(N): 							# idx: 첫번째 포인터의 인덱스 번호
		first = solute[idx]							# first: 첫번째 용액
		ans_idx = [1000000000,1000000000]

		low = idx + 1
		high = N

		while low<high:
			mid = (low+high)//2  					# mid: 두번째 포인터의 인덱스 번호
			second = solute[mid]					# second: 두번째 용액
			temp = [first,second]

			# 정확히 0이면 return 해서 종료
			if sum(temp)==0:
				return temp

			# temp가 정답 후보인 경우, 인덱스 idx에서의 정답인 ans_idx에 저장
			if abs(sum(ans_idx)) > abs(sum(temp)):
				ans_idx = temp

			# 위끝, 아래끝 조절 ((음수,음수),(음수,양수),(양수,양수) 인 경우로 나눔)
			if first <0 and second <0:
				low = mid + 1

			elif first<0 and second > 0: # cf) (first,second)가 (음수, 양수) 인 경우는 없음.
				if abs(first) > abs(second):
					low = mid + 1
				else:
					high = mid

			else: # 양수 양수
					high = mid

		# 최종정답인 ans_final 업데이트
		if abs(sum(ans_final)) > abs(sum(ans_idx)):
			ans_final = ans_idx

	return ans_final

print(*test())