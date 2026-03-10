import heapq

n, m = map(int, input().split())
board = [list(map(int, input())) for _ in range(n)]
result = -1
bfs_queue = [(1, 0, 0, False)] # (dist, x, y, breaked)
visited = [[[False]*2 for _ in range(m)] for _ in range(n)]
visited[0][0][0]=True
while bfs_queue and result == -1:
  dist, x, y, breaked = heapq.heappop(bfs_queue)
  # print(dist, x, y, breaked)
  for dx, dy in [(0, 1), (0, -1), (1, 0), (-1,0)]:
    nx, ny = x + dx, y + dy
    if not (0 <= nx < n and 0 <= ny < m):
      continue
    if board[nx][ny] == 1 and not breaked:
      if not visited[nx][ny][1]:
        if nx==n-1 and ny==m-1:
          result = dist + 1
        heapq.heappush(bfs_queue, (dist + 1, nx, ny, True))
        visited[nx][ny][1]=True
    if board[nx][ny] == 0:
      b = int(breaked)
      if not visited[nx][ny][b]:
        if nx==n-1 and ny==m-1:
          result = dist + 1
        heapq.heappush(bfs_queue, (dist+1, nx, ny, breaked))
        visited[nx][ny][b]=True
if n == m == 1:
  result = 1
print(result)