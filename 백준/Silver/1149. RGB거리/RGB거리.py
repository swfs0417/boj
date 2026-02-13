N = int(input())
cost = [0, 0, 0]

for _ in range(N):
  r, g, b = map(int, input().split())
  temp = [0, 0, 0]
  temp[0] = r + (cost[1] if cost[1] < cost[2] else cost[2])
  temp[1] = g + (cost[0] if cost[0] < cost[2] else cost[2])
  temp[2] = b + (cost[0] if cost[0] < cost[1] else cost[1])
  cost = temp
  # print(cost)

print(min(cost))