# BFS, visited 3차원 배열로 활용 (dp)
import sys
from collections import deque

input = sys.stdin.readline

n, m, k = map(int, input().rstrip().split())
graph = []
for _ in range(n):
    graph.append(list(map(int,input().rstrip())))

# n, m, k = 6, 4, 2
# graph = [[0, 1, 0, 0], [1, 1, 1, 0], [1, 0, 0, 0], [0, 0, 0, 0], [0, 1, 1, 1], [0, 0, 0, 0]]

# k+1만큼 [0] 배열 만들기 (방문처리 및 dp 활용)
# k = 2라면 [0, 0, 0] 이런 식으로 [0, 0, 0]의 
# 0번째 index는 0번 벽을 부쉈을 때의 경로
# 1번째 index는 1번 벽을 부쉈을 때의 경로
# 2번째 index는 2번 벽을 부쉈을 때의 경로를 나타낸다.

visited = [[[0]*(k+1) for _ in range(m)] for _ in range(n)]


dx = [-1,1,0,0]
dy = [0,0,-1,1]


def bfs(a, b):
    q = deque()
    q.append((a,b,0))
    visited[a][b][0] = 1        # start_x, start_y, 처음 벽을 부순 횟수 = 0 (0, 0, 0)
    
    while q:
        x,y,cnt = q.popleft()
        
        if [x,y] == [n-1,m-1]:
            return visited[x][y][cnt]
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0<=nx<n and 0<=ny<m:
                # 다음 step이 벽이고, 벽을 부순 횟수가 k 보다 작고, 
                # visited[nx][ny][cnt+1] == 다음 스텝의 방문 여부가 없을 때(0) 방문한다.
                if graph[nx][ny] == 1 and cnt < k and visited[nx][ny][cnt+1] == 0:
                    visited[nx][ny][cnt+1] = visited[x][y][cnt] + 1
                    q.append((nx,ny,cnt+1)) 
                    
                # 다음 step이 벽이 아니고, 
                # visited[nx][ny][cnt] == 다음 스텝의 방문 여부가 없을 때(0) 방문한다.
                elif graph[nx][ny] == 0 and visited[nx][ny][cnt] == 0:
                    visited[nx][ny][cnt] = visited[x][y][cnt] + 1
                    q.append((nx,ny,cnt)) 
    return -1
                
    
                    
print(bfs(0,0))





