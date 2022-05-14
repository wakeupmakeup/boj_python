a = input()
length = len(a)

for i in range(0, length, 10):    #keypoint 1. range(1,2,3)에서 1은 처음 2는 끝나는 범위 3은 간격임. 
    print(a[i:i+10])        # keypoint 2. 범위를 슬라이싱 할 수 있는데 i:i+10처럼 처음 첫범위, 첫 범위에서 +10만큼 증가한 값을 자를수 있음. 