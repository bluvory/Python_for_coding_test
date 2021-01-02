# 정렬 라이브러리에서 key를 활용한 소스코드
# key 값 = 정렬 기준

arr = [('바나나', 2), ('사과', 5), ('당근', 3)]

def setting(data):
  return data[1]

res = sorted(arr, key=setting)
print(res)