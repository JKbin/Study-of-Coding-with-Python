from collections import deque
from sys import stdin



t = list(map(int,stdin.readline().rstrip().split()))


F = t[0]    # 총 건물의 층
S = t[1]    # 현재 위치
G = t[2]    # 도착 위치
U = t[3]    # up
D = t[4]    # down
visited = [False] * (F+1)


def bfs(F,S,G,U,D,visited):
    
    q = deque()
    q.append((S,0))
    
    while q:
        
        x,cnt = q.popleft()
        
        if x == G:
            return cnt
        
        if visited[x] == False:
            if x+U <= F:
                visited[x] = True
                q.append((x+U,cnt+1))
            if x-D >= 1:
                visited[x] = True
                q.append((x-D,cnt+1))
    else:
        return 'use the stairs'
    

print(bfs(F,S,G,U,D,visited))

        
    
    
    
    
    
