from sys import stdin
a,b=stdin.readline().split()
an=len(a)
bn=len(b)
result=0
for i in range(an):
    if a[i]!=b[i]:
        result+=1
for i in range(1,bn-an+1):
    t1=b[i:]
    t2=b[:-i]
    result1=0
    result2=0
    for j in range(an):
        if a[j]!=t1[j]:
            result1+=1
        if a[j]!=t2[j]:
            result2+=1
    if result>result1:
        result=result1
    if result>result2:
        result=result2
print(result)