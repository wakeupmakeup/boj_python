# A는 3자리 숫자로 된 정답을 하나 정한다. 
# A가 정답으로 생각할 수 있는 모든 수를 넣어보기!

# 그리고 B가 도전한 내용에 맞는지 확인하기! 

num = int(input())


hint = [list(map(str,input().split())) for _ in range(num)] # 입력받은 숫자만큼 한다.  

# [[123,1,1], [356,1,0], ... ]

answer = 0
# 100 ~ 999
for a in range(1,10): # 100의 자리수
    for b in range(1, 10): #10의 자리수
        for c in range(1, 10): # 1의 자리수
            cnt = 0
            
            if (a == b or b == c or c == a):
                continue    # 서로다른 3자리수가 나와야 하니 같은 수가 있다면 무시한다. 

            
           
            
            
            for arr in hint: 
                number = list(arr[0])
                strike = int(arr[1])
                ball = int(arr[2])
            
                
                # a,b,c 라는 숫자를 number와 비교
                # 자리수를 나눠서 strike, ball을 측정하는 부분.
                # strike 측정하기. = 숫자가 같고 자리까지 같을 경우
                
                strike_count = 0
                ball_count = 0
                
                
                # 스트라이크 측정
                # 100의 자리
                if(a == int(number[0])):
                    strike_count += 1
                
                if(b == int(number[1])):
                    strike_count += 1
                    
                if(c == int(number[2])):
                    strike_count += 1
                
                
                # ball 측정
                # 100의 자리
                if(a == int(number[1]) or a == int(number[2])):
                    ball_count += 1
                
                if(b == int(number[0]) or b == int(number[2])):
                    ball_count += 1
                    
                if(c == int(number[0]) or c == int(number[1])):
                    ball_count += 1
                    
                    
                
                # 매칭 여부 확인 하기.
                if (strike != strike_count):
                    break
                if (ball != ball_count):
                    break
                
                cnt += 1

            if cnt == num:
                answer += 1
        
            
print(answer)