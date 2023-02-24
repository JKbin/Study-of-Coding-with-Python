import sys

# 정렬, 투포인터

input = sys.stdin.readline

#n = int(input().rstrip())
#arr = list(map(int, input().rstrip().split()))

n = 10
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]          # 8

#n = 4   
#arr = [1, 1, 2, 3]                              # 2

#n = 5
#arr = [-1, 1, 6, 6, 7]                          # 3

ans = 0
n = len(arr)
arr.sort()

for i in range(n):
    temp_list = arr[:i] + arr[i+1:]     # 해당 번호 제외하고 리스트
    target_number = arr[i]
    
    left, right = 0, len(temp_list) - 1
    
    while left < right:
        sum_number = temp_list[left] + temp_list[right]
        
        if sum_number == target_number:
            ans += 1
            break
        elif sum_number > target_number:        # target 넘버가 작으면
            right -= 1
        elif sum_number < target_number:        # target 넘버가 크면
            left += 1

print(ans)
            

    
    