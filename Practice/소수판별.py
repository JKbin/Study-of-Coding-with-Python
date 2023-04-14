from sys import stdin
from math import sqrt

# 소수 판별 함수

n = int(stdin.readline().rstrip())
soo = list(map(int,stdin.readline().rstrip().split()))

def prime_number(n):
    
    if n == 1:
        return False
    
    
    for i in range(2,int(sqrt(n))+1):
        
        if n % i == 0:
            return False
    return True

result = 0
for i in soo:
    if prime_number(i):
        result += 1
        
print(result)


        

        
    

            
    