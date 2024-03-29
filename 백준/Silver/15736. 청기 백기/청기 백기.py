# N개의 초록색 조명이 있다. 
# 이 조명은 버튼을 눌러서 초록색 -> 빨간색 -> 초록색으로 바꿀 수 있다.

# 1~N명 까지의 학생들이 나와서 자신의 순서의 배수에 해당하는 조명에 버튼을 눌러서 색을 바꾼다.
# 1번째는 1의 배수 2번째는 2의 배수, 3은 3의 배수 ... N은 N의 배수

# 숫자 N이 주어졌을때 N명의 학생들이 모두 버튼을 누른 뒤 남은 빨간색 조명의 개수는? 

# 조명도 N개 사람도 N명 

# n이 10일때

#   1 2 3 4 5 6 7 8 9 10
#   x x x x x x x x x x 
# 1 o o o o o o o o o o 
# 2   x   x   x   x   x
# 3     x     o     x 
# 4       o       o   
# 5         x         x
# 6           x           
# 7             x           
# 8               x       
# 9                 o       
# 10                  x

# 규칙 -> 제곱수만 남는다!

n = int(input())


# 조명은 한번 누르면 빨, 두번 누르면 초록. 
# -> 홀수는 빨강, 짝수는 초록 
# ** 기호는 파이썬 에서 거듭제곱 연산을 수행하는 연산자.
# **0.5는 변수 n의 제곱근을 계산.
# 0.5를 사용하는 이뉴는 제곱 연산의 역연산을 하기 위해. 

answer = int(n**0.5)
print(answer)