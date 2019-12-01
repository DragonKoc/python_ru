a = int(input())
b = int(input())
c = int(input())
t = int(1)

if (((a + b) / 2) == a and ((a + c) / 2) == a and ((c + b) / 2) == c):
    t = 3
elif (((a + b) / 2) == a or ((a + c) / 2) == a or ((c + b) / 2) == c):
    if (a == b):
        t = t + 1
    if (b == c):
        t = t + 1
    if (c == a):
        t = t + 1
else:
    t = 0

print (t)