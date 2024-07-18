import os
problem_data = [
    {'step': 1, 'number': 27433, 'title': '팩토리얼 2', 'correct_ratio': 48.978},
    {'step': 2, 'number': 10870, 'title': '피보나치 수 5', 'correct_ratio': 61.277},
    {'step': 3, 'number': 25501, 'title': '재귀의 귀재', 'correct_ratio': 54.631},
    {'step': 4, 'number': 24060, 'title': '알고리즘 수업 - 병합 정렬 1', 'correct_ratio': 44.326},
    {'step': 5, 'number': 4779, 'title': '칸토어 집합'},
    {'step': 6, 'number': 2447, 'title': '별 찍기 - 10', 'correct_ratio': 54.848},
    {'step': 7, 'number': 11729, 'title': '하노이 탑 이동 순서', 'correct_ratio': 50.453}

]

# 파일 저장 디렉토리 경로
new_path = r"C:\Users\Sese\baekjun\19. 재귀"

for problem in problem_data:
    file_name = f"#{problem['step']}_{problem['number']}_{problem['title']}.py"
    file_path = os.path.join(new_path,file_name)

    with open(file_path,'w') as file:
        file.write
