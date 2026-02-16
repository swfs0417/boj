from collections import deque


n, k = map(int, input().split())

queue = deque([(n, 0)])
visited = [False]*100001
while queue:
  point, dist = queue.popleft()
  visited[point] = True
  if point == k:
    print(dist)
    break
  if 0<=point*2<=100000 and not visited[point*2]:
    queue.appendleft((point*2, dist))
  for i in [+1, -1]:
    if 0<=point+i<=100000 and not visited[point+i]:
      queue.append((point+i, dist+1))



