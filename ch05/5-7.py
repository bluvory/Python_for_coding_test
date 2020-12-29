# 탐색 알고리즘 - 깊이우선탐색 DFS
# 그래프에서 깊은 부분을 우선적으로 탐색하는 알고리즘
# 인접 리스트: 리스트로 그래프의 연결 관계를 표현하는 방식

# 인접 리스트 방식 예제
graph = [[] for _ in range(3)]

# 노드에 연결된 노드 정보 저장 (노드, 거리)
graph[0].append((1, 7))
graph[0].append((2, 5))
graph[1].append((0, 7))
graph[2].append((0, 5))

print(graph)