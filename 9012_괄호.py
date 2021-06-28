import sys
n=int(input())
for _ in range(n):
    l=list(sys.stdin.readline().rstrip('\n'))
    n=0
    for j in l:
        if j=='(':
            n+=1
        else:
            n-=1
        if n<0:
            break
    if n==0:
        print("YES")
    else:
        print("NO")