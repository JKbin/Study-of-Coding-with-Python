from itertools import combinations
from sys import stdin


n,m = map(int,stdin.readline().rstrip().split())
num = list(map(int,stdin.readline().rstrip().split()))
# n,m = 5,0
# num = [-7, -3, -2, 5, 8]

answer = 0
temp = []



for i in range(1,len(num)+1):
    temp.extend(combinations(num,i))
    
for i in temp:
    if sum(i) == m:
        answer += 1
        
print(answer)


        


            
    
    
