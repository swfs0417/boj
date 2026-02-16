import sys

sys.setrecursionlimit(10**6)

forwards = list(map(int, sys.stdin.read().strip().split('\n')))

def postorder(start, end):
  if start > end:
    return
  
  root = forwards[start]
  
  # 오른쪽 서브트리 시작점 찾기
  right = start + 1
  while right <= end and forwards[right] < root:
    right += 1
  
  # 후위 순회: 왼쪽 → 오른쪽 → 루트
  postorder(start + 1, right - 1)  # 왼쪽 서브트리
  postorder(right, end)             # 오른쪽 서브트리
  print(root)

postorder(0, len(forwards) - 1)
