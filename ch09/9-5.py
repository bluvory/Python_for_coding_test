# 전보
# n개의 도시 존재
# x라는 도시에서 y라는 도시로 전보를 보내고사 한다면 도시 x에서 y로 향하는 통로가 설치되어 있어야한다
# c라는 도시에서 위급 상황이 발생했는데 최대한 많이 퍼져나가게 하고싶을 때, 메시지를 받게 되는 도시의 개수는 총 몇개이며 도시들이 모두 메시지를 받는 데까지 걸리는 시간은 얼마인지 계산하는 프로그램

import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

n, m, start = map(int, input().split())
graph = [[] for i in range(n+1)]
distance = [INF]*(n+1)

for _ in range(m):
  x, y, z = map(int, input().split())
  graph[x].append((y, z))

def dijkstra(start):
  q = []
  heapq.heappush(q, (0, start))
  distance[start] = 0

  while q:
    dist, now = heapq.heappop(q)
    if distance[now] < dist:
      continue

    for i in graph[now]:
      cost = dist + i[1]
      if cost < distance[i[0]]:
        distance[i[0]] = cost
        heapq.heappush(q, (cost, i[0]))

dijkstra(start)

cnt = 0
max_distance = 0
for d in distance:
  if d != INF:
    cnt += 1
    max_distance = max(max_distance, d)

print(cnt-1, max_distance)