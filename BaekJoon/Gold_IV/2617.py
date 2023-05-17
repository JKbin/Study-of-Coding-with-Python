# 현재 노드의 자식노드의 개수 구하기
# 자식 노드의 개수가 mid보다 같거나 많으면 중간 무게가 절대로 될 수 없음

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n, m = map(int, input().rstrip().split())

bigger_list = [[]for _ in range(n+1)]
smaller_list = [[]for _ in range(n+1)]
mid = (n+1)/2

for _ in range(m):
    a, b = map(int, input().rstrip().split())
    bigger_list[b].append(a)
    smaller_list[a].append(b)

def dfs(graph, now):
    global sonNode
    for next_node in graph[now]:
        if not visited[next_node]:
            visited[next_node] = True
            sonNode += 1
            dfs(graph, next_node)
    
    
answer = 0
for i in range(1, n+1):
    visited = [False] * (n+1)
    #bigger
    sonNode = 0
    dfs(bigger_list, i)
    if sonNode >= mid:
        answer += 1
    #smaller
    sonNode = 0
    dfs(smaller_list, i)
    if sonNode >= mid:
        answer += 1
print(answer)
    
    


        
    
    
        
        








