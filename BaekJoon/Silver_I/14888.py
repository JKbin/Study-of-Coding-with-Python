# 재귀함수

import sys

input = sys.stdin.readline

n = int(input().rstrip())
numbers = list(map(int,input().rstrip().split()))
add,sub,mul,div = map(int,input().rstrip().split())

max_n = -sys.maxsize
min_n = sys.maxsize


def solution(num,a,s,m,d,idx):
    global max_n, min_n
    if idx == n:
        max_n = max(num,max_n)
        min_n = min(num,min_n)
        return
    
    if a > 0:
        solution(num + numbers[idx],a-1,s,m,d,idx+1)
    if s > 0:
        solution(num - numbers[idx],a,s-1,m,d,idx+1)    
    if m > 0:
        solution(num * numbers[idx],a,s,m-1,d,idx+1)
    if d > 0:
        solution(int(num / numbers[idx]),a,s,m,d-1,idx+1)

solution(numbers[0],add,sub,mul,div,1)

print(max_n)
print(min_n)







