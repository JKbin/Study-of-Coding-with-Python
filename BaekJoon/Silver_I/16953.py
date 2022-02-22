

from collections import deque
from sys import stdin


n,m = map(int,stdin.readline().rstrip().split())

q = deque()
q.append((n,1))

result = -1
while q:
    x,cnt = q.popleft()
    
    if x == m:
        result = cnt
        break
    
    if x*2 <= m:
        q.append((x*2,cnt+1))
    if int(str(x)+'1') <= m:
        q.append((int(str(x)+'1'),cnt+1))
        
        
print(result)

        
        
    
    
    
    
    
    
    

