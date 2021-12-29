def prime(n):
    for i in range(2,int(n**0.5)+1):
        if pl[i]==True:
            for j in range(i+i,n+1,i):
                pl[j]=False
m,n=map(int,input().split())
pl=[False]+[False]+[True]*(n-1)
prime(n)
for i in range(m,n+1):
    if pl[i]==True:
        print(i)
#에라토스테네스의 체