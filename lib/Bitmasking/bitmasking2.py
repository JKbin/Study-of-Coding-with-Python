    # 부분 집합 연습 - 두 수의 합이 7인 경우의 수
n = 6
arr = [1, 2, 3, 4, 5, 6]

def solve():
    ret = 0
    for i in range(1 << n):
        print(bin(i))
        if bin(i).count('1') != 2:
            continue
        sum = 0
        for j in range(n):
            if i & 1 << j:
                sum += arr[j]
        if sum == 7:
            ret += 1
            
    return ret

print(solve())



