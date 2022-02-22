import sys
sys.setrecursionlimit(50000000)

n = int(sys.stdin.readline().rstrip())
graph = [ []*n for i in range(n+1)]
visited = [False] * (n+1)
for i in range(n-1):
    x,y = map(int,sys.stdin.readline().rstrip().split())
    graph[x].append(y)
    graph[y].append(x)
    graph[x].sort()
    graph[y].sort()

temp = [[]*n for i in range(n+1)]

check = 0

def dfs(graph,start,visited):
    global check
    visited[start] = True
    check += 1
    
    for i in graph[start]:
        if not visited[i]:
            temp[i].append(start)
            dfs(graph,i,visited)
            
dfs(graph,1,visited)

for i in temp:
    if len(i) != 0:
        for j in i:
            print(j)
            
    


    
    
    
    
        
                

