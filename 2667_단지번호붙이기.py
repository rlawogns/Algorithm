import sys
n=int(input())
xl=[-1,0,1,0]
yl=[0,1,0,-1]
l=[sys.stdin.readline().rstrip() for i in range(n)]
check=[[0]*n for i in range(n)]
def a(y,x):
    check[y][x]=1
    global count
    count+=1
    for i in range(4):
        xn=xl[i]+x
        yn=yl[i]+y
        if xn>=0 and yn>=0 and xn<n and yn<n:
            if l[yn][xn]=='1' and check[yn][xn]==0:
                a(yn,xn)
    return count
cl=[]
for i in range(n):
    for j in range(n):
        if l[j][i] == '1' and check[j][i] == 0:
            count=0
            a(j,i)
            if count!=0:
                cl.append(count)
print(len(cl))
cl.sort()
for i in cl:
    print(i)