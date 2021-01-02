# 두 배열의 원소 교체
# 배열 A에서 가장 작은 원소를 골라서, 배열 B에서 가장 큰 원소와 교체
# 단 배열 A에서 가장 작은 원소 < 배열 B에서 가장 큰 원소일 경우에만

n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort(reverse=True)

for i in range(k):
  if a[i] < b[i]:
    a[i], b[i] = b[i], a[i]
  else:
    break

print(sum(a))