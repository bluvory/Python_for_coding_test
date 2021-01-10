# 미래 도시
# A는 1번 회사에서 출발하여 K번 회사를 방문한 뒤 X번 회사로 가는 것이 목표
# 가능한 한 빠르게 이동하고자 할 때, A가 회사 사이를 이동하게 되는 최소 시간을 계산하는 프로그램

INF = int(1e9)

# 노드의 개수와 간선의 개수 입력받기
n, m = map(int, input().split())

graph = [[INF]*(n+1) for _ in range(n+1)]

for a in range(1, n+1):
  for b in range(1, n+1):
    if a == b:
      graph[a][b] = 0


# 각 간선에 대한 정보 입력받기
for _ in range(m):
  a, b = map(int, input().split())
  graph[a][b] = 1
  graph[b][a] = 1


# 거쳐 갈 노드 x와 최종 목적지 노드 k 입력받기
x, k = map(int, input().split())


# 점화식에 따라 플로이드 워셜 알고리즘 수행
for k in range(1, n+1):
  for a in range(1, n+1):
    for b in range(1, n+1):
      graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

distance = graph[1][k] + graph[k][x]

if distance >= INF:
  print(-1)
else:
  print(distance)