# 최대 공약수 계산(유클리드 호제법)예제

# 두 개의 자연수에 대한 최대공약수를 구하는 대표적인 알고리즘

# 유클리드 호제법
# 두 자연수 A, B에 대하여 (A ? B) A를 B로 나눈 나머지를 R이라고 한다.
# 이때 A와 B의 최대공약수는 B와 R의 최대공약수와 같다.

# 예시
# 단계     A       B
#  1      192     162
#  2      162     30
#  3      30      12
#  4      12      6


def gcd(a, b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)

print(gcd(192, 162))


# 재귀 함수 사용시 유의 사항

# 1. 재귀 함수를 잘 활용하면 복잡한 알고리즘을 간결하게 작성 가능
# 하지만, 다른 사람이 이해하기 어려운 코드가 될 수 있다.
# 2. 모든 재귀 함수는 반복문을 이용하여 동일한 기능을 구현 가능
# 3. 재귀 함수가 반복문보다 유리할 경우도 있고 불리한 경우도 있다.
# 4. 컴퓨터가 함수를 연속적으로 호출하면 컴퓨터 메모리 내부의 스택 프레임에 쌓인다.
# 5. 그래서 스택을 사용해야 할 때 구현상 스택 라이브러리 대신 재귀 함수를 이용하는 경우가 많다.
