n, k = map(int, input().split())
l = 100001
visited = [0 for _ in range(l)]
visited[n] = 0
queue = [n]
time = 0
while visited[k] == 0 and n != k:
  time += 1
  temp = []
  for x in queue:
    if x > 0 and visited[x-1] == 0:
      visited[x-1]=time
      temp.append(x-1)
    if x+1 < l and visited[x+1] == 0:
      visited[x+1]=time
      temp.append(x+1)
    if x*2 < l and visited[x*2] == 0:
      visited[x*2]=time
      temp.append(x*2)
  queue = temp

print(visited[k])