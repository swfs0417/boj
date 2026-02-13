n = int(input())
A = list(map(int, input().split()))

d = [1 for _ in range(n)]

for i in range(n):
  m = 1
  for j in range(i):
    # print(i, d[j], A[j], d[i], A[i])
    if A[j] < A[i] and d[j] + 1 > m:
      m = d[j] + 1
  d[i] = m
print(max(d))