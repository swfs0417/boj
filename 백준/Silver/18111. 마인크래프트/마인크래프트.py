N, M, B = map(int, input().split())
land = []

for _ in range(N):
  land+= list(map(int, input().split()))

result = (float('inf'), -1)
for th in range(min(land), max(land)+1):
  remove, add = 0, 0
  for h in land:
    if h > th:
      remove += (h-th)
    if h < th:
      add += (th-h)
  if remove + B >= add:
    time = remove * 2 + add
    if (time < result[0]) or (result[0]==time and result[1]<th):
      result = (time, th)
      

print(*result)

  