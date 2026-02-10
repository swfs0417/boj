# BFS 해결
# 1로 표시된 곳부터 각각 BFS(visited 마킹)
# -1 검사안함, 0은 1로 바꾸고 스택에 추가
# 
# 큐가 끝나면 완전히 숙성됐는지 검사


m, n = map(int, input().split())

visited = [list(map(int, input().split())) for _ in range(n)]

time = -1
stack = [(x, y) for x in range(n) for y in range(m) if visited[x][y] == 1] # (x, y)

while stack:
  time += 1
  temp = []
  for x, y in stack:
    if x > 0 and visited[x-1][y] == 0:
      temp.append((x-1, y))
      visited[x-1][y] = 1
    if x < n-1 and visited[x+1][y] == 0:
      temp.append((x+1, y))
      visited[x+1][y] = 1
    if y > 0 and visited[x][y-1] == 0:
      temp.append((x, y-1))
      visited[x][y-1] = 1
    if y < m-1 and visited[x][y+1] == 0:
      temp.append((x, y+1))
      visited[x][y+1] = 1
  stack = temp
time = -1 if any(0 in row for row in visited) else time

print(time)



