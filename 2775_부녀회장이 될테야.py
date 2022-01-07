def a(l,k):
    if len(l)<k:
        l=a(l,k-1)
    if len(l)==k:
        l2=[0]
        suml2=0
        for i in l[k-1][1:]:
            suml2+=i
            l2.append(suml2)
        l.append(l2)
    return l
t=int(input())
l=[[i for i in range(15)]]
for _ in range(t):
    k=int(input())
    n=int(input())
    l=a(l,k)
    print(l[k][n])