# 떡볶이 떡 만들기
# 파라메트릭 서치 Parametric Search
# 최적화 문제를 결정 문제로 바꾸어 해결하는 기법
# 원하는 조건을 만족하는 가장 알맞은 값을 찾는 문제에 사용

n, m = map(int, input().split())
arr = list(map(int, input().split()))

start = 0
end = max(arr)

res = 0
while (start < end):
  total = 0
  mid = (start + end)//2

  for x in arr:
    if x > mid:
      total += x - mid
  
  if total < m:
    end = mid - 1
  
  else:
    res = mid
    start = mid + 1

print(res)