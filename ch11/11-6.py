# 다시풀기
# 무지의 먹방 라이브
# https://programmers.co.kr/learn/courses/30/lessons/42891?language=python3
# 무지가 먹방을 시작한 지 K 초 후에 네트워크 장애로 인해 방송이 잠시 중단되었다. 무지는 네트워크 정상화 후 다시 방송을 이어갈 때, 몇 번 음식부터 섭취해야 하는지를 알고자 한다
# food_times 는 각 음식을 모두 먹는데 필요한 시간이 음식의 번호 순서대로 들어있는 배열
# k 는 방송이 중단된 시간
# 만약 더 섭취해야 할 음식이 없다면 -1 반환

def solution(food_times, k):

    answer = 0

    for i in range(k):
      a = i%k
      if food_times[a] == 0:
        a += 1
      food_times[a] -= 1
      answer += 1

    return answer

food_times = list(map(int, input().split()))
k = int(input())

print(solution(food_times, k))