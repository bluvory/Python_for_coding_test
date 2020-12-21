# 큰 수의 법칙
n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
a = data[-1]
b = data[-2]

res = 0
x = m // k
res = a * (m-x) + b * x

print(res)


# 책 답안
cnt = int(m / (k + 1)) * k
cnt += m % (k + 1)
res = 0
res += cnt*a
res += (m-cnt)*b
print(res)