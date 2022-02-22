import sys
sys.setrecursionlimit(10000)
start = int(sys.stdin.readline().rstrip())

# n : 가로길이
# m : 세로길이
# k : 배추갯수
for i in range(start):
      n,m,k = map(int,sys.stdin.readline().rstrip().split())
      graph = []
      for i in range(m):
            graph.append([0]*n)

      for i in range(k):
            z,s = map(int,sys.stdin.readline().rstrip().split())
            graph[s][z] = 1

      def dfs(x,y):
            if x <= -1 or y <= -1 or x >= m or y >= n:
                  return False
            if graph[x][y] == 1:
                  graph[x][y] = 2
                  dfs(x-1,y)
                  dfs(x,y-1)
                  dfs(x+1,y)
                  dfs(x,y+1)
                  return True
            return False

      result = 0

      for i in range(m):
            for j in range(n):
                  if dfs(i,j) == 1:
                        result += 1
      print(result)







