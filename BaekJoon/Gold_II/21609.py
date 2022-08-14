from collections import deque
import sys
input = sys.stdin.readline

dx = [-1,1,0,0]
dy = [0,0,-1,1]


n,m = map(int,input().rstrip().split())
graph = []
for _ in range(n):
    graph.append(list(map(int,input().rstrip().split())))


total_score = 0 


# 그룹 블록 찾기
def bfs(i,j,color):
    visited[i][j] = True
    q = deque()
    q.append((i,j))
    
    normal_blocks = []
    normal_blocks.append((i,j))
    rainbow_blocks = []
    
    while q:
        x,y = q.popleft()
        
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            
            if 0<=nx<n and 0<=ny<n and graph[nx][ny] != -1 and not visited[nx][ny]:
                if graph[nx][ny] == 0:                                  # 무지개블록
                    rainbow_blocks.append((nx,ny))
                    q.append((nx,ny))
                    visited[nx][ny] = True
                elif graph[nx][ny] == color:                            # 일반블록
                    normal_blocks.append((nx,ny))
                    q.append((nx,ny))
                    visited[nx][ny] = True
    
    for i in rainbow_blocks:                    # 무지개는 중복으로 가질 수 있기 때문에 visited False로 바꿔야함
        visited[i[0]][i[1]] = False
    
    if len(normal_blocks) + len(rainbow_blocks) >= 2:
        normal_blocks.sort()
        rainbow_blocks.sort()
        return normal_blocks+rainbow_blocks,len(rainbow_blocks)


    
# 가장 큰 그룹 블록 제거 
def remove(tmp,graph):
    arr = tmp[0]
    cnt = 0
    for x,y in arr:
        graph[x][y] = '#'
        cnt += 1
    return cnt**2


# 중력 
def gravity(i,j,num):
    x,y = i,j
    while True:
        nx = x + dx[1]
        ny = y + dy[1]
        
        if 0<=nx<n and 0<=ny<n:
            if graph[nx][ny] == '#':
                graph[nx][ny] = num
                graph[x][y] = '#'
                x,y = nx,ny
            elif graph[nx][ny] == -1:
                break
            else:
                break
        else:
            break

# 반시계 회전 
def rotate(graph):
    grp = [[0]*n for i in range(n)]
    for i in range(n):
        for j in range(n):
            grp[n-j-1][i] = graph[i][j]
    return grp
    
    

while True:
    visited = [[False]*n for i in range(n)]
    tmp = []
    for i in range(n):
        for j in range(n):
            if not visited[i][j] and graph[i][j] != '#':
                if graph[i][j] > 0:
                    value = bfs(i,j,graph[i][j])
                    if value:
                        tmp.append([value[0],value[1]])
                    
    if not tmp:
        break
    
    # 크기가 가장 큰 블록, 무지개 블록 개수, 행, 열 기준으로 정렬
    tmp.sort(key=lambda x: (-len(x[0]),-x[1],-x[0][0][0],-x[0][0][1] ))
    total_score += remove(tmp[0],graph)
    
    for i in range(n-2,-1,-1):
        for j in range(n):
            if graph[i][j] != -1 and graph[i][j] != '#':
                gravity(i,j,graph[i][j])
    graph = rotate(graph)
    for i in range(n-2,-1,-1):
        for j in range(n):
            if graph[i][j] != -1 and graph[i][j] != '#':
                gravity(i,j,graph[i][j])

print(total_score)

    
    
    
    
                
    
    
    
    
                    
                
                
            
    