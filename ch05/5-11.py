# 미로 탈출
# 첫째 줄에 최소 이동 칸의 개수를 출력

from collections import deque

n, m = map(int, input().split())

graph = []
for _ in range(n):
  graph.append(list(map(int, input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
  queue = deque()
  queue.append((x, y))
  while queue:
    x, y = queue.popleft()

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      # 미로 찾기 공간 벗어난 경우
      if nx<0 or nx>=n or ny<0 or ny>=m:
        continue

      # 벽인 경우
      if graph[nx][ny] == 0:
        continue
      
      # 해당 노드를 처음 방문하는 경우에만 최단 거리 기록
      if graph[nx][ny] == 1:
        graph[nx][ny] = graph[x][y] + 1
        queue.append((nx, ny))

  return graph[n-1][m-1]

print(bfs(0, 0))
