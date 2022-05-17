N = int(input())
args = input().split()

m = int(args[0])
n = int(args[0])

for i in range(1,N):
    m = max(m, int(args[i]))
    n = min(n, int(args[i]))
print(n, m)