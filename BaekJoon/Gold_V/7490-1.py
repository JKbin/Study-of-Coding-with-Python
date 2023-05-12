# 중복 순열
# 연산기호들의 모든 경우의 수를 product로 구한다.

import sys
from itertools import product

input = sys.stdin.readline

T = int(input().rstrip())

for _ in range(T):
    n = int(input().rstrip())
    
    operators = [' ', '+', '-']
    array = [i for i in range(1, n+1)]
    
    for i in product(operators, repeat=n-1):
        string = ''
        for j in range(n-1):
            string += str(array[j])+i[j]
        string += str(array[-1])
        #print(string)
        if eval(string.replace(" ", "")) == 0:
            print(string)
    print()