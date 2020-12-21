# 거스름돈
# Greedy: 현재 상황에서 지금 당장 좋은 것만 고르는 방법

n = 1260
cnt = 0

# 큰 단위의 화폐부터 차례대로 확인
coin_types = [500, 100, 50, 10]

for coin in coin_types:
  cnt += n // coin
  n %= coin

print(cnt)

# 가지고 있는 동전 중에서 큰 단위가 항상 작은 단위의 배수이므로
# 작은 단위의 동전들을 종합해 다른 해가 나올 수 없다