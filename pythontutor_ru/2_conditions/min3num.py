a = int(input())
b = int(input())
c = int(input())
t = 0

def WhatMin (a, b):
        if a <= b:
            t = a
        else:
            t = b
        return int(t)

t = WhatMin(WhatMin(a,b), c)
print(t)
