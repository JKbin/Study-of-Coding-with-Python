#a = (lambda a,b : a+b)(3,7)
#print(a)
##################################################
# 튜플 형식의 리스트에서 숫자를 기준으로 오름차순 정렬할 때
# array = [('홍길동',50),('이순신',32),('아무개',74)]

# def my_key(x):
#     return x[1]

# print(sorted(array, key=my_key))
# print(sorted(array, key=lambda x: x[1]))

##################################################

# 여러 개의 리스트에 적용
list1 = [1,2,3,4,5]
list2 = [6,7,8,9,10]

# map : 각 각의 원소에 함수를 적용하고 싶을 때 사용
result = map(lambda a,b: a+b, list1, list2)
print(list(result))     # result = [7,9,11,13,15]







