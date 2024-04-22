from collections import deque

def roundUp(x):
    if(x - int(x)) >= 0.5:
        return int(x) + 1
    else :
        return int(x)


n = int(input())
levels = deque([])

for i in range(n):
    number = int(input())
    levels.append(number)

temp = list(levels)
sorted_levels = deque(sorted(temp))

# 절사평균 구하기
firstAvr = len(sorted_levels) * 0.15
firstResult = roundUp(firstAvr)

# 첫 절사 평균대로 위 아래 자르기
for i in range(firstResult):
    if(sorted_levels):
        sorted_levels.popleft()
    if(sorted_levels):
        sorted_levels.pop()
 

# 자른 결과 평균 구하기
if (len(sorted_levels)) > 0:
    secondAvr = sum(sorted_levels) / len(sorted_levels)
else: secondAvr = 0


# 평균 결과 반올림 하기
totalResult = roundUp(secondAvr)

print(totalResult)

