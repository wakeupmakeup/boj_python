import sys

t = int(sys.stdin.readline().rstrip())
res = 0

for i in range(t):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    res = a+b
    print(res)