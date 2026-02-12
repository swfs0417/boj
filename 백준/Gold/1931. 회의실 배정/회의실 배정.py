N = int(input())
schedules = sorted([tuple(map(int, input().split())) for _ in range(N)], key=lambda x: (-x[1], -x[0]))
count = 0

while schedules:
  schedule = schedules.pop()
  count += 1
  while schedules:
    if schedules[-1][0] < schedule[1]:
      schedules.pop()
    else:
      break

print(count)