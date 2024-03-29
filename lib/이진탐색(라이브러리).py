from bisect import bisect_left, bisect_right

# bisect_left(a,x) : 정렬된 순서를 유지하면서 배열 a에 x를 삽입할 가장 왼쪽 인덱스 반환
# bisect_right(a,x) : 정렬된 순서를 유지하면서 배열 a에 x를 삽입할 가장 오른쪽 인덱스 반환


# 값이 특정 범위에 속하는 데이터의 개수 구하기

# 값이 [left_value, right_value]인 데이터의 개수를 반환하는 함수
def conut_by_range(a,left_value, right_value):
    right_index = bisect_right(a,right_value)
    left_index = bisect_left(a,left_value)
    return right_index - left_index

a = [1,2,3,3,3,3,4,4,8,9]

# 값이 4인 데이터의 개수 출력
print(conut_by_range(a,4,4))

# 값이 -1 이상 3이하인 범위에 있는 데이터의 개수 출력
print(conut_by_range(a,-1,3))


