import sys

N, K = map(int,sys.stdin.readline().strip().split())
A = list(map(int,sys.stdin.readline().strip().split()))
KL = K
count = 0
ans = 0
def merge_sort(A,p,r): # A[p..r]을 오름차순 정렬한다.
    if (p < r):
        q = (p + r) // 2       # q는 p, r의 중간 지점
        merge_sort(A, p, q)      # 전반부 정렬
        merge_sort(A, q + 1, r)  # 후반부 정렬
        merge(A, p, q, r)        # 병합
    else:
        return

def merge(A, p, q, r):
    i = p
    j = q + 1
    t = 1
    tmp = []
    global count, K, ans
    while i <= q and j <= r:
        if A[i] <= A[j]:
            tmp.append(A[i])
            if K ==1:
                ans = A[i]
            K = K - 1
            i = i + 1
        else:
            tmp.append(A[j])
            if K ==1:
                ans = A[j]
            j = j + 1
            K = K - 1
    while (i <= q):  # 왼쪽 배열 부분이 남은 경우
        tmp.append(A[i])
        if K == 1:
            ans = A[i]
        i = i + 1
        K = K - 1
    while (j <= r):  # 오른쪽 배열 부분이 남은 경우
        tmp.append(A[j])
        if K == 1:
            ans = A[j]
        j = j + 1
        K = K - 1
    i = p
    t = 0
    while (i <= r):  # 결과를 A[p..r]에 저장
        A[i] = tmp[t]
        count += 1
        i = i + 1
        t = t + 1


merge_sort(A,0,4)

if count  < KL:
    print(-1)
else:
    print(ans)