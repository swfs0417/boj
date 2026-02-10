# BFS 해결
# 1로 표시된 곳부터 각각 BFS(visited 마킹)
# -1 검사안함, 0은 1로 바꾸고 스택에 추가
# 
# 큐가 끝나면 완전히 숙성됐는지 검사


m, n, h = map(int, input().split())

visited = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]

time = -1
stack = [(x, y, z) for z in range(h) for y in range(n) for x in range(m) if visited[z][y][x] == 1]

while stack:
  time += 1
  temp = []
  # print(visited)
  for x, y, z in stack:
    # print(x, y, z)
    if z > 0 and visited[z-1][y][x] == 0:
      temp.append((x, y, z-1))
      visited[z-1][y][x] = 1
    if z < h-1 and visited[z+1][y][x] == 0:
      temp.append((x, y, z+1))
      visited[z+1][y][x] = 1
    if y > 0 and visited[z][y-1][x] == 0:
      temp.append((x, y-1, z))
      visited[z][y-1][x] = 1
    if y < n-1 and visited[z][y+1][x] == 0:
      temp.append((x, y+1, z))
      visited[z][y+1][x] = 1
    if x > 0 and visited[z][y][x-1] == 0:
      temp.append((x-1, y, z))
      visited[z][y][x-1] = 1
    if x < m-1 and visited[z][y][x+1] == 0:
      temp.append((x+1, y, z))
      visited[z][y][x+1] = 1
  stack = temp
# print(visited)
for plane in visited:
  time = -1 if any(0 in row for row in plane) else time

print(time)



