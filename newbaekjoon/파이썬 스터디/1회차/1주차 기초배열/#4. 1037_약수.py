yaksu_num = int(input())
yaksu_list = list(map(int,input().split()))
yaksu_list.sort()

"""
양수 A가 N의 진짜 약수가 되려면 N이 A의 배수여야 하고 A는 1,N이 아니어야 함.
"""
print(yaksu_list[0]*yaksu_list[-1])