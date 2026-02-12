from collections import deque

e = int(input())
n = int(input())
nodes = {i: [] for i in range(1, e+1)}
for _ in range(n):
  a, b = map(int, input().split())
  nodes[a].append(b)
  nodes[b].append(a)

queue = deque([1])
visited = [1]
while queue:
  edge = queue.popleft()
  for next in nodes[edge]:
    if next not in visited:
      visited.append(next)
      queue.append(next)

print(len(visited)-1)