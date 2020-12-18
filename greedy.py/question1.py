# 어떠한 수 N이 1이 될 때까지 다음의 두 과정 중 하나를 반복 수행하시오.
# 단, 두번째 연산은 N이 K로 나누어 떨어질 때만 선택이 가능하다.

# 1. N에서 1을 뺍니다. > N - 1
# 2. N을 K로 나눕니다. > N % K

# 예를 들어, N = 17, K = 4라면 나눌 수 없으므로 1번 과정 실행
# 17 - 1 = 16(N)
# 16은 K로 나눌 수 있으므로 2번과정 실행
# 16 % 4 = 4
# 4는 K로 나눌 수 있으므로 2번과정 실행
# 4 % 4 = 1
# N이 1이 되었으므로 총 과정을 실행한 횟수는 3이다.

n = 17
k = 4
count = 0


# 내가 처음 생각한 코드 (실행 x)
# while(True):
#     if n % 4 == 0:
#         n %= 4
#         count += 1
#     else:
#         n -=1
#         count += 1
#     if n == 1:
#         break
    
# log(K)의 연산법 (정답)
while True:
    # N이 K로 나누어 떨어지는 수가 될 때까지 빼기
    target = (n // k) * k
    count += (n - target)
    n = target
    # N이 K보다 작을 때 (더 이상 나눌 수 없을 때) 반복문 탈출
    if n < k:
        break
    # K로 나누기
    count += 1
    n //= k

count += (n - 1)
print(count)

