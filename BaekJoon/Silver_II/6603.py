from itertools import combinations
from sys import stdin

while True:
    
    temp = list(map(int,stdin.readline().rstrip().split()))
    
    if temp[0] == 0:
        break
    
    x = temp.pop(0)
    
    temp = list(combinations(temp,6))
    
    for i in temp:
        for j in i:
            print(j,end=' ')
        print()
    print()
        
    





