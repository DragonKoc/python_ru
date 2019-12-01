#Дано положительное действительное число X. Выведите его дробную часть.

from math import *

n = float(input())
if n<1:
    N = n
    s = N
else:
    N =  int(n)
    s = n % int(N)

print(s)