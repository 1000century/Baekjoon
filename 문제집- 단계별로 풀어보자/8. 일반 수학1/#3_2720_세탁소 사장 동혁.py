T = int(input())
for _ in range(T):
    N = int(input())
    quarter = N // 25
    dime = (N%25) // 10
    nickel = ((N%25)%10) //5
    penny = (((N%25)%10)%5) 
    print(quarter,dime,nickel,penny, sep=" ")
