import sys

input = sys.stdin.readline

n,k = map(int,input().rstrip().split())

nums = list(map(int,input().rstrip().split()))

each = 0
# K개를 더해주기
for i in range(k):
    each += nums[i]
maxv = each

# 다음 인덱스 더해주고, 이전 인덱스 빼기
for i in range(k,n):
    each += nums[i]
    each -= nums[i-k]
    maxv = max(maxv,each)
    
    
print(maxv)

    



