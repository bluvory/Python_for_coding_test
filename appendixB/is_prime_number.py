# 소수의 판별
# 2보다 큰 자연수 중에서 1과 자기 자신을 제외한 자연수로는 나누어떨어지지 않는 자연수

import math

def is_prime_number(x):
  for i in range(2, x):
  # for i in range(2, int(math.sqrt(x)) + 1):
    if x%i == 0:
      return False
  return True

print(is_prime_number(4))
print(is_prime_number(7))