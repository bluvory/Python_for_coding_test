# 상하좌우
# L왼쪽 R오른쪽 U위 D아래

n = int(input())
data = input().split()

x, y = 1, 1
dx = [0,0,-1,1]
dy = [-1,1,0,0]
move = ['L', 'R', 'U', 'D']

for i in data:
  for j in range(4):
    if i == move[j]:
      nx = x + dx[j]
      ny = y + dy[j]
  if nx < 1 or ny < 1 or nx > n  or ny > n:
    continue
  x, y = nx, ny

print(x, y)

