n=int(input())
result=0
for i in range(1,n+1):
    while i%10==0:
        i=i//10
        result+=1
    while i%5==0:
        i=i//5
        result+=1
print(result)