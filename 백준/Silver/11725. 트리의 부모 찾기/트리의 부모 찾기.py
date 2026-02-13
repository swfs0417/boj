from collections import deque

n = int(input())
edges = {i:[] for i in range(1, n+1)}
for _ in range(n-1):
  a, b = map(int, input().split())
  edges[a].append(b)
  edges[b].append(a)

visited = [False for _ in range(n)]
queue = deque([1])
parents = [0 for _ in range(n)]
while queue:
  p = queue.popleft()
  visited[p-1] = True
  for nxt in edges[p]:
    if not visited[nxt-1]:
      parents[nxt-1] = p
      queue.append(nxt)

print('\n'.join(map(str, parents[1:])))