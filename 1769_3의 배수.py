n=int(input())
result=0
while n//10>0:
    l=list(str(n))
    n=sum(map(int,l))
    result+=1
print(result)
if n==3 or n==6 or n==9:
    print("YES")
else:
    print("NO")