# (세현)

N = int(input())
arr = input()

front = arr[0]
cnt = 0
for i in range(N):
	if arr[i] != front:
		break
	cnt = cnt + 1
fr = arr.count(front)
ans1 = min(fr-cnt,N-fr)

back = arr[-1]
cnt = 0
for i in range(N-1,-1,-1):
	if arr[i] != back:
		break
	cnt = cnt + 1
ba = arr.count(back)
ans2 = min(ba-cnt,N-ba)

print(min(ans1,ans2))