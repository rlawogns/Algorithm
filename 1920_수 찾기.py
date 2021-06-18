n=int(input())
nn=set(input().split())
m=int(input())
for i in input().split():
    if i in nn:
        print(1)
    else:
        print(0)