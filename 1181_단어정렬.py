import sys
a=list(set(sys.stdin.readline().strip() for _ in range(int(input()))))
a.sort()
a.sort(key=len)
for i in a:
    print(i)