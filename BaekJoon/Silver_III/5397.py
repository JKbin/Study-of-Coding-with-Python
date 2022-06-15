import sys

input = sys.stdin.readline

n = int(input().rstrip())    

# stack 2개 활용
# 마지막에 right를 뒤집어서 붙이기


for _ in range(n):
    s = input().rstrip()
    
    left, right = [],[]
    
    for i in s:
        if i == '<':
            if left:
                right.append(left.pop())
        elif i == '>':
            if right:
                left.append(right.pop())
        elif i == '-':
            if left:
                left.pop()
        else:
            left.append(i)
        
    left.extend(reversed(right))
    print(''.join(left))
    
                



    
    

    

    
    



    
    
