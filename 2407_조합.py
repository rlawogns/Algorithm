import math
from fractions import Fraction
n,r=map(int,input().split())
m=n-r
print(Fraction(math.factorial(n),(math.factorial(m)*math.factorial(r))))