# 모든 지점에서 다른 모든 지점까지의 최단 경로를 구해야 하는 경우
import sys
input = sys.stdin.readline

INF = int(1e9)

#n = int(input())
n = 4

#m = int(input())
m = 7

# graph = [[INF]* (n+1) for i in range(n+1)]
# # 자기 자신에서 자기 자신으로 갖는 비용은 0으로 초기화
# for a in range(1,n+1):
#     for b in range(1,n+1):
#         if a == b:
#             graph[a][b] = 0
            
# # 각 간선에 대한 정보를 입력받아, 그 값으로 초기화
# for i in range(m):
#     # A에서 B로가는 비용을 C라고 설정
#     a,b,c = map(int,input().split())
#     graph[a][b] = c
    
graph = [[1000000000, 1000000000, 1000000000, 1000000000, 1000000000], [1000000000, 0, 4, 1000000000, 6], [1000000000, 3, 0, 7, 1000000000], [1000000000, 5, 1000000000, 0, 4], [1000000000, 1000000000, 1000000000, 2, 0]]

# 점화식에 따라 플로이드 워셜 알고리즘 수행
for i in range(1,n+1):
    for j in range(1,n+1):
        for k in range(1,n+1):
            graph[j][k] = min(graph[j][k],graph[j][i]+graph[i][k])
            

# 수행된 결과물을 출력
for i in range(1,n+1):
    for j in range(1,n+1):
        # 도달할 수 없는 경우
        if graph[i][j] == INF:
            print("INFINITY",end=' ')
        # 도달할 수 있는 경우
        else:
            print(graph[i][j],end=' ')
    print()
    
    
