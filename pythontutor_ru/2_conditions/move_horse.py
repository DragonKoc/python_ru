a = int(input())
b = int(input())
c = int(input())
d = int(input())

if ((a == c + 1 or a == c - 1) and abs(b - d) == 2) or ((b == d + 1 or b == d - 1) and abs(a - c) ==2):
        print('YES')
else:
        print('NO')
