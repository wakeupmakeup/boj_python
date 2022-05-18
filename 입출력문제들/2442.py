N = int(input())

for i in range(1,N+1):
    print(" " * (N-i), end="")
    print("*" * ((2*i)-1), end="")  #end=""을 왜쓰냐?, 기본값은 \n인 줄바꿈인데 이것을 없애주기위해서 사용.
    print()