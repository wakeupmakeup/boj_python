n = int(input())
text = "int"

# n은 항상 4의 배수이다.
# 4가 곱해진 수 만큼 long이 반복해서 출력되어야 한다.
# 마지막은 항상 int 여야 한다.
# 4가 곱해진 수 만큼을 어떻게 표현할까?
# 입력값을 4로 나눈 몫만큼 반복하고 싶다. 이걸 어떻게 하지?

for i in range(n//4):
    text = 'long ' + text
print(text)

