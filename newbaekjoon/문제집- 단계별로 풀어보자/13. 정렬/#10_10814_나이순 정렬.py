N = int(input())
A = []
for _ in range(N):
    case = list(input().split())
    case[0]= int(case[0])
    A.append(case)
    A[_].insert(1,_)
A = sorted(A)
for _ in range(N):
    print(A[_][0],A[_][2],sep=" ")


    """숫자를 정수형으로 입력받아서 정렬을 하게 되면 정수 비교로 크고 작음을 결정하지만 문자로 입력받게 되면 아스키코드 값으로 비교를 하기 때문에 ‘7’이 ‘55’보다 뒤에 위치하게 됩니다.

정수로 입력받으시면 돼요."""