T = int(input())       # T는 총 몇번 시행하는지
for _ in range(T):     # T번 시행할거야
        
    R, S = input().split(" ")   #R은 반복횟수, S는 처음 입력 문자열
    R = int(R)                  #R,S 중에 R만 정수화 해주고

    # 여기서부터 어떻게 할까 고민했는데 더 효율적으로 하는 코드가 있을거 가ㅏㅌ긶마
    # S의 문자열 길이를 구해서(len) 
    # >> S의 문자ㅏ열의 index를 통해서 R번씩 반복 >> 이과정에서는 반복문사용
    k = len(S)
    for letter_index in range(k):
        print(S[letter_index]*R,sep="",end="")
    print()

