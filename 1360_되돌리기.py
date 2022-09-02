from sys import stdin
n= int(input())
d={0:''}
pre=''
prel=[['',0]]
for i in range(n):
    a,b,c = stdin.readline().split()
    if a=="type":
        prel.append([prel[-1][0]+b,int(c)])
        pre+=b
        d[int(c)]=prel[-1][0]
    else:
        t=int(c)-int(b)-1
        if t in d:
            pre=d[t]
            prel.append([d[t],int(c)])
            d[int(c)]=prel[-1][0]
        else:
            pre=''
            for j in prel:
                if j[1]>t:
                    break
                pre=j[0]
            prel.append([pre,int(c)])
            d[int(c)] = prel[-1][0]
print(prel[-1][0])