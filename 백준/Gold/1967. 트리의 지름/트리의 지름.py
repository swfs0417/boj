import sys

n = int(input())
if n == 1:
  print(0)
  sys.exit(0)

sys.setrecursionlimit(10010)

edges = {}
for _ in range(n-1):
  u, v, w = map(int, input().split())
  if u not in edges:
    edges[u] = []
  if v not in edges:
    edges[v] = []
  edges[u].append((w, v))
  edges[v].append((w, u))


def dfs(w, u):
  dists = [(w, u)]
  for weight, nxt in edges[u]:
    if nxt not in visited:
      visited.add(nxt)
      dists += dfs(w+weight, nxt)
  return dists


visited = set([1])
first = max(dfs(0, 1))[1]
visited = set([first])
result = max(dfs(0, first))
print(result[0])