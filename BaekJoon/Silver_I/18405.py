from collections import deque
import sys
input = sys.stdin.readline

n,k = map(int,input().rstrip().split())
graph = []
for i in range(n):
    graph.append(list(map(int,input().rstrip().split())))
second,a,b = map(int,input().rstrip().split())

# n,k = 3,3
# graph = [[1, 0, 2], [0, 0, 0], [3, 0, 0]]
# second,a,b = 2,3,2

dx = [-1,1,0,0]
dy = [0,0,-1,1]


data = []


for i in range(n):
    for j in range(n):
        if graph[i][j] != 0:
            data.append((graph[i][j],0,i,j))
            
data.sort()

q = deque(data)

while q:
    
    virus,sec,x,y = q.popleft()
    
    if sec == second:
        break
    
    for i in range(4):
        nx = x + dx[i] 
        ny = y + dy[i]
        
        if 0<=nx<n and 0<=ny<n and graph[nx][ny] == 0:
            graph[nx][ny] = virus
            q.append((virus,sec+1,nx,ny))

print(graph[a-1][b-1])
            
