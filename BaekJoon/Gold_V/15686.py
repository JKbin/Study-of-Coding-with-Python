# 구현
from itertools import combinations
import sys

input = sys.stdin.readline

n,m = map(int,input().rstrip().split())
#n,m = 5,2
graph = []
#graph = [[0, 2, 0, 1, 0], [1, 0, 1, 0, 0], [0, 0, 0, 0, 0], [2, 0, 0, 1, 1], [2, 2, 0, 1, 2]]
for i in range(n):
    graph.append(list(map(int,input().rstrip().split())))
    
house = []
chicken = []

for i in range(n):
    for j in range(n):
        if graph[i][j] == 2:
            chicken.append((i,j))
        elif graph[i][j] == 1:
            house.append((i,j))
            
INF = int(1e9) 
a = list(combinations(chicken,m))

def calc(chick):
    temp = [[0]*n for i in range(n)]
    
    for i in house:
        dist = INF
        r1 = i[0]
        c1 = i[1]
        for j in chick:
            r2 = j[0]
            c2 = j[1]
            
            dist = min(dist,abs(r1-r2)+abs(c1-c2))
        temp[r1][c1] = dist
    return temp
        
        
        
        
ans = []
            

for i in a:
    b = calc(i)
    result = 0
    for j in range(n):
        for k in range(n):
            result += b[j][k]
    ans.append(result)
    
    
print(min(ans))

            
    
            
    