from copy import deepcopy
import sys

input = sys.stdin.readline


n = 4
dx = [-1,-1,0,1,1,1,0,-1]
dy = [0,-1,-1,-1,0,1,1,1]

graph = [[None]*n for i in range(n)]
for i in range(n):
    data = list(map(int,input().rstrip().split()))
    for j in range(n):
        graph[i][j] = [data[j*2],data[j*2+1]-1]

# graph = [[[7, 5], [2, 2], [15, 5], [9, 7]], [[3, 0], [1, 7], [14, 6], [10, 0]], [[6, 0], [13, 5], [4, 2], [11, 3]], 
# [[16, 0], [8, 6], [5, 1], [12, 1]]]

res = 0         # 최종결과

# 물고기 위치 찾기
def search_fish(graph,index):
    for i in range(n):
        for j in range(n):
            if graph[i][j][0] == index:
                return (i,j)

# 물고기 움직이기
def move_fish(graph,now_x,now_y):
    for i in range(1,17):
        positions = search_fish(graph,i)
        if positions != None:
            fish_x,fish_y = positions[0],positions[1]
            fish_dir = graph[fish_x][fish_y][1]     # 물고기의 방향

            for idx in range(8):
                next_x = fish_x + dx[fish_dir]
                next_y = fish_y + dy[fish_dir]

                if 0<=next_x<n and 0<=next_y<n:
                    if not (next_x == now_x and next_y == now_y):
                        graph[fish_x][fish_y][1] = fish_dir
                        graph[fish_x][fish_y], graph[next_x][next_y] = graph[next_x][next_y],graph[fish_x][fish_y]
                        break
                fish_dir = (fish_dir + 1) % 8
                
                
# 상어가 움직일 수 있는 공간 찾기 
def shark_move(graph,now_x,now_y,shark_dir):
    tmp = []
    for i in range(4):
        now_x += dx[shark_dir]
        now_y += dy[shark_dir]
        if 0<=now_x<n and 0<=now_y<n and graph[now_x][now_y][0] != -1:
            tmp.append((now_x,now_y))
    return tmp
          
          
            
def dfs(graph,now_x,now_y,total):
    global res
    graph = deepcopy(graph)
    shark_dir = graph[now_x][now_y][1]
    total += graph[now_x][now_y][0]
    graph[now_x][now_y][0] = -1             # 상어가 먹었다는 것을 표시
    
    move_fish(graph,now_x,now_y)
    positions = shark_move(graph,now_x,now_y,shark_dir)
    
    # 상어가 움직일 수 있는 공간이 없으면 종료
    if not positions:
        res = max(res,total)
        return
    
    # 상어가 움직일 수 있는 공간만큼 재귀적으로 수행
    for x,y in positions:
        dfs(graph,x,y,total)
    


dfs(graph,0,0,0)
print(res)







        
        
    
    
    



    