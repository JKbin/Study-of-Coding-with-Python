# 다익스트라
# 최소비용을 갖는 경로 찾는 문제

import sys, heapq

input = sys.stdin.readline

INF = int(1e9)
n, m = map(int, input().rstrip().split())
graph = [[]for i in range(n+1)]
for _ in range(m):
    a,b,c = map(int, input().rstrip().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

#n, m = 6, 10
#graph = [[], [(2, 2), (3, 1)], [(1, 2), (4, 5), (5, 3), (6, 7)], [(1, 1), (4, 4), (5, 6), (6, 7)], [(2, 5), (3, 4), (6, 4)], [(2, 3), (3, 6), (6, 2)], [(2, 7), (3, 7), (4, 4), (5, 2)]]

# start부터 시작해서 다른 지점까지 가는 최단 경로
def fun(start):
    distance = [INF] * (n+1)
    q = []
    heapq.heappush(q,(0,start))         # 비용, 노드
    distance[start] = 0
    
    path = [start] * (n + 1)        # 경로 추가

    
    while q:
        dist, now = heapq.heappop(q)
        
        if distance[now] < dist:
            continue
        
        for i in graph[now]:
            cost = dist + i[1]
            
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                path[i[0]] = now        # 경로
                heapq.heappush(q,(cost,i[0]))
                
    return path

## 4 -> 5로 가는 최단경로 찾기
#start = 4
#end = 5
#ans = []
#a = fun(start,end)
#tmp = end
#while tmp != start:
#    ans.append(str(tmp))
#    tmp = a[tmp]
#ans.append(str(start))
#ans.reverse()
#print(ans)



total_result = []

for i in range(1, n+1):
    tmp_result = []
    list_a = fun(i)
    start = i
    for j in range(1, n+1):
        if i != j:
            ans = []
            end = j
            tmp = end
            
            while tmp != start:
                ans.append(str(tmp))
                tmp = list_a[tmp]
                
            ans.append(str(start))
            ans.reverse()
            tmp_result.append(ans[1])
        else:
            tmp_result.append('-')
    total_result.append(tmp_result)

for i in total_result:
    for k in i:
        print(k,end=' ')
    print()
    
    