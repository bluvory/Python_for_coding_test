# 시각: 3이 존재하면 세기
n = int(input())
res = 0
for i in range(n+1):
  for j in range(60):
    for k in range(60):
      if ('3' in str(i) or '3' in str(j) or '3' in str(k)):
        res += 1
print(res)


# 책 답안
if '3' in str(i)+str(j)+str(k)