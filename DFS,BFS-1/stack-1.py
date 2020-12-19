# 스택 자료 구조 구현
# 일반적인 리스트 함수로 구현 가능

stack = []

stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop()
stack.append(1)
stack.append(4)
stack.pop()

# 5 2 3 1

# 최상단 원소부터 출력
print(stack[::-1])
# 최하단 원소부터 출력
print(stack)

