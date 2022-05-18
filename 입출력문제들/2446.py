N = int(input())
x = 2*N-1

for i in range(x):
    if (i <= N-1):
        print(' '*i + '*'*(x-2*i))
    else:
        print(" "*(x-i-1) + '*'*(2*(i+1)-x))
    