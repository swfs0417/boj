from collections import deque

n, m = map(int, input().split())
nums = (sorted(set(map(int, input().split()))))

def choose(m, choosen, remainder):
  if m == 0:
    return [choosen]
  if not remainder:
    return []
  result = []
  for i in range(len(remainder)):
    result += choose(m - 1, choosen + [remainder[i]], remainder[i:])
  return result

result = choose(m, [], nums)
for r in result:
  print(*r)