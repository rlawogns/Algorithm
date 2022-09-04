from sys import stdin
n=int(input())
sl=set([])
for i in range(n):
    ok=False
    s=stdin.readline().rstrip()
    l=s.split()
    for j in range(len(l)):
        if ok:
            break
        if l[j][0].upper() not in sl:
            sl.add(l[j][0].upper())
            ok=True
            l[j]="["+l[j][0]+"]"+l[j][1:]
            print(" ".join(l))
    if ok:
        continue
    for j in s.replace(' ',''):
        if ok:
            break
        if j.upper() not in sl:
            sl.add(j.upper())
            ok=True
            key = s.index(j)
            print(s[:key] + "[" + s[key] + "]" + s[key+1:])
    if ok:
        continue
    print(s)