from itertools import combinations
from sys import stdin
n = int(stdin.readline().rstrip())

nums = [i for i in range(0,10)]

temp = list()
result = list()

for i in range(1,11):
    for j in combinations(nums,i):
        temp = list(j)
        temp.sort(reverse=True)
        result.append(int(''.join(map(str,temp))))
        
result.sort()


try:
    print(result[n])
except:
    print(-1)
        
        
        
        
        
        
            