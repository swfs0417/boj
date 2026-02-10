n = int(input())

# 1칸 전진 or 2칸 전진
# n = n-1 + n-2
template = []
template.append(1)
template.append(1)
for i in range(2, n+1):
  template.append(template[i-1] + template[i-2])

print(template[n]%10007)