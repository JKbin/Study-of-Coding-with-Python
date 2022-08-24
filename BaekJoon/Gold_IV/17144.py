from collections import deque
import sys

input = sys.stdin.readline
              
R,C,T = map(int,input().rstrip().split())
graph = []
for _ in range(R):
    graph.append(list(map(int,input().rstrip().split())))

dx = [-1,1,0,0]
dy = [0,0,-1,1]


vaccumes = []

for i in range(R):
    if graph[i][0] == -1:
        vaccumes.append([i,0])
        
# 미세먼지 확산
def diff(graph):
    grp = [[0]*C for i in range(R)]
    
    for i in range(R):
        for j in range(C):
            if graph[i][j] > 0:
                q = deque()
                q.append((i,j))
                tmp = []
                
                while q:
                    x,y = q.popleft()
                    
                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]
                        
                        if 0<=nx<R and 0<=ny<C:
                            if graph[nx][ny] != -1:
                                tmp.append([nx,ny])
                                
                if tmp:
                    for x1,y1 in tmp:
                        grp[x1][y1] += (graph[i][j] // 5)
                grp[i][j] += graph[i][j] - ((graph[i][j] // 5)*len(tmp)) 
    for v1,v2 in vaccumes:
        grp[v1][v2] = -1
    return grp
                

# 청소기 동작              
def fun(x1,y1,x2,y2,graph):
    # x1 : 헤더의 x , y1 : 헤더의 y
    # x2 : 테일의 x , y2 : 테일의 y
    # x1 : 2 / y1 : 0
    # x2 : 3 / y2 : 0
    # R : 행, C : 열
    
    tmp = [[0]*C for i in range(R)]
    
    # 헤더 아래
    for i in range(1,C-1):
        if graph[x1][i] > 0:
            tmp[x1][i+1] = graph[x1][i]
    # 헤더 오른쪽        
    for i in range(x1,0,-1):
        if graph[i][C-1] > 0:
            tmp[i-1][C-1] = graph[i][C-1]
    # 헤더 위쪽
    for i in range(C-1,0,-1):
        if graph[0][i] > 0:
            tmp[0][i-1] = graph[0][i]
    # 헤더 왼쪽
    for i in range(x1-1):
        if graph[i][0] > 0:
            tmp[i+1][0] = graph[i][0]
    
    
    # 테일 위쪽
    for i in range(1,C-1):
        if graph[x2][i] > 0:
            tmp[x2][i+1] = graph[x2][i]
    # 테일 오른쪽
    for i in range(x2,R-1):
        if graph[i][C-1] > 0:
            tmp[i+1][C-1] = graph[i][C-1]
    # 테일 아래쪽
    for i in range(C,1,-1):
        if graph[R-1][i-1] > 0:
            tmp[R-1][i-2] = graph[R-1][i-1]
    # 테일 왼쪽
    for i in range(R-1,x2+1,-1):
        if graph[i][0] > 0:
            tmp[i-1][0] = graph[i][0]
            
    # 처음과 헤더의 사이값 갱신
    for i in range(1,x1):
        for j in range(1,C-1):
            tmp[i][j] = graph[i][j]
            
    # 테일과 끝의 사이값 갱신
    for i in range(x2+1,R-1):
        for j in range(1,C-1):
            tmp[i][j] = graph[i][j]
    
    for v1,v2 in vaccumes:
        tmp[v1][v2] = -1
    return tmp
    
    
def sum_graph(graph):
    res = 0
    for i in range(R):
        for j in range(C):
            if graph[i][j] > 0:
                res += graph[i][j]
    return res
                

for _ in range(T):
    graph = diff(graph)
    graph = fun(vaccumes[0][0],vaccumes[0][1],vaccumes[1][0],vaccumes[1][1],graph)
print(sum_graph(graph))

    
    

