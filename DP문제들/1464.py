N = int(input())
cnt = 0
result = 0
while (result == 1):
    N -= 1
    cnt += 1

    if (N % 3 == 0):
        result = N / 3
        cnt += 1

    if(N % 2 == 0):
        result = N / 2
        cnt += 1
    print(cnt)
