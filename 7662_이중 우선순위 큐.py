import heapq
from sys import stdin
n=int(input())
for _ in range(n):
    hq1 = []
    hq2 = []
    check = [False] * 1000001
    m=int(input())
    for i in range(m):
        s,num=stdin.readline().split()
        if s=='I':
            heapq.heappush(hq1,[int(num),i])
            heapq.heappush(hq2, [-(int(num)), i])
            check[i]=True
        elif hq1 and hq2:
            if num=="-1":
                deln=heapq.heappop(hq1)
                while hq1 and check[deln[1]]==False:
                    deln = heapq.heappop(hq1)
                check[deln[1]]=False
            else:
                deln = heapq.heappop(hq2)
                while hq2 and check[deln[1]] == False:
                    deln = heapq.heappop(hq2)
                check[deln[1]] = False
    s=""
    while hq2:
        n2 = heapq.heappop(hq2)
        if check[n2[1]] == True:
            s += str(-n2[0])
            break
    while hq1:
        n1 = heapq.heappop(hq1)
        if check[n1[1]] == True:
            s += " " + str(n1[0])
            break

    if s=="":
        print("EMPTY")
    else:
        print(s)