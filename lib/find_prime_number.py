import math
# 에라토스테네스의 체
# 1 ~ n 까지 소수인 수 출력하는 함수

n = 110
array = [True for i in range(n+1)]

for i in range(2, int(math.sqrt(n))+1):
    if array[i] == True:
        j = 2
        while i * j <= n:
            array[i * j] = False
            j += 1

for i in range(2, n+1):
    if array[i]:
        print(i, end=' ')


