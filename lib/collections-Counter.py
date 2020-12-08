# Counter : 등장 횟수를 세는 기능을 제공하는 라이브러리

from collections import Counter

counter = Counter(['red','blue','red','green','blue','blue'])

# 'blue'가 몇개 있는지 ? 3
print(counter['blue'])
# 'green'이 몇개 있는지 ? 1
print(counter['green'])
# 사전 type으로 변환
print(dict(counter))



