N = int(input())

paper = [list(map(int, input().split())) for _ in range(N)]

def color(paper, x1, x2, y1, y2):
  temp = set(sum([paper[i][x1:x2] for i in range(y1, y2)], []))
  if len(temp) == 1:
    c = temp.pop()
    return (0, 1) if c else (1, 0)
  else:
    l = (x2-x1)//2
    a, b = (0, 0)
    for dx1, dx2, dy1, dy2 in [(0, l, 0, l), (0, l, l, l*2), (l, l*2, 0, l), (l, l*2, l, l*2)]:
      # print(x1+dx1, x1+dx2, y1+dy1, y1+dy2)
      r = color(paper, x1+dx1, x1+dx2, y1+dy1, y1+dy2)
      a += r[0]
      b += r[1]
    return (a, b)

print(*color(paper, 0, N, 0, N), sep='\n')
