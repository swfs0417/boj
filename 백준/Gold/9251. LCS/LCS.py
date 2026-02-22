L1 = input()
L2 = input()

dp = [[0]*(len(L2)+1) for _ in range(len(L1)+1)]

for i in range(1, len(L1)+1):
  for j in range(1, len(L2)+1):
    if L1[i-1] == L2[j-1]:
      dp[i][j] = dp[i-1][j-1] + 1
    else:
      dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(dp[-1][-1])