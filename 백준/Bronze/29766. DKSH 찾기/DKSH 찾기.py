s = input()
r = 0
while "DKSH" in s:
  s = s.replace('DKSH', '', 1)
  r += 1
print(r)