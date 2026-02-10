from collections import deque
N, M = map(int, input().split())
relation = [[0 for _ in range(N)] for _ in range(N)]

for _ in range(M):
  x, y = map(int, input().split())
  relation[x-1][y-1] = relation[y-1][x-1] = 1
bacon = [[-1 for _ in range(N)] for _ in range(N)]

for i in range(N):
  queue = deque()
  visited = [-1 for _ in range(N)]
  dist = 1
  for j in range(N):
    if relation[i][j] == 1:
      queue.append((j, dist))
      visited[j] = dist
  while queue:
    node, dist = queue.popleft()
    for x in range(N):
      if relation[node][x] == 1 and visited[x] == -1:
        visited[x] = dist + 1
        queue.append((x, dist + 1))
  bacon[i] = visited

bacon = list(map(sum, bacon))
result = (N**3, -1)
for i in range(N):
  if result[0] > bacon[i]:
    result = (bacon[i], i)

print(result[1]+1)