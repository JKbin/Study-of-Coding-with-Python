import sys
sys.setrecursionlimit(50000000)

def dfs(x,y):
    if 0 <= x < h and 0 <= y < w:
        if graph[x][y] == 1:
            graph[x][y] = 2
            dfs(x,y-1)
            dfs(x+1,y+1)
            dfs(x+1,y)
            dfs(x+1,y-1)
            dfs(x,y+1)
            dfs(x-1,y-1)
            dfs(x-1,y)
            dfs(x-1,y+1)
            return True    
        return False

while True:
    w,h = map(int,sys.stdin.readline().rstrip().split())
    if not w and not h:
        break
    graph = []
    for i in range(h):
        graph.append(list(map(int,sys.stdin.readline().rstrip().split())))
        
    result = 0
    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1:
                dfs(i,j)
                result += 1
    print(result)
    
    

        
    
    