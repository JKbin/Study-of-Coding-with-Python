#  다익스트라 알고리즘
import sys
import heapq
input = sys.stdin.readline

n,m = map(int,input().rstrip().split())

graph = [[]for i in range(n+1)]
INF = int(1e9)

distance = [INF] * (n+1)
start = 1

for i in range(m):
    a,b = map(int,input().rstrip().split())
    graph[a].append((b,1))
    graph[b].append((a,1))

def fun(start):
    q = []
    
    heapq.heappush(q,(0,start))
    distance[start] = 0
    
    while q:
        
        dist,now = heapq.heappop(q)
        
        if distance[now] < dist:
            continue
        
        for i in graph[now]:
            cost = dist + i[1]
            
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))
                
                
fun(start)


max_distance = max(distance[1:])            # 헛간까지의 거리

temp = []
first = -1          # 숨어야 하는 번호 (가장 작은 번호)
count = 0           # 그 헛간과 같은 거리를 갖는 헛간의 개수

for i in range(1,n+1):
    if distance[i] == max_distance:
        count += 1
        temp.append(i)

temp.sort()
        
print(temp[0],max_distance,count)

        
        
        
        
        
    
    
        
        
            
    
    

            
                
    
    


        

        




    
          
        
            



