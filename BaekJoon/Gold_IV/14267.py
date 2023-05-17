# DFS

import sys

sys.setrecursionlimit(10**6)

iuput = sys.stdin.readline

n, m = map(int, input().rstrip().split())

s = list(map(int, input().rstrip().split()))
graph = [[] for _ in range(n+1)]
answer = [0] * (n+1)

# 직속 관계 그래프 만들기
for i in range(1, n):
    graph[s[i]].append(i+1)

# 미리 먼저 칭찬더해주기
for i in range(m):
    a, b = map(int, input().rstrip().split())
    answer[a] += b

def dfs(now):
    for next_node in graph[now]:
        answer[next_node] += answer[now]
        dfs(next_node)
        
# 1번부터 방문 하면서 상사의 칭찬들을 나한테 더하기
dfs(1)

print(*answer[1:])




