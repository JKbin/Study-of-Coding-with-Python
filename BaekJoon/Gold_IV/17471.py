# BFS, 모든 경우의 수

import sys
from collections import defaultdict, deque
from itertools import combinations


n = int(input().rstrip())
_data = list(map(int, input().rstrip().split()))
peoples = defaultdict(int)

for i in range(len(_data)):
    peoples[i+1] = _data[i]

graph = [[]for i in range(n+1)]

for i in range(n):
    data = list(map(int, input().rstrip().split()))
    for j in data[1:]:
        graph[i+1].append(j)

result = sys.maxsize

#n = 6
#peoples = {1: 5, 2: 2, 3: 3, 4: 4, 5: 1, 6: 2}
#graph = [[], [2, 4], [1, 3, 6, 5], [4, 2], [1, 3], [2], [2]]

def bfs(combis):
    q = deque()
    q.append(combis[0])     # combis[0] == start
    visited = set()
    visited.add(combis[0])
    _sum = 0                # 사람들 누적 합계 수
    
    while q:
        x = q.popleft()
        _sum += peoples[x]
        
        for i in graph[x]:
            if i not in visited and i in combis:
                q.append(i)
                visited.add(i)
    
    return _sum, len(visited)

        
for i in range(1, n//2+1):
    for combis in combinations(range(1,n+1), i):
        sum1, len1 = bfs(combis)
        sum2, len2 = bfs([i for i in range(1,n+1) if i not in combis])
        
        if len1+len2 == n:
            result = min(result, abs(sum1-sum2))
        
print(result) if result != sys.maxsize else print(-1)
            
        
        
        
        
            
        
        
        
        
        
        

    



    