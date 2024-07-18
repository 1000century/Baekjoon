# str을 사용하는 대신 다른 변수명 사용 (예: text_list)

text_list = list(input())

N = int(input())
cur = len(text_list)
for _ in range(N):
    rawCMD = input().split()
    cmd = rawCMD[0]
    if len(rawCMD) == 2:
        num = rawCMD[1]
    if cmd == "L":
        if cur != 0:
            cur = cur - 1
    elif cmd == "D":
        if cur < len(text_list):
            cur = cur + 1
    elif cmd == "B":
        if cur != 0:
            del text_list[cur - 1]
            cur = cur - 1
    elif cmd == "P":
        text_list.insert(cur, num)
        cur += 1  # 문자를 추가한 후 커서 위치 업데이트
print(*text_list, sep="")  # 수정된 리스트를 문자열로 출력