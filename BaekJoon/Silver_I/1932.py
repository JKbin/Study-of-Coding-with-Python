import sys

n = int(sys.stdin.readline().rstrip())
graph = []

for i in range(n):
    graph.append(list(map(int,sys.stdin.readline().rstrip().split())))


for i in range(1,len(graph)):
    for j in range(len(graph[i])):
        if j == 0:
            graph[i][j] += graph[i-1][j]
        elif j == len(graph[i])-1:
            graph[i][j] += graph[i-1][j-1]
        else:
            graph[i][j] += max( graph[i-1][j],graph[i-1][j-1])
            
print(max(graph[-1]))
            
