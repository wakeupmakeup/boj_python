N = int(input())

for i in range(1,N+1):
    blank = " "*(N-i)
    if(i==1 or i==N):
        star = "*"*(2*i-1)
        print (blank + star)
    
    else:
        star = "*"+" "*(2*(i-1)-1) + "*"
        print(blank + star)
    
        
  