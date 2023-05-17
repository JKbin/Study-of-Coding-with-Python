
import sys
input = sys.stdin.readline

n = int(input().rstrip())

# 양수, 음수, 0의 원소를 따로 저장
plus = []
minus = []
zero = []

for _ in range(n):
    a = int(input().rstrip())
    if a > 0:
        plus.append(a)
    elif a < 0:
        minus.append(a)
    else:
        zero.append(a)

# 양수는 내림차순 정렬
plus.sort(reverse=True)
# 음수는 오름차순 정렬
minus.sort()

result = 0

while len(plus) >= 2:
    a = plus.pop(0)
    b = plus.pop(0)
    # 둘 중 하나라도 1이면 곱하는 것보다 더하는게 더 큰 값을 준다.
    if a == 1 or b == 1:
        result += a
        result += b
    else:
        result += (a*b)
while len(minus) >= 2:
    a = minus.pop(0)
    b = minus.pop(0)
    result += (a*b)

while plus:
    result += plus.pop(0)
while minus:
    # 0의 원소가 남아있으면 음수와 곱해서 없애버리기
    if zero:
        z = zero.pop(0)
        a = minus.pop(0)
    else:
        result += minus.pop(0)
        

print(result)


