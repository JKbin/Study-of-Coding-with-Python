# 플로이드 워셜, pypy3로 제출(시간 복잡도 때문에)
# 자기 자신을 0으로 초기화 해주는 코드 없이 풀었음

import sys
INF = int(1e9)
input = sys.stdin.readline

n,m = map(int,input().rstrip().split())

graph = [[INF]*(n+1) for i in range(n+1)]    

for i in range(m):
    a,b,c = map(int,input().rstrip().split())
    graph[a][b] = c
    
for i in range(1, n+1):
    for j in range(1, n+1):
        for k in range(1, n+1):
            graph[j][k] = min(graph[j][k], graph[j][i] + graph[i][k])

        
res = INF

for i in range(1, n+1):
    res = min(res, graph[i][i])
    
print(-1) if res == INF else print(res)