## 모르겠다 

def dfs(graph, x,y,alpha,visited,count=1):
    global M
    visited[alpha] = 1
    for next in [[x+1,y],[x,y+1],[x-1,y],[x,y-1]]:
        try:
            x,y,alpha= direction(graph,next)
            if visited[alpha] == 0:
                count = count + 1
                dfs(graph, x,y,alpha,visited,count)
                M = max(M,count)
                print(visited,count,M)

        except:
            M = max(M,count)
            continue

def main():
    R, C = map(int, input().split())
    graph = [input() for _ in range(R)]  # 문자열로 그래프의 각 행을 입력받음
    visited = {'A':0, 'B':0,'C':0, 'D':0, 'E':0, 'F':0, 'G':0, 'H':0, 'I':0, 'J':0, 'K':0, 'L':0, 'M':0, 'N':0, 'O':0, 'P':0, 'Q':0, 'R':0, 'S':0, 'T':0, 'U':0, 'V':0, 'W':0, 'X':0, 'Y':0, 'Z':0}
    start = [0,0]
    x,y,alpha = direction(graph,start)
    dfs(graph,x,y,alpha,visited)
    print(M)

def direction(graph,point):
    return [point[0], point[1], graph[point[1]][point[0]]]

if __name__ == "__main__":
    M = 1
    main()
