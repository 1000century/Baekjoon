# (유경)
def solution(m, musicinfos):
    m = exit_star(m)
    musicinfos = [x.split(',') for x in musicinfos]

    new = []
    print(musicinfos)

    for music in musicinfos:
        name = music[2] # 제목
        # 재생시간
        length = int(music[1][:2])*60 + int(music[1][3:]) - (int(music[0][:2])*60 + int(music[0][3:]))
        # 악보
        music_3 = exit_star(music[3])
        paper = music_3 * (length // len(music_3)) + music_3[:length%len(music_3)+1]
        new.append([name, length,paper])

    answer = []
    for i in range(len(new)):
        if m in new[i][2]:
            answer.append(new[i])
    answer = sorted(answer, key = lambda x : (-x[1]))

    if not answer:
        return '(None)'
    else:
        return answer[0][0]

# 음에 #이 있다면 소문자로 바꿔줌
def exit_star(string):
    if '#' not in string:
        return string
    answer = ''
    for i in range(len(string)):
        if string[i] == '#':
            answer = answer[:-1]+answer[-1].lower()
        else:
            answer += string[i]
    return answer
