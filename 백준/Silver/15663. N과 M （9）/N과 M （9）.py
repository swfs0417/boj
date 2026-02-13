from collections import deque

N, M = map(int, input().split())
A = sorted(list(map(int, input().split())))

queue = deque()
result = set()


def search(remain_depth, remain_elements, selected):
  if remain_depth == 0:
    result.add(tuple(selected))
    return
  for i in range(len(remain_elements)):
    search(
      remain_depth - 1,
      remain_elements[:i]+remain_elements[i + 1 :],
      selected + [remain_elements[i]],
    )

search(M, A, [])
print(*map(lambda x: ' '.join(map(str, x)), sorted(list(result))), sep='\n')
