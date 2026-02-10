from collections import deque

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
distmap = [[0 for _ in range(m)] for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]
queue = deque()

dest = 0
for y in range(n):
  if 2 in grid[y]:
    dest = (grid[y].index(2), y, 1)
    break
queue.append(dest)
visited[dest[1]][dest[0]] = True

while queue:
  x, y, dist = queue.popleft()
  for nx in [x+1, x-1]:
    if 0 <= nx < m and not visited[y][nx] and grid[y][nx] != 0:
      visited[y][nx] = True
      distmap[y][nx] = dist
      queue.append((nx, y, dist + 1))
  for ny in [y+1, y-1]:
    if 0 <= ny < n and not visited[ny][x] and grid[ny][x] != 0:
      visited[ny][x] = True
      distmap[ny][x] = dist
      queue.append((x, ny, dist + 1))

for y in range(n):
  for x in range(m):
    if visited[y][x] == False and grid[y][x] == 1:
      distmap[y][x] = -1

print('\n'.join(map(lambda x: ' '.join(map(str, x)), distmap)))