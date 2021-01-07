# 부품 찾기
# 계수 정렬 이용

n = int(input())
arr = list(map(int, input().split()))
cnt = [0]*(max(arr)+1)

for i in range(len(arr)):
  cnt[arr[i]] += 1

m = int(input())
find = list(map(int, input().split()))

for i in find:
  if cnt[i] == 1:
    print('yes', end=' ')
  else:
    print('no', end=' ')