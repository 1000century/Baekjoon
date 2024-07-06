def solution(food):
    answer = '1'
    dic = []
    for i in range(1,len(food)):
        dic.append(food[i],i)
    dic.sort()
    print(dic)
    for i in range(1,len(food)):
        answer = answer + str(i+1)*(food[i])
    return answer
food = [1,3,4,6]
solution(food)