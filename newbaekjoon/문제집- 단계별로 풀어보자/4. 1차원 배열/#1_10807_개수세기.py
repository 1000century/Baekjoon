N = int(input())
a = list(map(int, input().split()))
v = int(input())
t = 0

for num in a:
    if num == v:
        t +=1
print(t)

#    else:        t = t 는 없어도 된다고 함
# pop을 쓰면 원래의 리스트가 사라지므로 리스트를 복사해서 사용하는 것을 추천한다고 함

# 나는
# for i in range(N):
#    if a.pop()== v:
#        t += 1    이렇게 짯는데
