N = int(input())
nums = list(map(int,input().split()))
num_dict = {item:1 for item in nums}

M = int(input())
check = list(map(int,input().split()))

for i in check:
    try:
        if num_dict[i] ==1:
            print(1,end=" ")
    except:
        print(0,end=" ")