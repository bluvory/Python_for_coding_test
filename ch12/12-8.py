data = input()
data = sorted(list(data))

res = 0
for i in data:
  if '0' <= i <= '9':
    res += int(i)

print(''.join(data)+str(res))