import heapq
import sys

input = sys.stdin.readline

n = int(input())
m = int(input())

edges = {i: {} for i in range(1, n+1)}
dist = [[float('inf')]*(n+1) for _ in range(n+1)]

for _ in range(m):
  a, b, c = map(int, input().split())
  edges[a][b] = c if b not in edges[a] or c < edges[a][b] else edges[a][b]


for i in range(1, n+1):
  queue = list(map(lambda x: (edges[i][x], x), edges[i]))
  heapq.heapify(queue)
  visited = [False for _ in range(n+1)]
  dist[i][i] = 0
  visited[i] = True
  while queue:
    w, v = heapq.heappop(queue)
    if not visited[v]:
      dist[i][v] = w
      visited[v] = True
    for node, weight in edges[v].items():
      if not visited[node]:
        heapq.heappush(queue, (w + weight, node))

for line in dist[1:]:
  line = map(lambda x: 0 if x == float('inf') else x, line[1:])
  print(*line)


