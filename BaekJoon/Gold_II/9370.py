import sys, heapq

input = sys.stdin.readline

T = int(input().rstrip())

INF = int(1e9)

for _ in range(T):
    n, m, t = map(int, input().rstrip().split())
    s, g, h = map(int, input().rstrip().split())
    graph = [[]for i in range(n+1)]
    for _ in range(m):
        a,b,c = map(int, input().rstrip().split())
        graph[a].append((b,c))
        graph[b].append((a,c))
    candidates = []
    for _ in range(t):
        candidates.append(int(input().rstrip()))
    
    def dijkstra(start):
        distance = [INF] * (n+1)
        q = []
        distance[start] = 0             # 출발지점 방문처리
        heapq.heappush(q, (0, start))   # 비용, 노드
        
        while q:
            dist, now = heapq.heappop(q)
            
            if distance[now] < dist: continue
            
            for next_node, next_cost in graph[now]:
                cost = dist + next_cost
                
                if cost < distance[next_node]:
                    distance[next_node] = cost
                    heapq.heappush(q, (cost, next_node))
                    
        return distance             
    
    
    s_dist = dijkstra(s)            # s에서 출발
    g_dist = dijkstra(g)            # g에서 출발
    h_dist = dijkstra(h)            # h에서 출발
    
    #print(f's_distance = {s_distance}')
    #print(f'g_disatnce = {g_disatnce}')
    #print(f'h_disatnce = {h_disatnce}')
    
    ans = []
    for c in candidates:
        # s -> g -> h로 거쳐서 c까지 경우 == s에서 c까지 바로 가는 경우 
        #                           OR
        # s -> h -> g로 거쳐서 c까지 경우 == s에서 c까지 바로 가는 경우
        if s_dist[g] + g_dist[h] + h_dist[c] == s_dist[c] or s_dist[h] + h_dist[g] + g_dist[c] == s_dist[c]:
            ans.append(c)
    
    ans.sort()
    print(*ans)
        
        