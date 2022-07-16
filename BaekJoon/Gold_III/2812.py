import sys

input = sys.stdin.readline

n,k = map(int,input().rstrip().split())
s = input().rstrip()

stack = []


for i in s:
    
    while k > 0 and stack and stack[-1] < i:
        stack.pop()
        k -= 1
    stack.append(i)
        
    
    
            
print(''.join(stack[:len(stack)-k]))        # k가 남는 경우가 있음



            
                        
        
    





    
    
    
        
    
        



        


    
    
    