import sys
from collections import deque

dx = [-1,1,0,0]
dy = [0,0,-1,1]

input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
graph = []
for _ in range(2**n):
    graph.append(list(map(int, input().rstrip().split())))
q = list(map(int, input().rstrip().split()))

# 배열 회전
def rotate(graph, n, a):
    n_size = 2**n
    r_size = 2**a
    result = [[0 for _ in range(n_size)] for _ in range(n_size)]
    for x in range(0, n_size, r_size):
        for y in range(0, n_size, r_size):
            for i in range(r_size):
                for j in range(r_size):
                    #result[j][n-i-1] = graph[i][j]
                    result[j+x][y+r_size-i-1] = graph[i+x][y+j]
    return result

# 인접한 칸의 얼음이 3칸 미만인 얼음들의 좌표 찾기
def ice_break(a, b, graph):
    q = deque()
    q.append((a, b))
    cnt = 0
    
    for i in range(4):
        nx = a + dx[i]
        ny = b + dy[i]
        
        if 0<=nx<n_size and 0<=ny<n_size:
            if graph[nx][ny] > 0:
                cnt += 1
    
    if cnt >= 3:
        return True
    return False

# 최대 연결 된 얼음 찾기
def bfs(a, b):
    global sumValue
    q = deque()
    q.append((a,b))
    visited[a][b] = 1
    cnt = 1
    
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0<=nx<n_size and 0<=ny<n_size and graph[nx][ny] > 0 and not visited[nx][ny]:
                q.append((nx, ny))
                visited[nx][ny] = 1
                cnt += 1
                sumValue += graph[nx][ny]
    return cnt
    
    
    
n_size = 2**n
for i in q:
    graph = rotate(graph, n, i)
    
    # 인접한 칸의 얼음이 3칸 미만인 얼음들의 좌표 찾기
    minus = []
    for i in range(n_size):
        for j in range(n_size):
            if graph[i][j] > 0:
                if not ice_break(i, j, graph):
                    minus.append([i, j])
    
    for _x, _y in minus:
        if graph[_x][_y] > 0:
            graph[_x][_y] -= 1

# 얼음의 총합        
sumValue = 0
# 가장 큰 얼음 덩어리 
bigIce = 0
visited = [[0 for _ in range(n_size)] for _ in range(n_size)]
for i in range(n_size):
    for j in range(n_size):
        if graph[i][j] > 0:
            if visited[i][j] == 0:
                sumValue += graph[i][j]
                bigIce = max(bfs(i, j), bigIce)

print(sumValue)
print(bigIce)
