N, M = map(int, input().split())
table = []
for _ in range(N):
  l = list(map(int, input().split()))
  temp = []
  for i in range(N):
    if temp:
      if table:
        temp.append(table[-1][i]+temp[-1]-(0 if i-1 < 0 else table[-1][i-1])+l[i])
      else:
        temp.append(temp[-1]+l[i])
    else:
      if table:
        temp.append(table[-1][i]+l[i])
      else:
        temp.append(l[i])
  table.append(temp)
for _ in range(M):
  y1, x1, y2, x2 = map(lambda x: int(x)-1, input().split())
  s = table[y2][x2]
  if x1 > 0 and y1 > 0:
    s += table[y1-1][x1-1]
  if y1 > 0:
    s -= table[y1-1][x2]
  if x1 > 0:
    s -= table[y2][x1-1]
  print(s)