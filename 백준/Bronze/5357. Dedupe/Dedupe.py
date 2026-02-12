n = int(input())
for _ in range(n):
  l = input()
  r=''
  for s in l:
    if r == '' or r[-1] != s:
      r += s
  print(r)