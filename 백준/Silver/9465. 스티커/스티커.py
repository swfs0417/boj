T = int(input())
for _ in range(T):
  n = int(input())
  stickers = [list(map(int, input().split())) for _ in range(2)]
  dp = [(0, 0) for _ in range(n)]
  for i in range(n):
    up = stickers[0][i] + (dp[i-1][1] if i == 0 or dp[i-1][1] > dp[i-2][1] else dp[i-2][1])
    down = stickers[1][i] + (dp[i-1][0] if i == 0 or dp[i-1][0] > dp[i-2][0] else dp[i-2][0])
    dp[i] = (up, down)
  print(max(dp[-1]))