import sys

input = sys.stdin.readline

s = input().rstrip()

target = input().rstrip()


stack = []
n = len(target)

for i in range(len(s)):
    
    stack.append(s[i])
    
    if stack[-1] == target[-1]:
        if ''.join(stack[-n:]) == target:
            del stack[-n:]
    
if not stack:
    print('FRULA')
else:
    print(''.join(stack))
        
        
    
    
