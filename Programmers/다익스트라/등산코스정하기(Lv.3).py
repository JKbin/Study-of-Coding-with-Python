import heapq
from collections import defaultdict

def solution(n, paths, gates, summits):
    
    INF = int(1e9)
    #graph = [[]for i in range(n+1)]
    
    # 딕셔너리 자료형 사용할 것!! (시간 줄여줌)
    graph = defaultdict(list)
    vistied = [INF] * (n+1)
    
    for a,b,c in paths:
        graph[a].append((b,c))
        graph[b].append((a,c))
    
    summits.sort()
    summits_set = set(summits)          # set 자료형 사용할 것!! (시간 줄여줌)
    q = []
    
    # 1. 0(intensity), gates로 초기화
    for g in gates:
        heapq.heappush(q, (0, g))           # intensity, node
        vistied[g] = 0                      # 방문처리
        
    
    while q:
        intensity, now = heapq.heappop(q)
        
        # 현재 intensity가 현재 경로의 max intensity보다 작으면 continue
        if vistied[now] < intensity:
            continue
        
        # 산봉우리 다음으로 경로를 만들 수 없으므로 continue
        # 현재 now가 산봉우리인지 check 해야되서 summuit을 set 자료형으로 바꿔줌 (시간 단축)
        if now in summits_set:              
            continue
        
        for next_node, next_intensity in graph[now]:
            max_intensity = max(intensity, next_intensity)
            
            # intensity 갱신
            if max_intensity < vistied[next_node]:
                vistied[next_node] = max_intensity
                heapq.heappush(q, (max_intensity, next_node))
    
    # 산봉우리 번호, intensity
    answer = [0, INF]
    
    for s in summits:
        if vistied[s] < answer[1]:
            answer[0] = s
            answer[1] = vistied[s]
    
    return answer