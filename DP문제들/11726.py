N = int(input())
dy = [0] * (N+1)

if N == 3: 
    print(N)

else:
    dy[1] = 1
    dy[2] = 2

    for i in range(3, N+1):
        dy[i] = dy[i-1] + dy[i-2]
    
    print(dy[N]%10007)