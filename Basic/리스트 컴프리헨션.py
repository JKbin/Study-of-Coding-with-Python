
#1 1 ~ 20까지 홀수만 포함하는 리스트
array = [i for i in range(1,21) if i % 2 == 1]


#2 1 ~ 9까지의 수의 제곱을 포함하는 리스트
array = [i * i for i in range(1,10)]


#3 N x M 크기의 2차원 배열 초기화(반드시 컴프리헨션 사용)
n = 3
m = 4
array = [[0]*m for _ in range(n)]


#4 리스트에서 특정 원소를 제거할 때
a = [1, 2, 3, 4, 5, 5, 5]
# set type 사용
remove_set = {3, 5}
# remove_set에 포함되지 않는 값만 저장
result = [i for i in a if i not in remove_set]
# result = [1, 2, 4]

