N = int(input())

for i in range(N):
    star = '*'*(N-i)
    print(star.rjust(N))