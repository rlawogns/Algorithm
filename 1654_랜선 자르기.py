k,n=map(int,input().split())
klist=[int(input()) for i in range(k)]
s,end=1,max(klist)
while(s<=end):
    count=0
    mid = (end + s) // 2
    for i in klist:
        count+=i//mid
    if(count>=n):
        s=mid+1
        ans=mid
    elif(count<n):
        end=mid-1
print(end)