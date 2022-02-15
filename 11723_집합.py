from sys import stdin
n= int(input())
l=[0 for _ in range(21)]
for _ in range(n):
    m=stdin.readline().split()
    if m[0]=="add":
        if l[int(m[1])]==0:
            l[int(m[1])]=1
    elif m[0]=="remove":
        if l[int(m[1])]==1:
            l[int(m[1])]=0
    elif m[0]=="check":
        print(l[int(m[1])])
    elif m[0]=="toggle":
        if l[int(m[1])]==0:
            l[int(m[1])]=1
        else:
            l[int(m[1])]=0
    elif m[0]=="all":
        l=[1 for _ in range(21)]
    elif m[0]=="empty":
        l=[0 for _ in range(21)]