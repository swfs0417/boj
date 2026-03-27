n = int(input())
max_score = [0, 0, 0]
min_score = [0, 0, 0]
for _ in range(n):
  line = tuple(map(int, input().split()))
  # print(min_score, max_score)
  min_score = [min(min_score[:2]) + line[0], min(min_score) + line[1], min(min_score[1:3]) + line[2]]
  max_score = [max(max_score[:2]) + line[0], max(max_score) + line[1], max(max_score[1:3]) + line[2]]

print(max(max_score), min(min_score))