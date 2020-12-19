# 알파벳 대문자와 숫자(0 ~ 9)로만 구성된 문자열이 주어진다.
# 이때 모든 알파벳을 오름차순으로 정렬하여 이어서 출력하고
# 그 뒤에 모든 숫자를 더한 값을 이어서 출력한다

# 입력예시
# K1KA5CB7
# 출력예시
# ABCKK13

# 입력예시
# AJKDLSI412K4JSJ9D
# 출력예시
# ADDIJJJKKLSS20

#######################################
# 나의 풀이(힌트)

# s = str(input())
# num = 0
# alpha_str = ''

# for alpha in s:
#     # 문자열이 숫자라면?
#     if alpha.isdigit() == True:
#         num += int(alpha)
#     else:
#         alpha_str += alpha

# alpha_str = ''.join(sorted(alpha_str))
# print(alpha_str + str(num))

#######################################

# 풀이
data = input()
result = []
value = 0

for x in data:
    # 알파벳인 경우 result에 삽입
    if x.isalpha():
        result.append(x)
    # 숫자는 따로 더히기
    else:
        value += int(x)

# 알파벳을 오름차순으로 정렬
result.sort()

# 숫자가 하나라도 존재하는 경우 가장 뒤에 삽입
if value != 0:
    result.append(str(value))

# 최종 결과 출력
print(''.join(result))
