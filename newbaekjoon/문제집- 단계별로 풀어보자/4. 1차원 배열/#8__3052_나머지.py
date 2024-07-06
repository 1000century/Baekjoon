a = []
for _ in range(10):
    element = int(input()) % 42
    a.append(element)
sorted(a)

b = []
for _ in range(10):
    if a[_] not in b:
        b.append(a[_])
print(len(b))

# 중복 제거 방법
#1. 새로운 리스트를 만들어 거기에 저장시킨다.
#2. list를 set으로 바꿨다가 list로 바꾼다.

# a = []
# for _ in range(10):
#     element = int(input()) % 42
#     a.append(element)
# sorted(a)
# list1 = set(a)
# rist2 = list(list1)
# print(len(rist2))