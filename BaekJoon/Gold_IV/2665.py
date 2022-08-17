import heapq
import sys

input = sys.stdin.readline

dx = [-1,1,0,0]
dy = [0,0,-1,1]

# 흰방 : 1
# 검은방 : 0

n = int(input().rstrip())    
graph = []
for _ in range(n):
    graph.append(list(map(int,input().rstrip())))
    
    
visited = [[0]*n for i in range(n)]

q = []
heapq.heappush(q,(0,0,0))
visited[0][0] = 1

while q:
    cnt,x,y = heapq.heappop(q)
    
    if x == n-1 and y == n-1:
        print(cnt)
        break
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if 0<=nx<n and 0<=ny<n and visited[nx][ny] == 0:
            visited[nx][ny] = 1
            if graph[nx][ny] == 0:              # 검은방일 때 cnt + 1
                heapq.heappush(q,(cnt+1,nx,ny))
            else:
                heapq.heappush(q,(cnt,nx,ny))
                
                


