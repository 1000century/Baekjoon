S = input()
a = len(S)


chk = []
for i in range(a-1):    # i는 번째 / 돌려서 몇개 나오는지
    chk.append(S[i:i+2])
for i in range(a-2):    # i는 번째 / 돌려서 몇개 나오는지
    chk.append(S[i:i+3])
    
two_letters = chk.count("dz=")+chk.count("lj")+chk.count("nj")
print(two_letters)
result = len(S) - two_letters - S.count("=") - S.count("-")

print(len(S))
print(two_letters)
print(S.count("="))
print(S.count("-"))
print(result)


### 킹 갓 제너럴 갓이썬 replace
### 개지리네

## a = input()
## croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
## for i in croatia:
##     if i in a:
##         a = a.replace(i,'0')
## print(len(a))