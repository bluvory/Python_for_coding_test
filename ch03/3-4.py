# 1이 될 때까지
# 최대한 많이 나누기

n, k = map(int, input().split())
res = 0

while True:
  if (n % k == 0):
    n /= k
    res += 1
  else:
    n -= 1
    res += 1
  if (n < k):
    break

if (n<k):
  res += int(n) - 1

print(res)


# 책 답안
while True:
  # (n == k로 나누어떨어지는 수)가 될때까지 1빼기
  target = (n // k) * k
  res += (n - target)

  # n이 k보다 작을 때 반복문 탈출
  n = target
  if n < k:
    break

  # k로 나누기
  res += 1
  n //= k

res += (n-1)
print(res)