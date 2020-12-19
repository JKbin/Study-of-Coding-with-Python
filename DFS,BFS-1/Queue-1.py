# 큐 구현 예제

from collections import deque

queue = deque()

queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()
queue.append(1)
queue.append(4)
queue.popleft()
# 양방향으로 뚫려있고 나갈 때는 오른쪽에서, 들어올 때는 왼쪽에서

# 4 1 7 3 

print(queue)    # 먼저 들어온 순서대로 출력
queue.reverse()
print(queue)    # 나중에 들어온 순서대로 출력


