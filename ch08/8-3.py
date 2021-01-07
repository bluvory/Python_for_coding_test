# 분할 정복 Divide and Conquer 알고리즘
# 탑다운 Top-Down 방식 (하향식)
# 재귀 함수를 이용하여 다이나믹 프로그래밍 소스코드를 작성하는 방법은 큰 문제를 해결하기 위해 작은 문제를 호출한다

# 호출되는 함수 확인
d = [0]*100

def pibo(x):
  print('f('+str(x)+')', end=' ')
  if x==1 or x==2:
    return 1
  if d[x] != 0:
    return d[x]
  d[x] = pibo(x-1) + pibo(x-2)
  return d[x]

pibo(6)