import heapq

n = int(input().rstrip())
m = int(input().rstrip())
graph = [[] for i in range(n+1)]
for _ in range(m):
   a,b,c = map(int, input().rstrip().split())      # c: 비용
   graph[a].append((b,c))
start, end = map(int, input().rstrip().split())
INF = int(1e9)

#n,m = 5, 8
#graph = [[], [(2, 2), (3, 3), (4, 1), (5, 10)], [(4, 2)], [(4, 1), (5, 1)], [(5, 3)], []]
#start, end = 1, 5


def fun(start, end):
    distance = [INF]* (n+1)
    nearnest = [start] * (n + 1)        # 경로 추가

    q = []
    heapq.heappush(q, (0,start))
    distance[start] = 0
    
    while q:
        dist, now = heapq.heappop(q)
        
        if distance[now] < dist:
            continue
        
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                nearnest[i[0]] = now
                heapq.heappush(q, (cost, i[0]))
    
    return distance, nearnest
                


final_distance, final_nearnest = fun(start, end)

ans = []
tmp = end
while tmp != start:
    ans.append(str(tmp))
    tmp = final_nearnest[tmp]

ans.append(str(start))
ans.reverse()
 
print(final_distance[end])
print(len(ans))
print(" ".join(ans))






        
        







