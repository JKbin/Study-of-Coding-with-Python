from bisect import bisect_left, bisect_right

# bisect_left(a, x): 정렬된 순서를 유지하면서 리스트 a에 데이터 x를 삽입할 가장 왼쪽 
# 인덱스를 찾는 메서드

# bisect_right(a, x): 정렬된 순서를 유지하면서 리스트 a에 데이터 x를 삽입할 가장 오른쪽 
# 인덱스를 찾는 메서드


# 1. bisect 라이브러리는 '정렬된 배열'에서 특정한 원소를 찾을 때 매우 효과적이다.
# a = [1, 2, 4, 4, 5, 8]
# x = 4
# print(bisect_left(a,x))     # 2
# print(bisect_right(a,x))    # 4



# 2. '정렬된 배열'에서 '값이 특정 범위에 속하는 원소의 개수'를 구할 때
#                   (a,     4,      4)
def count_by_range(a, left_value, right_value):
    # right_index : 4가 들어갈 오른쪽 자리 : 8
    right_index = bisect_right(a, right_value)
    # left_index : 4가 들어갈 왼쪽 자리 : 6
    left_index = bisect_left(a, left_value)
    # return 값은 : 2
    return right_index - left_index


# 리스트 선언
a = [1, 2, 3, 3, 3, 3, 4, 4, 8, 9]    

# 다시 말해 a 리스트 안의 원소 [4, 4]사이의 갯수를 구하는 함수
print(count_by_range(a, 4, 4))

# 값이 [1, 3] 범위에 있는 데이터의 개수 출력
print(count_by_range(a, 1, 3))
