val = '0abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
word = input()
result = [val.index(x) for x in word]
# print(result)
result = sum(result)
for i in range(2, int(result**0.5) + 1):
  if result % i == 0:
    print('It is not a prime word.')
    break
else:
  print("It is a prime word.")