'''
소문자로만 이뤄진 단어가 하나 주어진다.

각각의 알파벳에 대해서 단어에 포함되어 있는 경우
처음 등장하는 위치를 출력하고
포함 안되어 있다면 -1을 출력해야 한다.
'''

str = input()
check = [-1] * 26  #알파벳 개수대로 초기화 하기

# 이제 처음 등장하는 위치를 어떻게 알게 하지?
# -> 입력된 문자열을 정렬하면 되지 않을까? -> 안된다.

# 일단 a~z까지 하나씩 입력된 문자열 배열을 돌면서 검사하는 수 밖에 없다.
# for 문으로 입력된 문자열을 돌면서 if문으로 비교했을때 빠져나올 수 밖에 없음.
# 그러면 a부터 z까지 하나씩 할 수도 없다. 이를 어떻게 하지?
# 아스키를 이용해야한다. ord()를 이용하자.
for i in range(len(str)):
    char = str[i]
    idx = ord(char) - ord('a') # 알파벳 인덱스 계산하기

    if check[idx] == -1:  # 처음 나온 문자라면
        check[idx] = i

for idx in check:
    print(idx, end=" ")




