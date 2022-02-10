l=[0,1,1]
def fibo(n):
    if len(l)>n:
        return l[n]
    l.append(fibo(n-1)+fibo(n-2))
    return l[n]
n=int(input())
print(fibo(n))