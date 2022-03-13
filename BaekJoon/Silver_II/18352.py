from collections import deque
import sys

input = sys.stdin.readline
n,m,k,x = map(int,input().rstrip().split())
#n,m,k,x = 4,4,2,1

graph = [[] for i in range(n+1)]
for i in range(m):
    a,b = map(int,input().rstrip().split())
    graph[a].append(b)
    
#graph = [[], [2, 3], [3, 4], [], []]


distance = [-1] * (n+1)

q = deque([x])
distance[x] = 0

while q:
    
    c = q.popleft()
    
    for i in graph[c]:
        if distance[i] == -1:
            distance[i] = distance[c] + 1
            q.append(i)
            

if k not in distance:
    print(-1)
else:
    for i in range(len(distance)):
        if distance[i] == k:
            print(i)

    
