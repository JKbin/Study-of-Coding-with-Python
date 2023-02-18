from collections import deque

n,m = map(int, input().rstrip().split())

indegree = [0] * (n+1)
graph = [[]for _ in range(n+1)]

for i in range(1, m+1):
    data = list(map(int ,input().rstrip().split()))
    # 차수 증가
    indegree[data[1]] += 1
    graph[data[0]].append(data[1])
    
def topology_sort():
    q = deque()
    result = []
    # 처음 차수가 0인 것 부터 큐에 넣기
    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)
    
    while q:
        now = q.popleft()
        result.append(now)
        
        for i in graph[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)
        
    return result

print(*topology_sort())

        
    
    
    
    
    