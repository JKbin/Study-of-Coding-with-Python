my_list = [[1, 2], [3, 4], [5, 6]]

# 방법 1 - sum 함수
answer = sum(my_list, [])
print(answer)

# 방법 3 - itertools와 unpacking
import itertools
print(list(itertools.chain(*my_list)))