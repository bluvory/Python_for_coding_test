# 피보나치 함수 소스코드
# x가 커지면 수행 시간이 기하급수적으로 늘어남
# 동일한 함수가 반복적으로 호출되기 때문

def fibo(x):
  if x==1 or x==2:
    return 1
  return fibo(x-1)+fibo(x-2)

print(fibo(4))