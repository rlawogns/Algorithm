n=int(input())
l=[0]*(n+1)
for i in range(1,n+1):
    minn=50001
    j=1
    while j**2<=i:
        minn=min(minn,l[i-(j**2)])
        j+=1
    l[i]=minn+1
print(l[n])