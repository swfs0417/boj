import heapq

N, M, X = map(int, input().split())
nodes = {i: [] for i in range(1, N+1)}

for _ in range(M):
  u, v, w = map(int, input().split())
  nodes[u].append((w, v))

dist = [[float('inf')]*(N+1) for _ in range(N+1)]

for i in range(1, N+1):
  queue = nodes[i][:]
  heapq.heapify(queue)
  visited = [False for _ in range(N+1)]
  dist[i][i] = 0
  visited[i] = True
  while queue:
    w, v = heapq.heappop(queue)
    if not visited[v]:
      dist[i][v] = w
      visited[v] = True
      if i != X and v == X:
        break
    for weight, node in nodes[v]:
      if not visited[node]:
        heapq.heappush(queue, (w + weight, node))

result = 0
for i in range(1, N+1):
  if i == X:
    continue
  result = max(result, dist[i][X]+dist[X][i])
print(result)