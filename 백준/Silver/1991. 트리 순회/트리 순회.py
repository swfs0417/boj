n = int(input())
childs = {}

for _ in range(n):
  root, left, right = input().split()
  childs[root] = (left, right)

a = []
def dfs_a(node):
  a.append(node)
  if childs[node][0] != '.':
    dfs_a(childs[node][0])
  if childs[node][1] != '.':
    dfs_a(childs[node][1])

b = []

def dfs_b(node):
  if childs[node][0] != '.':
    dfs_b(childs[node][0])
  b.append(node)
  if childs[node][1] != '.':
    dfs_b(childs[node][1])

c = []

def dfs_c(node):
  if childs[node][0] != '.':
    dfs_c(childs[node][0])
  if childs[node][1] != '.':
    dfs_c(childs[node][1])
  c.append(node)

dfs_a('A')
dfs_b('A')
dfs_c('A')
print(''.join(a))
print(''.join(b))
print(''.join(c))
