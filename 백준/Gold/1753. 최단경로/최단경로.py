import heapq

V, E = map(int, input().split())
k = int(input())
edges = [[] for _ in range(V+1)]

for _ in range(E):
  u, v, w = map(int, input().split())
  edges[u].append((v, w))

dists = [float('inf')]*(V+1)
dists[k] = 0
queue = [(0, k)] # (이동거리, 현재 정점)

while queue:
  dist, current = heapq.heappop(queue)
  if dist > dists[current]:
    continue
  
  for v, w in edges[current]:
    new_dist = dist + w
    if new_dist < dists[v]:
      dists[v]= new_dist
      heapq.heappush(queue, (new_dist, v))
      
print(*map(lambda x: str(x).upper(), dists[1:]), sep='\n')
