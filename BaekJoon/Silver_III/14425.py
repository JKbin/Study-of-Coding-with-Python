# 딕셔너리 활용
import sys

input = sys.stdin.readline

n,m = map(int,input().rstrip().split())    

table = dict()
answer = 0

for _ in range(n):
    s = input().rstrip()
    table[s] = 0
    
for _ in range(m):
    s = input().rstrip()
    
    if s in table:
        answer += 1
    
        
        
print(answer)

    

                



    
    

    

    
    



    
    
