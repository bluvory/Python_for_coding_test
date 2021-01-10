# 만들 수 없는 금액
# N개의 동전을 이요하여 만들 수 없는 양의 정수 금액 중 최솟값을 구하는 프로그램

n = int(input())
data = list(map(int, input().split()))
data.sort()

res = 1
for i in data:
  if res < i:
    print(res, i)
    break
  res += i
  print(res, i)