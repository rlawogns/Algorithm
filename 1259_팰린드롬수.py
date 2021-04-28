while True:
    l=input()
    if l=='0': break
    if l[::-1]==l:
        print("yes")
    else:
        print("no")