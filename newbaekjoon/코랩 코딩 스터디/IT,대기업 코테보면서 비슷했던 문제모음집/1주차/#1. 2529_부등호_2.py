k = int(input())
X = input().split()

maxused = [False] * (10)
MM = None

def test_max(arr):
	global MM
	if len(arr) == k+1:
		if MM is None:
			MM = arr[:]
		return

	for i in range(9,8-k,-1):
		if not maxused[i]:
			if not arr or (X[len(arr) - 1] == '<' and arr[-1] < i) or (X[len(arr) - 1] == '>' and arr[-1] > i):
				maxused[i] = True
				test_max(arr + [i])
				maxused[i] = False

test_max([])
print(*MM,sep='')

minused = [False] * (10)
mm = None

def test_min(arr):
	global mm
	if len(arr) == k+1:
		if mm is None:
			mm = arr[:]
		return

	for i in range(k+1):
		if not minused[i]:
			if not arr or (X[len(arr) - 1] == '<' and arr[-1] < i) or (X[len(arr) - 1] == '>' and arr[-1] > i):
				minused[i] = True
				test_min(arr + [i])
				minused[i] = False

test_min([])
print(*mm,sep='')