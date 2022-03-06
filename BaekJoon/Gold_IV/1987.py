from collections import deque
from sys import stdin


# m,n = 3,6
# graph = [['H', 'F', 'D', 'F', 'F', 'B'], ['A', 'J', 'H', 'G', 'D', 'H'], ['D', 'G', 'A', 'G', 'E', 'H']]
# m,n = 2,4
# graph = [['C','A','A','B'],['A','D','C','B']]

m,n = map(int,stdin.readline().rstrip().split())
graph = []
for i in range(m):
    graph.append(list(map(str,stdin.readline().rstrip())))
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs():
    result = 1
    
    q = set()               # 시간초과로 인해 deque 대신 set으로 사용
    q.add((0,0,graph[0][0]))
    #q.append((0,0,graph[0][0]))
    
    while q:
        x,y,alpha = q.pop()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            
            if 0<=nx<m and 0<=ny<n:
                nz = graph[nx][ny]
                if nz not in alpha:
                    q.add((nx,ny,alpha+nz))
                    #q.append((nx,ny,alpha+nz))
                    result = max(result,len(alpha+nz))
    return result
        
        


print(bfs())




    
    