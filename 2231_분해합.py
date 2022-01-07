n=int(input())
for i in range(1,n+1):
    t=i
    c=i
    while(i//10>=1):
       c+=i%10
       i=i//10
    c+=i
    if c==n:
        print(t)
        break
    if t==n:
        print(0)