k, n = map(int, input().split())  # 두 정수 입력받기
cables = [int(input()) for _ in range(k)] # 랜선 길이 입력받기

start = 1
end = max(cables)
result = 0

while start <= end:
    mid = (start + end) // 2 # 중간값
    count = 0

    for i in cables:
        count += i // mid # 랜선을 잘라서 나온 개수를 count에 더해줌

    if count >= n:
        start = mid + 1 # 오른쪽으로 이동해야 값이 커지니 +1 하는 것
    else:
        end = mid - 1 # 왼쪽으로 이동해야 값이 작아지니 -1 하는 것
    
print(end)


    

