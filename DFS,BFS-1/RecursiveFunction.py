# 재귀 함수 : 자기 자신을 다시 호출하는 함수

# 예제
# 종료 조건을 포함하지 않은 재귀 함수

# def recursive_function():
#     print("재귀 함수를 호출합니다.")
#     recursive_function()

# recursive_function()

# 파이썬에서는 재귀함수 깊이가 제한이 있으므로 종료된다.

# 재귀 함수를 문제 풀이에서 사용할 때는 종료 조건을 반드시 명시해야 한다.
# 종료 조건을 제대로 명시하지 않으면 함수가 무한히 호출될 수 있다.

# 종료 조건을 포함한 재귀 함수(필수)
def recursive_function(i):
    # 100번째 호출을 했을 때 종료되도록 종료 조건 명시(시작부분)
    if i == 100:
        return
    print(i, "번째 재귀함수에서", i + 1, "번째 재귀함수를 호출합니다.")
    recursive_function(i + 1)
    print(i, "번째 재귀함수를 종료합니다.")

recursive_function(1)
