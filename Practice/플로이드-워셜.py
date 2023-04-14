# 모든 지점에서 다른 모든 지점까지의 최단 경로를 구해야 하는 경우
# BOJ 11404

import sys
input = sys.stdin.readline

INF = int(1e9)

n = int(input().rstrip())
m = int(input().rstrip())

graph = [[INF]*(n+1) for i in range(n+1)]

# 자기 자신으로 가는 비용 0으로 초기화
for i in range(1, n+1):
    for j in range(1, n+1):
        if i == j:
            graph[i][j] = 0

for _ in range(m):
    a, b, cost = map(int, input().rstrip().split())
    # 가장 짧은정보만 저장
    if cost < graph[a][b]:
        graph[a][b] = cost


# 플로이드-워셜 알고리즘
for i in range(1, n+1):
    for j in range(1, n+1):
        for k in range(1, n+1):
            graph[j][k] = min(graph[j][k], graph[j][i]+graph[i][k]) 

for i in range(1, n+1):
    for j in range(1, n+1):
        if graph[i][j] == INF:
            print(0, end=' ')
        else:
            print(graph[i][j], end=' ')
    print()


        
    
    
