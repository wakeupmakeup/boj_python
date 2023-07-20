''' 1. 남는 사탕이 없어야 한다. 
    2. A는 B보다 2개 이상 많은 사탕을 가져야 한다.
    3. 셋 중 사탕을 하나도 못 받는 친구는 없어야 한다.
    4. C가 받는 사탕의 수는 짝수다. 
'''

num = int(input()) #6
answer = 0

for A in range(0, num+1):  # A에게 줄 수 있는 사탕은 0~6개
    for B in range(0, num+1):  # B에게 줄 수 있는 사탕은 0~6개
        for C in range(0, num+1): # C에게 줄 수 있는 사탕은 0~6개
            if A+B+C == num: # 6개 이상으로 줄 수는 없으니 나눠준 사탕을 모두 합치면 6개여야 한다. (1번 조건)
                if A >= B+2: # 2번 조건
                    if A != 0 and B != 0 and C != 0:  # 3번 조건
                        if C % 2 == 0:  # 4번 조건
                            answer += 1

print(answer)
                        
    