N = int(input())

def hanoi(n):
    temp = []
    if n == 1:
        temp.append([1,3])
        return temp
    elif n == 2:
        temp.append([1,2])
        temp.append([1,3])
        temp.append([2,3])
        return temp
    else:
        temp_both = hanoi(n-1)
        temp_prev = [x[:] for x in temp_both]  # 이 부분을 수정하여 리스트를 복사합니다
        temp_aft = [x[:] for x in temp_both]  # 이 부분을 수정하여 리스트를 복사합니다
        for i in temp_prev:
            if i[0] == 2:
                i[0] = 3
            elif i[0] == 3:
                i[0] = 2
            if i[1] == 2:
                i[1] = 3
            elif i[1] == 3:
                i[1] = 2
            temp.append(i)
        temp.append([1, 3])
        for i in temp_aft:
            if i[0] == 1:
                i[0] = 2
            elif i[0] == 2:
                i[0] = 1
            if i[1] == 1:
                i[1] = 2
            elif i[1] == 2:
                i[1] = 1
            temp.append(i)
        return temp
result = hanoi(N)
print(len(result))
for i in result:
    print(i[0],i[1], sep=" ")