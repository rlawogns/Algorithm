a=list(set(input() for _ in range(int(input()))))
a.sort()
a.sort(key=len)
for i in a:
    print(i)