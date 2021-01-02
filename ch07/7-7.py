# 부품 찾기
# 집합 자료형 이용

n = int(input())
arr = set(map(int, input().split()))
m = int(input())
find = list(map(int, input().split()))

for i in find:
  if i in arr:
    print("yes", end=' ')
  else:
    print("no", end=' ')