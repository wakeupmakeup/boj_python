# 같은 단어는 연속적으로 나와야한다. 
# 한번 나온 문자는 같이 붙어 나오는 것을 제외하면 다시는 나와선 안된다.
# 즉, 서로 다른 알파벳으로 이어진 단어여야 한다.
# 그룹 단어인지 아닌지는 입력받은 알파벳을 하나하나 비교해봐야 한다(이전에 입력됐던 것들과도)


n = int(input())
gWord = 0 # 그룹언어 선언 

for _ in range(n):
    word = input()
    error = 0   #그룹단어가 아닌것들을 찾기위한 변수
    for index in range(len(word)-1):    # 인덱스 범위를 생성한다. 0 부터 -1까지 (단어개수)
        if word[index] != word[index+1]: # 이어진 두 문자가 다를 때
            new_word = word[index+1:] # 현재글자 이후 문자열을 새로운 단어로 만들기
            if new_word.count(word[index]) > 0: #남은 문자열에서 현재글자가 있었다면 
                error += 1 # 에러에 1증가. 
    if error == 0:
        gWord += 1 # 에러가 0이면 그룹 단어 +1
print(gWord)

# 만약에 word가 asd 였다면 길이는 3이지만 -1 을 해서 2가 나옴. 3을 기준으로 첫번째는 0,1번째 비교 그 다음은 1,2번째 비고를 해서 전부 비교할 수 있음
