import sys
from collections import deque

# BFS, 조건 조금 까다로움
# 행, 열 처리 잘할 것 (IndexError)

input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
graph = []
for _ in range(n):
    graph.append(list(input().rstrip()))

#n,m = 4, 4
#graph = [['#', '#', '#', '#'], ['#', 'J', 'F', '#'], ['#', '.', '.', '#'], ['#', '.', '.', '#']]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

jihoon = None
fires = []
ans = sys.maxsize

for i in range(n):
    for j in range(m):
        if graph[i][j] == 'J':      # 지훈이
            jihoon = [i, j, 0]
        if graph[i][j] == 'F':      # 불
            fires.append([i, j, 0])
            
q = deque()
q.append(jihoon)
for f in fires:
    q.append(f)
    

while q:
    x,y,cnt = q.popleft()
    cur = graph[x][y]
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        # 범위 내
        if 0<=nx<n and 0<=ny<m:
            if graph[nx][ny] != '#':
                if cur == 'J':       # 지훈
                    if graph[nx][ny] == '.':
                        q.append((nx,ny,cnt+1))
                        graph[nx][ny] = 'J'
                elif cur == 'F' and graph[nx][ny] != 'F' and graph[nx][ny] != '#':
                    q.append((nx,ny,0))
                    graph[nx][ny] = 'F'
        else:
            if cur == 'J':
                ans = min(cnt+1, ans)
        

print(ans) if ans != sys.maxsize else print('IMPOSSIBLE')