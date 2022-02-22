import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())
m,k = map(int,sys.stdin.readline().rstrip().split())
s = int(sys.stdin.readline().rstrip())

check = [0] * (n+1)

graph = [[] for i in range(n+1)]
for i in range(s):
    a,b = map(int,sys.stdin.readline().rstrip().split())
    graph[a].append(b)
    graph[b].append(a)
    
    graph[a].sort()
    graph[b].sort()



def bfs(m):
    q = deque([m])
    
    while q:
        x = q.popleft()
        
        for i in graph[x]:
            if not check[i]:
                q.append(i)
                check[i] = check[x]+1
                


bfs(m)

answer = check[k]
if answer == 0:
    print(-1)
else:
    print(answer)