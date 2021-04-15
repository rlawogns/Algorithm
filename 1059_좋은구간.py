sn=int(input())
s=list(map(int,input().split()))
s.sort()
s=[0]+s
n=int(input())
for i in range(sn):
    if s[i]==n:
        print(0)
    elif s[i]<n and n<s[i+1]:
        print((n-s[i])*(s[i+1]-n)-1)