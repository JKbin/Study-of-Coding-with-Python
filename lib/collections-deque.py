# 보통 deque를 이용하여 자료구조인 스택이나 큐를 구현한다.

from collections import deque
data = deque([2, 3, 4])

# 데이터 리스트 왼쪽에 1 삽입
data.appendleft(1)
# 데이터 리스트 끝(오른쪽)에 5 삽입
data.append(5)

print(data)
print(list(data))