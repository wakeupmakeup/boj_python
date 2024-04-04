''' 
문제 간략화

1.  현재 Queue의 가장 앞에 있는 문서의 ‘중요도’를 확인한다.

2.  나머지 문서들 중 현재 문서보다 중요도가 높은 문서가 하나라도 있다면, 
    이 문서를 인쇄하지 않고 Queue의 가장 뒤에 재배치 한다. 
    그렇지 않다면 바로 인쇄를 한다.

    필요한 것

    1. 파이썬 큐 사용법
    

'''

from collections import deque
import sys

t = int(input())

for i in range(t):
    n, m = map(int, input().split())
    queue = deque(list(map(int, sys.stdin.readline().split())))
    count = 0
    while queue:
        best = max(queue)  #현재의 최댓값이 가장 먼저 배출되므로 최댓값을 저장
        front = queue.popleft() # 큐의 front를 뽑았으므로
        m -= 1 # 내 위치가 한 칸 당겨진다.

        if best == front: # 뽑은 숫자가 제일 큰 숫자일 때
            count += 1 # 하나가 영원히 배출되므로 순번 하나 추가
            if m < 0: # m이 0이라는 것은 뽑은 숫자가 내 숫자라는 뜻.
                print(count)
                break

        else:   # 뽑은 숫자가 제일 큰 숫자가 아니면
            queue.append(front) # 제일 뒤로 밀려나게 됨
            if m < 0 :  # 제일 앞에서 뽑히면
                m = len(queue) - 1 # 제일 뒤로 이동