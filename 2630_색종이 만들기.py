import sys
def cutlist(l,n):
    fl=[]
    for m in range(4):
        tl = []
        if m==0:
            aa=0
        elif m==1:
            aa=n//2
        elif m==2:
            aa=n*n//2
        else:
            aa=n*n//2+n//2
        for i in range(n // 2):
            tn = i * n
            for j in range(n // 2):
                tl.append(l[j + tn + aa])
        if sum(tl)==len(tl) or sum(tl)==0:
            fl.append(tl)
        else:
            fl+=(cutlist(tl,n//2))
    return fl
a=int(input())
l=[]
for i in range(a):
    l+=list(map(int,sys.stdin.readline().split()))
if sum(l)==len(l):
    print("0\n1")
elif sum(l)==0:
    print("1\n0")
else:
    ll = cutlist(l, a)
    bn = 0
    for i in ll:
        if sum(i):
            bn += 1
    print(len(ll) - bn)
    print(bn)