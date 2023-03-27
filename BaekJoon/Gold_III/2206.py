# BFS, visited를 3차원 배열로 관리

import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
graph = []
for _ in range(n):
    graph.append(list(map(int,input().rstrip())))

# n, m = 6, 4
# graph = [[0, 1, 0, 0], [1, 1, 1, 0], [1, 0, 0, 0], [0, 0, 0, 0], [0, 1, 1, 1], [0, 0, 0, 0]]

# [0, 0]    
# index 0은 벽을 안 부순 경우
# index 1은 벽을 부순 경우

visited = [[[0,0] for i in range(m)] for _ in range(n)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]


def bfs(a, b):
    q = deque()
    q.append((a,b,0))
    visited[a][b][0] = 1
    
    while q:
        x,y,cnt = q.popleft()
        
        if [x,y] == [n-1,m-1]:
            return visited[x][y][cnt]
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0<=nx<n and 0<=ny<m:
                # 다음 step이 벽이고, 아직 벽을 안 부순 경우
                if graph[nx][ny] == 1 and cnt == 0:
                    q.append((nx, ny, 1))
                    visited[nx][ny][cnt+1] = visited[x][y][cnt] + 1
                # 다음 step이 벽이 아니고, 아직 방문하지 않은 경우
                elif graph[nx][ny] == 0 and visited[nx][ny][cnt] == 0:
                    visited[nx][ny][cnt] = visited[x][y][cnt] + 1  
                    q.append((nx, ny, cnt))
    return -1
                    
print(bfs(0,0))



