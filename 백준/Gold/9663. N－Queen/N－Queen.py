n = int(input())

result = 0
col = [0] * n
d1 = [0]*(2*n-1) # /
d2 = [0]*(2*n-1) # \

def dfs(row):
  global result
  if row == n:
    result += 1
    return
  for c in range(n):
    if not col[c] and not d1[row+c] and not d2[row-c+n-1]:
      col[c] = d1[row+c] = d2[row-c+n-1] = 1
      dfs(row+1)
      col[c] = d1[row+c] = d2[row-c+n-1] = 0

dfs(0)
print(result)