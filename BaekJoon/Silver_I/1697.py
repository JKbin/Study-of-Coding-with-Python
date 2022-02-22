import sys
from collections import deque
n,m = map(int,sys.stdin.readline().rstrip().split())

limit = 100001
time = [0] * limit


def bfs():
    q = deque([n])
    
    while q:
        x = q.popleft()
        
        if x == m:
            print(time[x])
            return
        
        for next in [x-1,x+1,2*x]:
            if 0 <= next < limit and not time[next]:
                time[next] = time[x] + 1
                q.append(next)
            
            
bfs()








