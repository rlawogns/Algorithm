import sys
l=[]
for _ in range(int(input())):
    a,b=list(sys.stdin.readline().split())
    l.append([int(a),b])
l.sort(key=lambda x : x[0])
for i,j in l:
    print(i,j)