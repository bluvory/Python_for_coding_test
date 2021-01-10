# 볼링공 고르기
# 두 사람이 서로 무게가 다른 볼링공을 고르려고 하는데 두 사람이 볼링공을 고르는 경우의 수

n, m = map(int, input().split())
data = list(map(int, input().split()))

cnt = 0
for i in range(len(data)):
  for j in range(i+1, len(data)):
    if not data[i]==data[j]:
      cnt += 1

print(cnt)