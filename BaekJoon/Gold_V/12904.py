import sys

input = sys.stdin.readline

s = list(input().rstrip())
t = list(input().rstrip())

# 반대로 생각하기

chk = False

while t:
    
    if t == s:
        chk = True
        break
    
    if t[-1] == 'A':
        t.pop()
    elif t[-1] == 'B':
        t.pop()
        t.reverse()
        
print(1) if chk else print(0)

    
        
    
    



