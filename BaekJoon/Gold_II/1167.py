# DFS 두 번 돌리기
# 1. 1번 노드를 기준으로 가장 먼 노드 찾기
# 2. 찾은 노드를 기준으로 가장 먼 노드의 거리 찾기


import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input().rstrip())
graph = [[]for _ in range(n+1)]
for _ in range(n):
    data = list(map(int, input().rstrip().split()))
    node = data[0]
    l = data[1:-1]
    for i in range(0, len(l),2 ):
        graph[node].append((l[i], l[i+1]))

#n = 5
#graph = [[], [(3, 2)], [(4, 4)], [(1, 2), (4, 3)], [(2, 4), (3, 3), (5, 6)], [(4, 6)]]

def dfs(now, weight):
    for next_node, cost in graph[now]:
        if dist[next_node] == -1:
            dist[next_node] = cost + weight
            dfs(next_node, cost+weight)
            
dist = [-1] * (n+1)
dist[1] = 0
dfs(1, 0)

maxIdx = dist.index(max(dist))
dist = [-1] * (n+1)
dist[maxIdx] = 0
dfs(maxIdx, 0)

print(max(dist))

