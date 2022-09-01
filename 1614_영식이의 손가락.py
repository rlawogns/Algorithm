n=int(input())
m=int(input())
if n==1:
    print(8*m)
elif n==5:
    print(8*m+4)
elif n==2:
    print(m+((m+1)//2*6)+((m+1)%2))
elif n==3:
    print(2+m*4)
else:
    print(m+(((m+2)//2*2-1)*3)+(m%2))