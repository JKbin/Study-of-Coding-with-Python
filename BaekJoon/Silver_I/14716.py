import sys

sys.setrecursionlimit(10**6)


m,n = map(int,sys.stdin.readline().rstrip().split())
graph = []
for i in range(m):
    graph.append(list(map(int,sys.stdin.readline().rstrip().split())))
    


def dfs(x,y):
    
    if x <= -1 or y <= -1 or x >= m or y >= n:
        return False
    if graph[x][y] == 1:
        graph[x][y] = 0
        dfs(x+1,y)
        dfs(x+1,y+1)
        dfs(x+1,y-1)
        dfs(x-1,y)
        dfs(x-1,y+1)
        dfs(x-1,y-1)
        dfs(x,y+1)
        dfs(x,y-1)
        return True
    return False

result = 0

for i in range(m):
    for j in range(n):
        if dfs(i,j) == 1:
            result += 1
            
print(result)


    
        




                
            
