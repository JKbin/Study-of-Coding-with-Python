from collections import deque
import sys
import copy

n = int(input().rstrip())    

graph = [[]for _ in range(n+1)]
indegree = [0] * (n+1)
times = [0] * (n+1)


for i in range(1, n+1):
    data = list(map(int, input().rstrip().split()))
    times[i] = data[0]
    chasoo = data[1]
    indegree[i] = chasoo
    
    for j in data[2:]:
        graph[j].append(i)
    

def topology_sort():
    q = deque()
    time_table = copy.deepcopy(times)
    
    # 차수가 0인 거 넣기
    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)
            
    while q:
        now = q.popleft()
        
        for i in graph[now]:
            # 차수 - 1
            indegree[i] -= 1
            time_table[i] = max(time_table[i], time_table[now]+times[i])
            if indegree[i] == 0:
                q.append(i)
    return max(time_table)

print(topology_sort())
                
    
    
    
    

