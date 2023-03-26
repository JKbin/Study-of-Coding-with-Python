# 오큰수
# stack 사용, 뒤에서 부터 문제 전개

import sys

input = sys.stdin.readline

# n = int(input().rstrip())
# data = list(map(int, input().rstrip().split()))

n = 4
data = [3, 5, 2, 7]

result = [-1] * (n)
stack = []

for i in range(n-1, -1, -1):
    
    num = data[i]       # 7
    
    while stack and stack[-1] <= num :
        stack.pop()
        
    if stack:
        result[i] = stack[-1]
    
    stack.append(num)


print(' '.join(map(str, result)))


    
        
    
    

    
    
    