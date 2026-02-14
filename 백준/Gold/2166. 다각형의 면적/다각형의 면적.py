# https://mathworld.wolfram.com/PolygonArea.html 참조
n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
points += [points[0]]
s = 0
for i in range(n):
  s += points[i][0] * points[i+1][1] - points[i][1] * points[i+1][0]
s = -s if s < 0 else s
print(f'{round(s/2, 2):.1f}')