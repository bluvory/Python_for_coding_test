# 이진 탐색 Binary Search
# 찾으려는 데이터와 중간점 위치에 있는 데이터를 반복적으로 비교

# 반복문으로 구현한 이진 탐색 소스코드

def binary_search(arr, target, start, end):

  while start <= end:
    mid = (start + end) // 2

    # 찾은 경우 중간점 인덱스 반환
    if arr[mid] == target:
      return mid
    
    # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
    elif arr[mid] > target:
      end = mid-1

    # 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
    else:
      start = mid+1
      
  return None

# n(원소의 개수)과 target(찾고자 하는 문자열)을 입력
n, target = list(map(int, input().split()))
# 전체 원소 입력
arr = list(map(int, input().split()))

# 이진 탐색 수행 결과 출력
res = binary_search(arr, target, 0, n-1)
if res == None:
  print("원소가 존재하지 않습니다")
else:
  print(res+1)