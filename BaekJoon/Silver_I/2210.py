from collections import deque
import sys
input = sys.stdin.readline

graph = []
dx = [-1,1,0,0]
dy = [0,0,-1,1]

for _ in range(5):
    graph.append(list(map(int,input().rstrip().split())))
    
result = set()

def bfs(a,b,c):
    q = deque()
    q.append([a,b,c,1])
    
    
    while q:
        T = q.popleft()
        x = T[0]
        y = T[1]
        s = T[2]
        cnt = T[3]
        
        if cnt == 6:
            result.add(s)
            continue
            
            
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0<=nx<5 and 0<=ny<5:
                ns = s + str(graph[nx][ny])
                q.append([nx,ny,ns,cnt+1])
                    
            
        
for i in range(5):
    for j in range(5):
        bfs(i,j,str(graph[i][j]))
        
print(len(result))

        

        
    
    



