a, b, c = map(int, input().split())
dp = {1: a}
p = 1
while p < b:
  dp[p*2] = (dp[p]**2) % c
  p *= 2

result = 1
for i in range(len(dp)):
  if b >> i & 1:
    result = (result * dp[2**i]) %c
print(result)