list = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
time = 0
N = input() # 기본 input은 문자열로 인식한다. 

# 한글자씩 분해하여 하나하나 숫자와 대입시켜야한다. 어떻게 해야할까? 

for i in list:
    for j in i: # 리스트에서 각 요소를 꺼내 한글자씩 분리함. 
        for k in N: #입력받은 문자를 하나씩 분리하기. 
            if j == k: #두 문자가 같다면 밑에를 실행한다
                time += list.index(i) + 3 
print(time)

