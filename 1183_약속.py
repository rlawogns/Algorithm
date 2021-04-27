n=int(input())
l=[]
for i in range(n):
    a,b=(map(int,input().split()))
    l.append(b-a)
l.sort()
if n%2==1:
    print(1)
else:
    print(l[n//2]-l[(n//2)-1]+1)