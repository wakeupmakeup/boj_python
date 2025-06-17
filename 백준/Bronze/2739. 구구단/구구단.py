n = int(input())
count = 1

while count < 10:
    print(f"{n} * {count} = {n*count}") # 안에 변수를 인식하게 하고 싶다면 f-string을 사용하자. (가장 추천하는 방법)
    count += 1