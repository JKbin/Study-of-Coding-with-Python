# Silver IV

import re,sys
input = sys.stdin.readline

# 규칙
# 문자열은 {A, B, C, D, E, F} 중 0개 또는 1개로 시작해야 한다.
# 그 다음에는 A가 하나 또는 그 이상 있어야 한다.
# 그 다음에는 F가 하나 또는 그 이상 있어야 한다.
# 그 다음에는 C가 하나 또는 그 이상 있어야 한다.
# 그 다음에는 {A, B, C, D, E, F} 중 0개 또는 1개가 있으며, 더 이상의 문자는 없어야 한다.

regex = re.compile('[A-F]{0,1}A+F+C+[A-F]{0,1}$')

n = int(input().rstrip())

for _ in range(n):
    s = input().rstrip()
    
    m = regex.match(s)
    if not m: print('Good')
    else: print('Infected!')














