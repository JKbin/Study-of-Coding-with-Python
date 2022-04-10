import sys

input = sys.stdin.readline

n = int(input().rstrip())
m = int(input().rstrip())

INF = int(1e9)

graph = [[INF]*(n+1) for i in range(n+1)]

for i in range(1,n+1):
    for j in range(1,n+1):
        if i == j:
            graph[i][j] = 0
            
for _ in range(m):
    c,d = map(int,input().rstrip().split())
    graph[c][d] = 1
    
            
            
for i in range(1,n+1):
    for j in range(1,n+1):
        for k in range(1,n+1):
            graph[j][k] = min(graph[j][k],graph[j][i]+graph[i][k])
            


res = []
        
for i in range(1,n+1):
    cnt = 0
    for j in range(1,n+1):
        if graph[i][j] != INF or graph[j][i] != INF:
            cnt += 1
    res.append(n-cnt)
    
for i in res:
    print(i)
    

    
            
            
            
