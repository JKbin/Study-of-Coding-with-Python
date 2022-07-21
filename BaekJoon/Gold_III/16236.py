from collections import deque
import sys

input = sys.stdin.readline

n = int(input().rstrip())
graph = []

for _ in range(n):
    graph.append(list(map(int,input().rstrip().split())))
    
dx = [-1,1,0,0]
dy = [0,0,-1,1]

now_size = 2
now_x,now_y = 0,0

# 아기 상어 위치 찾기
for i in range(n):
    for j in range(n):
        if graph[i][j] == 9:
            now_x,now_y = i,j
            graph[i][j] = 0
            

# 각 거리의 최단거리 찾기
def bfs():
    dist = [[-1]*n for i in range(n)]
    q = deque()
    q.append((now_x,now_y))
    
    dist[now_x][now_y] = 0
    
    while q:
        x,y = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0<=nx<n and 0<=ny<n and dist[nx][ny] == -1 and graph[nx][ny] <= now_size:
                dist[nx][ny] = dist[x][y] + 1
                q.append((nx,ny))
    return dist

                

# 먹을 수 있는 물고기 찾기
def find(dist):
    tmp = []
    for i in range(n):
        for j in range(n):
            if graph[i][j] >= 1 and graph[i][j] < now_size and dist[i][j] != -1:    # 물고기가 있어야하며, 크기는 작고, 도달가능한 지점에서만 찾기
                tmp.append((i,j,dist[i][j]))
    
    if not tmp:
        return None
    else:           
        tmp.sort(key=lambda x:(x[2],x[0],x[1]))
        z = tmp[0]
        return z[0],z[1],z[2]

                
                
    
res = 0
ate = 0

while True:
    
    value = find(bfs())
    
    if not value:
        print(res)
        break
    else:
        res += value[2]         # 거리 더하기(= 시간더하기)
        ate += 1            
        
        now_x,now_y = value[0],value[1]     # 먹은자리 = 현재위치로 변경
        graph[now_x][now_y] = 0       # 먹은자리 초기화
        
    if ate >= now_size:                     # 사이즈변경
        now_size += 1
        ate = 0
        
        
    
    
    

