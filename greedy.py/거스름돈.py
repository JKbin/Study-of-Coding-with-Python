# 500, 100, 50, 10 동전이 있을 때 최소로 거슬러주는 동전의 개수는?

n = 1260
count = 0

array = [500, 100, 50, 10]

for coin in array:
    count += n // coin
    n %= coin
    
print(count)
