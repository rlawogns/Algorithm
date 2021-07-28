import itertools
n=int(input())
l=[str(_) for _ in range(1,n+1)]
for i in itertools.permutations(l):
   print(' '.join(i))