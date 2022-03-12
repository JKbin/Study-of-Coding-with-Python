# 자주 사용되는 내장 함수

# sum() : 총 합을 구할 때 사용
result = sum([1,2,3,4,5])
print(result)


# min(), max() : 최솟값, 최댓값을 구할 때 사용 
min_result = min([7, 3, 5, 2])
max_result = max([7, 3, 5, 2])
print(min_result, max_result)


# eval() : 수학연산식을 계산할 때 사용
result = eval("(3+5)*7")
print(result)


# sorted() : 오름차순 정렬, 내림차순 정렬
result = sorted([9, 1, 8, 5, 4])
reverse_result = sorted([9, 1, 8, 5, 4], reverse=True)
print(result)
print(reverse_result)


# sorted() with key : key를 기준으로 정렬
array = [('홍길동',50),('이순신',32),('아무개',74)]
print(sorted(array, key=lambda x: x[1]))
