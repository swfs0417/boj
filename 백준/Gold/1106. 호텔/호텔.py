C, N = map(int, input().split())
costs = {}

for _ in range(N):
  c, p = map(int, input().split())
  if p in costs:
    costs[p] = c if costs[p] > c else costs[p]
  else:
    costs[p] = c

dp = {customer: cost for customer, cost in costs.items()}
for i in range(1, C+max(costs)+1):
  for customer in costs:
    if (i-customer) not in dp:
      continue
    if i not in dp:
      dp[i] = dp[i-customer] + costs[customer]
    else:
      dp[i] = min(dp[i], dp[i-customer] + costs[customer])
print(min([dp[i] for i in range(C, C+max(costs)+1) if i in dp]))