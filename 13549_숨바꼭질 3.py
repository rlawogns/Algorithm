n,k=map(int,input().split())
result=0
l=[0]*1000001
l[k]=1
tl=[k]
while True:
    tt=[]
    for i in tl:
        if i==n:
            print(result)
            exit()
        if i-1>=0 and i-1<=1000000:
            if l[i-1]==0:
                tt.append(i-1)
                l[i-1]=1
        if i+1>=0 and i+1<=1000000:
            if l[i+1]==0:
                tt.append(i+1)
                l[i+1]=1
        if i%2==0:
            j=i
            while j//2>0 and j%2==0:
                j//=2
                l[j]=1
                if j==n:
                    print(result)
                    exit()
                if j-1>=0 and j-1<=1000000:
                    if l[j-1]==0:
                        tt.append(j-1)
                        l[j-1]=1
                if j+1>=0 and j+1<=1000000:
                    if l[j+1]==0:
                        tt.append(j+1)
                        l[j+1]=1
    tl=tt
    result+=1