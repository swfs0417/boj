n = int(input())
a, b, c = map(int, input().split())

print((a if a < n else n) + (b if b < n else n) + (c if c < n else n))