S = input()
for _ in range(97,123):
    a = chr(_)
    print(S.find(a), end=" ")


# index는 배열에서 값의 위치를 찾아주며
#         중복된 값이 있으면 최소의 위치를 리턴
#         찾는 값이 없으면 오류를 발생시킴(substring을 찾을 수 없다는 valueerror)
# find는 찾는 문자나 문자열이 없을 경우에는 -1을 return 함