import heapq

# 1. 힙 정렬(오름차순)
# 원소를 힙에 넣었다가 빼는 것만으로도 오름차순 정렬이 완료된다.
# def heapsort(iterable):
#     h = []
#     result = []
#     # iterable의 모든 원소를 h에 삽입
#     for value in iterable:
#         heapq.heappush(h, value)
#     # h(힙)에 삽입된 모든 원소를 차례대로 꺼내어 result에 넣기
#     for _ in range(len(h)):
#         result.append(heapq.heappop(h))
#     return result

# a = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
# result = heapsort(a)
# print(result)





# 2. 힙 정렬(내림차순)
# 힙에 원소를 삽입하기 전에 잠시 부호를 반대로 바꾸었다가, 힙에서 원소를 꺼낸 뒤 다시 부호를 바꾼다.
def heapsort(iterable):
    h = []
    result = []
    # 모든 원소를 차례대로 h(힙)에 삽입
    for value in iterable:
        heapq.heappush(h, -value)
    # h(힙)에 삽입된 모든 원소를 차례대로 꺼내어 result에 넣기
    for _ in range(len(h)):
        result.append(-heapq.heappop(h))
    return result

a = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
result = heapsort(a)
print(result)



