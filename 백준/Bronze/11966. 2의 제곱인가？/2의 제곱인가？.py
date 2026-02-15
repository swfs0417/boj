n = int(input())
i = 2
while n != 1:
  if n % 2 == 0:
    n //= 2
  else:
    print(0)
    break
else:
  print(1)