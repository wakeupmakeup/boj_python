#1407, 2247

# 아이디어 1
# 20! = 20*19*18*17*16 ... * 1
# 그러면 20!에는 2가 몇번 곱해져 있을까?

# 일단! 완전 탐색을 시도해 보자. 

# 1  2  3  4  5  6  7  8  9  10
#    1     2     1     3      1

# 11 12 13 14 15 16 17 18 19 20
#    2      1    4     1     2

# 여기 아랫 숫자를 전부 더하면 2가 몇번 곱해져있는지 알 수 있다. 
# 총 18이라는 숫자가 나왔다. 

# 이제 완전 탐색이 아니라 정수론으로 최적화를 해야하는데 어떻게 할까? 
# 일단 2로 나누어지는 숫자를 표시한다. 
# 그다음 4로 나눠지는 수도 표시 
# 그다음 8
# 그다음 20보다 작은 2의 제곱수인 16

# 다시 해보자. 
# 1 2 3 4 5 6 7 8 9 10
#   o   o   o   o   o (2)
#       o       o     (4)
#               o     (8)

# 11 12 13 14 15 16 17 18 19 20 
#    o     o     o      o     o (2)
#    o           o            o (4)
#                o              (8)
#                o              (16)

# 여기서 o 갯수를 다 더하면 18이 똑같이 나온다. 

# 신기한점은 20을 2,4,8,16으로 각각 나눴을때 나오는 몫(소수점 제외)을 전부 더하면 똑같이 18이 나온다. 


# 문제를 보면
# 2 176 177

''' 여기서 176과 177는 수의 범위다. 
그리고 2는 이 범위안에서 있는 수들이 2의 배수가 몇개인지 물어보는 문제이다. 
이것을 위와 같은 방식으로 생각하는 연습을 해보자. 

먼저 177이라는 숫자는 2로 나누어 지지 못한다(홀수이므로) 그래서 1로 나누어 떨어짐.
176은 2로 나눌 수 있음.
-> 2의 제곱수에서 각각 나누어 지는 제곱수에서 가장 큰 숫자를 구하고 더하면 된다. (예시 16 + 1 = 17)

-> 177!안에 2의 배수가 몇개있는지 구하고 175!의 2의 배수가 몇번 포함되어있는지 구하고 빼주면 된다.

-> 176 177 178... 하나하나 확인 하지 않고 
176을 2의 제곱수로 여러번 나눠서 더하고 1억을 2의 제곱수로 여러번 나눠더 더하고 
이 양 값을 빼면 된다. 
'''

a, b = map(int, input().split())

a -= 1
temp_a = 0

# 1로 나눴을때 값을 더하자.
temp_a += a 
# 이 작업이 위에서 했던 (2**0)으로 나눠지는 수의 갯수를 다 더한것. 
# 일단은 다 1이라고 생각하는 부분이 윗 부분

# 그리고 순서대로 2,4,8,16으로 돌자. 
for i in range(1, 99):
    temp_a += (a//(2**i))*((2**i)-(2**(i-1)))
    
temp_b = b

for i in range(1,99):
    temp_b += (b//(2**i))*((2**i)-(2**(i-1)))
    
print(temp_b - temp_a)