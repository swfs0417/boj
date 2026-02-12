N, r, c = map(int, input().split())
row = [0]
for i in range(N):
  row += [j+4**i for j in row]
col = [i*2 for i in row]
# print(row, col)
print(row[c] + col[r])