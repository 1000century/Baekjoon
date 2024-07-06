import sys
M,N = map(int,sys.stdin.readline().strip().split())
A = []
dict = {}
for _ in range(M):
    word = sys.stdin.readline().strip()
    leng = len(word)
    if leng >= N:
        if word in dict:
            dict[word][1] += 1
        else:
            dict[word] = [leng,1]
sorted_2 = sorted(dict.items(),key=lambda x: (-x[1][1], -x[1][0],x[0]))

sorted_keys = [item[0] for item in sorted_2]  # 정렬된 아이템에서 키만 추출하여 리스트로 만들기
for i in sorted_keys:
    print(i)

## 딕셔너리를 리스트로 vs 딕셔너리의 key만 빼서 리스트 만들기