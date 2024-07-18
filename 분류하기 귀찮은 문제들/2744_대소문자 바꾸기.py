n = input()
for _ in range(len(n)):
    if ord(n[_]) >96:
        print(chr(ord(n[_])-32),end="")
    else:
        print(chr(ord(n[_])+32),end="")