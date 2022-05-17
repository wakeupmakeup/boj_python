rg = int(input())
num = input()
num_ls = []
sum = 0 

    # 빈 리스트에 요소를 채워 넣는 for문 1
for i in range(rg):
    num_ls.append(num[i])
    # 리스트에 들어간 것들 정수화 처리 해주기. 
for i in range(rg): 
    num_ls[i] = int(num_ls[i])
    # 다 더하기.
for i in range(rg):
    sum += num_ls[i]

print(sum)

