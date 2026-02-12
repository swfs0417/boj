import sys

input = lambda: sys.stdin.readline().strip()

i = 1
while True:
  l = list(map(int, input().split()))
  if l[-1]==l[0]==0:
    break
  print(f'Case {i}: Sorting... done!')
  i+=1

