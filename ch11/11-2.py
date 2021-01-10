# 곱하기 혹은 더하기
# 문자열 S가 주어졌을 때, 왼쪽부터 오른쪽으로 하나씩 모든 숫자를 확인하며 숫자 사이에 'x' 혹은 '+' 연산자를 넣어 결과적으로 만들어질 수 있는 가장 큰 수 구하기

s = input()

if (int(s[0])*int(s[1])) > (int(s[0])+int(s[1])):
  res = int(s[0])*int(s[1])
else:
  res = int(s[0])+int(s[1])

for i in range(2, len(s)):
  if (res*int(s[i])) > (res+int(s[i])):
    res *= int(s[i])
  else:
    res += int(s[i])

print(res)