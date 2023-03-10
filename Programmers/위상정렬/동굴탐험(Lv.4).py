from collections import deque

# BFS를 통해 새로운 단방향 그래프 정의
def bfs(n, graph, indegree):
    visited = [False] * (n)
    visited[0] = True
    q = deque()
    q.append(0)
    new_graph = [[]for i in range(n)]
    
    while q:
        now = q.popleft()
        
        for i in graph[now]:
            if not visited[i]:
                new_graph[now].append(i)
                q.append(i)
                visited[i] = True
                indegree[i] += 1
    
    return new_graph, indegree

def topology_sort(new_graph, indegree):
    res = []
    q = deque()
    
    for i in range(len(indegree)):
        if indegree[i] == 0:
            q.append(i)
    
    while q:
        now = q.popleft()
        res.append(now)
        
        for i in new_graph[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)
                
    return len(res)
    
def solution(n, path, order):
    answer = True
    graph = [[]for i in range(n)]
    # 차수 초기화
    indegree = [0] * n  
    
    # 양방향 그래프 정의
    for i in path:
        a,b = i
        graph[a].append(b)
        graph[b].append(a)
    
    # BFS를 통해 단방향 그래프로 변환
    new_graph, indegree = bfs(n, graph, indegree)
    
    # 우선순위가 있는 노드 연결 및 차수 늘리기
    for i in order:
        a,b = i
        new_graph[a].append(b)
        indegree[b] += 1
    
    if n == topology_sort(new_graph, indegree):
        return True
    return False



