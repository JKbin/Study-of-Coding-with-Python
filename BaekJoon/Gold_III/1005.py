# 위상정렬, DP

import sys
from collections import deque

input = sys.stdin.readline

T = int(input().rstrip())

for _ in range(T):
    n, k = map(int, input().rstrip().split())
    
    times = list(map(int, input().rstrip().split()))
    times.insert(0, -1)
    
    graph = [[]*(n+1) for _ in range(n+1)] 
    indegee = [0] * (n+1)
    
    for _ in range(k):
        a, b = map(int, input().rstrip().split())
        graph[a].append(b)
        indegee[b] += 1
    
    end = int(input().rstrip())
    
    # dp 초기화
    dp = [0] * (n+1)        # i번째 건물까지 짓는데 걸리는 시간
    
    q = deque()
    for i in range(1, n+1):
        if indegee[i] == 0:
            q.append(i)
            dp[i] = times[i]
    
    
    while q: 
        now = q.popleft()
        
        for next in graph[now]:
            indegee[next] -= 1
            
            # 건물 짓는데 걸리는 시간
            dp[next] = max(dp[now] + times[next], dp[next])       
            if indegee[next] == 0:
                q.append(next)
    
    print(dp[end])
    