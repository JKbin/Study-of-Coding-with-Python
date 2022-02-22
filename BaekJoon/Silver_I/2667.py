# 음료수 얼려먹기

import sys

n = int(sys.stdin.readline().rstrip())

graph = []
for i in range(n):
      graph.append(list(map(int,sys.stdin.readline().rstrip())))

cnt = 0

def dfs(x,y):
      global cnt
      if x <= -1 or y <= -1 or x >= n or y >= n:
            return False
      if graph[x][y] == 1:
            graph[x][y] = 100
            cnt += 1
            dfs(x,y-1)
            dfs(x-1,y)
            dfs(x+1,y)
            dfs(x,y+1)
            return True
      return False

result = 0
temp = []
for i in range(n):
      for j in range(n):
            if dfs(i,j) == 1:
                  result += 1
                  temp.append(cnt)
                  cnt = 0
                  
            
                  

print(result)
temp.sort()
for i in temp:
      print(i)

