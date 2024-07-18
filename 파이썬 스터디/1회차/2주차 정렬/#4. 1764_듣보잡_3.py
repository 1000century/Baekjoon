"""
시간 오래 걸림 3696ms

그래서 딕셔너리 쓰는 거 사용
근데 그래서 이 문제의 의의가 뭐지?

딕셔너리가 아니라 set 쓰는 거인듯
>> in함수는 set함수를 사용시 해시테이블을 이용하므로 O(1)
>> in함수 list에서 시간복잡도는 o(n)

그럼에도 하나의 리스트로 만들어서 앞뒤로 비교하는 게 시간복잡도는 제일 적었음
(	if X[i] == X[i+1] and X[i]!=before:)
"""


n,m = map(int,input().split())
a=set()
b=set()
result =[]
for _ in range(n):
    a.add(input())
for _ in range(m):
    b.add(input())

for i in a :
    if i in b :
        result.append(i)
result.sort()
print(len(result))
for i in result :
    print(i)