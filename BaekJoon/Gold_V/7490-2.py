# 중복 순열
# 연산기호들의 모든 경우의 수를 재귀로 구한다.

import sys, copy

sys.setrecursionlimit(10**6)

input = sys.stdin.readline

T = int(input().rstrip())

for _ in range(T):
    n = int(input().rstrip())
    
    def recursive(s):
        if len(s) == n - 1:
            operators.append(copy.deepcopy(s))
            return
        
        s.append(' ')
        recursive(s)
        s.pop()
        
        s.append('+')
        recursive(s)
        s.pop()
        
        s.append('-')
        recursive(s)
        s.pop()
            
    
    operators = []
    recursive([])
    
    array = [i for i in range(1, n+1)]
    
    for op in operators:
        string = ''
        for i in range(n-1):
            string += str(array[i])+op[i]
        string += str(array[-1])
        if eval(string.replace(" ","")) == 0:
            print(string)
    print()