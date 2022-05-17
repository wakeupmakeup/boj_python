N = int(input())

for i in range(N):
    star = '*'*(i*2)
    if (i%2 != 0):
        print(star.center(N))