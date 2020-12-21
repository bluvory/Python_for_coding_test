# 행이 N, 열이 M
# 뽑고자 하는 행 선택
# 선택된 행 들중 숫자가 낮은 카드
# 각 행마다 가장 작은 수를 찾은 뒤에 그 수 중에서 가장 큰 수

n, m = map(int, input().split())
a = 101
min_list = []

for i in range(n):
  data = list(map(int, input().split()))
  if (a > min(data)):
    min_list.append(min(data))

print(max(min_list))


# 책 답안
res = 0
for i in range(n):
  data = list(map(int, input().split()))
  min_value = min(data)
  res = max(res, min_value)
print(res)