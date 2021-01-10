# 모험가 길드
# 공포도가 X인 모험가는 반드시 X명 이상으로 구성된 모험가 그룹에 참여해야 여행을 떠날 수 있도록 지정했을 때 여행을 떠날 수 있는 그룹 수의 최댓값 구하기

n = int(input())
data = list(map(int, input().split()))

data.sort()
cnt = 0

while True:

  if len(data) == 0:
    break

  a = data[-1]

  if len(data) < a:
    break

  else:
    data = data[a-2:-2]
    cnt += 1

print(cnt)