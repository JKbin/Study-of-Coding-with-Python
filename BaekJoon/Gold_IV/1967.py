# DFS 2번 돌리기

import sys

sys.setrecursionlimit(10**6)

iuput = sys.stdin.readline

n = int(input().rstrip())
graph = [[]for i in range(n+1)]
for _ in range(n-1):
    a, b, c = map(int, input().rstrip().split())
    graph[a].append((b,c))
    graph[b].append((a,c))


#n = 12
#graph = [[], [(2, 3), (3, 2)], [(1, 3), (4, 5)], [(1, 2), (5, 11), (6, 9)], [(2, 5), (7, 1), (8, 7)], [(3, 11), (9, 15), (10, 4)], [(3, 9), (11, 6), (12, 10)], [(4, 1)], [(4, 7)], [(5, 15)], [(5, 4)], [(6, 6)], [(6, 10)]]

def dfs(now, weight):
    for next_node, cost in graph[now]:
        if dist[next_node] == -1:
            dist[next_node] = cost + weight
            dfs(next_node, weight+cost)

dist = [-1] * (n+1)
dist[1] = 0
# 루트 노드(1)에서 가장 거리가 먼 노드 찾기
dfs(1, 0)

# 루트 노드에서 가장 거리가 먼 노드(maxIndex)에서 또 거리가 가장 먼 노드(거리) 찾기
maxIndex = dist.index(max(dist))
dist = [-1] * (n+1)
dist[maxIndex] = 0
dfs(maxIndex, 0)
print(max(dist))






    




