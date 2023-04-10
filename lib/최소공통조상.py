# Lowest Common Ancestor

# BOJ (11437) -> 심화 : 11438

# 최소 공통 조상 찾기 알고리즘은 다음과 같다.
# 1. 모든 노드에 대한 깊이(depth)을 계산한다.
# 2. 최소 공통 조상을 찾을 두 노드를 확인한다.
#   2-1. 먼저 두 노드의 깊이(depth)가 동일하도록 거슬러 올라간다.
#   2-2. 이후에 부모가 같아질 때까지 반복적으로 두 노드의 부모 방향으로 거슬러 올라간다.
# 3. 모든 LCA(a,b) 연산에 대하여 2번의 과정을 반복한다.

# 시간복잡도 : O(NM)

import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline

n = int(input().rstrip())

graph = [[]for i in range(n+1)]
parent = [0] * (n+1)        # 부모 노드 정보
d = [0] * (n+1)             # 각 노드까지의 깊이
c = [0] * (n+1)             # 각 노드의 깊이가 계산되었는지 여부

for _ in range(n-1):
    a, b = map(int, input().rstrip().split())
    graph[a].append(b)
    graph[b].append(a)

# 루트 노드로부터 시작하여 depth를 구하는 함수
def dfs(x, depth):
    c[x] = True
    d[x] = depth
    
    for next in graph[x]:
        if c[next]:     # 이미 깊이를 구했다면 넘기기
            continue
        parent[next] = x
        dfs(next, depth+1)

# a와 b의 공통 조상을 찾는 함수
def lca(a, b):
    # 먼저 깊이(depth)가 동일하도록
    while d[a] != d[b]:
        if d[a] >= d[b]:
            a = parent[a]
        else:
            b = parent[b]
    
    # 노드가 같아지도록
    while a != b:
        a = parent[a]
        b = parent[b]
    return a

dfs(1, 0)

m = int(input().rstrip())

for i in range(m):
    a, b = map(int, input().rstrip().split())
    print(lca(a, b))
        
        
    
        

