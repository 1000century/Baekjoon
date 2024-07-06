T = int(input())
for _ in range(T):
        
    R, S = input().split(" ")
    R = int(R)
    k = len(S)
    for letter_index in range(k):
        print(S[letter_index]*R,sep="",end="")
    print()

