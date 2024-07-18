N, M = map(int,input().split())
A = list(map(int, input().split()))

countA = {}
countA[0] = 1  # 0인 경우는 1개가 더 있다고 생각해줘야 함

hap = 0
for i in A:
    hap = (hap + i) % M
    countA[hap] = countA.get(hap, 0) + 1
	# if countA.get(hap) == None: 를 간소화시킨 버전
"""  <dict.get(key, default) 메서드>
딕셔너리에서 주어진 key에 해당하는 값을 반환합니다.
만약 key가 딕셔너리에 없으면, default 값을 반환합니다.
이 특성을 활용하면 if 문을 사용하지 않고 코드를 단순화할 수 있습니다.
"""
ans = 0
for item,key in countA.items():
	if key>=2:
		ans = ans + key*(key-1)//2
print(ans)
