# 원형 deque 문제
# deque.rotate(y) : y방향으로 시계방향으로 회전, -y이면 반시계방향으로 회전
from collections import deque
import sys

input = sys.stdin.readline


n = int(input().rstrip())

arr = list(map(int,input().rstrip().split()))

q = deque(enumerate(arr,1))



for i in arr:
    x,y = q.popleft()
    print(x,end=' ')
    
    q.rotate(-(y-1)) if y > 0 else q.rotate(-y)
