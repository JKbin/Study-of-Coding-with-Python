import sys

input = sys.stdin.readline

n,m = 3,4

start = 1
graph = [[]for i in range(m)]


for i in range(m):
    for j in range(m):
        graph[i].append(start)
        start += 1
       
print(graph)
print(list(map(list,zip(*graph))))
print(list(zip(*graph)))







