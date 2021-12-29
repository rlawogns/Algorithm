N,L,W,H=map(int,input().split())
s,end=0,min(L,W,H)
for _ in range(100):
    mid = (end + s) / 2
    count=(L//mid)*(W//mid)*(H//mid)
    if(count>=N):
        s=mid
    else:
        end=mid
print("%.9f"%mid)