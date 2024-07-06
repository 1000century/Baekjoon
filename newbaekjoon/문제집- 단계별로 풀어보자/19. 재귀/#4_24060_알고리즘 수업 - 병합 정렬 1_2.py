import sys

N, K = map(int,sys.stdin.readline().strip().split())
A = list(map(int,sys.stdin.readline().strip().split()))
count = 0
output = []

def mergesort(A, p, r):
    global count
    if p < r:
        q = (p+r)//2
        mergesort(A, p, q)
        mergesort(A, q+1, r)
        merge(A, p, q, r)

def merge(A, p, q, r):
    global count
    temp = [0] * (r-p+1)  # 크기를 필요한 만큼만 할당
    i = p
    j = q  +1
    p = 0
    while i <= q and j <= r:
        if A[i] <= A[j]:
            temp[t] = A[i]
            i += 1
        else:
            temp[t] = A[j]
            j += 1
        t += 1
        count += 1  # 이동할 때마다 count를 증가
        if count == K:
            output.append(temp[t-1])  # 출력할 값을 저장

    while i <= q:
        temp[t] = A[i]
        i += 1; t += 1
        count += 1
        if count == K:
            output.append(temp[t-1])

    while j <= r:
        temp[t] = A[j]
        j += 1; t += 1
        count += 1
        if count == K:
            output.append(temp[t-1])

    # 병합된 결과를 원본 배열에 복사
    A[p:p+len(temp)] = temp

mergesort(A, 0, len(A)-1)

if output:
    print(output[0])
else:
    print(-1)