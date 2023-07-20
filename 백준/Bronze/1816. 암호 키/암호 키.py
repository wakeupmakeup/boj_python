# 비밀번호 문제

# 100만보다 작고, 2이상의 약수를 가지고 있다면 틀린 비밀번호!

# 테스트 케이스
number = int(input())

for _ in range(number):
    password = int(input()) # 1000036000099
    
    for i in range(2, 1_000_001):
        if(password % i == 0):  # 나누어 떨어지면 백만 이하의 약수가 존재함.
            print("NO")
            break
        if(i == 1_000_000): # 백만까지 돌았는데 멈추지 않았다 -> 100만 이하의 약수가 존재하지 않는다. 
            print("YES")
            break
    