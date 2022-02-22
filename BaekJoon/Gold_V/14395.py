from collections import deque
from sys import stdin


s,to = map(int,stdin.readline().rstrip().split())


MAX = 10e9

def bfs(s,to):
    answer = []
    check = set()
    check.add(s)
    
    if s == to:
        print(0)
        exit(0)
    
    q = deque()
    q.append((s,''))
    result = -1
    
    while q:
        x,y = q.popleft()
        
        if x == to:
            result = y
            print(result)
            exit(0)
            
        temp = x * x 
        if 0<=temp<MAX and temp not in check:
            q.append((temp,y+'*'))
            check.add(temp)
            
        temp = x + x
        if 0<=temp<MAX and temp not in check:
            q.append((temp,y+'+'))
            check.add(temp)
            
        temp = 1
        if 0<=temp<MAX and temp not in check:
            q.append((temp,y+'/'))
            check.add(temp)
        
        
            
    print(result)
    
bfs(s,to)