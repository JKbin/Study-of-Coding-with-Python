# 1. 순열 구하기
#from itertools import permutations
#data = ['A', 'B', 'C']
# data에서 2개를 뽑아 일렬로 나열할 수 있는 모든 경우의 수
# result = list(permutations(data, 2))
# print(result)
# 선택 순서가 결과에 영향을 미치는 경우 
# (1, 2)를 선택하는 경우와 (2, 1)을 선택하는 경우의 결과가 다르다.



# 2. 조합 구하기 (중복 x)
# from itertools import combinations
# data = ['A','B','C']
# data에서 2개를 뽑아 순서에 상관없이 나열하는 경우의 수
# result = list(combinations(data, 2))
# print(result)
# 선택 순서가 결과에 영향을 미치지 않느 ㄴ경우
# (1, 2)를 선택하는 경우와 (2, 1)을 선택하는 경우의 결과가 같다.




# 3. 순열 구하기 (중복 o)
# from itertools import product
# data = ['A','B','C']
# data에서 2개를 뽑아 중복을 포함하여 나열하는 경우
# result = list(product(data, repeat=2))
# print(result)




# 4. 조합 구하기 (중복 o)
# from itertools import combinations_with_replacement
# data = ['A','B','C']
# data에서 2개를 뽑는 모든 조합 구하기(중복 o)
# result = list(combinations_with_replacement(data, 2))
# print(result)




