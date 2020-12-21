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
  target = (n // k) * k
  res += (n - target)
  n = target
  if n < k:
    break
  res += 1
  n //= k

res += (n-1)
print(res)