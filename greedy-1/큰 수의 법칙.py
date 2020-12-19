arr = [2,4,5,4,6]
N = len(arr)       # 5
M = 8
K = 3

arr.sort()
# 2,4,4,5,6
# 6+6+6+5+6+6+6+5 = 46

# 제일 큰 수 : 6
max_num1 = arr[N-1]
# 2번째로 큰 수 : 5
max_num2 = arr[N-2]

result = 0


# 제일 큰 수 k번 더하기
for i in range(K):
    result += max_num1
    K -= 1
# 2번째 큰 수 1번 더하기
result += max_num2

print(result)