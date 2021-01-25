n = int(input())
left = 0
right = 0

for i in range(len(str(n))):
  if i < len(str(n))/2:
    left += int(str(n)[i])
  else:
    right += int(str(n)[i])

if right==left:
  print("LUCKY")
else:
  print("READY")