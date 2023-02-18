from collections import deque
import copy

n = int(input().rstrip())

indegree = [0] * (n+1)
graph = [[] for _ in range(n+1)]
times = [0] * (n+1)

for i in range(1, n+1):
    data = list(map(int, input().rstrip().split()))
    times[i] = data[0]
    
    for k in data[1:-1]:
        indegree[i] += 1
        graph[k].append(i)


def topology_sort():
    # 차수가 0인거 큐에 넣기
    time_table = copy.deepcopy(times)
    
    q = deque()
    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)
    
    while q:
        now = q.popleft()
        
        for i in graph[now]:
            time_table[i] = max(time_table[i], times[i]+time_table[now])
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)
    
    for i in range(1, n+1):
        print(time_table[i])

topology_sort()

    

        
