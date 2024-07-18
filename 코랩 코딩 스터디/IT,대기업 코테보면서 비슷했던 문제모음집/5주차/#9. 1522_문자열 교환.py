# (세현)
# 투포인터 - 슬라이싱 윈도우

arr = input()

len_a = arr.count("a")
arr = arr + arr[:len_a] # 원형이니까 window사이즈만큼 늘림.

st = 0
en = len_a
count = []
while en <=len(arr):
	count.append(arr[st:en].count("b"))
	st = st +1
	en = en + 1

print(min(count))