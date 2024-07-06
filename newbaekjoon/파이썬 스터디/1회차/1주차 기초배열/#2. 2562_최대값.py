def maxandindex(li):
    print(max(li))
    print(li.index(max(li))+1)


def main():
    # extend 메소드 vs 리스트 컴프리헨션
    # extend 메소드
    X = []
    for _ in range(9):
        X.extend(int(input()) for _ in range(9))
    # 리스트 컴프릿헨션
    X = [int(input()) for _ in range(9)]
    maxandindex(X)


if __name__ == "__main__":
    main()

