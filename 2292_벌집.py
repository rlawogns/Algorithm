n=int(input())
c=1
i=1
while c<=1000000000:
    if c>=n:
        break
    c+=i*6
    i+=1
print(i)