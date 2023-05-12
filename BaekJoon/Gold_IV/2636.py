# 가장자리(0)을 q에 넣고 bfs

import sys
from collections import deque

input = sys.stdin.readline

dx = [-1,1,0,0]
dy = [0,0,-1,1]

n, m = map(int, input().rstrip().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().rstrip().split())))


time = 0
ans = []

def bfs():
    q = deque()
    q.append([0,0])
    visited[0][0] = 1
    
    count = 0
    
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0<=nx<n and 0<=ny<m and visited[nx][ny] == 0:
                # 빈 공간인 경우, 가장 자리만 필요하므로 q에 넣기
                if graph[nx][ny] == 0:
                    visited[nx][ny] = 1
                    q.append([nx,ny])
                # 치즈인 경우
                elif graph[nx][ny] == 1:
                    visited[nx][ny] = 1
                    # 공기 접촉했으니 0으로 변환
                    graph[nx][ny] = 0   
                    count += 1
    return count
                    
while 1:
    time += 1
    visited = [[0 for _ in range(m)] for _ in range(n)]
    cnt = bfs()
    if cnt == 0:
        break
    else:
        ans.append(cnt)

print(time-1)
print(ans[-1])
