import math
""" 나의 논리
먼저 팩토리얼을 구한다.
그런 후 그것을 문자열로 해서 뒤에서부터 0이 몇개인지 센다.
개수를 출력한다. """

n = int(input())
result = 0

pNum = math.factorial(n)


for i in str(pNum)[::-1] : # [::-1]이 뜻은 역순으로 하나씩 선택하라는 의미 [시작인덱스:끝인덱스:간격]이다. 
    if i == '0':
        result += 1
    else:
        break

print(result)








