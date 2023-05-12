# Lowest Common Ancestor

# BOJ 심화 : 11438

# 최소 공통 조상 찾기 알고리즘은 다음과 같다.
# 1. 모든 노드에 대한 깊이(depth)을 계산한다.
# 2. 최소 공통 조상을 찾을 두 노드를 확인한다.
#   2-1. 먼저 두 노드의 깊이(depth)가 동일하도록 거슬러 올라간다.
#   2-2. 이후에 부모가 같아질 때까지 반복적으로 두 노드의 부모 방향으로 거슬러 올라간다.
# 3. 모든 LCA(a,b) 연산에 대하여 2번의 과정을 반복한다.

# 시간복잡도 : O(NM)

import sys
sys.setrecursionlimit(10**6)
LOG = 21            # 2^20 = 1_000_000
input = sys.stdin.readline

n = int(input().rstrip())

graph = [[]for i in range(n+1)]
parent = [[0]*(LOG) for _ in range(n+1)]        # 부모 노드 정보
d = [0] * (n+1)                                 # 각 노드까지의 깊이
c = [0] * (n+1)                                 # 각 노드의 깊이가 계산되었는지 여부

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
        parent[next][0] = x
        dfs(next, depth+1)

# 전체 부모 관계를 설정하는 함수
def set_parent():
    dfs(1, 0)
    for i in range(1, LOG):
        for j in range(1, n+1):
            parent[j][i] = parent[parent[j][i-1]][i-1]


# a와 b의 공통 조상을 찾는 함수
def lca(a, b):
    # b가 더 깊도록 설정
    if d[a] > d[b]:
        a, b = b, a
    # 먼저 깊이(depth)가 동일하도록
    for i in range(LOG-1, -1, -1):
        if d[b] - d[a] >= (1 << i):
            b = parent[b][i]
    
    # 부모가 같아지도록
    if a == b:
        return a
    for i in range(LOG-1, -1, -1):
        # 조상을 향해 거슬러 올라가기
        if parent[a][i] != parent[b][i]:
            a = parent[a][i]
            b = parent[b][i]
    
    # 이후에 부모가 찾고자 하는 조상
    return parent[a][0]
    
set_parent()

m = int(input().rstrip())

for i in range(m):
    a, b = map(int, input().rstrip().split())
    print(lca(a, b))
        
        
    
        

