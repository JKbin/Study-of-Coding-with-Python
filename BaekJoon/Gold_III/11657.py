# Bellman-Ford
# 음수 간선이 포함된 상황에서의 최단 거리 문제
# BOJ 11657 문제
# 시간 복잡도 : O(VE)   다익스트라보다는 알고리즘에 비해 느리다.

# 벨만-포드 알고리즘

# 1. 출발 노드 설정
# 2. 최단 거리 테이블 초기화
# 3. 다음의 과정을 N-1번 반복
#   3-1. 전체 간선 E개를 하나씩 확인한다.
#   3-2. 각 간선을 거쳐 다른 노드로 가는 비용을 계산하여 최단 거리 테이블을 갱신한다.

# 만약 음수 간선 순환이 발생하는지 체크하고 싶다면 3번의 과정을 1번 더 수행한다.
# 이 때, 최단 거리 테이블이 만약 갱신된다면...
# 음수 간선 순환(무한히 비용이 -로 갱신되는 순환)이 존재하는 것이다.

import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().rstrip().split())
edges = []
dist = [INF] * (n+1)

for _ in range(m):
    a, b, c = map(int, input().rstrip().split())
    edges.append((a, b, c))
    
def bf(start):
    # 시작 노드에 대해서 초기화
    dist[start] = 0
    
    # 전체 n번의 라운드를 반복
    for i in range(n):
        # 모든 간선 확인
        for j in range(m):
            cur = edges[j][0]
            next_node = edges[j][1]
            cost = edges[j][2]
            # 현재 간선을 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
            if dist[cur] != INF and dist[next_node] > dist[cur] + cost:
                # 최단 거리 갱신
                dist[next_node] = dist[cur] + cost
                # n번째 라운드에서도 값이 갱신된다면 음수 순환이 존재
                if i == n-1:
                    return True
    return False
                    
            
# 벨만-포드 알고리즘 수행
negative_cycle = bf(1)      # 시작노드 1

if negative_cycle:
    print(-1)
else:
    for i in range(2, n+1):
        if dist[i] == INF:
            print("-1")
        else:
            print(dist[i])
            

