data = input()
data = sorted(list(data))

res = 0
for i in data:
  if '0' <= i <= '9':
    res += int(i)

for i in range(len(data)-1, -1, -1):
  if '0' <= data[i] <= '9':
    data.remove(data[i])

print(''.join(data)+str(res))