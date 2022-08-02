from sys import stdin
mo=set(['a','e','i','o','u'])
s=stdin.readline().rstrip()
while s!='end':
    l=list(s)
    r1=False
    r2=True
    r3=True
    ml=0
    jl=0
    pre=''
    for i in l:
        if i in mo:
            r1=True
            ml+=1
            jl=0
        else:
            jl+=1
            ml=0
        if ml==3 or jl==3:
            r2=False
            break
        if i==pre:
            if i!='e' and i!='o':
                r3=False
                break
        pre=i
    if r1 and r2 and r3:
        print(f"<{s}> is acceptable.")
    else:
        print(f"<{s}> is not acceptable.")
    s=stdin.readline().rstrip()