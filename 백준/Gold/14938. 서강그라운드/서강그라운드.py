import heapq

n, m, r = map(int, input().split())
t = [0] + list(map(int, input().split()))

nodes = {k: [] for k in range(1, n+1)}
for _ in range(r):
  a, b, l = map(int, input().split())
  nodes[a].append((b, l))
  nodes[b].append((a, l))

result = {}

for i in range(1, n+1):
  q = [(0, i)]
  visited = [False] * (n+1)
  visited[i] = True
  items = t[i]
  while q:
    # print(i, q, items)
    dist, edge= heapq.heappop(q)
    if not visited[edge]:
      visited[edge]=True
      items += t[edge]
    for n_edge, n_dist in nodes[edge]:
      if not visited[n_edge] and dist + n_dist <= m:
        heapq.heappush(q, (dist+n_dist, n_edge))
  result[i]=items
# print(result)
print(max(result.values()))