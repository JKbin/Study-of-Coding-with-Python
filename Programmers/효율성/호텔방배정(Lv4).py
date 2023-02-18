#import sys
#sys.setrecursionlimit(10**6)

# def solution(k, room_number):
#     answer = []
#     tb = dict()

#     def find(rooms, n):
#         # tb에 없을 경우
#         if n not in rooms:
#             rooms[n] = n + 1
#             return n
#         empty = find(rooms, rooms[n])
#         rooms[n] = empty + 1
#         return empty
    
#     for num in room_number:
#         ans = find(tb, num)
#         answer.append(ans)
#     return answer

def solution(k, room_number):
    answer = []
    tb = dict()
    
    for num in room_number:
        # visited에 갱신할 방번호 저장해놓기
        visited = [num]
        while num in tb:
            num = tb[num]
            visited.append(num)
        answer.append(num)
        # 이미 차있는 방 다시 갱신하기
        for k in visited:
            tb[k] = num + 1
    return answer