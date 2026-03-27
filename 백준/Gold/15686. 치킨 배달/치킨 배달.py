n, m = map(int, input().split())
chickens, houses = [], []
for i in range(n):
  line = list(map(int, input().split()))
  for j in range(n):
    if line[j] == 1:
      houses.append((i, j))
    elif line[j] == 2:
      chickens.append((i, j))
chicken_dist = [[abs(h[0] - c[0]) + abs(h[1] - c[1]) for h in houses] for c in chickens]

def choose(m, chosen, remainder):
  if m == 0:
    return [chosen]
  if not remainder:
    return []
  result = []
  result += choose(m - 1, chosen + [remainder[0]], remainder[1:])
  result += choose(m, chosen, remainder[1:])
  return result

chosen = choose(m, [], list(range(len(chickens))))
result = float('inf')
for c in chosen:
  chicken_dist_temp = [chicken_dist[i] for i in c]
  sum_dist = []
  for i in range(len(houses)):
    sum_dist.append(min(chicken_dist_temp[j][i] for j in range(len(chicken_dist_temp))))
  result = min(result, sum(sum_dist))
print(result)