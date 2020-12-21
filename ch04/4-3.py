# 왕실의 나이트

a = input()
x = int(ord(a[0]) - 96)
y = int(a[1])
steps = [(-2,-1), (-1,-2), (1,-2), (2,-1), (2,1), (1,2), (-1,2), (-2,1)]

res = 0
for step in steps:
  nx, ny = x, y
  nx = x + step[0]
  ny = y + step[1]
  if (1 <= nx <= 8) and (1 <= ny <= 8):
    res += 1

print(res)
