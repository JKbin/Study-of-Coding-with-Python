import sys
from collections import deque

input = sys.stdin.readline

s = input().rstrip()
t = input().rstrip()

q = deque()
q.append(t)

ans = 0

# 거꾸로 생각하기
while q:
    word = q.popleft()
    word = list(word)
    
    if ''.join(word) == s:
        ans = 1
        break
    
    
    # 1. 뒤에 'A'를 제거
    if word[-1] == 'A':
        new_word1 = word[:-1]
        if new_word1:
            q.append(new_word1)
            
    # 2. 뒤집은 다음 뒤에 'B'를 제거
    word.reverse()
    if word[-1] == 'B':
        new_word2 = word[:-1]
        if new_word2:
            q.append(new_word2)
            

print(ans)

    
