n = int(input())
dp = []

for i in range(n):
  nums = list(map(int, input().split()))
  # print(dp)
  if len(dp) == 0:
    dp = nums
    continue
  temp = [0]*(i+1)
  for j in range(i):
    temp[j] = dp[j] + nums[j] if temp[j] < dp[j] + nums[j] else temp[j]
    temp[j+1] = dp[j] + nums[j+1]
  dp = temp
print(max(dp))