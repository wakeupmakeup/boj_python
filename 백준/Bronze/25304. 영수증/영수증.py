totalX = int(input())
n = int(input())
res = 0

for i in range(n):
    a, b = map(int, input().split())
    res += (a*b)

if totalX == res:
    print("Yes")

else:
    print("No")