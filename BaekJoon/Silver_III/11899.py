import sys

input = sys.stdin.readline

s = input().rstrip()


while True:
    
    if '()' not in s:
        break
    
    s = s.replace('()','Z')
    s = list(s)
    while 'Z' in s:
        s.remove('Z')
    s = ''.join(s)
        
print(len(s))




        
        
    


