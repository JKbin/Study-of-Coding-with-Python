# stack을 2개로 나누어서 활용

import sys

input = sys.stdin.readline

s1 = list(input().rstrip())
n = int(input().rstrip())

s2 = list()

for _ in range(n):
    x = input().rstrip().split()
    
    if x[0] == 'L':
        if s1:
            s2.append(s1.pop())
    elif x[0] == 'D':
        if s2:
            s1.append(s2.pop())
    elif x[0] == 'B':
        if s1:
            s1.pop()
    elif x[0] == 'P':
        s1.append(x[1])
        
s2 = reversed(s2)

s1.extend(s2)

print(''.join(s1))





        







        