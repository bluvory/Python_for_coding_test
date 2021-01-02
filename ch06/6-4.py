# 퀵 정렬 소스코드

arr = [5,7,9,0,3,1,6,2,4,8]

def quick_sort(arr, start, end):
  if start >= end:
    return

  pivot = start
  left = start + 1
  right = end

  while left <= right:

    # 피벗보다 큰 데이터를 찾을 때까지 반복
    while left <= end and arr[left] <= arr[pivot]:
      left += 1

    # 피벗보다 작은 데이터를 찾을 때까지 반복
    while right > start and arr[right] >= arr[pivot]:
      right -= 1

    # 엇갈렸다면 작은 데이터와 피벗을 교체
    if left > right:
      arr[right], arr[pivot] = arr[pivot], arr[right]

    # 엇갈리지 않았다면 작은 데이터와 큰 데이터를 교체
    else:
      arr[right], arr[left] = arr[left], arr[right]

  # 분할 이후 왼쪽 부분과 오른쪽부분에서 각각 정렬 수행
  quick_sort(arr, start, right-1)
  quick_sort(arr, right+1, end)

quick_sort(arr, 0, len(arr)-1)
print(arr)