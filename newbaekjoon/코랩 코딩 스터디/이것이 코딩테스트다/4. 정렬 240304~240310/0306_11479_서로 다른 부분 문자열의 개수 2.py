
"""
3/6 16:56 ~ 18:45 하고 메모리초과....
"""
# part 1. 데이터 입력받기
def main():
    S = input()
    charleng(S)
    
# part 2. 들어가기에 앞서...
def custom_sort(char):
    # 접미사 배열을 인덱스로 생성
    suffix_array = list(range(len(char)))

    # 접미사를 사전순으로 정렬하기 위한 사용자 정의 키 함수
    # 이 함수는 각 인덱스에 대해 전체 문자열에서 해당 인덱스로 시작하는 접미사를 반환
    suffix_array.sort(key=lambda index: char[index:])

    return suffix_array

def calculate_lcp(char, suffix_array):
    lcp = 0
    for i in range(len(char) - 1):
        # 현재 접미사와 다음 접미사의 LCP 계산
        lcp_length = 0
        while (i + lcp_length < len(char) and
               suffix_array[i] + lcp_length < len(char) and
               suffix_array[i+1] + lcp_length < len(char) and
               char[suffix_array[i] + lcp_length] == char[suffix_array[i+1] + lcp_length]):
            lcp_length += 1
        lcp = lcp + lcp_length
    return lcp

# part 2. 함수 설정
def charleng(char):
    # step 1. 접미사 배열
    suffix_array = custom_sort(char)

    # step 2. longest common prefix 계산 (접미사가 아니라 접"두"사!!)
    # 접미사들의 접'두'사를 비교해서 겹치는 것이 몇개 인지 센다
    # ex) bana 랑 ana는 겹치는 게 0개, ex) anana랑 ana는 겹치는 게 3개
    lcp = calculate_lcp(char,suffix_array)
    
    # step 3. 최종 계산법은 >> n*(n+1)//2 + LCP들의 합
    # 이거 이해가 어렵다. 모르겠음 외우자.

    print(len(char)*(len(char)+1)//2-sum(lcp))


# part 3. 실행 함수
if __name__ == "__main__":
    main()
