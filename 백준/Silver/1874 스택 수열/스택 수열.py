''' 나의 논리
임의의 수열이 있다고 하자. 
그러면 그것을 일단 오름차순으로 정렬 한다. 

그런 후 그대로 append한 후 원래 존재 했던 수열과 비교한다.
만약 top에 있는 숫자가 원래 있던 수열과 같지 않다면 계속 push하고 
같다면 pop을 한다. 

=> 위는 틀린 논리다.
먼저 수열은 하나가 주어지고 push를 할때 수열을 이용하는게 아니라 그냥 1부터 n까지 오름차순으로 
정수를 push하는 것이다. 
'''



n = int(input())
originSeq = [int(input()) for _ in range(n)] #주어진 수열

current = 1 #여기서 부터 push를 한다.
s = [] # 빈 스택 배열
result = [] # 결과 저장을 위한 배열

for num in originSeq:
    while current <= num: # 현재 숫자가 주어진 수열의 작거나 같다면 -> 수열의 num번째 숫자와 같을때 까지 push
        s.append(current)
        result.append('+')
        current += 1 # 정수를 오름차순으로 넣어야 함.

    if s[-1] == num: # 스택의 top이 현재 숫자와 같다면 pop한다. 
        s.pop()
        result.append('-')

    else:
        print("NO")
        break


    for i in result:
        print(i)




