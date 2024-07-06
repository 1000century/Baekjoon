def caesar(line,N):
    for i in list(line):
        if i =='A':
            print("X", end  = "")
        elif i =='B':
            print("Y", end  = "")
        elif i =='C':
            print("Z", end  = "")
        else:
            print(chr(ord(i)-N),end="")
    print()

def main():
    X = input()
    caesar(X,3)

if __name__ == "__main__":
    main()

## import 어쩌구 하는 게 있음
