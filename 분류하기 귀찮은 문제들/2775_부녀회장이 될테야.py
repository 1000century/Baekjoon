T = int(input())
for _ in range(T):
    k = int(input())
    n = int(input())                                    ## 우리가 아는 n 은 1호부터 있는 거고    예를 들어 3호를 보고 싶다면
    A = []
    fl_0=[]


    for i in range(0,k+1):     # i층 기준
      if i == 0:
        for t in range(1,n+1):
          fl_0.append(t)
        A.append(fl_0)
      else:

        B = []
        for j in range(0,n):        #j 번째 원소의 정보 새로고침  여기서는 j로는 0,1,2를 봐야겠지?
            specific_element = 0
            for t in range(0,j+1):    #1호부터 j ㅜ까지
                specific_element = specific_element + A[i-1][t]
            B.append(specific_element)
        A.append(B)

    print(A[k][n-1])