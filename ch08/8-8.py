# 효율적인 화폐 구성
# a_i-k를 만드는 방법이 존재하는 경우 : a_i = min(a_i, a_i-k+1)
# a_i-k를 만드는 방법이 존재하지 않는 경우 : a_i = 10001

n, m = map(int, input().split())

arr = []
for i in range(n):
  arr.append(int(input()))

d = [10001] * (m+1)

d[0] = 0
for i in range(n):
  for j in range(arr[i], m+1):
    if d[j - arr[i]] != 10001:
      d[j] = min(d[j], d[j - arr[i]] + 1)

if d[m] == 10001:
  print(-1)
else:
  print(d[m])