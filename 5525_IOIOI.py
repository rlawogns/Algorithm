n=int(input())
m=int(input())
s=input()
io="IOI"
result=0
t=0
i=0
while i+3<=m:
    if s[i:i+3]==io:
        t+=1
        i+=1
        if t==n:
            result+=1
            t-=1
    else:
        t=0
    i+=1
print(result)