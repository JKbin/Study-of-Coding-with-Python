# KMP(Knuth-Morris-Pratt) 알고리즘
# 문자열 매칭 알고리즘

# aba/cd/aba
# 우리가 구해야 할 것은 접두사와 접미사가 일치하는 최대 길이!
# 접두사와 접미사를 구하게 되면 접두사와 접미사가 일치하는 경우에 한해서는 jump(점프)를 수행할 수 있어서 매우 효율적이다.

# 풀이
# j i
# a b a c a a b a
# j와 i가 일치한다면 j,i 둘 다 증가 / j의 인덱스 + 1을 입력
# j와 i가 일치하지 않으면, i만 증가, j는 0 인덱스로 이동
# 0 0 1 0 1 1 2 3 이 나와야 한다.


def kmp(all_string, pattern):
    # kmp table
    table = [0 for _ in range(len(pattern))]
    i = 0
    for j in range(1, len(pattern)):
        while i > 0 and pattern[i] != pattern[j]:
            i = table[i-1]
        
        if pattern[i] == pattern[j]:
            i += 1
            table[j] = i
    
    # kmp
    result = []
    i = 0
    for j in range(len(all_string)):
        while i > 0 and pattern[i] != all_string[j]:
            i = table[i-1]
        
        if pattern[i] == all_string[j]:
            i += 1
            if i == len(pattern):
                result.append(j - i + 1)
                i = table[i-1]
    return result



print(kmp('ababacabacaabacaaba', 'abacaaba'))       # [6, 11]
print(kmp('abababab','abab'))                       # [0, 2, 4]


            