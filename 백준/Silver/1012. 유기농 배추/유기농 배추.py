from collections import deque

T = int(input())

for _ in range(T):
  result = 0
  M, N, K = map(int, input().split())
  land = [[0 for _ in range(N)] for _ in range(M)]
  baechoo = set()
  for _ in range(K):
    x, y = map(int, input().split())
    land[x][y] = 1
    baechoo.add((x, y))

  visited = [[False for _ in range(N)] for _ in range(M)]
  queue = deque()

  while queue or baechoo:
    if len(queue) == 0:
      queue.append(baechoo.pop())
      result += 1
    x, y = queue.popleft()
    for dx, dy in [(-1, 0), (+1, 0), (0, -1), (0, +1)]:
      tx = x + dx
      ty = y + dy
      if 0<=tx<M and 0<=ty<N and not visited[tx][ty] and land[tx][ty]==1:
        baechoo.discard((tx, ty))
        visited[tx][ty] = True
        queue.append((tx, ty))
  
  print(result)