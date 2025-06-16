h, m = map(int, input().split())

if (m - 45) < 0:

    if ((h - 1) < 0):
        h = (h - 1) + 24
        m = (m - 45) + 60
        print(h,m)

    elif ((h - 1) >= 0):
        h = (h - 1)
        m = (m - 45) + 60
        print(h, m)

else:
    m = m-45
    print(h, m)