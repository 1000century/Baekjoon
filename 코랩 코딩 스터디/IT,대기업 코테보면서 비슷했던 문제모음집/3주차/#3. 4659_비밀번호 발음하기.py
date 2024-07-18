def test(chk=[0,1,1], before_type="initialization", before_letter="initialization", count = 1):
	testcase = input()
	if testcase == "end":
		exit()
	
	for i in testcase:

		# 자음 모음 판별
		if not chk[0]:
			chk[0] = i in "aeiou"
		isit_moeum = i in "aeiou"
		
		# 자음 3번 연속 혹은 모음 3번 연속 확인
		if before_type == isit_moeum:
			count = count + 1
		else:
			count = 1
			before_type = isit_moeum
		if count == 3:
			chk[1] = 0
			break

		# e,o를 제외한 문자가 2번 연속 반복되는지 확인
		if before_letter == i and i not in "eo":
			chk[2] = 0
			break
		before_letter = i

	# 합이 3이면 올바른 비밀번호
	if sum(chk) == 3:
		print(f"<{testcase}> is acceptable.")
	else:
		print(f"<{testcase}> is not acceptable.")

while True:
	test(chk=[0,1,1], before_type="initialization", before_letter="initialization", count = 1)
