N = int(input())

for i in range(N):
    print("*"*(i+1))
    star = '*'*i
    print(star.rjust(N))

