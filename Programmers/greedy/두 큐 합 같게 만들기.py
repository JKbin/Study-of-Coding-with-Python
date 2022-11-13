from collections import deque

#queue1 = [3, 2, 7, 2]	
#queue2 = [4, 6, 5, 1]	


def solution(queue1, queue2):
    answer = 0
    
    q1 = deque(queue1)
    q2 = deque(queue2)
    
    q1_sum = sum(q1)
    q2_sum = sum(q2)
    
    for _ in range(300000):             # 각 큐의 최대 크기 300,000
        if q1_sum > q2_sum:             # q1의 합이 q2의 합보다 크면 q1에서 pop하고 q2에 append
            a = q1.popleft()
            q1_sum -= a
            q2_sum += a
            q2.append(a)
        elif q1_sum < q2_sum:           # q2의 합이 q1의 합보다 크면 q2에서 pop하고 q1에 append
            a = q2.popleft()
            q1_sum += a
            q2_sum -= a
            q1.append(a)
        else:
            return answer
        answer += 1
    return -1
    
    
#print(solution(queue1, queue2))
