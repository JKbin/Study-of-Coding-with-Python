import sys

input = sys.stdin.readline
n,m = map(int,input().rstrip().split())

INF = int(1e9)

graph=[[INF]*(n+1) for i in range(n+1)]

for i in range(1,n+1):
    for j in range(1,n+1):
        if i == j:
            graph[i][j] = 0
            
for i in range(m):
    a,b = map(int,input().rstrip().split())
    graph[a][b] = 1
    

for i in range(1,n+1):
    for j in range(1,n+1):
        for k in range(1,n+1):
            graph[j][k] = min(graph[j][k], graph[j][i] + graph[i][k])
            
            
res = 0 

for i in range(1,n+1):
    cnt = 0
    for j in range(1,n+1):
        if graph[i][j] != INF or graph[j][i] != INF:
            cnt += 1
    if cnt == n:
        res += 1
        
print(res)


    
